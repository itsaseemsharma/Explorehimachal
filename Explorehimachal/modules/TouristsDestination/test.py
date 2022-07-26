import citiesRepo
import TouristDestinationModel
import sqlite3

cities = TouristDestinationModel.TouristDestination(None, "Kangra", "Shimla", "Chamba", "test",
                                                    "9", "9", "1000Rs", "100$", "100",
                                                    "100", "100", "100", "100", "100", "100")

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
db = citiesRepo.Repo(db1)
db.createCityTable()

db.addCity("KARERI LAKE", "Himachal Pradesh")
#db.deleteUserById(user1.userid)

users = db.getAllCities()
print("cities =", users)