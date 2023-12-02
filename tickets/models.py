from .. import db
from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Ticket(db.Model):
    __tablename__ = "tickets_table"
    id = db.Column(db.String(128), primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    status = db.Column(db.String(32), nullable=False)
    priority = db.Column(db.Boolean, nullable=False, default=False)
    dashboard_id: Mapped[str] = mapped_column(ForeignKey("dashboards_table.id"))

    def __repr__(self):
        return '<Ticket %r>' % self.name

    def toDict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "status": self.status,
            "dashboard_id": self.dashboard_id,
            "priority": self.priority
        }