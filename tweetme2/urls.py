from django.contrib import admin
from django.urls import path
from tweets.views import home_view, tweet_detailed_view, tweet_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('tweets', tweet_list_view),
    path('tweets/<int:tweet_id>', tweet_detailed_view),
]
