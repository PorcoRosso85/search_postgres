from django.db import models

class Quote(models.Model):
    name = models.CharField(max_length=200)
    quote = models.TextField(max_length=2000)

    #def __str__(self):
    #    return self.quote
