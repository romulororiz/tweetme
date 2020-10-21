from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Tweet


def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)


def tweet_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    Consume by Javascript or Swift or Java or iOS/Android
    return json data
    """
    queryset = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content} for x in queryset]
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)


def tweet_detailed_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW
    Consume by Javascript or Swift or Java or iOS/Android
    return json data
    """
    data = {
        "id": tweet_id,
        # "image_path":"obj.img.url"
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = 'Not Found'
        status = 404
    return JsonResponse(data, status=status)
