from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Internship(models.Model):
    internship_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    apply_before = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    skills_required = models.ManyToManyField(Skill, through='InternshipSkill')
    duration = models.CharField(max_length=50)
    stipend = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.internship_id}: {self.title}"


class InternshipSkill(models.Model):
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.internship} requires {self.skill}"
