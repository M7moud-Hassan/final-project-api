from datetime import datetime

from django.db import models

from authentication.models import Skills, RegisterFreelancer

from authentication.models import RegisterUser


# Create your models here.

class JobImages(models.Model):
    id = models.AutoField
    image = models.ImageField(upload_to='images/images_job/')


class LikeJob(models.Model):
    id = models.AutoField
    id_free = models.ForeignKey(RegisterFreelancer, on_delete=models.CASCADE)


class DisLike(models.Model):
    id = models.AutoField
    id_free = models.ForeignKey(RegisterFreelancer, on_delete=models.CASCADE)


class Job(models.Model):
    id = models.AutoField
    create_at = models.DateTimeField(default=datetime.now, blank=True)
    title = models.CharField(max_length=50)
    cost = models.DecimalField(decimal_places=2, max_digits=10)
    images = models.ManyToManyField(JobImages, blank=True)
    description = models.CharField(max_length=1000)
    skills = models.ManyToManyField(Skills, blank=True)
    Proposals = models.ManyToManyField(RegisterFreelancer, blank=True)
    is_pyment = models.BooleanField(default=False)
    likes = models.ManyToManyField(LikeJob, blank=True)
    dislikes = models.ManyToManyField(DisLike, blank=True)
    is_hire=models.BooleanField(default=False)
    client_id = models.ForeignKey(RegisterUser, on_delete=models.CASCADE)


class notificationsClient(models.Model):
    user_sender = models.ForeignKey(RegisterFreelancer, null=True, blank=True, related_name='user_sender',
                                    on_delete=models.CASCADE)
    user_revoker = models.ForeignKey(RegisterUser, null=True, blank=True, related_name='user_revoker',
                                     on_delete=models.CASCADE)
    status = models.CharField(max_length=264, null=True, blank=True, default="unread")
    type_of_notification = models.CharField(max_length=264, null=True, blank=True)

class notificationsFree(models.Model):
    user_sender = models.ForeignKey(RegisterUser, null=True, blank=True, related_name='user_sender',
                                    on_delete=models.CASCADE)
    user_revoker = models.ForeignKey(RegisterFreelancer, null=True, blank=True, related_name='user_revoker',
                                     on_delete=models.CASCADE)
    status = models.CharField(max_length=264, null=True, blank=True, default="unread")
    type_of_notification = models.CharField(max_length=264, null=True, blank=True)


class ImagesSendApply(models.Model):
    id = models.AutoField
    image = models.ImageField(upload_to="images/applay_images/")


class SendApply(models.Model):
    free = models.ForeignKey(RegisterFreelancer,
                             on_delete=models.CASCADE)
    cover = models.CharField(max_length=20000)
    job = models.ForeignKey(Job,
                            on_delete=models.CASCADE)
    images = models.ManyToManyField(ImagesSendApply, blank=True)
    cost_re = models.DecimalField(max_digits=10, decimal_places=2)
    cost_comp = models.DecimalField(max_digits=10, decimal_places=2)
    is_hire=models.BooleanField(default=False)


class Hires(models.Model):
    client = models.ForeignKey(RegisterUser,
                               on_delete=models.CASCADE)
    free = models.ForeignKey(RegisterFreelancer,
                             on_delete=models.CASCADE)
    job = models.ForeignKey(Job,
                            on_delete=models.CASCADE)
    cost=models.DecimalField(decimal_places=2,max_digits=10)
    is_finish=models.BooleanField(default=False)
    is_payment=models.BooleanField(default=False)


class ReviewAndRate(models.Model):
    id=models.AutoField
    client= models.ForeignKey(RegisterUser,
                             on_delete=models.CASCADE)
    free = models.ForeignKey(RegisterFreelancer,
                             on_delete=models.CASCADE)
    rate=models.IntegerField(max_length=5)
    review=models.CharField(max_length=5000)
