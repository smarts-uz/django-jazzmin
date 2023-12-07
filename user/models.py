from django.db import models

# Create your models here.
class Profile(models.Model):
    f_name = models.CharField(verbose_name='First name',max_length=112)
    l_name = models.CharField(verbose_name='Last name',max_length=112)
    email = models.CharField(verbose_name='Email',max_length=112)

    def __str__(self):
        return self.f_name


