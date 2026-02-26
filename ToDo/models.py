from django.db import models

# Create your models here.
class ToDo(models.Model):
    titre = models.CharField(max_length=50)
    heure = models.TimeField()
    date = models.DateField()
    rappel = models.BooleanField(default=True)
    status = models.CharField(
        max_length=50,
        choices=[
            ('a_faire', 'à faire'),
            ('en__cours', 'en cours'),
            ('termine', 'terminé')
        ],
        default='a_faire'
    )

    def __str__(self):
        return self.titre