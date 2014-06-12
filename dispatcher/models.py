from django.db import models

# Create your models here.


class Owner(models.Model):
    name    = models.CharField(max_length=20)
    email   = models.EmailField(max_length=70)
    passwd  = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name

class Machine(models.Model):
    hostname = models.CharField(max_length=40)
    dtlref   = models.CharField(max_length=100, blank=True, null=True)
    arch     = models.CharField(max_length=20)
    os       = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    status   = models.CharField(max_length=10)
    note     = models.TextField(blank=True, null=True)
    owner  = models.ForeignKey(Owner)

    def __unicode__(self):
        return self.hostname
