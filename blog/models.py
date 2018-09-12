from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=225)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.title
    def summary(self):
        return self.body[0:100]