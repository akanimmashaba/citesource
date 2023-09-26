from django.db import models

# Create your models here.
class Book(models.Model):
    # Common fields for all book types
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    isbn = models.CharField(max_length=13)  # ISBN (International Standard Book Number)

    # Fields specific to certain book types
    is_single_author = models.BooleanField(default=True)  # Indicates if it's a single-authored book
    is_edited = models.BooleanField(default=False)  # Indicates if it's an edited book
    editor = models.CharField(max_length=100, blank=True, null=True)  # Editor's name (if edited)
    is_translated = models.BooleanField(default=False)  # Indicates if it's a translated book
    translator = models.CharField(max_length=100, blank=True, null=True)  # Translator's name (if translated)
    is_multi_volume = models.BooleanField(default=False)  # Indicates if it's a multi-volume book
    volume_number = models.PositiveIntegerField(blank=True, null=True)  # Volume number (if multi-volume)
    is_ebook = models.BooleanField(default=False)  # Indicates if it's an e-book
    is_audiobook = models.BooleanField(default=False)  # Indicates if it's an audiobook

    # Additional fields for e-books and audiobooks
    format = models.CharField(max_length=50, blank=True, null=True)  # E-book or audiobook format (e.g., PDF, MP3)
    url = models.URLField(blank=True, null=True)  # URL to access the e-book or audiobook online

    def __str__(self):
        return self.title