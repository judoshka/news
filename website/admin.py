from django.contrib import admin
from website.models import NewsItem
from website.models import Author
from website.models import ImageItem
from website.models import Source

# Register your models here.
admin.site.register(NewsItem)
admin.site.register(Author)
admin.site.register(ImageItem)
admin.site.register(Source)