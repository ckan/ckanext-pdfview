#!/bin/bash
set -e

pytest --ckan-ini=subdir/test.ini --cov=ckanext.pdfview ckanext/pdfview/tests
