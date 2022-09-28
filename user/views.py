from django.shortcuts import render, redirect
# render: html 파일을 화면에 보여줌

from .models import UserModel
# 지금 파일과 같은 위치에 있는 models라는 파일에서 UserModel을 가져온다
from django.http import HttpResponse
from django.contrib.auth import get_user_model
# 사용자가 데이터베이스 안에 있는지 검사하는 함수
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def sign_up_view(request): #리퀘스트가 들어옴
    if request.method == 'GET': #요청 방식이 겟이면
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signup.html') #화면을 보여주고(리퀘스트,템플릿이름)
    elif request.method == 'POST': # 포스트면  다른 거(데이터베이스 수정.추가.삭제같은 기능들)함
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        bio = request.POST.get('bio', '')

        if password != password2:
            return render(request, 'user/signup.html',{'error':'패스워드를 확인해주세요'})
        # 비밀번호가 다르면 회원가입 화면을 다시 띄워준다
        else:
            if username == '' or password == '':
                return render(request,'user/signup.html',{'error':'사용자의 이름과 비밀번호는 필수값입니다'})
            exist_user = get_user_model().objects.filter(username=username)
            # exist_user = UserModel.objects.filter(username=username)
            if exist_user:  # 무슨 뜻이지?? 0이 아니면 존재하는거니까??
                return render(request, 'user/signup.html',{'error':'사용자가 이미 존재합니다'})
            else:
                # new_user = UserModel()
                # new_user.username = username
                # new_user.password = password
                # new_user.bio = bio
                # new_user.save()
                UserModel.objects.create_user(username=username,password=password,bio=bio)
                return redirect('/sign-in')
        # 회원가입이 완료되면 로그인 페이지로 이동
        # render(request, user/signin.html)이랑 뭐가 다르지??


def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        # request.post에는 요청한 포스트 데이터가 모두 담겨있다 거기서 username, password를 가져온다
        # 화면에서 입력받은 정보를 장고 모듈로 넣어주고 검사하고 사용자가 있다면 me라는 변수에 정보를 넣어줌


        # 인증기능(암호화된 비번과 현재 입력된 비번, 그리고 사용자에 해당하는 비번이 맞는지 확인해줌)
        me = auth.authenticate(request, username=username, password=password)
        # => me = UserModel.objects.get(username=username)->user데이터가 데이터베이스에 있는지 확인하기
        if me is not None: # authenticate에서 모든걸 확인해주기때문에.. # 사용자가 있다면 (비어있지 않다면) 로그인시킨다
            auth.login(request, me)
            return redirect('/')
        else:
            return render(request,'user/signin.html',{'error':'유저이름 혹은 패스워드를 확인해주세요'})

    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signin.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required
def user_view(request):
    if request.method == 'GET':
        # 사용자를 불러오기, exclude와 request.user.username 를 사용해서 '로그인 한 사용자'를 제외하기
        user_list = UserModel.objects.all().exclude(username=request.user.username)
        return render(request, 'user/user_list.html', {'user_list': user_list})


@login_required
def user_follow(request, id):
    me = request.user #록인한 사용자
    click_user = UserModel.objects.get(id=id)
    if me in click_user.followee.all():
        click_user.followee.remove(request.user)
    else:
        click_user.followee.add(request.user)
    return redirect('/user')