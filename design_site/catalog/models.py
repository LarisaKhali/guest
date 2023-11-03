from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    fio = models.CharField(max_length=100)
    email =  models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class DesignCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Request(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(DesignCategory, on_delete=models.CASCADE, verbose_name='Категория')
    # room_image = models.ImageField(
    #     upload_to='design_images/',
    #     validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp'])],
    #     verbose_name='Фото помещения или план'
    # )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    status = models.CharField(max_length=20, default="Новая", verbose_name='Статус')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    is_completed = models.BooleanField(default=False)
    def __str__(self):
        return self.title

    # def get_absolute_url(self):

    # """Returns the URL to access a detail record for this book."""
    #     return reverse('book-detail', args=[str(self.id)])
