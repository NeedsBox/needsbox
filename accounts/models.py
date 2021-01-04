from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phone_field import PhoneField

# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")
        
        user = self.model(
            email = self.normalize_email(email),
            username=username,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            password=password,
            username=username,
        )
        
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    USER_TYPE =( 
    ("PES", "Pessoal"), 
    ("PRO", "Profissional"),
    ) 
    
    email = models.EmailField(max_length=60, unique=True, null=True)
    username = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=50, null=False, blank=True)
    profile_image = models.ImageField(blank=True)
    biography = models.TextField(blank=True)
    website = models.CharField(max_length=50, blank=True)
    contact = PhoneField(blank=True, help_text='Contact phone number')
    account_type = models.CharField(
        max_length=3,
        choices=USER_TYPE,
        default="PES",
    ) 
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    objects = MyAccountManager()
    
    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    
    