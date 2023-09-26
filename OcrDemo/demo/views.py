import json
import pytesseract
import cv2
import numpy as np
import sys
import re
import os
from PIL import Image
import ftfy
from .utils import pan_read_data, adhaar_read_data
import io
from rest_framework import generics
from django.http import HttpResponse
from .models import  OCRModel



class UserViewSet(generics.RetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.S
    """
    queryset = OCRModel.objects.all()

    def post(self, request):
        filename = request.FILES.get('image')
        text = pytesseract.image_to_string(Image.open(filename), lang='eng')
        text_output = open('output.txt', 'w', encoding='utf-8')
        text_output.write(text)
        text_output.close()
        file = open('output.txt', 'r', encoding='utf-8')
        text = file.read()
        text = ftfy.fix_text(text)
        text = ftfy.fix_encoding(text)
        data = pan_read_data(text)
        ocr_result = OCRModel.objects.create(ocr_result=data)
        return HttpResponse(ocr_result)


