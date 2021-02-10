from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=40)

    class Meta:
        db_table = 'companies'

class Image(models.Model):
    image = models.URLField(null=True)

    class Meta:
        db_table = 'images'

class Car(models.Model):
    username         = models.ForeignKey('user.User', on_delete=models.CASCADE)
    name             = models.CharField(max_length=30)
    accident_history = models.BooleanField(default=False)
    price            = models.IntegerField()
    create_at        = models.DateTimeField(auto_now_add=True)
    update_at        = models.DateTimeField(auto_now=True)
    company          = models.ForeignKey('Company', on_delete=models.CASCADE, blank=True, null=True)
    image            = models.ForeignKey('Image', on_delete=models.CASCADE, blank=True, null=True)

    class Mete:
        db_table = 'cars'

