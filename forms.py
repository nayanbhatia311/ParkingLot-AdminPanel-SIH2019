from flask_wtf import Form
from wtforms import TextField,IntegerField,SubmitField
from wtforms import validators, ValidationError

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    address1 = TextField('Address1:', validators=[validators.required()])
    address2 = TextField('Address2:', validators=[validators.required()])
    city = TextField('City:', validators=[validators.required()])
    latitude = IntegerField('Latitude:', validators=[validators.required()])
    longitude = IntegerField('Longitude:', validators=[validators.required()])
    capacity = TextField('Capacity:', validators=[validators.required()])
    days = TextField('Days:', validators=[validators.required()])
    restrictions = TextField('Restrictions:')
    category = TextField('Category:', validators=[validators.required()])
    timing = TextField('Time', validators=[validators.required()])
    chargesperhour = TextField('Charges Per Hour')
    submit = SubmitField('Send')