from flask import Blueprint, render_template
from app.modulos.consulta.models import Exames
from peewee import *

main = Blueprint("main", __name__)

@main.route("/")
def homepage():
  exames = Exames.select(Exames.status, fn.COUNT(Exames.status)).group_by(Exames.status)
  print(exames.scalar())
  return render_template('index.html', exames=exames)