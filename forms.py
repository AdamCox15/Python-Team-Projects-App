from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField

from wtforms.validators import DataRequired, Length



class TeamForm(FlaskForm):
    team_name = SubmitField('team name', validators=[DataRequired(), Length(min=4, max=255)])
    submit = SubmitField("submit")