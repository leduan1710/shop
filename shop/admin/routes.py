from flask import flash, render_template, session, request, redirect, url_for
from shop import app, db, bcrypt
from .models import User
from .forms import RegistrationForm, LoginForm
from shop.products.models import Addproduct, Brand, Category

@app.route('/')
@app.route('/admin')
def admin():
    if 'email' not in session:
        flash(f'Please login', 'danger')
        return redirect(url_for('login'))
    products = Addproduct.query.all()
    return render_template('admin/index.html', title = 'Home Page', products=products)
#brand
@app.route('/brand')
def brand():
    if 'email' not in session:
        flash(f'Please login', 'danger')
        return redirect(url_for('login'))
    brands = Brand.query.order_by(Brand.id.desc()).all()
    return render_template('admin/brand.html', title = 'Brand Page', brands = brands)
@app.route('category', methods=['GET', 'POST'])
def category():
    if 'email' not in session:
        flash(f'Please login', 'danger')
        return redirect(url_for('login'))
    categories = Category.query.order_by(Category.id.desc()).all()
    return render_template('admin/category.html', title = 'Category Page', categories = categories)
#register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, username= form.username.data,email= form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome {form.name.data}! You have successfully registered', 'success')
        return redirect(url_for('login'))
    return render_template('admin/register.html', form=form, title = 'Registeration Page')

#login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Welcome {form.email.data}! You have successfully logged in', 'success')
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash(f'Invalid email or password! Please try again', 'danger')

    return render_template('admin/login.html', form=form, title = 'Login Page')
# function to logout