from django.db import models

import datetime



PRIORITY_CHOICES = (
  (1, 'Low'),
  (2, 'Normal'),
  (3, 'High'),
)

STATE_CHOICES = (
  (1, 'Todo'),
  (2, 'Doing'),
  (3, 'Done'),
)


class Item(models.Model):
    title = models.CharField(max_length=250, unique=True)
    created_date = models.DateTimeField(default=datetime.datetime.now)
    due_date = models.DateTimeField()
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    completed = models.BooleanField(default=False)
    state = models.IntegerField(choices=STATE_CHOICES, default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-priority', 'title']

    class Admin:
        pass
