from hashlib import md5
from django.db import models
from django.db.models.signals import pre_save


class UrlShortener(models.Model):
    original_url = models.URLField(unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.original_url


def pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = md5(instance.original_url.encode()).hexdigest()[:10]


pre_save.connect(pre_save_reciever, sender=UrlShortener)
