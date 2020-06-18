from app.database import db

class UserRole(db.Model):
   __tablename__ = 'user_roles'
   id = db.Column('id', db.Integer, primary_key = True)
   userid = db.Column('user_id', db.Integer, nullable=False)
   roleid = db.Column('role_id', db.Integer, nullable=False)

def __init__(self, id, userId, roleid):
   self.id = id
   self.userid = userid
   self.roleid = roleid

def __repr__(self):
        return '<UserRole %d - %d>' % (self.userid, self.roleid)