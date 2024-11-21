from django import forms
from .models import Usuario

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmar contraseña")

    class Meta:
        model = Usuario
        fields = ['nombre', 'correo', 'password']  # Campos del modelo

    def clean_nombre(self):
        usuario = self.cleaned_data.get('nombre')
        if Usuario.objects.filter(nombre=usuario).exists():
            raise forms.ValidationError('El usuario ya fue registrado anteriormente.')
        return usuario

    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        if '@alumnos.udg.mx' not in correo:
            raise forms.ValidationError('El correo no pertenece a la Universidad de Guadalajara.')
        return correo

    def clean(self):
        datos = super().clean()
        password_1 = datos.get('password')
        password_2 = datos.get('password2')
        if password_1 and password_2 and password_1 != password_2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return datos

    def save(self, commit=True):
        usuario = super().save(commit=False)
        # Guardar la contraseña de manera segura
        usuario.contrasena = self.cleaned_data['password']
        if commit:
            usuario.save()
        return usuario
