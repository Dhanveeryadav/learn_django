from django.db import models

# Create your models here.
# model form
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()

    # clean or validator method which will clean or valid the data enter by user.
    def clean_title(self):
        cleaned_data = self.cleaned_data # it will return dictionary 
        # print(cleaned_data)
        title = cleaned_data.get("title")
        # print(title)
        return title