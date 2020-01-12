from django.shortcuts import render
from website.models import NewsItem

# Create your views here.
def home_render(request):
    news_items = NewsItem.objects.all()
    return render(request, 'home.html', {'news_items': news_items})
