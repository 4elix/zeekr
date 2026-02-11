from django.db import models


class News(models.Model):
    title_news = models.CharField(max_length=255)
    slug_news = models.CharField(max_length=255)
    main_image = models.ImageField(upload_to='images/news/main')
    sub_image = models.ImageField(upload_to='images/news/sub', blank=True, null=True)
    main_text = models.TextField()
    sub_text = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title_news
    
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
