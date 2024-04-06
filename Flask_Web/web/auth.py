from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sing_out():
    if request.method == 'POST':
        email = request.form.get('email')
        firts_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 4:
            flash('Email must be greater than 5 characters.', category='error')
        elif len(firts_name) < 2:
            flash('Name must be greater than 3 characters.', category='error')
        elif password1 != password2:
            flash('You password do not match.', category='error')
        elif len(password1) < 7:
            flash('Yout password must be greater than 8 characters', category='error')
        else:
            flash('Account created!', category='success')
            #Add to a database
    return render_template('sign_up.html')
