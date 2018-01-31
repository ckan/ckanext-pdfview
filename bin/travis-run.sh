#!/bin/sh -e

nosetests --ckan \
          --nologcapture \
          --with-pylons=subdir/test.ini \
          --with-coverage \
          --cover-package=ckanext.pdfview \
          --cover-inclusive \
          --cover-erase \
          --cover-tests
