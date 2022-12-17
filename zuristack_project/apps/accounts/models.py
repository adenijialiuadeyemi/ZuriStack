from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.template.defaultfilters import slugify
from . import utils
# Create your models here.

class CustomUser(AbstractUser):
    username=None
    email = models.EmailField(unique=True, blank=True)
    slug = models.SlugField(blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =[]

    objects = CustomUserManager()
    class Meta:
        ordering = ['email']
        verbose_name = "User"

    def __str__(self):
        return self.email

    #Creating a default slug for user if blank
    def generate_random_slug(self):
        random_slug = slugify(self.first_name + self.last_name + utils.generate_random_id)
        while CustomUser.objects.filter(slug=random_slug).exists():
            random_slug = slugify(self.first_name + self.last_name + utils.generate_random_id)
        return random_slug

    def save(self, *args, **kwargs):
        #check for slug:
        if not self.slug:
            #create default slug
            self.slug = self.generate_random_slug
        #finally save
        super().save(*args, **kwargs)