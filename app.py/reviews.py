from datetime import datetime
from app import db, login
from flask_login import UserMixin

class Review(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(64), index=True, unique=True)  # Assuming only unique authors can submit
    body = db.Column(db.Text, index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f'<Review {self.author}>'
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class ReviewForm(FlaskForm):
    author = StringField('Author', validators=[DataRequired()])
    body = TextAreaField('Body', validators=[DataRequired()])
from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import ReviewForm
from app.models import Review

@app.route('/review', methods=['GET', 'POST'])
@login_required  # This ensures only logged-in users can submit reviews
def review():
    form = ReviewForm()
    if form.validate_on_submit():
        review = Review(author=form.author.data, body=form.body.data)
        db.session.add(review)
        db.session.commit()
        flash('Your review has been submitted.', 'success')
        return redirect(url_for('index'))  # Redirect to the desired page after submission
    return render_template('review.html', title='Review', form=form)
