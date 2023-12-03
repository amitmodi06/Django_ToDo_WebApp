from django.db import models

# Create your models here.
class Todo_Task(models.Model):
    """Model representing a task."""
    task = models.CharField(max_length=500, help_text="Enter a to do task")

    class Meta:
        pass

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        """Returns the url to access a particular task instance."""
        return reverse("task-detail", args-[str(self.id)])
