
from .. import db
from flask_login import UserMixin
from typing import List
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
class User(UserMixin, db.Model):
    __tablename__ = "users_table"
    id = db.Column(db.String(128), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(126), nullable=False)
    specialty = db.Column(db.String(32), nullable=False)
    working_area = db.Column(db.String(32), nullable=False)
    dashboards: Mapped[List["Dashboard"]] = relationship()

    def __repr__(self):
        return '<User %r>' % self.username

    def toDict(self):
        return {
            "id": self.id,
            "username": self.username,
            "name": self.name,
            "email": self.email,
            "specialty": self.specialty,
            "working_area": self.working_area,
            "dashboards": [dashboard.toDict() for dashboard in self.dashboards]
        }