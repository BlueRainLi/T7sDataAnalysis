from flask_wtf import FlaskForm
from wtforms import SelectField,SubmitField,FieldList,StringField,IntegerField
from wtforms import widgets
from static.test import character_choice,rarity_id
from wtforms.validators import Required

class card_selection(FlaskForm):
    characters = SelectField(
        label="Character",
        choices=character_choice,
        widget=widgets.Select(),
        validators=[Required()]
    )
    Rarity = SelectField(
        label="Rare",
        choices=rarity_id,
        widget=widgets.Select(),
        validators=[Required()]
    )
    Cp = SelectField(
        label="Cost",
        choices=[(0, '-'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (999, '999')],
        widget=widgets.Select(),
        validators=[Required()]
    )
    submit = SubmitField('Submit')


# class songlist(FlaskForm):
#     song = FieldList()