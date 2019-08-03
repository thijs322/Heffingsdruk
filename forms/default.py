# Template placeholder
import decimal
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms.fields import Field
from wtformsparsleyjs import StringField, SelectMultipleField, BooleanField, SelectField, InputRequired, \
    NumberRange, Length, Optional, IntegerField, DecimalField


class DefaultForm(FlaskForm):
    # General Settings
    @property
    def form_fields(self):
        for k,v in self.__dict__.items():
            if isinstance(v,Field):
                yield v
    
    postcode = StringField('Postcode:', [InputRequired()],render_kw={"placeholder": "Vul uw postcode in"})
    leeftijd = IntegerField('Leeftijd:', [InputRequired()],render_kw={"placeholder": "Vul uw leeftijd in"})
    bruto_loon_mnd = IntegerField('Bruto loon per maand:', [InputRequired()],render_kw={"placeholder": "Vul uw bruto loon in"})
    bonus = IntegerField('Bonus:', [InputRequired()],render_kw={"placeholder": "Vul uw bonus in"})
    uitgaven_laag = IntegerField('Maandelijkse kosten BTW laag 6% (bedrag incl. btw):', [InputRequired()],render_kw={"placeholder": "Vul uw uitgaven met lage BTW in"})
    uitgaven_hoog = IntegerField('Maandelijkse kosten BTW hoog 21% (bedrag incl. btw):', [InputRequired()],render_kw={"placeholder": "Vul uw uitgaven met hoge BTW in"})
    spaargeld = IntegerField('Vermogen:', [InputRequired()],render_kw={"placeholder": "Vul in hoeveel spaargeld u heeft."})
    schulden = IntegerField('Schulden:', [InputRequired()],render_kw={"placeholder": "Vul in hoe veel schulden u heeft"})
    verbruik_gas = IntegerField('Verbruik gas (m3):', [InputRequired()],render_kw={"placeholder": "Vul in hoe veel gas u verbruikt"})
    verbruik_stroom = IntegerField('Verbruik stroom (kWh):', [InputRequired()],render_kw={"placeholder": "Vul in hoe veel stroom u verbruikt"})
    verbruik_water = IntegerField('Verbruik water (m3):', [InputRequired()],render_kw={"placeholder": "Vul in hoe veel water u verbruikt"})
    kenteken = StringField('Kenteken:', [InputRequired()],render_kw={"placeholder": "Vul het kenteken van uw auto in"})
    prijs = IntegerField('Prijs auto:', [InputRequired()],render_kw={"placeholder": "Vul in hoe veel uw auto gekost heeft"})
    km_jaar = IntegerField('Aantal kilometer per jaar:', [InputRequired()],render_kw={"placeholder": "Vul in hoe veel kilometer u per jaar rijdt"})
    huishouden_personen = IntegerField('Aantal personen in uw huishouden:', [InputRequired()],render_kw={"placeholder": "Vul in hoe personen uw huishouden heeft"})
    fiscale_partner = BooleanField('Heeft u een fiscale partner?',[InputRequired()])

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