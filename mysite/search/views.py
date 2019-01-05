from django.shortcuts import render
from django.http.response import HttpResponse
from . import models

# Create your views here.
def index(request):
    movie = models.MovieInfo.objects.get(id=1)   #从数据库获取数据
    return render(request, 'index.html', {'movie':movie})

def content(request):
    return render(request, 'content.html')

def content_url(request, movie_name):
    # 将点击页面的movie_name传到这里
    movie_info = models.MovieInfo.objects.get(name=movie_name)
    movie_score = models.MovieScore.objects.get(name=movie_name)
    # comment_info = models.CommentInfo.objects.filter(name=movie_name)
    comment_info = models.CommentInfo.objects.all().filter(name=movie_name)
    # 计算优质用户评价
    score = {'力荐':0, '推荐':0, '还行':0, '较差':0, '很差':0}
    sum = len(comment_info)
    for comment in comment_info:
        if comment.userscore == '空':
            continue
        score[comment.userscore] += 1
    for a in score:
        score[a] /= sum
        score[a] = int(score[a] * 100)

    movie_play = models.MoviePlay.objects.all().filter(name=movie_name)
    return render(request, 'content.html',{'movie_info':movie_info, 'movie_score':movie_score, 'score':score, 'movie_play':movie_play})

def content_action(request):
    search = request.POST.get('search', 'faild')
    return HttpResponse(search)