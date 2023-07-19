from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields specific to the company

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields specific to the skill

    def __str__(self):
        return self.name


class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    description = models.TextField()
    apply_before = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    skills_required = models.ManyToManyField(Skill, through='JobSkill')

    def __str__(self):
        return f"{self.job_id}: {self.description}"


class JobSkill(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.job} requires {self.skill}"