from django.db import models

class PersonalCorrespondence(models.Model):
    # Common fields for all types of personal correspondence
    title = models.CharField(max_length=200)
    sender = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100)
    communication_date = models.DateField()
    correspondence_type = models.CharField(max_length=50, choices=[
        ('interview', 'Interview'),
        ('letter', 'Letter'),
        ('email', 'Email'),
    ])
    content = models.TextField()
    
    def __str__(self):
        return self.title
