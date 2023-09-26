from django.db import models

# Create your models here.



class Chapter(models.Model):
    # Common fields for all chapter types
    title = models.CharField(max_length=200)
    book_title = models.CharField(max_length=200)  # Title of the edited book
    editor = models.CharField(max_length=100)  # Editor(s) of the edited book
    publication_year = models.IntegerField()
    pages = models.CharField(max_length=20)  # Page range within the book
    isbn = models.CharField(max_length=13)  # ISBN of the edited book

    # Fields specific to book chapters with a single author
    is_single_author = models.BooleanField(default=True)  # Indicates if it's a single-authored chapter
    author = models.CharField(max_length=100)  # Author's name (if single-authored)

    # Fields specific to book chapters with multiple authors
    is_multi_author = models.BooleanField(default=False)  # Indicates if it's a multi-authored chapter
    authors = models.ManyToManyField('Author', related_name='chapters')  # Many-to-many relationship with Author model

    def __str__(self):
        return self.title

class Author(models.Model):
    # Author information
    name = models.CharField(max_length=100)
    # Add more author-related fields as needed

    def __str__(self):
        return self.name
