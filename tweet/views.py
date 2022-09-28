from django.shortcuts import render, redirect
from .models import TweetModel
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, TemplateView
# Create your views here.

def home(request):
    user = request.user.is_authenticated
    # user가 로그인이 되어있는 상태인지, 인증이 되어있는 상태인지 확인가능
    if user:
        #user 가 있다면
        return redirect('/tweet')
        # 저 url로 리다이렉트
    else:
        return redirect('/sign-in')
        # 없으면 다시 로그인화면으로


def tweet(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        # 사용자가 로그인이 되어있는지 확인
        if user:
        # 로그인한 사용자가 있다면
            all_tweet = TweetModel.objects.all().order_by('-created_at')
            #역순정렬
            return render(request, 'tweet/home.html',{'tweet':all_tweet})
            #딕셔너리 현태
        else:
        # 직접 들어왓다면 로그인페이지로 이동
            return redirect('/sign-in')
    elif request.method == 'POST':
        user = request.user
        content = request.POST.get('my-content','')
        tags = request.POST.get('tag','').split(',')
        if content == '':
            all_tweet = TweetModel.objects.all().order_by('-created_at')
            return render(request,'tweet/home.html',{'error':'글은 공백일 수 없습니다','tweet':all_tweet})
        else:
            my_tweet = TweetModel.objects.create(author=user,content=content)
            for tag in tags:
                tag = tag.strip()
                if tag != '':
                    my_tweet.tags.add(tag)
            my_tweet.save()
            return redirect('/tweet')

@login_required
def delete_tweet(request, id):
    my_tweet = TweetModel.objects.get(id=id)
    my_tweet.delete()
    return redirect('/tweet')

class TagCloudTV(TemplateView):
    template_name = 'taggit/tag_cloud_view.html'


class TaggedObjectLV(ListView):
    template_name = 'taggit/tag_with_post.html'
    model = TweetModel

    def get_queryset(self):
        return TweetModel.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context