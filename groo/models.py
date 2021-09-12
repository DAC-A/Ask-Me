from django.db import models

class NewUser(models.Model):
    username=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.username
