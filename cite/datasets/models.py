from django.db import models

class Dataset(models.Model):
    # Common fields for all datasets
    title = models.CharField(max_length=200)
    creator = models.CharField(max_length=100)
    publication_date = models.DateField()
    description = models.TextField()
    dataset_type = models.CharField(max_length=50, choices=[
        ('research_data', 'Research Data'),
        ('dataset', 'Dataset'),
    ])
    url = models.URLField(blank=True, null=True)  # URL to access the dataset online (if available)

    def __str__(self):
        return self.title

