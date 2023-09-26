from django.db import models

class LectureNotes(models.Model):
    # Common fields for all lecture notes
    title = models.CharField(max_length=200)
    course_name = models.CharField(max_length=100)
    lecturer = models.CharField(max_length=100)
    publication_date = models.DateField()
    content = models.TextField()
    platform = models.CharField(max_length=100, blank=True, null=True)  # Name of the LMS or online course platform (if applicable)

    def __str__(self):
        return self.title
