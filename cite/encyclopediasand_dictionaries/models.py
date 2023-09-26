from django.db import models

class ReferenceSource(models.Model):
    # Common fields for all reference sources
    title = models.CharField(max_length=200)
    editor = models.CharField(max_length=100, blank=True, null=True)  # Editor(s) of the reference source
    publication_year = models.IntegerField()
    source_type = models.CharField(max_length=50, choices=[
        ('print_encyclopedia', 'Print Encyclopedia'),
        ('online_encyclopedia', 'Online Encyclopedia'),
        ('dictionary', 'Dictionary'),
    ])
    isbn = models.CharField(max_length=13, blank=True, null=True)  # ISBN of the reference source (if available)
    url = models.URLField(blank=True, null=True)  # URL to access the online source (if available)

    class Meta:
        abstract = True  # This makes it an abstract base class

class PrintedEncyclopedia(ReferenceSource):
    # Fields specific to printed encyclopedias
    pass

class OnlineEncyclopedia(ReferenceSource):
    # Fields specific to online encyclopedias
    pass

class Dictionary(ReferenceSource):
    # Fields specific to dictionaries
    dictionary_type = models.CharField(max_length=50, choices=[
        ('author_dictionary', 'Dictionary with Author(s)'),
        ('editor_dictionary', 'Dictionary with Editor(s)'),
    ])
    # Other fields specific to dictionary types

    def __str__(self):
        return self.title
