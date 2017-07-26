from django.conf import settings
import json

WAGTAIL_CKEDITOR_USE_MATH = getattr(settings, 'WAGTAIL_CKEDITOR_USE_MATH', True)
WAGTAIL_CKEDITOR_MATHJAX_URL = getattr(settings, 'WAGTAIL_CKEDITOR_MATHJAX_URL', "//cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_HTML")
WAGTAIL_CKEDITOR_CONFIG = getattr(settings, 'WAGTAIL_CKEDITOR_CONFIG',
                                  {'language': settings.LANGUAGE_CODE,
                                   'toolbar': [
                                      {'name': 'basicstyles',
                                       'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript']},
                                      {'name': 'clipboard',
                                       'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo',
                                                 'Redo']},
                                      {'name': 'paragraph',
                                       'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
                                                 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock']},
                                      {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
                                      '/',
                                      {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
                                      {'name': 'insert',
                                       'items': ['Image', 'Mathjax' if WAGTAIL_CKEDITOR_USE_MATH else '-', 'Table',
                                                 'HorizontalRule', 'SpecialChar']},
                                      {'name': 'colors', 'items': ['TextColor', 'BGColor']},
                                      {'name': 'document', 'items': ['Maximize', '-', 'Source']},
                                  ]
                                  })


if WAGTAIL_CKEDITOR_USE_MATH and not WAGTAIL_CKEDITOR_CONFIG.get("mathJaxLib"):
    WAGTAIL_CKEDITOR_CONFIG['mathJaxLib'] = WAGTAIL_CKEDITOR_MATHJAX_URL

JSON_CONFIG = json.dumps(WAGTAIL_CKEDITOR_CONFIG)