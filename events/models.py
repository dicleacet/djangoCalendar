from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

# Create your models here.
class Event(models.Model):
    start_time = models.DateTimeField("start time")
    end_time = models.DateTimeField("end time")
    title = models.CharField("event", max_length=50)
    description = models.TextField("description")

    class Meta:
        verbose_name = "Event Data"
        verbose_name_plural = "Event Data"

    def __str__(self):
        return self.title

    @property
    def get_html_url(self):
        url = reverse('edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'