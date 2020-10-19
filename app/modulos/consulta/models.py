import peewee
from app.modulos.core import models as core

class Exames(core.BaseModel):

  name = peewee.CharField(unique=True)
  gender = peewee.CharField()
  age = peewee.IntegerField()
  email = peewee.CharField()
  tell = peewee.IntegerField()
  district = peewee.CharField()
  group_risk = peewee.CharField()
  symptoms = peewee.TextField()

