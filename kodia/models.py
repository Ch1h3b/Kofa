from email.policy import default
from django.db.models import Model, CharField, BooleanField


# Create your models here.

class Kufa(Model):
    name = CharField(max_length=40)
    phone = CharField(max_length=10)
    adress = CharField(max_length=300)
    items = CharField(max_length= 500)
    taken = BooleanField(default=False)
    done = BooleanField(default=False)
    user = CharField(max_length=32)


