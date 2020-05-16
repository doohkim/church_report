import datetime

from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    # 무엇인지 파악 못하고 쓰는 것
    use_in_migrations = True

    def _create_user(self, email, name, password=None, **extra_fields):
        print(extra_fields)
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, name=None, password=None, **extra_fields):
        # extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_admin', False)

        return self._create_user(email, name, password, **extra_fields)

    def create_superuser(self, email, name, password, **extra_fields):
        # 왜 계속 오류나는 거지
        # extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)
        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True.')
        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin=True.')

        return self._create_user(email, name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name=_('email address'), unique=True, blank=False)
    name = models.CharField(_('name'), max_length=30, blank=True)
    is_superuser = models.BooleanField(
        _('superuser'),
        default=False,
        help_text=_(
            'Designates whether this user can have auth in charge of everything. '),
    )
    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_admin = models.BooleanField(
        _('admin'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as admin. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    recent_attend_date = models.DateField(default=datetime.date.today)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    team = models.ForeignKey(
        'Team',
        on_delete=models.SET_NULL,
        null=True,
        help_text="무소속 혹은 6개월이상 출석하지 않을 경우 팀소속을 잃어버린다."
    )
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        swappable = 'AUTH_USER_MODEL'

    # https: // docs.djangoproject.com / en / 3.0 / topics / email /
    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     send_mail(subject, message, from_email, [self.email], **kwargs)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return f'email : {self.email}'


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        unique=True,
        related_name='user_profile'
    )
    job = models.CharField(max_length=50, null=True, blank=True, default='정보없음')

    SEX = [('MALE', 'Male'), ('FEMALE', 'Female')]
    sex = models.CharField(max_length=6, default='Male', choices=SEX)
    phone_number = PhoneNumberField(blank=True, null=True, unique=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True, default=20)
    address = models.CharField(max_length=255, null=True, blank=True, default='정보없음')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    email_confirmed = models.BooleanField(default=False)
    recent_attend_date = models.DateField(default=datetime.date.today)

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     self.
    def __str__(self):
        return self.user.name


class UserImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='profile')


class Team(models.Model):
    BLESSING = "축복지역"
    IMMANUEL = "임마누엘지역"
    HOSANNA = "호산나지역"
    HOMIN = "호민지역"

    TEAM_NAME = [
        (BLESSING, "축복"),
        (IMMANUEL, "임마누엘"),
        (HOSANNA, "호산나"),
        (HOMIN, "호민"),
    ]
    name = models.CharField(
        max_length=10,
        choices=TEAM_NAME,
        default=BLESSING,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


