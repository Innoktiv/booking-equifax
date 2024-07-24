from django.db import models

# Create your models here.
class Room(models.Model):
    ROOM_CHOICES = (
        ('kitchen', 'Kitchen'),
        ('common_area', 'Common Area'),
        ('it_room', 'IT Room'),
        ('webinar_room', 'Webinar Room'),
        ('work_room', 'Work Room'),
    )

    name = models.CharField(max_length=20, choices=ROOM_CHOICES)
    number = models.PositiveSmallIntegerField()  # For rooms like Common Area 1, 2, 3
    capacity = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True, null=True)  # Optional description
    amenities = models.JSONField(blank=True, null=True)  # List of amenities as JSON

    class Meta:
        unique_together = ('name', 'number')  # Ensure unique combinations

    def __str__(self):
        return f"{self.get_name_display()} {self.number}"

class Reservation(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    )

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Reservation for {self.room} by {self.user} from {self.start_time} to {self.end_time}"