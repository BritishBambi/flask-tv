from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class NewShowForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()])
    genre = SelectField('Genre', validators=[DataRequired()], 
                        choices=[('Sci-Fi', 'Sci-Fi'),
                                 ('Crime', 'Crime'),
                                 ('Fantasy', 'Fantasy'),
                                 ('Romance', 'Romance'),
                                 ('Drama', 'Drama'), 
                                 ('Thriller', 'Thriller'),
                                 ('Action', 'Action')
                        ]
                        )
    rating = SelectField('Rating', choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])
    image_url = StringField('Image URL')
    
    submit = SubmitField('Add Show')