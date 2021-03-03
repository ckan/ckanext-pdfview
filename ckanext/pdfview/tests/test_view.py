# encoding: utf-8

import pytest
from ckan.tests import factories
from ckan.plugins import toolkit


@pytest.mark.ckan_config('ckan.views.default_views', '')
@pytest.mark.ckan_config('ckan.plugins', 'pdf_view')
@pytest.mark.usefixtures('clean_db', 'with_plugins')
def test_view_shown_on_resource_page_with_pdf_url(app):

    dataset = factories.Dataset()
    resource = factories.Resource(package_id=dataset['id'],
                                  format='pdf')
    resource_view = factories.ResourceView(
        resource_id=resource['id'],
        view_type='pdf_view',
        pdf_url='https://example/document.pdf')

    if toolkit.check_ckan_version("2.9"):
        url = toolkit.url_for('{}_resource.read'.format(dataset['type']),
                    id=dataset['name'], resource_id=resource['id'])
    else:
        url = toolkit.url_for(controller='package',
                      action='resource_read',
                      id=resource_view['package_id'],
                      resource_id=resource['id'])

    response = app.get(url)

    assert 'https://example/document.pdf' in response.body
