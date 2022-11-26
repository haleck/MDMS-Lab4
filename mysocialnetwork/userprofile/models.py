from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    status = models.TextField(max_length=200)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")

    def __str__(self):
        return self.name + f', user with id: {self.pk}'


class Points(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Post(models.Model):
    text = models.TextField(max_length=800)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")


class Comments(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=400)


class Photos(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")

