from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.utils import timezone
from django.core.paginator import Paginator



from .models import Blog
from .forms import BlogPost
# Create your views here.

def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'myapp/home.html', {'blogs':blogs, 'posts':posts})

def blog(request):
    blogs = Blog.objects #QuerySet
    return render(request, 'myapp/blog.html', {'blogs':blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'myapp/detail.html', {'blog':blog_detail})
    #get_object_or_404 (대상 클래스, 검색조건)

def new(request):
    return render(request, 'myapp/new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.pk))

def about(request):
    return render(request, 'myapp/about.html')

def count(request):
    full_text = request.GET['fulltext']

    word_list = full_text.split()

    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary:
            # Increase
            word_dictionary[word] += 1
        else:
            # add to the dictionary
            word_dictionary[word] = 1

    word_dictionary = collections.OrderedDict(sorted(word_dictionary.items(), key=lambda x: x[1], reverse=True))
    usedwords = len(word_dictionary)
    return render(request, 'myapp/count.html', {'fulltext':full_text, 'total': len(word_list), 'dictionary':word_dictionary.items(), 'usedwords':usedwords})

def blogpost(request):
    if request.method=='POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else :
        form = BlogPost()
        return render(request, 'myapp/new.html', {'form':form})        

def handler404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response

