from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=20, null=False)
    phone = models.CharField(max_length=20, null=False)

    def __str__(self):
        return "{} - {}".format(self.name, self.phone)


class Shoe(models.Model):
    user = models.ForeignKey(User, related_name='shoes', on_delete=models.CASCADE)
    size = models.IntegerField(default=0)
    color = models.CharField(max_length=20)

    def __str__(self):
        return "{} - {}".format(self.size, self.color)

    class Meta:
        unique_together = ('user', 'id')
        ordering = ['id']
