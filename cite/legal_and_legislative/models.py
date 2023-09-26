from django.db import models

class LegalDocument(models.Model):
    # Common fields for all legal and legislative sources
    title = models.CharField(max_length=200)
    jurisdiction = models.CharField(max_length=100)  # Jurisdiction or country where the legal document applies
    publication_date = models.DateField()
    source_type = models.CharField(max_length=50, choices=[
        ('act', 'Act or Statute'),
        ('law_report', 'Law Report'),
    ])
    document_number = models.CharField(max_length=50, blank=True, null=True)  # Document or report number (if available)
    url = models.URLField(blank=True, null=True)  # URL to access the document online (if available)

    class Meta:
        abstract = True  # This makes it an abstract base class

class ActStatute(LegalDocument):
    # Fields specific to acts and statutes
    legislative_body = models.CharField(max_length=200)  # The legislative body that passed the act or statute
    document_type = models.CharField(max_length=100)  # Type of legal document (e.g., Act, Statute)

class LawReport(LegalDocument):
    # Fields specific to law reports
    reporter_name = models.CharField(max_length=200)  # Name of the law reporter

    def __str__(self):
        return self.title
