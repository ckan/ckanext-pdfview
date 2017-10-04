import logging

import ckan.plugins as p
import ckan.lib.helpers as h
import ckan.lib.datapreview as datapreview

log = logging.getLogger(__name__)

def get_ckan_version():
    try:
        return float(h.ckan_version()[0:3])
    except AttributeError:
        #So old that we can't ask CKAN this way, but let's be optimistic
        return 2.4

def get_ckan_with_fa():
    if get_ckan_version() >= 2.7:
        return True
    else:
        return False

def get_bootstrap_version():
    public_setting = config.get('ckan.base_public_folder', 'public')
    if public_setting == 'public-bs2' or get_ckan_version() <= 2.7:
        return 2
    #Otherwise we're on 2.8+, or other folder; in that case assume 3 (future proofing)
    else:
        return 3

class PdfView(p.SingletonPlugin):
    '''This extension views PDFs. '''

    if not p.toolkit.check_ckan_version('2.3'):
        raise p.toolkit.CkanVersionException(
            'This extension requires CKAN >= 2.3. If you are using a ' +
            'previous CKAN version the PDF viewer is included in the main ' +
            'CKAN repository.')

    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.ITemplateHelpers, inherit=True)
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
        return {
            'pdfview_get_ckan_with_fa': get_ckan_with_fa,
            'pdfview_get_bootstrap_version': get_bootstrap_version
        }
