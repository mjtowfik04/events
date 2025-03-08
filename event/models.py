from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return self.name

class Participant(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    events = models.ManyToManyField(Event, related_name='participants')


    def __str__(self):
        return self.name


# @receiver(post_save, sender=Event)
# def notify_Participant_send_email(sender, instance, **kwargs):
#     if created:
#         category_emails = [emp.email for emp in instance.category.all()]
#         send_mail(
#             "New event category",
#             f"You have been categorized for the event: {instance.name}",
#             "mjtowfik659672@gmail.com",
#             category_emails,
#             fail_silently=False,
#         )
