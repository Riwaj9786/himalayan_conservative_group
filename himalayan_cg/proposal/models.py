from django.db import models
from datetime import datetime

# Create your models here.
class Proposal(models.Model):
    full_name = models.CharField(max_length=155)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    project = models.CharField(max_length=255, help_text="Write your Project Name!")
    proposal_document = models.FileField(upload_to='projects/proposal/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)
    project_year = models.IntegerField(default=datetime.now().year, help_text="Enter the project year (e.g., 2024)")

    class Meta:
        unique_together = ('email', 'project_year')

    def __str__(self):
        return f"{self.full_name}_{self.project}"