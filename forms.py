from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,BooleanField, SelectField, URLField
from wtforms.validators import optional

class AddPetForm(FlaskForm):
    name = StringField("Pet's name")
    species = SelectField("Species", choices=[('cat','cat'),('dog','dog'),('porcupine','porcupine')])
    photo_url = URLField("Image URL")
    age= IntegerField("Pet's Age", validators=[optional()])
    notes = StringField("Notes")
    available = BooleanField("Availibility", default = True)

class EditPetForm(FlaskForm):
    photo_url = URLField("Image URL")
    notes = StringField("Notes")
    available = BooleanField("Availibility")
