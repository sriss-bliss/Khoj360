from django.conf import settings
from django.db import models


class Profile(models.Model):
    BLOOD_GROUPS = [
        ("", "Unknown"),
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-"),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30, blank=True)
    area = models.CharField(max_length=120, blank=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS, blank=True)
    is_available = models.BooleanField(default=True)
    is_volunteer = models.BooleanField(default=False)
    is_donor = models.BooleanField(default=False)
    is_repair_provider = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name or self.user.username

# Create your models here.
