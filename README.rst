.. You should enable this project on travis-ci.org and coveralls.io to make
   these badges work. The necessary Travis and Coverage config files have been
   generated for you.

.. image:: https://travis-ci.org/ckan/ckanext-pdfview.svg?branch=master
    :target: https://travis-ci.org/ckan/ckanext-pdfview

.. image:: https://img.shields.io/pypi/dm/ckanext-pdfview.svg
    :target: https://pypi.python.org/pypi//ckanext-pdfview/
    :alt: Downloads

.. image:: https://img.shields.io/pypi/v/ckanext-pdfview.svg
    :target: https://pypi.python.org/pypi/ckanext-pdfview/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/pyversions/ckanext-pdfview.svg
    :target: https://pypi.python.org/pypi/ckanext-pdfview/
    :alt: Supported Python versions

.. image:: https://img.shields.io/pypi/status/ckanext-pdfview.svg
    :target: https://pypi.python.org/pypi/ckanext-pdfview/
    :alt: Development Status

.. image:: https://img.shields.io/pypi/l/ckanext-pdfview.svg
    :target: https://pypi.python.org/pypi/ckanext-pdfview/
    :alt: License

===============
ckanext-pdfview
===============

This extension provides a view plugin for PDF files using an `html object tag <https://www.w3schools.com/tags/tag_object.asp>`_.

------------
Requirements
------------

This extension works with CKAN >= 2.7 and runs both on Python 2.7 and 3.6+.


------------
Installation
------------

To install ckanext-pdfview:

1. Activate your CKAN virtual environment, for example::

     source /usr/lib/ckan/default/bin/activate

2. Install the ckanext-pdfview Python package into your virtual environment::

     pip install ckanext-pdfview

3. Add ``pdf_view`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. If you want to render PDF files which are not located in the same server as
   CKAN you also need to enable the ``resource_proxy`` plugin.

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


------------------------
Development Installation
------------------------

To install ckanext-pdfview for development, activate your CKAN virtualenv and
do::

    git clone https://github.com/ckan/ckanext-pdfview.git
    cd ckanext-pdfview
    pip install -r dev-requirements.txt
    python setup.py develop


-----------------
Running the Tests
-----------------

To run the tests, do::

    pytest --ckan-ini=test.ini ckanext/pdfview


-----------------------------------
Registering ckanext-pdfview on PyPI
-----------------------------------

ckanext-pdfview should be availabe on PyPI as
https://pypi.python.org/pypi/ckanext-pdfview. If that link doesn't work, then
you can register the project on PyPI for the first time by following these
steps:

1. Create a source distribution of the project::

     python setup.py sdist

2. Register the project::

     python setup.py register

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the first release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.1 then do::

       git tag 0.0.1
       git push --tags


------------------------------------------
Releasing a New Version of ckanext-pdfview
------------------------------------------

ckanext-pdfview is availabe on PyPI as https://pypi.python.org/pypi/ckanext-pdfview.
To publish a new version to PyPI follow these steps:

1. Update the version number in the ``setup.py`` file.
   See `PEP 440 <http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers>`_
   for how to choose version numbers.

2. Create a source distribution of the new version::

     python setup.py sdist

3. Upload the source distribution to PyPI::

     python setup.py sdist upload

4. Tag the new release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.2 then do::

       git tag 0.0.2
       git push --tags
