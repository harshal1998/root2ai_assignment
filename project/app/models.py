from django.db import models


# Create your models here.

class demo(models.Model):
    a = models.TextField()
    b = models.IntegerField()
    c = models.IntegerField()
    d = models.IntegerField()
    e = models.IntegerField()
    f = models.IntegerField()
    g = models.IntegerField()
    h = models.IntegerField()
    i = models.IntegerField()
    j = models.IntegerField()
    k = models.IntegerField()
    l = models.IntegerField()
    m = models.IntegerField()
    n = models.IntegerField()
    o = models.IntegerField()
    p = models.IntegerField()
    q = models.IntegerField()
    r = models.IntegerField()
    s = models.IntegerField()

    def __str__(self):
        return self.a
