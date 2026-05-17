from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class Resource(models.Model):
    RESOURCE_TYPES = [
        ('Notes', 'Notes'),
        ('PYQ', 'PYQ'),
        ('Quiz', 'Quiz'),
        ('Assignment', 'Assignment'),
        ('Lab File', 'Lab File'),
    ]
    SEMESTER_CHOICES = [
        ('1', 'Semester 1'),
        ('2', 'Semester 2'),
        ('3', 'Semester 3'),
        ('4', 'Semester 4'),
        ('5', 'Semester 5'),
        ('6', 'Semester 6'),
        ('7', 'Semester 7'),
        ('8', 'Semester 8'),
    ]
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    resource_type = models.CharField(
        max_length=50,
        choices=RESOURCE_TYPES
    )
    semester = models.CharField(
        max_length=10,
        choices=SEMESTER_CHOICES
    )
    description = models.TextField()
    file = models.FileField(upload_to='notes/')
    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    upload_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    resource = models.ForeignKey(
        Resource,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    text = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.resource.title}"