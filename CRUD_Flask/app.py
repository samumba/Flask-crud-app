from app import create_app, db
from app.models import User, Role, VisitLog

app = create_app()

@app.cli.command('init-db')
def init_db():
    db.create_all()
    admin_role = Role.query.filter_by(name='Администратор').first()
    if not admin_role:
        admin_role = Role(name='Администратор', description='Полный доступ к системе')
        db.session.add(admin_role)
    
    user_role = Role.query.filter_by(name='Пользователь').first()
    if not user_role:
        user_role = Role(name='Пользователь', description='Ограниченный доступ к системе')
        db.session.add(user_role)
    
    db.session.commit()
    print('База данных инициализирована.')

@app.cli.command('create-admin')
def create_admin():
    admin_role = Role.query.filter_by(name='Администратор').first()
    if not admin_role:
        admin_role = Role(name='Администратор', description='Полный доступ к системе')
        db.session.add(admin_role)
        db.session.commit()
    
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin = User(
            username='admin',
            firstname='ЭСОНО',
            lastname='МАНГЕ',
            role_id=admin_role.id
        )
        admin.set_password('Admin123')
        db.session.add(admin)
        db.session.commit()
    print('Администратор создан.')

@app.cli.command('create-user')
def create_user():
    user_role = Role.query.filter_by(name='Пользователь').first()
    if not user_role:
        user_role = Role(name='Пользователь', description='Ограниченный доступ к системе')
        db.session.add(user_role)
        db.session.commit()
    
    user = User.query.filter_by(username='user').first()
    if not user:
        user = User(
            username='user',
            firstname='ОЛЬГА',
            lastname='МАНУЭЛА',
            middlename='OЙАНА',
            role_id=user_role.id
        )
        user.set_password('User123')
        db.session.add(user)
        db.session.commit()
    print('Пользователь создан.')

with app.app_context():
    db.create_all()
    admin_role = Role.query.filter_by(name='Администратор').first()
    if not admin_role:
        admin_role = Role(name='Администратор', description='Полный доступ к системе')
        db.session.add(admin_role)
    
    user_role = Role.query.filter_by(name='Пользователь').first()
    if not user_role:
        user_role = Role(name='Пользователь', description='Ограниченный доступ к системе')
        db.session.add(user_role)
    
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)