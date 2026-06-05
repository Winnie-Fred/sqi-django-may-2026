from django.db import models

from django.core.validators import MaxValueValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


from authors.models import Author

User = get_user_model()

def published_on_not_before_1955(date_published):
    if date_published.year < 1955:
        raise ValidationError("Date published year must not be before 1955")

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255, validators=[MaxLengthValidator(200)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    number_of_pages = models.PositiveIntegerField(validators=[MaxValueValidator(1000)])
    published_on = models.DateField(validators=[published_on_not_before_1955])
    cover_image = models.ImageField(upload_to="cover_images/", blank=True, null=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return f"{self.title} by {self.author}"
    