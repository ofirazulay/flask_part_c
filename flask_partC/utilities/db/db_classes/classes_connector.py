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

user=user()