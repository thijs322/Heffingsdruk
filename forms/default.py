# Template placeholder
import decimal
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtformsparsleyjs import StringField, SelectMultipleField, BooleanField, SelectField, InputRequired, \
    NumberRange, Length, Optional, IntegerField, DecimalField


class DefaultForm(FlaskForm):
    # General Settings
    name = StringField('Write your name', [InputRequired()],
                                render_kw={"placeholder": "Just your name"}, default="Simon")

    number1 = IntegerField('Pick a number', default=4)
    number2 = IntegerField('Pick a number between 1000 and 2000', [NumberRange(1000, 2000)], default=1019)
    number3 = IntegerField('Pick a number between 1000 and 2000', [NumberRange(1000, 2000)], default=1019)
    provincies = [
                    ("Groningen","Groningen"),
                    ("Friesland","Friesland"),
                    ("Drenthe","Drenthe"),
                    ("Overijssel","Overijssel"),
                    ("Flevoland","Flevoland"),
                    ("Gelderland","Gelderland"),
                    ("Utrecht","Utrecht"),
                    ("NoordHolland","Noord-Holland"),
                    ("ZuidHolland","Zuid-Holland"),
                    ("Zeeland","Zeeland"),
                    ("NoordBrabant","Noord-Brabant"),
                    ("Limburg","Limburg")
                    ]
    provincie = SelectField('Provincies', choices=provincies)

    example_boolean = BooleanField('Example Boolean', default=False)

    def get_errors(self):
        errors = list()
        if self.errors:
            for title, message in self.errors.items():
                if isinstance(message, (list,)):
                    for unique_message in message:
                        new_error = dict()
                        new_error['label'] = self[title].label.text
                        new_error['message'] = unique_message
                        errors.append(new_error)
                else:
                    new_error = dict()
                    new_error['label'] = self[title].label.text
                    new_error['message'] = message
                    errors.append(new_error)
        return errors