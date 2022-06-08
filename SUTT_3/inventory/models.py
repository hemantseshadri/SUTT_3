from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import datetime
from django.core.validators import MinValueValidator

# Create your models here.

class Category(models.Model):
    category=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.category

class inventory(models.Model):

    Item_name = models.CharField(max_length=50)
    Quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    category = models.ForeignKey(Category,default=None,on_delete=models.SET_NULL,null=True)


    def __str__(self):
        return self.Item_name



class IssueItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    issued = models.BooleanField(default=False)
    item = models.ForeignKey(inventory, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date = models.DateTimeField(default=datetime.datetime.now, blank=True)

    def __str__(self):
        return self.user.username

#class Issue(models.Model):
#    user = models.ForeignKey(User,on_delete=models.CASCADE)
#    items = models.ForeignKey(inventory,on_delete=models.CASCADE,default=None)
#    date = models.DateTimeField(default=datetime.datetime.now, blank=True)


class Userlog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=None)
    issue_details = models.ForeignKey(IssueItem,on_delete=models.SET_NULL,default=None,null=True)
    copy_issue_item_name = models.CharField(max_length=50,default=None,null=True,blank=True)
    copy_issue_item_quantity= models.PositiveIntegerField(default=1)
    copy_issue_category = models.CharField(max_length=50,default=None,null=True,blank=True)
    quantity_to_be_returned=models.PositiveIntegerField(null=True,default=None)
    copy_issue_item_date=models.DateTimeField(default=None, blank=True, null=True)
    return_date = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return self.copy_issue_item_name

class IsMod(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    isMod = models.BooleanField(default=False)

class Moderatorlog(models.Model):
    Item_name = models.CharField(max_length=50,unique=True)
    Quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category,default=None,on_delete=models.SET_NULL,null=True)
    date_added =  models.DateTimeField(default=datetime.datetime.now, blank=True)

    def __str__(self):
        return self.Item_name
