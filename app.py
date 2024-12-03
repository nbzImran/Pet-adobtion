from flask import Flask, render_template, redirect, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config.from_object('config')

# Connect the database
connect_db(app)

# Intialize extention
toolbar = DebugToolbarExtension(app)

# Create the tables
with app.app_context():
    db.create_all



@app.route('/')
def home():
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)


@app.route('/add', methods=["GET", "POST"])
def show_add_pet():
    form = AddPetForm()

    # Handle form submission
    if form.validate_on_submit():
        #if form validates, create a new pet and save to DB
        pet = Pet(
            name = form.name.data,
            species = form.species.data,
            photo_url = form.photo_url.data,
            age = form.age.data,
            notes = form.notes.data
        )

        db.session.add(pet)
        db.session.commit()

        # Flash success message and redirect to home page
        flash(f"{pet.name} has been added successfully!", "success")
        return redirect('/')

    return render_template('pet_add.html', form=form)


@app.route('/<int:pet_id>', methods=["GET", "POST"])
def edit_pet(pet_id):
    """show pet details and allow editing."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)


    if form.validate_on_submit():
        #Update pet details from the form 

        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        flash(f"{pet.name}'s detail have been updated!", "success")
        return redirect('/')
    
    return render_template('edit_pet.html', pet=pet, form=form)