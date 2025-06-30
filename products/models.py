from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


# custom manager
class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManager, self).get_queryset().filter(active=True)


# how to use custom manageR
#         Comment.active_comments_manager.all()


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    active = models.BooleanField(default=True)
    price = models.PositiveIntegerField(default=0)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])


class Comment(models.Model):
    body = models.TextField(verbose_name='Please write your comment: ')
    author = models.ForeignKey(

        get_user_model(),
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Comment Author'
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', )
    active = models.BooleanField(default=True)
    recommend = models.BooleanField(default=True, verbose_name='Do you recommend this product?')
    datetime_created = models.DateTimeField(auto_now_add=True)
