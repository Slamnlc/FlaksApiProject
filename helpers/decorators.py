from database.models import Users
from helpers.helpers import get_current_token


def is_login(role=None):
    def check_auth(user_role: str = None):
        token = get_current_token()
        if not token:
            return {"error": "Missing token"}, 401
        user = Users.filter_by(access_token=token)
        if not user:
            return {"error": "Incorrect token"}, 401
        if user.is_token_expired:
            return {"error": "Token expired"}, 401
        if user_role and user.role.name != user_role:
            return {"error": "Wrong access"}

    def wrapper_with_role(func):
        def wrap(*args, **kwargs):
            result = check_auth(role)
            return result if result else func(*args, **kwargs)

        return wrap

    def wrapper_cls(*args, **kwargs):
        result = check_auth()
        return result if result else role(*args, **kwargs)

    if callable(role):
        return wrapper_cls
    return wrapper_with_role
