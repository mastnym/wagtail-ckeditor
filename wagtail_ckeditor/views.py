from django.views.generic.base import TemplateView
from wagtail_ckeditor import settings


class IndexView(TemplateView):
    template_name = "wagtail_ckeditor/index.html"

    def get_context_data(self, **kwargs):
        data = super(IndexView, self).get_context_data(**kwargs)
        data["use_math"] = settings.WAGTAIL_CKEDITOR_USE_MATH
        data["ckeditor_config"] = settings.JSON_CONFIG
        data["mathjax_url"] = settings.WAGTAIL_CKEDITOR_MATHJAX_URL
        return data