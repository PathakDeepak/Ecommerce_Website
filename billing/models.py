from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL

# abc@gmail.com  -->> 100000 billing profiles
# user abc@gmail.com  -->> 1 billing profile

# Create your models here.
class BillingProfile(models.Model):
    user      = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    email     = models.EmailField()
    active    = models.BooleanField(default=True)

    # customer_id  in stripe or braintree

    def __str__(self):
        return self.email

def user_created_receiver(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        BillingProfile.objects.get_or_create(user=instance, email=instance.email)

post_save.connect(user_created_receiver, sender=User)
