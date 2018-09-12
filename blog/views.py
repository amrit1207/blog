from django.shortcuts import render,get_object_or_404
from .models import Blog


def allblogs(request):
    detailsblog=Blog.objects
    return render(request,'blog/blog.html',{'detailsblog':detailsblog})

def alldetails(request,blog_id):
    details=get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/details.html',{'blogdetails':details})
