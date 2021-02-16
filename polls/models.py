import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # self.pub_date = timezone.now()
        # self.question_text = kwargs.get('question_text', '')

    def __str__(self) -> str:
        if len(self.question_text) > 20:
            return self.question_text[:10].strip() + '...' + self.question_text[-10:].strip()
        else:
            return self.question_text.strip()

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    # you can control how a function is displayed in the Admin UI by adding attributes to it
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        if len(self.choice_text) > 20:
            return self.choice_text[:10].strip() + '...' + self.choice_text[-10:].strip()
        else:
            return self.choice_text.strip()

