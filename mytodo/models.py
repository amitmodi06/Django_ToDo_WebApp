from django.db import models

# Create your models here.
class Todo_Task(models.Model):
    """Model representing a task."""
    task = models.CharField(max_length=100, help_text="Enter a to do task")
    is_done = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        """Returns the url to access a particular task instance."""
        return reverse("task-detail", args-[str(self.id)])
