from django.db import models


class Task(models.Model):
    ege_num = models.IntegerField(unique=False, blank=False, null=False, verbose_name='EGE Number')
    desc = models.TextField(unique=False, blank=False, null=False, verbose_name="Description")
    ege_data = models.CharField(max_length=4, unique=False, blank=False, null=True, verbose_name="First appeared in EGE")
    is_used_in_exam = models.BooleanField(default=False, blank=False, null=False, verbose_name="Is used in exam")

    def __str__(self):
        return f'№{self.ege_num} ({self.ege_data})'


