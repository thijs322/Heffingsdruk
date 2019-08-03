from flask import Flask, render_template, jsonify, request, session
from forms.default import DefaultForm
import os
from resources.utils import get_next_ten_numbers
from resources.plots import create_plot
from src.calculate_tax import Persoon, Voertuig, Belasting, Calculation


def create_app():
    new_app = Flask(__name__)
    new_app.config.update(dict(
        SECRET_KEY="powerful secretkey",
        WTF_CSRF_SECRET_KEY="a csrf secret key"
    ))
    return new_app


app = create_app()

@app.route('/', methods=['GET', 'POST'])
def main_page():
    data = dict()  # data object to be passed back to the web page
    plots = dict()
    data['submitted'] = False

    settings_dict = None

    if settings_dict is None:
        form = DefaultForm()
    else:  # Can be used later as a sort of cookie, not relevant now
        form_data = process_settings_dict(settings_dict)
        form = DefaultForm(data=form_data)

    if form.validate_on_submit() or settings_dict is not None:
        data = form.data  # Gets all variable values from the form
        data['submitted'] = True  # Add hardcoded variables, for example to show whether the form has already been submitted

        # Process input with logic
        data['number_range'] = get_next_ten_numbers(data['number2'])
        plots['example_plot'] = create_plot(data['number1'])

    data['errors'] = form.get_errors()  # Relay errors, can be usefull for debugging

    return render_template('main.html', title='Titel template', form=form, data=data, plots=plots)

@app.route('/page2')
def show_page2():
    return render_template('page2.html', title='Page2')

if __name__ == '__main__':
    # start the app
    boris = Persoon('5531vg', 25, 2500, 10000, 300, 600, 2000, 35000, 1500, 3000, 93)
    auto = Voertuig(boris, '85tdpv', 2500, 20000)
    tax = Belasting(boris, auto, 2, 0)
    resultaat = Calculation(boris, auto, tax)
    resultaat.get_auto()
    resultaat.get_loon()
    resultaat.get_BTW()
    resultaat.show('both')
    app.run(debug=True)
