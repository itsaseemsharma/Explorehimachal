#!/usr/bin/env python3

import UserRepo
from .. import MainRepo
import UserModel
import bcrypt
password = "password"
password = str(password).encode('utf-8')
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
hashed = hashed.decode()

user = UserModel.User(None,
                      "Aseem sharma", "99aseem@gmail.com", hashed, "superadmin", 1, "Full Stack Developer", "India", "Student", "12/09/1999", "yes")

# db = UserRepo.Repo()
db = MainRepo.Repo()
# db.createUserTable()


db.addUser(user)
# db.deleteUserById(user1.userid)

# print(db.isUserIdUsed(user1.userid))

#users = db.getAllUsers()
# db.createUserTable()

#newUser = db.getUserById("danku")

"""
for newUser in users:
    print(newUser.name)
    print(newUser.userid)
    print(newUser.password)
    print(newUser.usertype)
    """
