from app.models.role import Role
from app.database import db

class RoleSeeder():

    def run():
        customer = Role(id = 1, name = 'Customer', keyword = 'customer')
        ace = Role(id = 2, name = 'AccountExecutive', keyword = 'account_executive')
        cashier = Role(id = 3, name = 'Cashier', keyword = 'cashier')
        teller = Role(id = 4, name = 'Teller', keyword = 'teller')

        db.session.add(customer)   
        db.session.add(ace)  
        db.session.add(cashier)  
        db.session.add(teller)  
        db.session.commit()
    