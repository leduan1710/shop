from flask import flash, render_template, request, redirect, url_for, session
from shop import app, db, photos
from .models import Brand, Category, Addproduct
from .forms import Addproducts
import secrets
# addBrand
@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    if request.method == "POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash(f'The brand {getbrand} added successfully', 'success')
        db.session.commit()
        return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html', brands='brands')

@app.route('/addcate', methods=['GET', 'POST'])
def addcate():
    if 'email' not in session:
        flash(f'Please login first', 'danger')
        return redirect(url_for('login'))
    if request.method == "POST":
        getcate = request.form.get('category')
        cate = Category(name=getcate)
        db.session.add(cate)
        flash(f'The category {getcate} added successfully', 'success')
        db.session.commit()
        return redirect(url_for('addcate'))
    return render_template('products/addbrand.html')

#addproduct
@app.route('/addproduct', methods=['GET', 'POST'])
def addproduct():
    if 'email' not in session:
        flash(f'Please login', 'danger')
        return redirect(url_for('login'))
    brands = Brand.query.all()
    categories = Category.query.all()

    form = Addproducts(request.form)
    if request.method == "POST":
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        colors = form.colors.data
        desc = form.description.data
        brand = request.form.get('brand')
        category = request.form.get('category')
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10)+".")
        addpro = Addproduct(name=name, price=price, discount=discount, stock=stock, colors=colors, desc=desc, 
                             brand_id=brand, category_id=category, image_1=image_1)
        db.session.add(addpro)
        flash(f'The product {name} has been addded', 'success')
        db.session.commit()
        return redirect(url_for('addproduct'))
    return render_template('products/addproduct.html', title = 'Add Product Page',form=form, brands=brands, categories=categories) 

    
