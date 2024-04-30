from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_user import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False, default='')
    last_name = db.Column(db.String(50), nullable=False, default='')
    gender = db.Column(db.String(10))
    date_of_birth = db.Column(db.DateTime)

    def __repr__(self):
        return f'User({self.username}, {self.email})'
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class UserProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    date_of_birth = DateField('Date of Birth', format='%Y-%m-%d', validators=[DataRequired()])
@app.route('/profile', methods=['GET', 'POST'])
@login_required  # This ensures only logged-in users can access the profile
def profile():
    form = UserProfileForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.gender = form.gender.data
        current_user.date_of_birth = form.date_of_birth.data
        db.session.commit()
        flash('Your profile has been updated.', 'success')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.gender.data = current_user.gender
        form.date_of_birth.data = current_user.date_of_birth
    return render_template('profile.html', form=form)
{% extends "base.html" %}

{% block content %}
<h2>User Profile</h2>
<form action="" method="post">
    {{ form.hidden_tag() }}  <div>
        {{ form.first_name.label }} {{ form.first_name(size=30) }}  <span>{{ form.first_name.errors }}</span>  </div>
    <div>
        {{ form.last_name.label }} {{ form.last_name(size=30) }}
        <span>{{ form.last_name.errors }}</span>
    </div>
    <div>
        {{ form.gender.label }} {{ form.gender(coerce=int) }}  <span>{{ form.gender.errors }}</span>
    </div>
    <div>
        {{ form.date_of_birth.label }} {{ form.date_of_birth }}
        <span>{{ form.date_of_birth.errors }}</span>
    </div>
    <input type="submit" value="Update Profile">
</form>
{% endblock %}
