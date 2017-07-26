from django.templatetags.static import static
from django.utils.html import format_html
from wagtail.wagtailcore import hooks


@hooks.register('insert_editor_js')
def ckeditorjs():
    return format_html('<script src="{src}"></script>', src=static("wagtail_ckeditor/ckeditor/ckeditor.js"))
