# encoding: utf-8

import logging
import ckan.plugins as p

log = logging.getLogger(__name__)
ignore_empty = p.toolkit.get_validator("ignore_empty")
url_validator = p.toolkit.get_validator("url_validator")


class PDFView(p.SingletonPlugin):
    """This plugin makes views of PDF resources, using an <object> tag"""

    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IResourceView, inherit=True)

    def update_config(self, config):
        p.toolkit.add_template_directory(config, "theme/templates")

    def info(self):
        return {
            "name": "pdf_view",
            "title": p.toolkit._("PDF"),
            "icon": "file-pdf-o",
            "schema": {"pdf_url": [ignore_empty, url_validator]},
            "iframed": False,
            "always_available": False,
            "default_title": p.toolkit._("PDF"),
        }

    def can_view(self, data_dict):
        return data_dict["resource"].get("format", "").lower() == "pdf"

    def view_template(self, context, data_dict):
        return "pdf_view.html"

    def form_template(self, context, data_dict):
        return "pdf_form.html"
