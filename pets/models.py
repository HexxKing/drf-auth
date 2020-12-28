from django.db import models
from django.contrib.auth import get_user_model

class Pet(models.Model):
  name = models.CharField(max_length=50)
  human = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  about = models.TextField()

  def __str__(self):
    return self.name
