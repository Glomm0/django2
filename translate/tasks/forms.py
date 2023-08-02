from django import forms
from .models import Task,TakenTask
INPUT_CLASSES='w-full py-4 px-6 rounded-xl border'
class NewTaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=('text',)
        widgets= {
            'text':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            
        }

class EditTaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=('text',)
        widgets= {
            'text':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            
        }

class NewTakenForm(forms.ModelForm):
    class Meta:
        model=TakenTask
        fields=('answer_text',)
        widgets= {
            'answer_text':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            
        }