from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

    

class Post(models.Model):
  STATUS_CHOICES = (
        ('draft', 'آماده ی انتشار'),
        ('published', 'منتشر شده'),
    )
  title = models.CharField(max_length=50,verbose_name='عنوان')
  content = models.TextField(verbose_name='متن')
  date_posted = models.DateTimeField(default=timezone.now,verbose_name='تاریخ انتشار')
  author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده')
  status = models.CharField(max_length=60, choices= STATUS_CHOICES, default='draft', verbose_name='وضعیت')


  class Meta:
    verbose_name= 'پست'
    verbose_name_plural= 'پست ها'

  def __str__(self):
    return self.title   

    
  def get_absolute_url(self):
    return reverse('post-detail', kwargs={'pk': self.pk})