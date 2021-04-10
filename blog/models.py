from django.db import models
from django.utils import timezone
# Create a Blog models.
# title, pub_date, body, image


class Blog(models.Model):

    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(default=timezone.now)
    body = models.TextField()
    # upload_to requires a relative path
    image = models.ImageField(upload_to='images/blog')

# Add the blog app to settings

# Create a migration

# Migrate

# Add to the admin

