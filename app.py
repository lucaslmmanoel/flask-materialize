

from flask import Flask, render_template
from flask_materialize import Material
from flask_wtf import Form, RecaptchaField
from flask_wtf.file import FileField
from wtforms import TextField, HiddenField, ValidationError, RadioField,\
    BooleanField, SubmitField, IntegerField, FormField, validators
from wtforms.validators import Required

app = Flask(__name__)
Material(app)
app.config['SECRET_KEY'] = 'USE-YOUR-OWN-SECRET-KEY-DAMNIT'
app.config['RECAPTCHA_PUBLIC_KEY'] = 'TEST'


class ExampleForm(Form):
    name = TextField('Name', [validators.required()])
    area_code = IntegerField('Years', [validators.required()])
    number = TextField('Number')


@app.route('/')
def hello_world():
      form = ExampleForm()
      return render_template('test.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
