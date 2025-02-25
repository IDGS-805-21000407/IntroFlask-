from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField,EmailField
from wtforms import validators
from wtforms import StringField, IntegerField, BooleanField, SubmitField, EmailField, RadioField

class UserForm(Form):
    matricula = StringField("Matricula",[
        validators.DataRequired(message="Matricula es requerido"),
        validators.Length(min=3, max=10, message="Matricula debe tener entre 3 y 10 caracteres")
    ])
    nombre = StringField("Nombre",[
        validators.DataRequired(message="Nombre es requerido"),
    ])
    apellido = StringField("Apellido",[
        validators.DataRequired(message="Apellido es requerido"),
    ])
    email = EmailField("Correo",[
        validators.Email(message="Correo no valido"),
    ])
    
class UserFormZodiaco(Form):
    nombre = StringField("Nombre", [
        validators.DataRequired(message="Nombre es requerido"),
    ])
    apaterno = StringField("Apellido Paterno", [
        validators.DataRequired(message="Apellido paterno es requerido"),
    ])
    amaterno = StringField("Apellido Materno", [
        validators.DataRequired(message="Apellido materno es requerido"),
    ])
    dia = IntegerField("Día", [
        validators.DataRequired(message="El día es requerido"),
        validators.NumberRange(min=1, max=31, message="El día debe estar entre 1 y 31")
    ])
    mes = IntegerField("Mes", [
        validators.DataRequired(message="El mes es requerido"),
        validators.NumberRange(min=1, max=12, message="El mes debe estar entre 1 y 12")
    ])
    anio = IntegerField("Año", [
        validators.DataRequired(message="El año es requerido"),
        validators.NumberRange(min=1900, max=2025, message="El año debe estar entre 1900 y 2025")
    ])
    sexo = RadioField("Sexo", choices=[('M', 'Masculino'), ('F', 'Femenino')], 
                      validators=[validators.DataRequired(message="Debe seleccionar un sexo")])
    submit = SubmitField("Enviar")