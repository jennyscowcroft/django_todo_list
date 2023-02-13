# todo_list/todo_app/models.py
from django.utils import timezone

from django.db import models
from django.urls import reverse
from datetime import datetime


def in_one_week():
    return timezone.now() + timezone.timedelta(days=7)


class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title


class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=in_one_week)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    def is_overdue(self):
        return bool(self.due_date and self.due_date < timezone.now())

    class Meta:
        ordering = ["due_date"]
