from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField



# Create your models here.

class BlogsCategory(models.Model):
    category = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.category


class BlogSubCategory(models.Model):
    category = models.ForeignKey(BlogsCategory, on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=100)

    def __str__(self):
        return self.subcategory


class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_short_description = models.TextField(max_length=500)
    blog_category = models.ForeignKey(BlogsCategory, on_delete=models.CASCADE)
    blog_subcategory = models.ForeignKey(BlogSubCategory, on_delete=models.CASCADE)
    blog_image = models.ImageField(upload_to="blogs/images", default="")
    blog_desc = RichTextUploadingField(blank=True, null=True)
    pub_date = models.DateTimeField('date published')
    views = models.IntegerField(default=0)


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
