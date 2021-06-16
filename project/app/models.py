from django.db import models


# Create your models here.

class demo(models.Model):
    a = models.TextField(default="null", null=True)
    b = models.IntegerField(default=0)
    c = models.IntegerField(default=0)
    d = models.IntegerField(default=0)
    e = models.IntegerField(default=0)
    f = models.IntegerField(default=0)
    g = models.IntegerField(default=0)
    h = models.IntegerField(default=0)
    i = models.IntegerField(default=0)
    j = models.IntegerField(default=0)
    k = models.IntegerField(default=0)
    l = models.IntegerField(default=0)
    m = models.IntegerField(default=0)
    n = models.IntegerField(default=0)
    o = models.IntegerField(default=0)
    p = models.IntegerField(default=0)
    q = models.IntegerField(default=0)
    r = models.IntegerField(default=0)
    s = models.IntegerField(default=0)

    def __str__(self):
        return self.a
