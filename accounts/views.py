from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # user 클래스를 가져옴
from django.contrib import auth # 계정의 권한을 가져옴
# Create your views here.


def signup(request):
    if request.method == 'POST':  # request의 방식이 post 일 때
        if request.POST['password1'] == request.POST['password2']: # 첫번째로 입력한 비밀번호와 두번째로 입력한 비밀번호
            user = User.objects.create_user(  # user 함수에서 새로 유저를 만드는 함수를 씀
                request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)  # 바로 로그인을 하게 만듦
            return redirect('home') # 로그인을 하면 blog 페이지로 돌아가도록 함
    return render(request, 'signup.html')   # 실패하면 그대로 signup에 머물음


# def login(request):
#     if request.method == 'POST':
# 		username = request.POST['username']
# 		password = request.POST['password']
#         user = auth.authenticate(request, username=username, password=password)  
#         if user is not None:  # 회원이 존재하지 않다면, none으로 return, 존재한다면 아래 코드 실행
#             auth.login(request, user)   # 로그인 함
#             return redirect('home')   # home 페이지로 감
#         else:
#             return render(request, 'login.html', {'error': 'username or password is incorrect.'})
#     else:
#         return render(request, 'login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        redirect('home')
    return render(request, 'login.html')