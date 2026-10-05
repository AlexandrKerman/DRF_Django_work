from django.db import models

class Course (models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name='Название')
    preview = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Превью')
    description = models.TextField(max_length=500, blank=True, null=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name='Название')
    description = models.TextField(max_length=500, blank=True, null=True, verbose_name='Описание')
    preview = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Превью')
    video_link = models.CharField(max_length=150, blank=False, verbose_name='Видео')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons', verbose_name='Курс')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'