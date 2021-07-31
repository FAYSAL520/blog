from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib import messages
from .forms import *
from .models import *

# Create your views here.
def view(request, pk, tit):
    blog = Blog.objects.filter(id=pk, blog_title=tit)
    contex = {'blog':blog}

    return render(request, 'blogs/blogview.html', contex)


def index(request):
    blog = Blog.objects.all()
    contex = {'all_blog':blog}
    return render(request, 'blogs/index.html', contex)



# def contactb(request):
#     if request.method == "POST":
#         name = request.POST['name']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         content = request.POST['content']
#
#
#         contactb = Contact(name=name, email=email, phone=phone, content=content)
#         contactb.save()
#
#     return render(request, "blogs/contactb.html")



def contact_view(request):
    template = 'blogs/contactb.html'
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST, request.FILES)
        if contact_form.is_valid():
            contact_form.save()
        return HttpResponseRedirect('contactb')
    context = {
        'contact_form': contact_form
    }
    return render(request, template_name=template, context=context)


def create_post(request):
    template = 'blogs/addblog.html'
    blog_form = BlogForm()
    if request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES)
        if blog_form.is_valid():
            blog_form.save()
        return HttpResponseRedirect('http://localhost:8000/')
    context = {
        'blog_form': blog_form
    }
    return render(request, template_name=template, context=context)

# def addblog(request):
#     if request.method == 'POST':
#         blog_title = request.POST['blog_title']
#         blog_short_description = request.POST['blog_short_description']
#         blog_category = request.POST['blog_category']
#         blog_subcategory = request.POST['blog_subcategory']
#         blog_image = request.POST['blog_image']
#         blog_desc = request.POST['blog_desc']
#         pub_date = request.POST['pub_date']
#         views = request.POST['views']
#
#
#         addblog = Blog(blog_title=blog_title, blog_short_description=blog_short_description, blog_category=blog_category, blog_subcategory=blog_subcategory, blog_image=blog_image, blog_desc=blog_desc, pub_date=pub_date, views=views)
#         addblog.save()
#
#     return render(request, 'blogs/addblog.html')











# def create_post(request):
#     template = 'blogs/addblog.html'
#     post_form = ModelPost()
#     if request.method == 'POST':
#         post_form = ModelPost(request.POST, request.FILES)
#         if post_form.is_valid():
#             post_form.save()
#         return redirect('http://localhost:8000/')
#     context = {
#         'post_form': post_form
#     }
#     return render(request, template_name=template, context=context)




# def edit_post(request, pk):
#
#     template = 'blogs/editblog.html'
#
#     if request.method == 'POST':
#         post = get_object_or_404(Blog, id=pk)
#         editpost = ModelPost(request.POST, request.FILES, instance=post)
#         editpost.save()
#         return redirect('http://localhost:8000/')
#     else:
#         post = get_object_or_404(Blog, id=pk)
#         editpost = ModelPost(instance=post)
#
#     context = {
#         'post_form': editpost,
#
#     }
#
#     return render(request, template_name=template, context=context)