from django.db import models

class OnlineSource(models.Model):
    # Common fields for all online sources
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, blank=True, null=True)
    publication_date = models.DateField()
    url = models.URLField()

    class Meta:
        abstract = True  # This makes it an abstract base class

class Website(OnlineSource):
    # Fields specific to websites
    website_name = models.CharField(max_length=200)

class WebArticle(OnlineSource):
    # Fields specific to web articles or blog posts
    source_name = models.CharField(max_length=200)  # Name of the website or blog

class OnlineReport(OnlineSource):
    # Fields specific to online reports and whitepapers
    organization = models.CharField(max_length=200)  # Organization or institution that published the report

class OnlineNewsletter(OnlineSource):
    # Fields specific to online newsletters
    newsletter_name = models.CharField(max_length=200)

class Citation(models.Model):
    # Common fields for all citations
    source = models.ForeignKey(OnlineSource, on_delete=models.CASCADE)
    # Other fields related to citations, e.g., page numbers, specific section, etc.


class NewspaperArticle(models.Model):
    # Common fields for all newspaper and magazine articles
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, blank=True, null=True)
    publication_date = models.DateField()
    newspaper_name = models.CharField(max_length=200)

    class Meta:
        abstract = True  # This makes it an abstract base class

class PrintedNewspaperArticle(NewspaperArticle):
    # Fields specific to printed newspaper articles
    page_number = models.CharField(max_length=20)

class OnlineNewspaperArticle(NewspaperArticle):
    # Fields specific to online newspaper articles
    url = models.URLField()

class MagazineArticle(models.Model):
    # Common fields for all magazine articles
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, blank=True, null=True)
    publication_date = models.DateField()
    magazine_name = models.CharField(max_length=200)

    class Meta:
        abstract = True  # This makes it an abstract base class

class PrintedMagazineArticle(MagazineArticle):
    # Fields specific to printed magazine articles
    page_number = models.CharField(max_length=20)

class OnlineMagazineArticle(MagazineArticle):
    # Fields specific to online magazine articles
    url = models.URLField()
