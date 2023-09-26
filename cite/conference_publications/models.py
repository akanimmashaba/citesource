from django.db import models

class ConferencePublication(models.Model):
    # Common fields for all conference publications
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField('Author', related_name='conference_publications')
    conference_name = models.CharField(max_length=200)
    conference_date = models.DateField()
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, blank=True, null=True)  # ISBN of the conference proceedings (if available)
    url = models.URLField(blank=True, null=True)  # URL to access the publication online (if available)

    class Meta:
        abstract = True  # This makes it an abstract base class

class ConferencePaper(ConferencePublication):
    # Fields specific to conference papers published in proceedings
    proceedings_title = models.CharField(max_length=200)  # Title of the conference proceedings

class OnlineConferencePaper(ConferencePublication):
    # Fields specific to conference papers published online
    online_source_name = models.CharField(max_length=200)  # Name of the online platform or source where the paper is hosted
