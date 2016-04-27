from flask import render_template
from flask.ext.appbuilder import expose, ModelView
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface

from app import appbuilder, db
from app.models import Invitation
from app.sec_views import MyUserDBModelView


@expose("/map/")
def map(self):
    return self.render_template('map.html', param1="Hi")


class InvitationView(ModelView):
    datamodel = SQLAInterface(Invitation)
    related_views = [MyUserDBModelView]

    label_columns = {'question1': 'First Question', 'question2': 'Second Question'}
    list_columns = ['name', 'text', 'question1', 'question2']

    show_fieldsets = [
        ('Summary',{'fields':['name', 'text', 'question1', 'question2']}),
        ('Extended',{'fields':['name', 'text', 'question1', 'question2'],'expanded':False}),
        ]


"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

db.create_all()
appbuilder.add_view(InvitationView(), "Invitations")

