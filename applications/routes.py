from applications import app, db
from flask import render_template, flash, redirect, url_for, get_flashed_messages, request
from applications.forms import NewShowForm
from applications.models import TVShow

@app.route('/')
def index():
    entries = TVShow.query.order_by(TVShow.title.asc()).all()
    return render_template('index.html', entries=entries)

@app.route('/add' , methods = ['GET', 'POST'])
def add_tvshow():
    form = NewShowForm()
    if form.validate_on_submit():
        entry = TVShow(title = form.title.data, genre = form.genre.data, rating = form.rating.data, image_url = form.image_url.data)
        db.session.add(entry)
        db.session.commit()
        flash(f"Added {form.title.data} to the database", "success")
        return redirect(url_for('index'))
    return render_template('add.html', form = form)

@app.route('/edit/<int:entry_id>' , methods = ['GET', 'POST'])
def edit_tvshow(entry_id):
    form = NewShowForm()
    if form.validate_on_submit():
        entry = TVShow.query.get_or_404(entry_id)
        entry.title = request.form.get('title')
        entry.genre = request.form.get('genre')
        entry.rating = request.form.get('rating')
        entry.image_url = request.form.get('image_url')
        db.session.commit()
        flash(f"Edited {form.title.data} in the database", "success")
        return redirect(url_for('index'))
    return render_template('edit.html', form = form)



@app.route('/delete/<int:entry_id>')
def delete(entry_id):
    entry = TVShow.query.get_or_404(entry_id)
    db.session.delete(entry)
    db.session.commit()
    flash('Your show has been deleted!', 'success')
    return redirect(url_for('index'))

