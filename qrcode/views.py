from django.shortcuts import render
import pyqrcode
from django.http import HttpResponse

def generate_qr(request, text_to_gen):
    if request.method == 'GET':
        qr = pyqrcode.create(text_to_gen)
        qrcode_filename = "media/qrcode/qr.png"
        qr.png(qrcode_filename, scale=16)
        image_qrcode = open(qrcode_filename, "rb").read()
        return HttpResponse(image_qrcode, content_type="image/png")
