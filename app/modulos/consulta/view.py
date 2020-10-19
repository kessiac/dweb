import peewee
from flask import Blueprint, render_template, request, redirect, url_for

from .models import Exames
from .forms import CategoryForm

cons = Blueprint("cons", __name__)

@cons.route("/consulta", methods=['GET'])
def conspage():
  form = CategoryForm(request.form)
  return render_template('consulta.html', form=form)

@cons.route('/consulta', methods=['POST'])
def formPost():
  form = CategoryForm(request.form)
  if form.validate_on_submit():

    try:
      Exames.create(name=form.name.data, gender=form.gender.data, age=form.age.data,email=form.email.data, tell= form.tell.data, district= form.district.data, group_risk= form.group_risk.data, symptoms= form.symptoms.data)
    except peewee.IntegrityError:
      return render_template('enviado.html', error='Paciente já cadastrado!')

  return render_template('enviado.html', form=form)