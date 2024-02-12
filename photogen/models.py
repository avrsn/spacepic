from django.db import models

# Create your models here. Remember the three-step guide to making model changes:

#    1 Change your models (in models.py).
#    2 Run python manage.py makemigrations to create migrations for those changes
#    3 Run python manage.py migrate to apply those changes to the database.

class RandomImage(models.Model):
    image_num = models.PositiveSmallIntegerField()
    image_url = models.ImageField() #https://docs.djangoproject.com/en/5.0/ref/models/fields/#field-options
    