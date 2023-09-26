from django.db import models

class JournalArticle(models.Model):
    # Common fields for all journal article types
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    journal_name = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    volume = models.CharField(max_length=20)
    issue = models.CharField(max_length=20)
    page_range = models.CharField(max_length=20)
    doi = models.CharField(max_length=100, blank=True, null=True)  # Digital Object Identifier
    url = models.URLField(blank=True, null=True)  # URL to access the article online

    # Fields specific to journal articles "in press"
    is_in_press = models.BooleanField(default=False)  # Indicates if the article is "in press"
    publication_status = models.CharField(max_length=50, blank=True, null=True)  # Status of the article (e.g., "in press," "forthcoming")

    # Fields specific to abstracts of journal articles
    is_abstract = models.BooleanField(default=False)  # Indicates if it's an abstract
    full_article_url = models.URLField(blank=True, null=True)  # URL to access the full article (if available)

    def __str__(self):
        return self.title
