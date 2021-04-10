from django.db import models
from django.utils import timezone
# Create a Blog models.
# title, pub_date, body, image


class Blog(models.Model):

    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    summary = models.CharField(max_length=250, null=True)
    # upload_to requires a relative path
    image = models.ImageField(upload_to='images/blog')

    def description(self):
        return self.body[:100] + '...'

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return f'{self.title}'

# Add the blog app to settings

# Create a migration

# Migrate

# Add to the admin

