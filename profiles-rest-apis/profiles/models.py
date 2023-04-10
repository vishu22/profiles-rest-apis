from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
# Create your models here.


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """create a new user profile"""
        if not email:
            raise ValueError("Users must have an email address")

        # make second part case insensitive
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        # set_password will encrypt the the password
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff =  True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database models for user in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """retrieve full name of the user"""
        return self.name

    def get_short_name(self):
        """retrieve self name of user"""
        return self.name

    def __str__(self):
        """return string represenation of the user"""
        return self.email

class ProfileFeedItem(models.Model):
    """profile status update"""

    user_profile = models.ForeignKey(UserProfile,settings.AUTH_USER_MODEL)

    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.status_text