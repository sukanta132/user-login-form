from django.db import models

# Create your models here.
class sukanta_user(models.Model):
    Username = models.CharField(max_length=200)
    PhoneNumber = models.CharField(max_length=50)
    email = models.EmailField()
    psw = models.CharField(max_length=200)
    pswrepeat = models.CharField(max_length=200)

    class Meta:
        db_table = "sukanta_user"

