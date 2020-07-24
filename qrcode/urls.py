from django.conf.urls import url
from django.urls import path
from qrcode.views import generate_qr

urlpatterns = [
    url(r'^qrcode/(?P<text_to_gen>[\w\-]+)$', generate_qr, name='generate_qrcode'),
]
