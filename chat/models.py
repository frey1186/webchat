from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=32)
    signature = models.CharField(max_length=255,
                                 blank=True,null=True)
    head_img = models.ImageField(u"用户头像",
                                 upload_to="uploads/userprofile",
                                 default="uploads/userprofile/default_user_head.ipg")
    #for web chat
    friends = models.ManyToManyField("self",
                                     related_name="my_friends",
                                     blank=True)
    status_choice = (
        (1,"在线"),
        (2,"忙碌"),
        (3,"离线"),
    )
    status = models.IntegerField(choices=status_choice,
                                 default=1)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=64,unique=True)
    brief = models.CharField(max_length=256,
                              blank=True,null=True)
    creater = models.ForeignKey(UserProfile)
    admins = models.ManyToManyField(UserProfile,
                                    related_name="admin_group",
                                    blank=True)
    members = models.ManyToManyField(UserProfile,
                                     related_name="belong_to_group")
    max_members = models.IntegerField(default=200)

    def __str__(self):
        return self.name