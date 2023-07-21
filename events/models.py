from django.db import models

class Mentor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Event(models.Model):
    event_id = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    join_link = models.URLField()
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_id

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class RSVP(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.candidate.name} - {self.event.event_id}"




# python manage.py makemigrations
# python manage.py migrate

