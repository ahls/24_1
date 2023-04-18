"""Blogly application."""
from flask import Flask, request, render_template,redirect, flash, session

#from flask_debugtoolbar import DebugToolBarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///petadoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'hehe123'
#debug= DebugToolBarExtension(app)
connect_db(app)

with app.app_context():
    db.create_all()

@app.route('/')
def homepage():
    pets = Pet.query.all()
    return render_template('homepage.html',pets = pets)

@app.route('/add', methods=['POST','GET'])
def addPage():
    form = AddPetForm()
    if form.validate_on_submit():
        newPet = Pet(name = form.name.data,species = form.species.data, photo_url = form.photo_url.data, age = form.age.data,notes = form.notes.data )
        db.session.add(newPet)
        db.session.commit()
        return redirect('/') 
    else:
        print("failed on ifstatement")
        return render_template('addPet.html',form = form)
    
@app.route('/pets/<int:id>')
def petDetail(id):
    pet = Pet.query.get_or_404(id)
    return render_template('petDetail.html',pet=pet)

@app.route('/pets/<int:id>/edit', methods=['POST','GET'])
def editPet(id):
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj = pet)
    if form.validate_on_submit(): 
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data 
        pet.available = form.available.data
        db.session.commit()
        return redirect(f'/pets/{id}') 
    else:
        print("failed on ifstatement")
        return render_template('editPet.html',pet = pet, form = form)
    