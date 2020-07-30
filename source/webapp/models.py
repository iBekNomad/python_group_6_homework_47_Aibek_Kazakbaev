from django.db import models
from django.utils import timezone

STATUS_CHOICES = [
    ('new', 'New'),
    ('in_progress', 'In progress'),
    ('done', 'Done')
]


class QuickMemo(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name='Description')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='new', verbose_name='New')
    text = models.TextField(max_length=3000, null=True, blank=False, default='', verbose_name='Detailed description')
    execution_date = models.DateField(blank=True, default=timezone.now, verbose_name='Execution date')
    updated_at = models.DateField(auto_now=True, verbose_name='Updated date')

    def __str__(self):
        return "{}. {}".format(self.pk, self.description)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
