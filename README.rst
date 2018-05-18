========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls|
        | |landscape| |scrutinizer| |codacy| |codeclimate|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-catalpa-tools/badge/?style=flat
    :target: https://readthedocs.org/projects/python-catalpa-tools
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/PeteCoward/python-catalpa-tools.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/PeteCoward/python-catalpa-tools

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/PeteCoward/python-catalpa-tools?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/PeteCoward/python-catalpa-tools

.. |requires| image:: https://requires.io/github/PeteCoward/python-catalpa-tools/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/PeteCoward/python-catalpa-tools/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/PeteCoward/python-catalpa-tools/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/PeteCoward/python-catalpa-tools

.. |landscape| image:: https://landscape.io/github/PeteCoward/python-catalpa-tools/master/landscape.svg?style=flat
    :target: https://landscape.io/github/PeteCoward/python-catalpa-tools/master
    :alt: Code Quality Status

.. |codacy| image:: https://img.shields.io/codacy/REPLACE_WITH_PROJECT_ID.svg
    :target: https://www.codacy.com/app/PeteCoward/python-catalpa-tools
    :alt: Codacy Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/PeteCoward/python-catalpa-tools/badges/gpa.svg
   :target: https://codeclimate.com/github/PeteCoward/python-catalpa-tools
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/catalpa-tools.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/catalpa-tools

.. |commits-since| image:: https://img.shields.io/github/commits-since/PeteCoward/python-catalpa-tools/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/PeteCoward/python-catalpa-tools/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/catalpa-tools.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/catalpa-tools

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/catalpa-tools.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/catalpa-tools

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/catalpa-tools.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/catalpa-tools

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/PeteCoward/python-catalpa-tools/master.svg
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/PeteCoward/python-catalpa-tools/


.. end-badges

A collection of useful tools developed for and by Catalpa International

* Free software: BSD 2-Clause License

Installation
============

::

    pip install catalpa-tools

Documentation
=============

https://python-catalpa-tools.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
