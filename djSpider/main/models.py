import json
from datetime import datetime
from django.db import models
from django.utils import timezone
# Create your models here.


class ScrapyItem(models.Model):
    url = models.CharField(max_length=100)
    unique_id = models.CharField(max_length=100)
    data = models.TextField()
    date = models.CharField(default=timezone.now)
    
    @property
    def to_dict(self):
       data = {
               "data": json.dumps(self.data),
               "date": self.date
            } 
       return data


class Store(models.Model):
    store_name = models.CharField(verbose_name="store name", max_length=100, null=False, blank=False)
    store_rating = models.IntegerField(verbose_name="store rating", default=0, null=False, blank=False)
    store_review_total = models.IntegerField(verbose_name="store review total", default=0, null=False, blank=False)

    class Meta:
        app_label = "main"
        db_table = "store"

    def __str__(self):
        return self.store_name
    

class StoreProductReview(models.Model):
    store_name = models.CharField(verbose_name="store name", max_length=100, null=False, blank=False)
    author_name = models.CharField(verbose_name="author name", max_length=100, null=False, blank=False)
    author_profile_url = models.URLField(verbose_name="author profile url", max_length=255)
    review_content = models.TextField(verbose_name="review content", default="")
    comment_date = models.DateTimeField(verbose_name="comment date", default=datetime.now)
    product_image_url = models.ImageField(verbose_name="product image url", max_length=255)
    product_title = models.TextField(verbose_name="product title", default="")
    product_rating = models.IntegerField(verbose_name="product rating", default=0)

    class Meta:
        app_label = "main"
        db_table = "store_product_review"

    def __str__(self):
        return self.store_name


class StoreProductDetail(models.Model):
    store_name = models.CharField(verbose_name="store name", max_length=100, null=False, blank=False)
    product_title = models.TextField(verbose_name="product title", default="")
    ask_a_question_url = models.URLField(verbose_name="ask a question", max_length=255)
    over_view = models.TextField(verbose_name="over view", default="")
    review_count = models.IntegerField(verbose_name="review count", default=0)
    favorited_count = models.IntegerField(verbose_name="favorited count", default=0)
    favorite_url = models.URLField(verbose_name="favorite url", max_length=255)
    description = models.TextField(verbose_name="description", default="")

    class Meta:
        app_label = "main"
        db_table = "store_product_detail"

    def __str__(self):
        return self.store_name

