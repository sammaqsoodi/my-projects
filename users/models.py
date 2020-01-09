from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE,verbose_name='نام کاربری')
  image = models.ImageField(default='default.jpg', upload_to='profile_pics',verbose_name='عکس')
  curentCity = models.CharField(max_length=30,verbose_name='شهر محل سکونت')
  bio = models.TextField(verbose_name='درباره')



  def __str__(self):
    return f'{self.user.username} profile'

  def save(self):

    super().save() 

    img = Image.open(self.image.path)

    if img.height > 300 or img.width > 300:
      output_size = (300, 300)
      img.thumbnail(output_size)
      img.save(self.image.path)

  class Meta:
      verbose_name='پروفایل'
      verbose_name_plural= 'پروفایل ها'

