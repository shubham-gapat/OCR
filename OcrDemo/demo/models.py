from django.db import models

# Create your models here.

class OCRModel(models.Model):
    ocr_result = models.JSONField(null=True, blank=False)
