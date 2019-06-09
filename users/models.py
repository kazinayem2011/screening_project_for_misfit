from __future__ import unicode_literals

from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import SmartResize
from imagekit.conf import ImageKitConf
from auditlog.registry import auditlog


class Role(models.Model):
    role_title = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.role_title

    def as_json(self):
        return dict(
            role_title=str(self.role_title),
        )


class User(models.Model):
    ImageKitConf.CACHEFILE_DIR = 'uploads/200/'
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='uploads/800/', default='uploads/800/default.png')
    thumb = ImageSpecField(
        source='photo',
        processors=[SmartResize(200, 200)],
    )
    role = models.ForeignKey('Role', default=1, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def as_json(self):
        return dict(
            first_name=str(self.first_name),
            last_name=str(self.last_name),
            email=str(self.email),
            photo=str(self.photo),
            role_id=self.role_id,
            is_active=(self.is_active),
        )

    def is_authenticated(self):
        pass


auditlog.register(User)
auditlog.register(Role)
