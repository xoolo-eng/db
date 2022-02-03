from django.db import models
from user.models import User
from django.db.models.signals import pre_save, pre_delete
from django.dispatch.dispatcher import receiver
from random import randint
from datetime import datetime
from django.conf import settings
import os


class Post(models.Model):
    def file_path(self, filename):
        file_type = filename.split(".")[-1]
        path_file = datetime.strftime(datetime.now(), "post/%Y/%m/%d/%H/")
        return path_file + str(randint(100000000, 999999999)) + "." + file_type

    title = models.CharField(max_length=256, unique=True, verbose_name="Post title")
    tags = models.ManyToManyField("Tag", related_name="posts")
    author = models.ForeignKey(
        User,
        related_name="posts",
        on_delete=models.CASCADE,
        verbose_name="Post author",
    )
    text = models.TextField(verbose_name="Post data")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Post created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Post update")
    is_moderated = models.BooleanField(default=False)
    views = models.BigIntegerField(default=0)
    image = models.ImageField(upload_to=file_path)
    slug = models.SlugField(max_length=256, unique=True, verbose_name="Link to Post")

    def __str__(self) -> str:
        return (self.title[:20] + "...") if len(self.title) > 20 else self.title

    class Meta:
        db_table = "posts"
        verbose_name = "Post"
        ordering=("-id",)


class Tag(models.Model):
    value = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.value

    class Meta:
        db_table = "tags"
        verbose_name = "Tag"


@receiver(pre_delete, sender=Post)
def hash_passwd(sender, instance, **kwargs):
    path_to_file = settings.BASE_DIR / str(instance.image.path)
    try:
        path_to_file.unlink()
    except Exception:
        print("HON FOUND")


@receiver(pre_save, sender=Post)
def to_url(sender, instance, **kwargs):
    def ttu(title):
        return title.replace(" ", "_").lower()

    if (instance.id is None) or (instance.url != ttu(instance.title)):
        instance.url = ttu(instance.title)
        print(instance.url, "\n\n\n")


@receiver(pre_save, sender=Tag)
def sharp(sender, instance, **kwargs):
    if instance.value[0] != "#":
        instance.value = "#" + instance.value
