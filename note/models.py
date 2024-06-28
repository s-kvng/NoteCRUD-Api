from django.db import models

# Create your models here.


class Note(models.Model):
    body = models.TextField(max_length=2200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.body

    class Meta:
        ordering = ["-created_at"]
