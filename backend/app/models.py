from django.db import models

class Jobs(models.Model):
    job = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.job + ' | ' + self.location


