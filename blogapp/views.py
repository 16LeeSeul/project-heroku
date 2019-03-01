from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogPost

def home(request):
    blogs = Blog.objects
    #블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 3)
    #request된 페이지가 뭔지를 알아내고(request페이지를 변수에 담아내고)
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})

def new(request): # new.html을 띄워주는 함수
    return render(request, 'new.html')

def create(request): # 입력받은 함수를 데이터베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()  # 쿼리셋 메소드 - 객체를 데이터베이스에 저장, 객체.delete()도 있음
    return redirect('/blog/blog/'+str(blog.id))

def blogpost(request):
    #1. 입력된 내용을 처리하는 기능 -> POST
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid(): 
            post = form.save(commit=False) 
            post.pub_date = timezone.now() 
            post.save()
            return redirect('home')
    #2. 빈 페이지를 띄워주는 기능 -> GET
    else:
        form = BlogPost() # 빈 객체
        return render(request, 'new.html', {'forms':form})

# redirect : 바로 창을 띄워라(프로젝트와 상관없는 url도 가능)
# render : 함수 내에서
# -> 결국 받는 인자에 따라서 달라짐

# Create your views here.

def index(request):
        return render(request, 'index.html')
