from django.contrib.auth.models import User
from django.db import models
from author.models import Profile


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=202)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=202)

    def __str__(self):
        return self.title


class Season(models.Model):
    title = models.IntegerField()


class Article(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categorys')
    Season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='seasons')
    title = models.CharField(max_length=202)
    image = models.ImageField()
    audio = models.FileField()
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='tags')
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes')


class CommentArticle(models.Model):
    Name = models.CharField(max_length=202, null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Phone = models.CharField(max_length=202, null=True, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    Description = models.TextField(max_length=303, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.article.title


class Blog(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=202)
    image = models.ImageField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CommentBlog(models.Model):
    Name = models.CharField(max_length=202, null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Phone = models.CharField(max_length=202, null=True, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    article = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    Description = models.TextField(max_length=303, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.article.title
