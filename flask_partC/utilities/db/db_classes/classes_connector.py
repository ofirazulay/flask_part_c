from utilities.db.db_manager import dbManager


class user:
    def _init_(self):
     pass

    def login(self, email, password):
        query = "SELECT * FROM users WHERE email ='%s' AND password ='%s'"% (email, password)
        ans = dbManager.fetch(query)
        if len(ans) == 0:
            return 'notFound'
        ans = ans[0]
        return (ans[0], ans[1], ans[2], ans[3], ans[4], ans[5])

    def sign_in_fun(self, full_name, date_of_birth, email,phone_number,username,password):
        if self.check_exist_user(email,username)=='email Exist':
            return 'email Exist'
        if self.check_exist_user(email,username)=='userName Exist':
            return 'userName Exist'
        else:
            query = "INSERT INTO users(full_name,date_of_birth,email,phone_number,username,password) VALUES ('%s','%s', '%s','%s','%s','%s')" %  (full_name, date_of_birth, email,phone_number,username,password)
            ans = dbManager.commit(query)
            return (ans)


    def check_exist_user(self ,email, username):
        query = "select * FROM users WHERE email='%s';" % email
        users_with_same_email = dbManager.fetch(query)

        query = "select * FROM users WHERE username='%s';" % username
        users_with_same_name = dbManager.fetch(query)

        if len(users_with_same_email)!=0:
            return 'email Exist'
        if len(users_with_same_name) != 0:
            return 'userName Exist'
        else:
            return False


class contact:
    def _init_(self):
        pass

    def Add_contact(self, full_name, email, phone_number,review):
        query = "INSERT INTO contact_us(full_name,email,phone_number,review) VALUES ('%s', '%s', '%s','%s')" % (full_name,email, phone_number,review)
        ans = dbManager.commit(query)
        return (ans)


contact=contact()
user=user()


