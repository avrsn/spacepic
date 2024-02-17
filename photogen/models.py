from django.core.exceptions import ValidationError
from django.db import models

# Create your models here. Remember the three-step guide to making model changes:

#    1 Change your models (in models.py).
#    2 Run python manage.py makemigrations to create migrations for those changes
#    3 Run python manage.py migrate to apply those changes to the database.  

class SessionZip(models.Model):
    session_id = models.CharField(max_length=12)
    file_download = models.FileField(upload_to='zip_files/', default="")