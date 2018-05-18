import json
import os

DEFAULT_FILE_NAME = "config.json"

TEST_CONFIGS = {
    1: {'a': 'a_1',
        'b': 'b_1'},
    2: {'b': 'b_2',
        'c': 'c_2'},
    3: {'c': 'c_3',
        'd': 'd_3'}
}


def merge_config(fp, original_config=False):
    ''' Merges a json file in a location into an original config dict
    >>> import io
    >>> original = TEST_CONFIGS[1]
    >>> test_file = io.StringIO(json.dumps(TEST_CONFIGS[2]))
    >>> merged = merge_config(test_file, original)
    >>> merged['a']
    'a_1'
    >>> merged['b']
    'b_2'
    >>> merged['c']
    'c_2'

    '''
    config = original_config if original_config else {}
    config.update(json.load(fp))
    return config


def merge_config_file(file_path, original_config=False):
    ''' Merges a json file in a location into an original config dict
    >>> import tempfile
    >>> original = TEST_CONFIGS[1]
    >>> with tempfile.NamedTemporaryFile(mode='w+t') as tmpfile:
    ...     tmpfile.write(json.dumps(TEST_CONFIGS[2]))
    ...     tmpfile.flush()
    ...     merged = merge_config_file(tmpfile.name, original)
    True
    >>> merged['a']
    'a_1'
    >>> merged['b']
    'b_2'
    >>> merged['c']
    'c_2'

    '''
    with open(file_path, 'r') as fp:
        return merge_config(fp, original_config)


def files_in_directory_ancestors(directory, file_name=DEFAULT_FILE_NAME, stop_depth=False):
    ''' Walk up a directory tree finding all files matching file_name

    '''

    parent_dir = os.path.dirname(directory)
    if file_name in os.listdir(directory):
        yield os.path.join(directory, file_name)
    if directory == parent_dir or stop_depth is 1:
        raise StopIteration
    yield from files_in_directory_ancestors(parent_dir, file_name, stop_depth - 1 if stop_depth else stop_depth)


def test_files_in_directory_ancestors():
    import tempfile
    import shutil
    config_file_name = 'test_couch_config.json'
    # set up directories
    try:
        dir_1 = tempfile.mkdtemp(suffix='test')
        dir_2 = tempfile.mkdtemp(suffix='test', dir=dir_1)
        dir_3 = tempfile.mkdtemp(suffix='test', dir=dir_2)
        # set up config files
        file_location_1 = os.path.join(dir_1, config_file_name)
        with open(file_location_1, 'w+t') as fp_config_1:
            json.dump(TEST_CONFIGS[1], fp_config_1)
        file_location_2 = os.path.join(dir_2, config_file_name)
        with open(file_location_2, 'w+t') as fp_config_2:
            json.dump(TEST_CONFIGS[2], fp_config_2)
        file_location_3 = os.path.join(dir_3, config_file_name)
        with open(file_location_3, 'w+t') as fp_config_3:
            json.dump(TEST_CONFIGS[3], fp_config_3)

        files = list(files_in_directory_ancestors(dir_3, config_file_name, False))
        expected_files = [file_location_3, file_location_2, file_location_1]
        assert files == expected_files

        files = list(files_in_directory_ancestors(dir_3, config_file_name, 2))
        expected_files = [file_location_3, file_location_2]
        assert files == expected_files
    finally:
        shutil.rmtree(dir_1)
