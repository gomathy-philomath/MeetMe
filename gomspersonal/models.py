from django.db import models

# Create your models here.
class book(models.Model):
    id = models.AutoField(primary_key=True)
    bookName = models.CharField(max_length=100)
    bookCover = models.CharField(max_length=200)
    bookAuthor = models.CharField(max_length=50)
    bookReview = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bookName

class photo(models.Model):
        id = models.AutoField(primary_key=True)
        photoName = models.CharField(max_length=100)
        photo = models.CharField(max_length=200)
        photoLocation = models.CharField(max_length=50)
        photoReview = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.photoName

