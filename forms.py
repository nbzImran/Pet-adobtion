from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import input_required, Optional, URL, NumberRange, AnyOf


class AddPetForm(FlaskForm):
    """Form for adding a new pet."""
    name = StringField("pet Name", validators=[input_required()])
    species = StringField(
        "Species",
        validators=[
            input_required(),
            AnyOf(["cat", "dog", "porcupine"], message="species must be cate, dog, or porcupine"),
        ],
    )
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField(
        "Age",
        validators=[Optional(), NumberRange(min=0, max=30, message="Age must be between 0 and 30")],
    )
    notes = TextAreaField("Notes", validators=[Optional()])



class EditPetForm(FlaskForm):
    """Form for editing an existed pet."""
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available")