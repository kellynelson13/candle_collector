from django.db import models
from django.urls import reverse

ROOM = (
    ('L', 'Living Room'),
    ('B', 'Bedroom'),
    ('D', 'Dining Room')
)

# Create your models here.
class Candle(models.Model):
    scent = models.CharField(max_length=75)
    color = models.CharField(max_length=75)
    ounces = models.IntegerField()
    burn_time = models.IntegerField()

    def __str__(self):
        return self.scent

    def get_absolute_url(self):
        return reverse('detail', kwargs={'candle_id': self.id})


class Burning(models.Model):
    date = models.DateField('burning date')
    duration = models.IntegerField()
    room = models.CharField(
        max_length=1,
        choices=ROOM,
        default=ROOM[0][0]
    )
    # Create a cat_id FK
    candle = models.ForeignKey(Candle, on_delete=models.CASCADE)

    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.candle} in the {self.get_room_display()} was burning for {self.duration} minutes on {self.date}."

    class Meta:
        ordering = ['-date']