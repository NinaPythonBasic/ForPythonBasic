from django.db import models


class Category(models.Model):
    name = models.CharField(
        verbose_name="name", max_length=128, blank=False, null=False
    )


class Book(models.Model):
    author = models.CharField(
        verbose_name="author", max_length=128, blank=False, db_index=True
    )
    name = models.CharField(
        verbose_name="name", max_length=256, blank=False, db_index=True
    )
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    publisher = models.CharField(verbose_name="publisher", max_length=104)
    year = models.IntegerField(verbose_name="year of publication")
    place = models.CharField(verbose_name="place in library", max_length=256)
    details = models.TextField(verbose_name="details", default="")
    onhand = models.BooleanField(verbose_name="book on hand", default=False)


class Reader(models.Model):
    name = models.CharField(
        verbose_name="first name and last name",
        max_length=184,
        blank=False,
        db_index=True,
    )
    address = models.CharField(verbose_name="address", max_length=256)
    phone = models.CharField(verbose_name="phone", max_length=10)


class BookOnHand(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    reader = models.ForeignKey(Reader, on_delete=models.PROTECT)
    issuedate = models.DateField(verbose_name="date of issue")
    returndate = models.DateField(verbose_name="return date", null=True)
    details = models.TextField(verbose_name="details", default="")
