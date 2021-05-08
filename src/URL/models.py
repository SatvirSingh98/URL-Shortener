from hashlib import md5
from django.db import models
from django.db.models.signals import pre_save


class UrlShortener(models.Model):
    original_url = models.URLField(unique=True, db_index=True)
    slug = models.SlugField(unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_url


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = md5(instance.original_url.encode()).hexdigest()[:8]
    qs = instance.__class__.objects.filter(slug=slug)
    if qs.exists():
        new_slug = md5(instance.original_url.encode()).hexdigest()[:8]
        return unique_slug_generator(instance, new_slug)
    return slug


def pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_reciever, sender=UrlShortener)
