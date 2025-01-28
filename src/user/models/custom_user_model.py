import uuid
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from datetime import datetime
from django.utils.text import slugify
from django.contrib.auth.validators import UnicodeUsernameValidator
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
from base.models.cards_type_enum import CardsTypeEnum

FILE_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 10  # 10mb


def file_validation(file):
    if not file:
        raise ValidationError("Aucun fichier selectionné")

    if isinstance(file, UploadedFile):
        if file.size > FILE_UPLOAD_MAX_MEMORY_SIZE:
            raise ValidationError("Le fichier ne doit pas exceder 10MB.")


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Vous devez entrer un nom d'utilisateur")

        user = self.model(
            username=username
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(username=username, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.user_type = 'ADMIN'
        user.save()
        return user


class CustomUserModel(AbstractBaseUser, PermissionsMixin):
    TYPE_CHOICES = [
        ('LOCATAIRE', 'LOCATAIRE'),
        ('PROPRIETAIRE', 'PROPRIETAIRE'),
    ]

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(max_length=150, unique=True, validators=[username_validator],
                                help_text="Obligatoire ! 150 caractères ou moins. Seuls les lettres, chiffres et "
                                          "@/./+/-/_.",
                                error_messages={
                                    "unique": "A user with that username already exists.",
                                }, verbose_name="Nom d'utilisateur ")
    first_name = models.CharField(max_length=30, verbose_name="Nom ")
    last_name = models.CharField(max_length=60, verbose_name="Prénoms ")
    email = models.EmailField(unique=True, verbose_name="Email ")
    phone_number = models.CharField(max_length=15, verbose_name="Téléphone ", unique=True, blank=True, null=True)
    num_cni = models.CharField(max_length=20, unique=True, verbose_name="ID de la carte ", blank=True, null=True)
    image_recto = CloudinaryField('image_recto', folder='CNI', validators=[file_validation], blank=True, null=True)
    image_verso = CloudinaryField('image_verso', folder='CNI', validators=[file_validation], blank=True, null=True)
    user_type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='LOCATAIRE',
                                 verbose_name="Type d'utilisateur ")
    cards_type = models.CharField(max_length=20, choices=CardsTypeEnum.choices,
                                  default=CardsTypeEnum.CNI, verbose_name="Type de carte ")
    avatar = CloudinaryField('avatar', folder='Avatar', validators=[file_validation], blank=True, null=True)
    slug = models.SlugField(unique=True)
    date_joined = models.DateTimeField(verbose_name="Date d'inscription ", default=timezone.now)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    objects = CustomUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return f"{self.username}"

    class Meta:
        ordering = ["username"]
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

    def save(self, *args, **kwargs):
        today = datetime.now()

        if not self.slug:
            self.slug = slugify(uuid.uuid4())

        if self.avatar:
            self.avatar.public_id = f"Avatar_{self.username}_{self.pk}"
            self.avatar.folder = f"Avatar/{today.year}/{today.month}/{today.day}/"

        folder_path = f"CNI/{today.year}/{today.month}/{today.day}/"

        if self.image_recto:
            self.image_recto.folder = folder_path
            self.image_recto.public_id = f"Avatar_{self.username}_{self.pk}"

        if self.image_verso:
            self.image_verso.folder = folder_path

        super(CustomUserModel, self).save(*args, **kwargs)
