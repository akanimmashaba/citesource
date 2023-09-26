from django.db import models

class ReligiousText(models.Model):
    # Common fields for all religious texts
    title = models.CharField(max_length=200)
    religion = models.CharField(max_length=100)  # Religion to which the text belongs
    author = models.CharField(max_length=100, blank=True, null=True)  # Author of the text (if applicable)
    publication_year = models.IntegerField()
    text_type = models.CharField(max_length=50, choices=[
        ('bible', 'The Bible'),
        ('quran', 'The Quran'),
        ('other', 'Other Religious Writing'),
    ])
    translation = models.CharField(max_length=200, blank=True, null=True)  # Translation or version of the text (if applicable)
    url = models.URLField(blank=True, null=True)  # URL to access the text online (if available)

    def __str__(self):
        return self.title
