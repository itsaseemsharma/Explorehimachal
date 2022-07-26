import TouristDestinationRepo
import TouristDestinationModel
import sqlite3

destination = TouristDestinationModel.TouristDestination(None, "Shimla Mall Road", "Himachal Pradesh", "Shimla", "test",
                                                    "9am", "9pm", "1000Rs", "vaccination (yes)",
                                                    "kangra loc", "100", "100", "3 days", "rohru is beautifull city ")


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
db = TouristDestinationRepo.Repo(db1)
#db.delteTouristDestinationTable()
#db.createTouristDestinationTable()

# db.addTouristDestination(destination)
#db.deleteUserById(user1.userid)
"""
print(" destination =", destination)
db.addTouristDestination(destination)
users = db.getAllDestinations()
for user in users:
    print("getAllDestinations =", users)
city_name =db.getDestinationsByCity("Shimla")
print("city_name", city_name)
"""
db.delteTouristDestinationTable()
db.createContactList()