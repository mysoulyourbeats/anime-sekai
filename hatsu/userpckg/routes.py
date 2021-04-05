from flask import Flask, render_template, url_for, redirect, flash, request
from flask_wtf import validators
from flask import Blueprint
from hatsu.userpckg.forms import Registerform, Loginform, Fanform
from hatsu import db, bcrypt
from hatsu.models import Scraped, Register, Fan
from flask_login import login_user, logout_user, login_required, current_user
users = Blueprint('users', __name__)





@users.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = Registerform()
    taken = None
    if form.validate_on_submit():
        user = Register.query.filter_by(email=form.email.data).first()
        if user:
            taken = "Email already in use"
        else:
            hash_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = Register(email=form.email.data, password=hash_pw)
            db.session.add(user)
            db.session.commit()
            flash("Successfully created your account. Check out your email to confirm, if you don't mind?")
            return redirect(url_for('users.layout'))
    return render_template('signup.html', form=form, taken=taken)


@users.route('/login/', methods=['GET', 'POST'])
def login():
    form = Loginform()
    incorrect = None
    if form.validate_on_submit():
        user = Register.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('users.layout'))
        else:
            incorrect = "Email or password incorrect"
    return render_template('login.html', form=form, incorrect=incorrect)


@users.route('/anime/')
def anime():
    page = request.args.get('page', 1, type=int)
    obj = db.session.query(Scraped.thumblist, Scraped.titlelist, Scraped.id).paginate(page=page, per_page=3)
    return render_template('anime.html', obj=obj)


@users.route('/detail/<int:desc_id>')
def detail(desc_id):
    description = db.session.query(Scraped.description).filter_by(id=desc_id).scalar()
    titlelist = db.session.query(Scraped.titlelist).filter_by(id=desc_id).scalar()
    coverimg = db.session.query(Scraped.coverimg).filter_by(id=desc_id).scalar()
    return render_template('detail.html', description=description, titlelist=titlelist, coverimg=coverimg)


@users.route('/layout/')
def layout():
    return render_template('layout.html')


@users.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('users.home'))

@users.route('/submitfiction', methods=['GET', 'POST'])
def submitfiction():
    form = Fanform()
    if form.validate_on_submit():
        user = Fan.query.filter_by(title=form.title.data).first()
        if user:
            flash('taken')
        else:
            user = Fan(title=form.title.data, content=form.content.data)
            db.session.add(user)
            db.session.commit()
            flash('succesful')
            return redirect(url_for('users.layout'))
    return render_template('submitfiction.html', form=form)


@users.route('/fictionlist/')
def fictionlist():
    user = Fan.query.all()
    return render_template('fictionlist.html', user=user)

@users.route('/viewfanfiction/<int:fiction_id>')
def viewfanfiction(fiction_id):
    view = db.session.query(Fan.title, Fan.content).filter_by(id=fiction_id).first()
    return render_template('viewfanfiction.html', view=view)

