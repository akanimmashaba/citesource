from django.db import models

class GovernmentPublication(models.Model):
    # Common fields for all government publications
    title = models.CharField(max_length=200)
    government_agency = models.CharField(max_length=200)  # The government agency responsible for the publication
    publication_date = models.DateField()
    publication_type = models.CharField(max_length=50, choices=[
        ('report', 'Government Report'),
        ('agency_publication', 'Government Agency Publication'),
        ('gazette', 'Government Gazette'),
    ])
    document_number = models.CharField(max_length=50, blank=True, null=True)  # Document or report number (if available)
    url = models.URLField(blank=True, null=True)  # URL to access the publication online (if available)

    def __str__(self):
        return self.title
