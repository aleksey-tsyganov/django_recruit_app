from django.db import models
from django.urls import reverse

# Create your models here.


class Planet(models.Model):
    planet_name = models.CharField(max_length=30)

    def __str__(self):
        return self.planet_name


class Recruit(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200)

    def get_absolute_url(self):
        return reverse("answer_form", kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.CharField(max_length=200)
    order_id = models.PositiveIntegerField()

    def __str__(self):
        return self.question


class Answer(models.Model):
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.BooleanField(default=False)

    def __str__(self):
        return str(self.recruit)

    def get_absolute_url(self):
        return reverse("index")


class Master(models.Model):
    name = models.CharField(max_length=200)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class RecruitStatus(models.Model):
    recruit = models.OneToOneField(Recruit, on_delete=models.CASCADE, primary_key=True)
    master = models.ForeignKey(Master, on_delete=models.CASCADE, blank=True, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.recruit)

    def get_absolute_url(self):
        return reverse("index")