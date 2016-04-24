from flask_appbuilder.security.sqla.manager import SecurityManager

from app.models import MyUser
from app.sec_views import MyUserDBModelView, MyAuthDBView


class MySecurityManager(SecurityManager):
    user_model = MyUser
    userdbmodelview = MyUserDBModelView
    authdbview = MyAuthDBView