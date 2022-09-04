from django.shortcuts import render
from django.http import request
# Create your views here.
d = {1:['search/videos/summerized/first.mp4','search/summary/summarized/1sum.txt','The Chainsmokers - Song'],
    2:['search/videos/summerized/second.mp4','search/summary/summarized/2sum.txt','The What is Physic ?'],
    3:['search/videos/summerized/third.mp4','search/summary/summarized/3sum.txt', 'The tree of life'],
    4:['search/videos/summerized/fourth.mp4','search/summary/summarized/4sum.txt', 'Four Friends'],
    5:['search/videos/summerized/fifth.mp4','search/summary/summarized/5sum.txt', 'Kung Fu Panda'],
    6:['search/videos/summerized/sixth.mp4','search/summary/summarized/6sum.txt','Cristiano Ronaldo Speech'],
    7:['search/videos/summerized/seventh.mp4','search/summary/summarized/7sum.txt' , 'Why not Focus ?'],

     }

def base(request):
    return render(request,'search/base.html')


def search(request):
    return render(request, 'search/search.html')


def upload(request):

    return render(request, 'search/upload.html')


def home(request):
    return render(request,'search/home.html')


def summary(request, myid):


    li  = d[myid]
    first = li[0]
    title = li[2]
    return render(request , 'search/summary.html',{'first':first , 'id':myid , 'title':title})

def textsummary(request,sid):
    li = d[sid]
    text = li[1]

    with open('search/static/'+text,'r') as f:
        data = f.read()
    heading = li[2]
    return render(request,'search/textSummary.html',{'text':data, 'heading':heading})