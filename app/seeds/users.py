from app.models.user import User
from app.models.user_role import UserRole
from app.database import db
from werkzeug.security import check_password_hash, generate_password_hash
import time


class UserSeeder():

    def run():
        customer = User(
            id = 1, 
            ssnid = int(time.time()), 
            customerid = int(time.time()),
            password = generate_password_hash('password'),
            name = 'Customer',
            addrln1 = 'Address Line 1',
            addrln2 = 'Address Line 2',
            city = 'City ',
            state = 'State',
            pin = '12345')

        ace = User(
            id = 2, 
            ssnid = int(time.time()) + 2, 
            customerid = int(time.time()) + 2,
            password = generate_password_hash('password'),
            name = 'ACE',
            addrln1 = 'Address Line 1',
            addrln2 = 'Address Line 2',
            city = 'City ',
            state = 'State',
            pin = '12345')
        
        cashier = User(
            id = 3, 
            ssnid = int(time.time()) + 3, 
            customerid = int(time.time()) + 3,
            password = generate_password_hash('password'),
            name = 'Cashier',
            addrln1 = 'Address Line 1',
            addrln2 = 'Address Line 2',
            city = 'City ',
            state = 'State',
            pin = '12345')

        teller = User(
            id = 4, 
            ssnid = int(time.time()) + 4, 
            customerid = int(time.time()) + 4,
            password = generate_password_hash('password'),
            name = 'Teller',
            addrln1 = 'Address Line 1',
            addrln2 = 'Address Line 2',
            city = 'City ',
            state = 'State',
            pin = '12345')

        db.session.add(customer) 
        db.session.add(ace)  
        db.session.add(cashier)  
        db.session.add(teller)  

        customerRole = UserRole(id = 1, userid = 1, roleid = 1)
        aceRole = UserRole(id = 2, userid = 2, roleid = 2)
        cashierRole = UserRole(id = 3, userid = 3, roleid = 3)
        tellerRole = UserRole(id = 4, userid = 4, roleid = 4)

        db.session.add(customerRole)   
        db.session.commit()