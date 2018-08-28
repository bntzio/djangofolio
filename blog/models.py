from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/blog/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:80] + '...'

    def pretty_pub_date(self):
        return self.pub_date.strftime('%b %e %Y')
