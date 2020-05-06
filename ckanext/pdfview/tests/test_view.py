import pytest

from six.moves.urllib.parse import urljoin


import ckan.model as model
import ckan.plugins as plugins
import ckan.lib.helpers as h
import ckanext.pdfview.plugin as plugin
import ckan.lib.create_test_data as create_test_data


@pytest.fixture
def test_view(clean_db):
    create_test_data.CreateTestData.create()

    context = {'model': model,
               'session': model.Session,
               'user': model.User.get('testsysadmin').name}

    package = model.Package.get('annakarenina')
    resource_id = package.resources[1].id
    resource_view = {'resource_id': resource_id,
                     'view_type': 'pdf_view',
                     'title': u'Test View',
                     'description': u'A *nice* test view'}
    resource_view = plugins.toolkit.get_action('resource_view_create')(
        context, resource_view)
    return resource_view, package, resource_id


@pytest.fixture
def pdf_view():
    return plugin.PdfView()


class TestPdfView(object):
    new_ckan = plugins.toolkit.check_ckan_version('2.8')

    def test_can_view(self, ckan_config, pdf_view):
        url_same_domain = urljoin(
            ckan_config.get('ckan.site_url', '//localhost:5000'),
            '/resource.txt')
        url_different_domain = 'http://some.com/resource.pdf'

        data_dict = {'resource': {'format': 'pdf', 'url': url_same_domain}}
        assert pdf_view.can_view(data_dict)

        data_dict = {'resource': {'format': 'x-pdf', 'url': url_same_domain}}
        assert pdf_view.can_view(data_dict)

        data_dict = {'resource': {'format': 'pdf',
                                  'url': url_different_domain}}
        assert not pdf_view.can_view(data_dict)

    def test_js_included(self, test_view, app):
        resource_view, package, resource_id = test_view
        if self.new_ckan:
            params = {'controller': 'resource', 'action': 'view'}
        else:
            params = {'controller': 'package', 'action': 'resource_view'}
        url = h.url_for(
            **params,
            id=package.name, resource_id=resource_id,
            view_id=resource_view['id'])
        result = app.get(url)
        assert (('pdf_view.js' in result.body) or
                ('pdf_view.min.js' in result.body))

    def test_title_description_iframe_shown(self, app, test_view):
        resource_view, package, resource_id = test_view
        if self.new_ckan:
            params = {'controller': 'resource', 'action': 'read'}
        else:
            params = {'controller': 'package', 'action': 'resource_read'}

        url = h.url_for(**params,
                        id=package.name, resource_id=resource_id)
        result = app.get(url)
        assert resource_view['title'] in result
        assert 'data-module="data-viewer"' in result.body

    def test_description_supports_markdown(self, test_view, app):
        resource_view, package, resource_id = test_view
        if self.new_ckan:
            params = {'controller': 'resource', 'action': 'read'}
        else:
            params = {'controller': 'package', 'action': 'resource_read'}

        url = h.url_for(**params, id=package.name, resource_id=resource_id)
        result = app.get(url)
        assert 'A <em>nice</em> test view' in result
