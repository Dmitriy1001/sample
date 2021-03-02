from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
	title = models.CharField(max_length=200, verbose_name='Заголовок')
	text = models.TextField(verbose_name='Текст')
	published_date = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')

	class Meta:
		verbose_name = 'Статью'
		verbose_name_plural = 'Статьи'

	def __str__(self):
		return self.title	
