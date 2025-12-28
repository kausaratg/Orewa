from django.db import models

from authentication.models import User

# Create your models here.
class UserProfile(models.Model):
    SKIN_TYPES = [
        ("oily", "Oily"),
        ("dry", "Dry"),
        ("combination", "Combination"),
        ("normal", "Normal"),
    ]

    AGE_RANGES = [
        ("under_18", "Under 18"),
        ("18_24", "18–24"),
        ("25_34", "25–34"),
        ("35_44", "35–44"),
        ("45_plus", "45+"),
    ]

    GENDERS = [
        ("female", "Female"),
        ("male", "Male"),
        ("other", "Other / Prefer not to say"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    skin_type = models.CharField(max_length=20, choices=SKIN_TYPES)
    sensitive = models.BooleanField(default=False)
    acne_prone = models.BooleanField(default=False)

    age_range = models.CharField(
        max_length=20,
        choices=AGE_RANGES,
        blank=True,
        null=True
    )

    gender = models.CharField(
        max_length=20,
        choices=GENDERS,
        blank=True,
        null=True
    )

    assessment_data = models.JSONField(default=dict)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email}"

