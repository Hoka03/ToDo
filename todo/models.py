from django.db import models


class ToDO(models.Model):
    title = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title