from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Usermaster(models.Model):
    # fields...
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=200)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    expiry_date = models.CharField(max_length=10, null=True)
    activation_date = models.CharField(max_length=10, null=True)
    last_login = models.CharField(max_length=10, null=True)
    status = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.username


class Subscription(models.Model):
    
    productname = models.CharField(max_length=50)
    user = models.ForeignKey(Usermaster, on_delete=models.CASCADE)
    #act_date = models.OneToOneField(Usermaster,on_delete=models.CASCADE)
    #act_date = models.OneToOneField(Usermaster.activation_date,on_delete=models.CASCADE)
    act_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    is_active = models.BooleanField()

    def __str__(self):
        return f"{self.productname} - User: {self.user.username}"



class Prodmaster(models.Model):
    productname = models.CharField(max_length=200)
    prod_id = models.IntegerField()

    def __str__(self):
        return self.productname


'''from django.db import models

class Usermaster(models.Model):
    # fields...
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=200)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    expiry_date = models.CharField(max_length=10, null=True)
    activation_date = models.CharField(max_length=10, null=True)
    last_login = models.CharField(max_length=10, null=True)
    status = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super(Usermaster, self).save(*args, **kwargs)

        # Update the corresponding Subscription act_date if it exists
        try:
            subscription = Subscription.objects.get(user=self)
            subscription.act_date = self.activation_date
            subscription.save()
        except Subscription.DoesNotExist:
            pass  # If no subscription is found, we ignore it

class Subscription(models.Model):
    # fields...
    productname = models.CharField(max_length=50)
    user = models.OneToOneField(Usermaster, on_delete=models.CASCADE)
    act_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    is_active = models.BooleanField()

    def __str__(self):
        return f"{self.productname} - User: {self.user.username}"
'''













'''class Subscription(models.Model):
    productname = models.CharField(max_length=50)
    user = models.ForeignKey(Usermaster, on_delete=models.CASCADE)
    activation_date = models.ForeignKey(Usermaster, to_field='activation_date', on_delete=models.CASCADE, related_name='subscription_activation_dates')
    expiry_date = models.ForeignKey(Usermaster, to_field='expiry_date', on_delete=models.CASCADE, related_name='subscription_expiry_dates')
    is_active = models.ForeignKey(Usermaster, to_field='is_active', on_delete=models.CASCADE, related_name='subscription_is_active')

    def __str__(self):
        return f"{self.productname} - User: {self.user.user_name}"
'''
'''class User(models.Model):
    username = models.CharField(max_length=100)
    activation_date = models.DateTimeField()
    expiry_date = models.DateTimeField()

    # Add any other existing fields or methods

    def __str__(self):
        return self.username'''


'''class Usermaster(models.Model):

    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=200)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    expiry_date = models.CharField(max_length=10,null=True)
    #activation_date = models.DateField(max_length=10, null=True)
    activation_date = models.CharField(max_length=10,null=True)
    last_login = models.CharField(max_length=10,null=True)
    status = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.username

    
class Subscription(models.Model):
    productname = models.CharField(max_length=50)
    user = models.ForeignKey('Usermaster', on_delete=models.CASCADE)
    act_date = models.CharField(max_length=10, null=True)
    end_date = models.CharField(max_length=10, null=True)
    is_active = models.BooleanField()

    def __str__(self):
        return f"{self.productname} - User: {self.user.user_name}"

     delete 13 migration to get back to normal.   
'''
# models.py


# Create your models here.
'''from django.db import models
from django.contrib.auth.models import User

class Usermaster(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=200)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    is_active = models.BooleanField()

class Subscription(models.Model):
    productname = models.CharField(max_length=50)
    user = models.ForeignKey(Usermaster, on_delete=models.CASCADE)
    act_date = models.DateField()
    is_active = models.BooleanField()
'''