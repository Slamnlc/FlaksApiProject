from config import Config
from helpers.helpers import hash_text


def create_admin_role():
    from database.models import Roles

    if not Roles.exists(name="admin"):
        Roles(name="admin", can_delete=True).add()


def create_admin_user():
    from database.models import Users, Roles

    if not Users.exists(username=Config.ADMIN_USER):
        role = Roles.filter_by(name="admin", can_delete=True).first()
        Users(
            role_id=role.id,
            username=Config.ADMIN_USER,
            password=hash_text(Config.ADMIN_PASS),
        ).add()
