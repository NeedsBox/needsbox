from django.contrib.gis.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.templatetags.static import static

from accounts.models import Account
from spatialdata.models import Limits


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    location = models.PointField()
    image = models.ImageField(default="static/images/default-service.jpg", blank=True, upload_to='advertisements')
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.FloatField(blank=True, null=True)
    location = models.PointField()
    image = models.ImageField(blank=True, upload_to='services')
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_url(self):
        if self.image:
            return self.image.url
        else:
            return static("images/default-service.jpg")

    def get_location(self):
        limits = Limits.objects.filter(geom__intersects=self.location).values('nome', 'distrito_title')
        return str(limits[0]['nome'])

    def get_reviews_count(self):
        reviews = Review.objects.filter(service=self)
        return reviews.count()

    def get_average_review(self):
        reviews = Review.objects.filter(service=self)
        count = reviews.count()

        if count == 0:
            context = {
                'average': "No reviews",
                'count': 0,
                'stars': 0,
                'empty_stars': 5,
                'half_stars': 0,
            }
            return context
        total = float(0)
        for x in reviews:
            total += x.stars

        final_count = count
        average = float(total) / float(count)

        stars = int(average)
        empty_stars = 5 - stars
        half_stars = average - stars

        if half_stars != 0:
            empty_stars -= 1

        context = {
            'average': average,
            'count': final_count,
            'stars': stars,
            'empty_stars': empty_stars,
            'half_stars': half_stars,
        }

        return context


class Review(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    msg = models.TextField()
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review de {self.user.username}: \n{self.msg}"


class User(models.Model):
    name = models.CharField(max_length=50)
    biography = models.CharField(max_length=1000)
    profile_image = models.ImageField(blank=True)
