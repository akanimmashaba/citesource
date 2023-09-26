from django.db import models

class UnpublishedWork(models.Model):
    # Common fields for all unpublished works
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    work_type = models.CharField(max_length=50, choices=[
        ('research_paper', 'Unpublished Research Paper'),
        ('manuscript', 'Unpublished Manuscript'),
        ('personal_notes', 'Personal Notes'),
    ])
    content = models.TextField()

    def __str__(self):
        return self.title
