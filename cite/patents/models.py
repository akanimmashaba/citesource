from django.db import models

class Patent(models.Model):
    # Common fields for all patents and patent applications
    title = models.CharField(max_length=200)
    inventors = models.ManyToManyField('Inventor', related_name='patents')
    patent_number = models.CharField(max_length=50)
    filing_date = models.DateField()
    publication_date = models.DateField()
    url = models.URLField(blank=True, null=True)  # URL to access the patent online (if available)

    class Meta:
        abstract = True  # This makes it an abstract base class

class Inventor(models.Model):
    # Inventor information
    name = models.CharField(max_length=100)
    # Add more inventor-related fields as needed

class GrantedPatent(Patent):
    # Fields specific to granted patents

class PatentApplication(Patent):
    # Fields specific to patent applications
    application_number = models.CharField(max_length=50)
    application_status = models.CharField(max_length=100)  # Status of the patent application (e.g., pending, granted)

    def __str__(self):
        return self.title
