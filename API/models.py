from django.db import models

from django.utils.safestring import mark_safe


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    state = models.BooleanField('State', default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

def url_book(self, filename):
    route = "static/images/Books/%s/%s" % (self.name, str(filename))
    return route

def url_book_file(self, filename):
    route = "static/books/%s/%s" % (self.name, filename)
    return route

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    image = models.ImageField(upload_to=url_book)
    file = models.FileField(upload_to=url_book_file)
    state = models.BooleanField('State',default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def image_book(self):
        return mark_safe('<a href="/%s"><img src="/%s" height="50px" width="50px" /></a>' % (self.image, self.image))
    image_book.allow_tags = True

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['name']

    def __str__(self):
        return self.name