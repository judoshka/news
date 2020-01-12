from django.db import models
from uuid import uuid4


def get_file_path(instance, filepath):
    folders = {
        ImageItem: 'Image'
    }
    extension = filepath.split()[-1]
    filepath = f'{folders.get(type(instance)), "other"}/{uuid4()}.{extension}"'
    return filepath


# Create your models here.
class NewsItem(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255, default='<<No title>>',
                             null=False, blank=False,)
    essay = models.CharField(verbose_name='Краткая информация', max_length=1024, null=False, blank=False)
    published_date = models.DateTimeField(verbose_name='Дата и время публикации', auto_now=True)
    content = models.TextField(verbose_name='Текст новости', null=True, blank=True)
    essay_img = models.ForeignKey('ImageItem', related_name='news_item', on_delete=models.SET_NULL,
                                  null=True)
    illustrations = models.ManyToManyField('ImageItem')
    authors = models.ManyToManyField('Author')
    source = models.ForeignKey('Source', on_delete=models.SET_NULL, related_name='news_items', null=True)

    def __str__(self):
        return f'Title:{self.title} Pub_date:{self.published_date}'

    class Meta:
        ordering = ['-id']


class Source(models.Model):
    title = models.CharField(verbose_name='Название', max_length=128)
    url = models.URLField(verbose_name='URL', default='https://127.0.0.1/home')

    def __str__(self):
        return f'url:{self.url}'


class Author(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=64, blank=False, null=False)
    last_name = models.CharField(verbose_name='Фамилия', max_length=64, blank=False, null=False)
    middle_name = models.CharField(verbose_name='Отчество', max_length=64, blank=True, null=True, default='')

    created_date = models.DateTimeField(verbose_name='Дата и время публикации', auto_now=True)

    def get_short_name(self):
        if self.middle_name is not None:
            return f'{self.last_name} {self.first_name[0]}.{self.middle_name[0]}.'
        else:
            return f'{self.last_name} {self.first_name[0]}.'

    def __str__(self):
        return self.get_short_name()


class ImageItem(models.Model):
    title = models.CharField(verbose_name='Название', max_length=128)
    description = models.CharField(verbose_name='Описание', max_length=128)
    img = models.ImageField(verbose_name='Картинка', upload_to=get_file_path)

    def __str__(self):
        return f'Name: {self.title}'
