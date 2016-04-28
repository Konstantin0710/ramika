from flask.ext.appbuilder import Model
from flask_appbuilder.security.sqla.models import User
from sqlalchemy import Column, Integer, Text, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship


class MyUser(User):
    invitation_id = Column(Integer, ForeignKey("invitation.id"))
    invitation = relationship("Invitation")
    assist = Column(Boolean)
    paid = Column(Boolean, default=False)


class Invitation(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    text = Column(Text)
    question1 = Column(Text)
    question2 = Column(Text)

