from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField('タイトル', max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField('本文')
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField('名前', max_length=200)
    text = models.TextField('コメント')
    date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)


    def __str__(self):
        return self.text
