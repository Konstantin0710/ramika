from flask.ext.appbuilder import IndexView
from flask.ext.appbuilder import expose, has_access, permission_name
from flask_appbuilder.security.views import UserDBModelView, AuthDBView
from flask_babelpkg import lazy_gettext


class MyUserDBModelView(UserDBModelView):
    """
        View that add DB specifics to User view.
        Override to implement your own custom view.
        Then override userdbmodelview property on SecurityManager
    """
    name = "MyUserDBModelView"

    show_fieldsets = [
        (lazy_gettext('User info'),
         {'fields': ['username', 'active', 'roles', 'login_count', 'invitation', 'assist', 'paid']}),
        (lazy_gettext('Personal Info'),
         {'fields': ['first_name', 'last_name', 'email'], 'expanded': True}),
        (lazy_gettext('Audit Info'),
         {'fields': ['last_login', 'fail_login_count', 'created_on',
                     'created_by', 'changed_on', 'changed_by'], 'expanded': False}),
    ]

    user_show_fieldsets = [
        (lazy_gettext('User info'),
         {'fields': ['username', 'active', 'roles', 'login_count', 'invitation', 'assist', 'paid']}),
        (lazy_gettext('Personal Info'),
         {'fields': ['first_name', 'last_name', 'email'], 'expanded': True}),
    ]

    add_columns = ['first_name', 'last_name', 'username', 'active', 'email', 'roles', 'invitation', 'password',
                   'conf_password', 'assist', 'paid']
    list_columns = ['first_name', 'last_name', 'username', 'email', 'active', 'roles', 'assist', 'paid']
    edit_columns = ['first_name', 'last_name', 'username', 'active', 'email', 'roles', 'invitation', 'assist', 'paid']


class MyIndexView(IndexView):
    index_template = 'index.html'

    @has_access
    @expose('/')
    def index(self):
        self.update_redirect()
        return self.render_template(self.index_template,
                                    appbuilder=self.appbuilder)


class MyAuthDBView(AuthDBView):
    login_template = 'login.html'
