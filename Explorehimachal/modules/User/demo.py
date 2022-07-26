import UserRepo
import UserModel

import sqlite3
import bcrypt

password = "password"
password = str(password).encode('utf-8')
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
hashed = hashed.decode()

user = UserModel.User(None,
                      "Aseem Sharma", "99aseem@gmail.com", hashed, "superadmin", 1, "Full Stack Developer", "India",
                      "Student", "12/09/1999", "test")


class Repo():
    def __init__(self):
        try:
            self.conn = sqlite3.connect('..\database.db')
            self.conn.row_factory = sqlite3.Row
            self.cur = self.conn.cursor()
            print("Opened database successfully")
        except Exception as e:
            print(e)

    def __del__(self):
        try:
            self.conn.close()
            print("Database Closed successfully")
        except Exception as e:
            print(e)

db1 = Repo()
db = UserRepo.Repo(db1)
db.createUserTable()

db.addUser(user)
#db.deleteUserById(user1.userid)

print("db user = ", db.isUserIdUsed(user.userid))

users = db.getAllUsers()
print("users =", users)
# db.createUserTable()

#newUser = db.getUserById("deshmukh.1@iitj.ac.in")
#print("newUser =", newUser[0])

