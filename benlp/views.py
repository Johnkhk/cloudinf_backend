from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from .serializers import SummarizerSerializer
from .summarizer import summarize
import json
import requests
# from .utils import test
# Create your views here.

# def main(request):
    # return HttpResponse("Hello")

# class SummarizerView(generics.ListAPIView):
# # class SummarizerView(generics.CreateAPIView):
#     queryset = Summarizer.objects.all()
#     serializer_class = SummarizerSerializer

# class Summarizer_View(request, *args, **kwargs):
from django.views.decorators.csrf import csrf_exempt

from django_nextjs.render import render_nextjs_page_sync

def index(request):
    return render_nextjs_page_sync(request)

@csrf_exempt
def Summarizer_View(request):
    print(request.body)
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    content = body['content']
    summary= summarize(content, 0.1)
    print(summary)
    # return HttpResponse(request)

    # "summary":summary
    response = JsonResponse(
        # your stuff here
        {
            # "hi":"bye",
            # "what":"hey"
            "summary":summary

        }
    )
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response

@csrf_exempt
def getWiki_View(request):
    x = requests.get('https://en.wikipedia.org/w/api.php?format=json&action=query&generator=random&grnnamespace=0&prop=revisions|images&rvprop=content&grnlimit=10')
    a = x.json()
    articles_dict = a['query']['pages']
    page_ids,titles,article_lengths=[],[],[]
    for art in articles_dict:
        # print(articles_dict[art].keys())
        # print('title',articles_dict[art]['title'])
        # print('pageid',articles_dict[art]['pageid'])
        # print('ns',articles_dict[art]['ns'])
        page_ids.append(articles_dict[art]['pageid'])
        titles.append(articles_dict[art]['title'])
        article_lengths.append(len(articles_dict[art]['revisions'][0]['*']))


    """
    You can just use a URL like this:
    http://en.wikipedia.org/?curid=18630637
    """
    tmp = list(zip(page_ids,titles,article_lengths))
    tmp = sorted(tmp, key = lambda x: x[2], reverse=True)
    # print(tmp)
    response = JsonResponse(
        {
            # "page_ids":page_ids,
            # "titles":titles,
            # "article_lengths":article_lengths
            "wikidata":tmp
        }
    )
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response


# @csrf_exempt
# def Summarizer_View(request):
# https://en.wikipedia.org/w/api.php?format=json&action=query&generator=random&grnnamespace=0&prop=revisions|images&rvprop=content&grnlimit=10