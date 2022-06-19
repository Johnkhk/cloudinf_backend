from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from .serializers import SummarizerSerializer
from .summarizer import summarize
import json
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