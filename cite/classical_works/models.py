from django.db import models

class ClassicalWork(models.Model):
    # Common fields for all classical works
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, blank=True, null=True)  # Author of the work (if known)
    original_language = models.CharField(max_length=50, blank=True, null=True)  # Original language of the work
    publication_year = models.IntegerField()
    work_type = models.CharField(max_length=50, choices=[
        ('ancient_text', 'Ancient Text or Classical Literature'),
        ('translation', 'Work in Translation'),
    ])
    translator = models.CharField(max_length=100, blank=True, null=True)  # Translator's name (if applicable)
    url = models.URLField(blank=True, null=True)  # URL to access the work online (if available)

    def __str__(self):
        return self.title
