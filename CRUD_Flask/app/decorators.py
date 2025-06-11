from functools import wraps
from flask import flash, redirect, url_for
from flask_login import current_user

def check_rights(required_role=None, check_self=False):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                flash('Пожалуйста, войдите для доступа к данной странице.', 'danger')
                from flask import request
                return redirect(url_for('auth.login', next=request.path))
            if current_user.is_admin():
                return f(*args, **kwargs)
            if required_role == 'admin' and not current_user.is_admin():
                flash('У вас недостаточно прав для доступа к данной странице.', 'danger')
                return redirect(url_for('main.index'))
            
            if check_self and 'id' in kwargs:
                user_id = int(kwargs['id'])
                if user_id != current_user.id:
                    flash('У вас недостаточно прав для доступа к данной странице.', 'danger')
                    return redirect(url_for('main.index'))
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator