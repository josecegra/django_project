from django.db import models
from django.urls import reverse
# Create your models here.
class Hashtag(models.Model):
    input_text       = models.CharField(max_length=120) # max_length = required


    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id}) #f"/products/{self.id}/"

class Image(models.Model):
    image = models.ImageField(upload_to='media',blank=True)