from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField()
    create_at = models.DateTimeField(auto_now_add=True)

class Vote(models.Model):
    voter_name = models.CharField(max_length=100, unique=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='votes')
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.voter_name} -> {self.candidate.name}"
     