from djongo import models


class Comment(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.author


class Tag(models.Model):
    title = models.CharField(max_length=300)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Entry(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ArrayField(model_container=Tag, blank=True, null=True)
    comments = models.EmbeddedField(model_container=Comment, blank=True, null=True)

    def __str__(self):
        return self.title

