from flask_wtf import Form
from wtforms import SelectField,SubmitField
from static.test import character_choice,rarity_id
from wtforms.validators import Required

class card_selection(Form):
    characters = SelectField(
        label="Character",
        choices=character_choice,
        validators=[Required()]
    )
    Rarity = SelectField(
        label="Rare",
        choices=rarity_id,
        validators=[Required()]
    )
    submit = SubmitField('Submit')