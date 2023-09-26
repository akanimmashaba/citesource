from django.db import models

class Media(models.Model):
    # Common fields for all audiovisual and other media
    title = models.CharField(max_length=200)
    creator = models.CharField(max_length=100)
    publication_date = models.DateField()
    media_type = models.CharField(max_length=50, choices=[
        ('film', 'Film'),
        ('documentary', 'Documentary'),
        ('tv_series', 'Television Series'),
        ('podcast', 'Podcast'),
        ('artwork', 'Artwork'),
        ('photograph', 'Photograph'),
        ('social_media_content', 'Social Media Content'),
    ])
    description = models.TextField()
    url = models.URLField(blank=True, null=True)  # URL to access the media online (if available)

    def __str__(self):
        return self.title
