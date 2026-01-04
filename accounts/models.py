from django.db import models
from django.contrib.auth.models import AbstractUser
from decimal import Decimal

# Create your models here.
class User(AbstractUser):
    """Extended User model with phone number and wallet balance"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    wallet_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email
    
    def add_to_wallet(self, amount):
        """Add funds to wallet"""
        self.wallet_balance += Decimal(str(amount))
        self.save()
    
    def deduct_from_wallet(self, amount):
        """Deduct funds from wallet"""
        if self.wallet_balance >= Decimal(str(amount)):
            self.wallet_balance -= Decimal(str(amount))
            self.save()
            return True
        return False


class UserProfile(models.Model):
    """Additional user profile information"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True)
    state = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, default='Nigeria')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    
   
    def __str__(self):
        return f"{self.user.email}'s Profile"