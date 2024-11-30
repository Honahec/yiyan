from django.db import models

class Sentence(models.Model):
    content = models.TextField(verbose_name='内容')
    author = models.CharField(max_length=100, blank=True, verbose_name='作者')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '句子'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content[:50]