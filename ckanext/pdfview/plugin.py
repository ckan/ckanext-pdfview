import logging

import ckan.plugins as p
import ckan.lib.datapreview as datapreview
from ckan.common import is_flask_request

log = logging.getLogger(__name__)

def request_type():
    return is_flask_request()

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
    p.implements(p.ITemplateHelpers)

    PDF = ['pdf', 'x-pdf', 'acrobat', 'vnd.pdf']
    proxy_is_enabled = False

    def info(self):
        return {'name': 'pdf_view',
                'title': 'PDF',
                'icon': 'file-text',
                'default_title': 'PDF',
                }

    def update_config(self, config):

        p.toolkit.add_public_directory(config, 'theme/public')
        p.toolkit.add_template_directory(config, 'theme/templates')
        p.toolkit.add_resource('theme/public', 'ckanext-pdfview')

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

    def get_helpers(self):
        return {'pdfview_request_type': request_type}
