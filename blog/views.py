from django.shortcuts import render
# from .models import Blog

# Create your views here.


# def blog_home(request):
#     if request.method == "POST":
#         tag = request.POST.get('tag')
#         searchstr = Blog.objects.filter(tag=tag)
#         return render(request, 'blog/blog.html', {'data': searchstr})
#     else:
#         blogdisplay = Blog.objects.all()
#         return render(request, 'blog/blog.html', {'data': blogdisplay})

#     blogdisplay = Blog.objects.all()
#     return render(request, 'blog/blog.html', {'data': blogdisplay})
