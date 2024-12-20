from django.forms import ModelForm
from movies.models import MovieInfo

class MovieForm(ModelForm):
    class Meta:
        model=MovieInfo
        fields='__all__'
        
    