from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http.response import HttpResponse
from . import models
from getData import spiderMain
from getData import createClound
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def index(request):
    xjcy = models.MovieInfo.objects.get(id=1)   #从数据库获取数据
    ls = models.MovieInfo.objects.get(id=4)
    dkek = models.MovieInfo.objects.get(id=6)
    dmkj = models.MovieInfo.objects.get(id=18)
    return render(request, 'index.html', {'xjcy':xjcy, 'ls':ls, 'dkek':dkek, 'dmkj':dmkj})

def content(request):
    return render(request, 'content.html')

def content_url(request, movie_name):
    # 将点击页面的movie_name传到这里
    movie_info, movie_score, movie_play, score ,movie_awards = search_data(movie_name)
    return render(request, 'content.html',{'movie_info':movie_info, 'movie_score':movie_score, 'score':score, 'movie_play':movie_play, 'movie_awards':movie_awards})

def content_action(request):
    search = request.POST.get('search', 'faild')
    try:
        movie_info = models.MovieInfo.objects.get(name=search)
        movie_info, movie_score, movie_play, score ,movie_awards= search_data(search)
    except ObjectDoesNotExist:
        movie_name = spiderMain.main(search)
        movie_info, movie_score, movie_play, score ,movie_awards= search_data(movie_name)

    return render(request, 'content.html',{'movie_info':movie_info, 'movie_score':movie_score, 'score':score, 'movie_play':movie_play, 'movie_awards':movie_awards})


def search_data(movie_name):
    # 根据电影名字返回数据

    movie_info = models.MovieInfo.objects.get(name=movie_name)
    movie_score = models.MovieScore.objects.get(name=movie_name)
    # comment_info = models.CommentInfo.objects.filter(name=movie_name)
    movie_awards = models.MovieAwards.objects.all().filter(name=movie_name)
    comment_info = models.CommentInfo.objects.all().filter(name=movie_name)

    with open('C:/Users/SiChengZ/OneDrive/桌面/django/mysite/getData/text2', 'w') as f:
        for comment in comment_info:
            f.write(comment.comment)

    createClound.ciyun()
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
    return movie_info, movie_score, movie_play, score, movie_awards

def send(request):
    content = request.POST.get('content')
    send_mail(
        '反馈',
        content,
        'sichengz2@163.com',
        ['609686536@qq.com'],
        fail_silently=False,
    )
    return HttpResponse(content)

