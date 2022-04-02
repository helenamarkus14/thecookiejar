from django.db import models



# Create your models here.

RATING_CHOICES = [
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
    ]

# Cookie
class Cookie(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(null=True, blank=True, upload_to="images/")
    description = models.CharField(max_length=250),
    appearance = models.CharField(max_length=3, choices = RATING_CHOICES, default='1')
    taste =  models.CharField(max_length=3, choices = RATING_CHOICES, default='1')
    overall_rating = models.CharField(max_length=3, choices = RATING_CHOICES, default='1')
    comments = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']