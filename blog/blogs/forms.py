from django.forms import ModelForm
from django import forms

from .models import *


class ModelPost(forms.ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        name = models.CharField(max_length=255)
        phone = models.CharField(max_length=13)
        email = models.EmailField(max_length=100)
        content = models.TextField()
        timeStamp = models.DateTimeField(auto_now_add=True, blank=True)


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        blog_title = models.CharField(max_length=100)
        blog_short_description = models.TextField(max_length=500)
        blog_category = models.ForeignKey(BlogsCategory, on_delete=models.CASCADE)
        blog_subcategory = models.ForeignKey(BlogSubCategory, on_delete=models.CASCADE)
        blog_image = models.ImageField(upload_to="blogs/images", default="")
        blog_desc = RichTextUploadingField(blank=True, null=True)
        pub_date = models.DateTimeField('date published')
        views = models.IntegerField(default=0)