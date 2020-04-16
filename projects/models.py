from django.db import models
WIP_CHOICES = (
    ('Ideation Phase', 'ID8'),
    ('Development Phase', 'DPP'),
    ('Testing Phase', 'TP'),
    ('Finished', 'FIN')
)
class Projects(models.Model):
    image = models.ImageField(upload_to='images/')
    date_posted = models.DateTimeField()
    post_desc = models.CharField(max_length = 150)
    post_title = models.CharField(max_length = 50)
    work_in_progress = models.CharField(max_length = 20, choices = WIP_CHOICES)
    #work_in_progress = models.BooleanField()
    post_link = models.CharField(max_length = 200, default='')
