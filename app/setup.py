from app.models.role import Role as RoleModel
from app.models.user import User as UserModel
from app.models.user_role import UserRole as UserRoleModel

from app.seeds.roles import RoleSeeder
from app.seeds.users import UserSeeder

def seedData(application, db):
    with application.app_context():
        print("Running Roles Seeder...")
        RoleSeeder.run()
        print("Running User Seeder...")
        UserSeeder.run()

def recreateTables(application, db):
    with application.app_context():
        print("Dropping All tables...")
        db.drop_all()
        print("Creating All tables...")
        db.create_all()
        print("Commiting Changes...")
        db.session.commit()
        print("All Table Re created")