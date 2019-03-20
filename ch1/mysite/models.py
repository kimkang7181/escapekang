from django.db import models
from django.shortcuts import reverse
from froala_editor.fields import FroalaField
from django.utils import timezone

# Create your models here.


class Popup(models.Model):
    title = models.CharField(max_length=50)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='popup/')
    text = models.TextField(max_length=100)
    width = models.CharField(max_length=10)
    height = models.CharField(max_length=10)
    popup_x = models.CharField(max_length=10)
    popup_y = models.CharField(max_length=10)
    popup_url = models.URLField()
    

#    def endPopup(self):
#        self.end_date = timezone.now()
#        self.save()
