from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, PermissionManager, Permission
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator


class UserManger(BaseUserManager, PermissionManager):

    def create_user(self, email, username, phone, birth_date, password=None):
        if not email:
            raise ValueError('Enter a valid Email.')
        if not username:
            raise ValueError('Enter a valid username')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone=phone,
            birth_date=birth_date
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phone, birth_date,  password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            phone=phone,
            birth_date=birth_date
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email           = models.EmailField(unique=True, max_length=128, null=False)
    username        = models.CharField(max_length=128, blank=False, null=False)
    phone           = PhoneNumberField(blank=False, null=True)
    company         = models.CharField(max_length=32, null=True, blank=True)
    current_role    = models.CharField(max_length=64, blank=True, null=True)
    birth_date      = models.DateField(blank=False, null=True)
    date_joined     = models.DateTimeField(auto_now_add=True, null=True)
    last_login      = models.DateTimeField(auto_now=True)
    is_active       = models.BooleanField(default=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    objects = UserManger()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone', 'birth_date']

    def __str__(self):
        return f'{self.username}'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin


class AiModel(models.Model):
    title               = models.TextField()
    description         = models.TextField()
    url                 = models.URLField()
    image_url           = models.URLField()
    creation_datetime   = models.DateTimeField(auto_now_add=True)
    description_summery = models.CharField(max_length=100)
    api_code            = models.CharField(max_length=6000)

    def str(self):
        return f'{self.title, self.desc_summery}'


class Request(models.Model):
    request_time   = models.DateTimeField(auto_now_add=True)
    user_id        = models.ForeignKey(User, on_delete=models.CASCADE)
    ai_model_id    = models.ForeignKey(AiModel, on_delete=models.CASCADE)


class Bookmark(models.Model):
    user_id        = models.ForeignKey(User, on_delete=models.CASCADE)
    ai_model_id    = models.ForeignKey(AiModel, on_delete=models.CASCADE)


class Tag(models.Model):
    name         = models.CharField(max_length=255)
    ai_model_tag = models.ManyToManyField(AiModel)


class Rate(models.Model):
    ai_model_id    = models.ForeignKey(AiModel, on_delete=models.CASCADE)
    user_id        = models.ForeignKey(User, on_delete=models.CASCADE)
    stars          = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

