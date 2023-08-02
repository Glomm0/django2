from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    class Meta:
        ordering=("created_at",)
        verbose_name_plural= "tasks"
    def __str__(self):
        return self.text[:20]
    
    created_by=models.ForeignKey(User,related_name='tasks',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    text=models.TextField(blank=False,null=False)
    is_done=models.BooleanField(default=False)
    # answer=models.ForeignKey("TakenTask",on_delete=models.DO_NOTHING)
class TakenTask(models.Model):
    class Meta:
        ordering=("taken_at",)
        verbose_name_plural= "taken tasks"
    def __str__(self):
        return self.answer_text[:20]
    
    taken_by=models.ForeignKey(User,related_name='taken_tasks',on_delete=models.CASCADE)
    taken_at=models.DateTimeField(auto_now_add=True)
    answer_text=models.TextField(blank=True,null=True)
    taken_task=models.ForeignKey(Task,related_name="answer",on_delete=models.CASCADE)