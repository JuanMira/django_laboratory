from django.db import models

# Create your models here.

class Categories(models.Model):
    nombre_categoria = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre_categoria}"
    
class Movies(models.Model):
    nombre_pelicula = models.CharField(max_length=50)
    fecha_estreno = models.DateField(auto_now=False)
    sinopsis = models.CharField(max_length=255)
    link_pelicula = models.CharField(max_length=255)
    imagen = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categories, on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return (
                f"Peliculas: {self.id},{self.nombre_pelicula},{self.fecha_estreno},{self.sinopsis},{self.link_pelicula}"
                f",{self.imagen},{self.categoria}"
            )
    