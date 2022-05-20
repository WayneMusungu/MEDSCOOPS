from flask import render_template, url_for, redirect, flash, request
import requests
from medscoop import app, db, bcrypt
from medscoop.forms import RegistrationForm,LoginForm
from medscoop.models import User
from flask_login import login_user, current_user, logout_user, login_required
from medscoop.request import get_drug


@app.route('/')
@app.route('/home')
@login_required
def home():
    drugs = get_drug()
    title = 'Pharyngitis'
    search_disease = request.args.get('disease_query')

    if search_disease:
        return redirect(url_for('search',disease_name = search_disease))
    else:
        return render_template('home.html', title =title, drugs = drugs)

@app.route('/about')
# add a decorator on the about page

def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        
        
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        
        flash(f'Your account has been created you are now able to login!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login',methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        
        return redirect(url_for('home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return  redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            # next_page = request.args.get('next')
            # return redirect(next_page) if next_page else redirect(url_for('home'))
       
            flash('Login Unsuccessful, Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/search/<disease_name>')
def search(disease_name):
    '''
    View function to display the search results
    '''
    disease_name_list = disease_name.split(" ")
    disease_name_format = "+".join(disease_name_list)
    searched_drug = search_drug(disease_name_format)
    title = f'search results for {disease_name}'

    return render_template('search.html',drugs = searched_drug)