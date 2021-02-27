from django.forms import ModelForm,DateInput,Textarea
from Movies.models import Movies

class MoviesForm(ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'
        widgets = {
            'fecha_estreno':DateInput(attrs={'type':'date'}),
            'sinopsis':Textarea(attrs={'rows':4,'cols':15})
        }