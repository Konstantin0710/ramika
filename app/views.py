from flask import render_template
from flask.ext.appbuilder import expose, ModelView, BaseView
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface

from app import appbuilder, db
from app.models import Invitation
from app.sec_views import MyUserDBModelView
from flask import g

class InvitationView(ModelView):
    datamodel = SQLAInterface(Invitation)
    related_views = [MyUserDBModelView]

    label_columns = {'question1': 'First Question', 'question2': 'Second Question'}
    list_columns = ['name', 'text', 'question1', 'question2']

    show_fieldsets = [
        ('Summary', {'fields': ['name', 'text', 'question1', 'question2']}),
        ('Extended', {'fields': ['name', 'text', 'question1', 'question2'], 'expanded': False}),
    ]


"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404


db.create_all()
appbuilder.add_view(InvitationView(), "Invitations")


class MapView(BaseView):
    default_view = 'map'

    @expose('/map/')
    def map(self):
        assist_classes = 'selected-button' if g.user.assist is True else ''
        not_assist_classes = 'selected-button' if g.user.assist is False else ''
        return self.render_template('map.html', assist_classes=assist_classes, not_assist_classes=not_assist_classes)

    @expose('/assist/')
    def assist(self):
        g.user.assist = True
        self.appbuilder.get_session().commit()
        return 'Success'

    @expose('/not-assist/')
    def not_assist(self):
        g.user.assist = False
        self.appbuilder.get_session().commit()
        return 'Success'


appbuilder.add_view(MapView(), "Map")
