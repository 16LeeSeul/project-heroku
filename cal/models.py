from django.db import models
from django.urls import reverse

FOOD_CHOICES = (
    ('^_^','^_^'),
    ('breakfast', 'BREAKFAST'),
    ('lunch', 'LUNCH'),
    ('dinner', 'DINNER'),
    ('snacks', 'SNACKS'),
)

class Event(models.Model):
    title = models.CharField(max_length=200)
    food = models.CharField(max_length=9, choices=FOOD_CHOICES, default='^_^')
    description = models.TextField()
    calorie = models.PositiveIntegerField(default=0, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.food} : {self.calorie} 칼로리, {self.title}</a>'
