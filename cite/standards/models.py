from django.db import models

class Standard(models.Model):
    # Common fields for all industry standards and specifications
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)  # The organization responsible for the standard
    publication_date = models.DateField()
    standard_number = models.CharField(max_length=50)
    url = models.URLField(blank=True, null=True)  # URL to access the standard online (if available)

    def __str__(self):
        return self.title
