from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    post_hit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    @property
    def update_counter(self):
        self.post_hit = self.post_hit + 1
        self.save()


# Create your models here.
