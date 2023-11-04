from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required

from pyttpass.passwords import password_bp
from pyttpass.extensions import db
from pyttpass.models.passwords import Password, AddPassword


@password_bp.route('/')
@login_required
def index():
    passwords = Password.query.all()
    return render_template('passwords/index.html', pwds=passwords)


@password_bp.route('/add_password/', methods=['GET', 'POST'])
@login_required
def add_password():
    form1 = AddPassword()
    if form1.validate_on_submit():
        name = request.form['name']
        website = request.form['website']
        username = request.form['username']
        value = request.form['value']
        desc = request.form['desc']
        record = Password(name, website, username, value, desc)
        db.session.add(record)
        db.session.commit()
        # create a message to send to the template
        message = f"The data for password {name} has been submitted."
        return render_template('passwords/add_password.html', message=message)
    else:
        for field, errors in form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(form1, field).label.text,
                    error
                ), 'error')
        return render_template('passwords/add_password.html', form1=form1)

#TODO: Create relation that ties password to user

@password_bp.route('/<int:password_id>/')
@login_required
def show_password(password_id):
    password = Password.query.get_or_404(password_id)
    return render_template('passwords/password.html', pwd=password)


@password_bp.post('/<int:password_id>/delete/')
@login_required
def del_password(password_id):
    password = Password.query.get_or_404(password_id)
    db.session.delete(password)
    db.session.commit()
    return redirect(url_for('passwords.index'))