from django.db import models
from django.db.models import Q
from django.template.defaultfilters import slugify
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
User = settings.AUTH_USER_MODEL



class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)

    def search(self, query):
        lookup = (

                    Q(title__icontains=query) |
                    Q(content__icontains=query) |
                    Q(slug__icontains=query) |
                    Q(user__first_name__icontains=query) |
                    Q(user__last_name__icontains=query) |
                    Q(user__username__icontains=query)
                    )
        return self.filter(lookup)




class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)









class BlogPost(models.Model):
    # one to many relationship, one post can have many post, but post can only have one user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True,blank=True,upload_to='images')
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=False,auto_now=False,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated','-timestamp','-publish_date']

    objects = BlogPostManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('post-detail',
                       args=[self.slug])

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url




