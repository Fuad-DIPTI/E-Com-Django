from django.db import models

class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=127)
    image_path = models.CharField(max_length=127)
    price = models.IntegerField()
    description = models.CharField(max_length=511)

    class ReviewStatus(models.IntegerChoices):
        PENDING = 0, "Pending"
        VERYBAD = 1, "Very Bad"
        BAD = 2, "Bad"
        USEABLE = 3, "Useable"
        GOOD = 4, "Good"
        VERYGOOD = 5, "Very Good"

    ratings = models.IntegerField(
        choices=ReviewStatus.choices,
        default=ReviewStatus.PENDING
    )

    review_comment = models.CharField(max_length=511)
    stock = models.IntegerField()

    def __str__(self):
        return self.name