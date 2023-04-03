from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import Form, StringField, TextAreaField, DecimalField, IntegerField, validators


class Addproducts(Form):
    name = StringField('Name', [validators.DataRequired()])
    price = DecimalField('Price', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Stock', [validators.DataRequired()])
    colors = StringField('Colors', [validators.DataRequired()])
    description = TextAreaField('Description', [validators.DataRequired()])

    image_1 = FileField('Image 1',
                        validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'], 'Images only please'), FileRequired()])