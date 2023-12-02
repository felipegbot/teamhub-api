from .. import db
from typing import List
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column

class Dashboard(db.Model):
    __tablename__ = "dashboards_table"
    id = db.Column(db.String(128), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    tickets: Mapped[List["Ticket"]] = relationship()
    user_id: Mapped[str] = mapped_column(ForeignKey("users_table.id"))

    def __repr__(self):
        return '<Dashboard %r>' % self.username

    def toDict(self):
        return {
            "id": self.id,
            "name": self.name,
            "tickets": [ticket.toDict() for ticket in self.tickets],
            "user_id": self.user_id
        }