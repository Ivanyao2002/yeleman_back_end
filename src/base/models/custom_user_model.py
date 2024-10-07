import uuid
from django.db import models
from .helpers.date_time_model import DateTimeModel
from .account_type_enum import AccountTypeEnum
from django.utils.text import slugify
from django.contrib.auth.validators import UnicodeUsernameValidator


# Create your models here.

class CustomUserModel(DateTimeModel):

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(max_length=150, unique=True, validators=[username_validator],
                                help_text="Requied. 150 caractères ou moins. Seuls les lettres, chiffres et @/./+/-/_.",
                                error_messages={
                                    "unique": "A user with that username already exists.",
                                }, verbose_name="Nom d'utilisateur "
                                )
    first_name = models.CharField(max_length=30, verbose_name="Nom ")
    last_name = models.CharField(max_length=60, verbose_name="Prénoms ")
    account_type_enum = models.CharField(max_length=10, choices=AccountTypeEnum.choices, default=AccountTypeEnum.FREEMIUM, verbose_name="Type de compte")
    phone_number = models.CharField(max_length=15, verbose_name="Téléphone ")
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=128, verbose_name="Mot de passe ")
    last_login = models.DateTimeField(verbose_name="Dernière connexion ", blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.username}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(uuid.uuid4())

        super(PersonModel, self).save(*args, **kwargs)

