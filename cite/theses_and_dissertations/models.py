from django.db import models

class ThesisDissertation(models.Model):
    # Common fields for all theses and dissertations
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    institution = models.CharField(max_length=200)  # The academic institution where the work was submitted
    year = models.IntegerField()
    type = models.CharField(max_length=50, choices=[('master', 'Master\'s Thesis'), ('doctoral', 'Doctoral Dissertation')])
    advisor = models.CharField(max_length=100)  # Advisor or supervisor for the work
    abstract = models.TextField()  # Abstract of the work
    url = models.URLField(blank=True, null=True)  # URL to access the work online (if available)

    def __str__(self):
        return self.title
