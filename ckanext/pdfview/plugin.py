import logging

import ckan.plugins as p
import ckan.lib.datapreview as datapreview
from ckan.plugins import toolkit as tk

log = logging.getLogger(__name__)


class PdfView(p.SingletonPlugin):
    '''This extension views PDFs. '''

    if not p.toolkit.check_ckan_version('2.3'):
        raise p.toolkit.CkanVersionException(
            'This extension requires CKAN >= 2.3. If you are using a ' +
            'previous CKAN version the PDF viewer is included in the main ' +
            'CKAN repository.')

    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IConfigurable, inherit=True)
    p.implements(p.IResourceView, inherit=True)

    PDF = ['pdf', 'x-pdf', 'acrobat', 'vnd.pdf']
    proxy_is_enabled = False

    def info(self):
        return {'name': 'pdf_view',
                'title': 'PDF',
                'icon': 'file-text',
                'default_title': 'PDF',
                }

    def update_config(self, config):

        # Add public/resource
        p.toolkit.add_public_directory(config, 'theme/public')
        p.toolkit.add_resource('theme/public', 'ckanext-pdfview')

        # Add templates depending on bootstap version
        if tk.check_ckan_version(min_version='2.8'):
            p.toolkit.add_template_directory(config, 'theme/templates')
        else:
            p.toolkit.add_template_directory(config, 'theme/templates-bs2')

    def configure(self, config):
        enabled = config.get('ckan.resource_proxy_enabled', False)
        self.proxy_is_enabled = enabled

    def can_view(self, data_dict):
        resource = data_dict['resource']
        format_lower = resource.get('format', '').lower()

        proxy_enabled = p.plugin_loaded('resource_proxy')
        same_domain = datapreview.on_same_domain(data_dict)

        if format_lower in self.PDF:
            return same_domain or proxy_enabled
        return False

    def view_template(self, context, data_dict):
        return 'pdf.html'
