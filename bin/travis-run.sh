#!/bin/bash
set -e

pytest --ckan-ini=subdir/test.ini --cov=ckanext.pdfview ckanext/pdfview/tests
pytest --ckan-ini=subdir/test_subclass.ini ckanext/pdfview/tests
