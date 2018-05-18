from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Roster(models.Model):
    name = models.CharField(max_length=50, default="Roster")
    document = models.FileField(upload_to='documents/')
    name_col = models.CharField(max_length=1)
    twitter_col = models.CharField(max_length=1)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    min_followers = models.IntegerField(default=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-uploaded_at']


@receiver(post_delete, sender=Roster)
def roster_delete(sender, instance, **kwargs):
    instance.document.delete(False)


class Player(models.Model):
    roster = models.ForeignKey(Roster, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200, null=True, default="")
    twitter_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class TwitterResult(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    screen_name = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    profile_banner_url = models.URLField(null=True,
                                         blank=True,
                                         default="https://pbs.twimg.com/profile_banners/17874544/1499274456")
    profile_image_url = models.URLField()
    friend = models.BooleanField(default=False)

    class Meta:
        ordering = ['-friend']


class Friend(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    roster = models.ForeignKey(Roster, on_delete=models.CASCADE)
    user_id = models.IntegerField()
