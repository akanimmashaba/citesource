from django.db import models

class MusicalScore(models.Model):
    # Common fields for all musical scores
    title = models.CharField(max_length=200)
    composer = models.CharField(max_length=100)
    publication_date = models.DateField()
    score_type = models.CharField(max_length=50, choices=[
        ('sheet_music', 'Sheet Music'),
        ('composition', 'Musical Composition'),
    ])
    instrument = models.CharField(max_length=100, blank=True, null=True)  # Instrumentation information (if applicable)
    url = models.URLField(blank=True, null=True)  # URL to access the musical score online (if available)

    def __str__(self):
        return self.title
