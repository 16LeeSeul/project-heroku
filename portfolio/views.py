from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Portfolio
from .forms import PortfolioPost
from django.utils import timezone



def portfolio(request):
    portfolios = Portfolio.objects
    portfolios_list = Portfolio.objects.all()
    paginator = Paginator(portfolios_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'portfolio.html', {'portfolios' :portfolios})

    
def create(request): # 입력받은 함수를 데이터베이스에 넣어주는 함수
    portfoilo = PortfolioPost()
    portfoilo.title = request.POST['title']
    portfoilo.image = request.POST['image']
    portfoilo.description = request.POST['description']
    portfoilo.save()  # 쿼리셋 메소드 - 객체를 데이터베이스에 저장, 객체.delete()도 있음
    return redirect('portfolio')

def new(request):
    if request.method == 'POST':
        form = PortfolioPost(request.POST)
        if form.is_valid(): 
            post = form.save(commit=False) 
            post.save()
            return redirect('portfolio')
    #2. 빈 페이지를 띄워주는 기능 -> GET
    else:
        form = PortfolioPost() # 빈 객체
        return render(request, 'new.html', {'forms':form})

# Create your views here.
