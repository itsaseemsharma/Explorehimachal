try:
    from TouristsDestination import TouristDestinationModel
except:
    import TouristDestinationModel
import json


class Repo():
    def __init__(self, db) -> None:
        self.conn = db.conn
        self.cur = db.cur

    def createTouristDestinationTable(self):
        try:
            query = """CREATE TABLE IF NOT EXISTS "TouristDestination" (
                "index" SERIAL UNIQUE,
                "name" TEXT,
                "state" TEXT,
                "city" TEXT,
	            "type" TEXT,
                "openingtime" TEXT,
                "closingtime" TEXT,
                "spendingforindian" TEXT,
                "isMedCondAllowed" TEXT,
                "location" TEXT,
                "longitude" TEXT,
                "latitude" TEXT,
                "timerequired" INTEGER,
                "blockData" TEXT
            );"""
            self.cur.execute(query)
            print("table created succefully")
        except Exception as e:
            print("Error in create table",e)
            return False
        return True

    def addTouristDestination(self, destination):
        try:
            query = """INSERT INTO "TouristDestination" ( "name" ,"state","city","type","openingtime","closingtime","spendingforindian","isMedCondAllowed","location", "longitude", "latitude","timerequired","blockData") VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');""".format(
                destination.name, destination.state, destination.city, destination.type, destination.openingTime, destination.closingTime, destination.spendingForIndian, destination.isMedCondAllowed, destination.location, destination.longitude, destination.latitude, destination.timeRequired, json.dumps(destination.blockData))
            self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            print("error",e)
            # with open("logs.txt", 'a', encoding='utf-8') as f:
            #     f.write(e + "\n")
            print(e)
            return False
        return True

    def updateTouristDestination(self, destination):
        try:
            query = """UPDATE "TouristDestination" 
                    SET "state" = '{}',
                        "city" = '{}',
                        "type" = '{}',
                        "openingtime" = '{}',
                        "closingtime" = '{}',
                        "spendingforindian" = '{}',
                        "isMedCondAllowed" = '{}',
                        "location" = '{}',
                        "longitude" = '{}', 
                        "latitude" = '{}',
                        "timerequired" = {},
                        "blockData" = '{}'
                    WHERE "name" = '{}';""".format(destination.state, destination.city, destination.type, destination.openingTime, destination.closingTime, destination.spendingForIndian, destination.isMedCondAllowed, destination.location, destination.longitude, destination.latitude, destination.timeRequired, json.dumps(destination.blockData), destination.name)
            self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            with open("logs.txt", 'a', encoding='utf-8') as f:
                f.write(e + "\n")
            print(e)
            return False
        return True

    def getDestinationByName(self, name):
        try:
            query = """ SELECT * from "TouristDestination" WHERE "name" = '{}';""".format(
                name)
            self.cur.execute(query)
            data = self.cur.fetchall()
            destination = TouristDestinationModel.TouristDestination(
                data[0][0], data[0][1], data[0][2], data[0][3], data[0][4], data[0][5], data[0][6], data[0][7], data[0][8], data[0][9], data[0][10], data[0][11], data[0][12], data[0][13], json.loads(data[0][14]), data[0][15])
        except Exception as e:
            print(e)
            return [False, None]
        return [True, destination]

    def getDestinationByIndex(self, index):
        try:
            query = """ SELECT * from "TouristDestination" WHERE "index" = '{}';""".format(
                index)
            self.cur.execute(query)
            data = self.cur.fetchall()
            destination = TouristDestinationModel.TouristDestination(
                data[0][0], data[0][1], data[0][2], data[0][3], data[0][4], data[0][5], data[0][6], data[0][7], data[0][8], data[0][9], data[0][10], data[0][11], data[0][12], data[0][13], json.loads(data[0][14]), data[0][15])
        except Exception as e:
            print(e)
            return [False, None]
        return [True, destination]

    def getAllDestinations(self):
        try:
            query = """ SELECT * from "TouristDestination"; """
            self.cur.execute(query)
            table = self.cur.fetchall()
        except Exception as e:
            print(e)
            return [False, None]
        destinations = []
        for data in table:
            destination = TouristDestinationModel.TouristDestination(
                data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], json.loads(data[13]))
            destinations.append(destination)
        return [True, destinations]

    def getDestinationsByCity(self, cityname):
        try:
            query = """ SELECT * from "TouristDestination"
                        WHERE "city" = '{}'; """.format(cityname)
            self.cur.execute(query)
            table = self.cur.fetchall()
        except Exception as e:
            print(e)
            return [False, None]
        destinations = []
        for data in table:
            print("Table = ", data, data[1])
            destination = TouristDestinationModel.TouristDestination(
                data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], json.loads(data[13]))
            destinations.append(destination)
        return [True, destinations]

    def deleteDestinationByName(self, name):
        try:
            query = """DELETE from "TouristDestination" WHERE "name" = '{}';""".format(
                name)
            self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            print(e)
            return False
        return True

    def deleteDestinationByIndex(self, index):
        try:
            query = """DELETE from "TouristDestination" WHERE "index" = '{}';""".format(
                index)
            self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            print(e)
            return False
        return True

    def delteTouristDestinationTable(self):
        try:
            query = """ DROP TABLE IF EXISTS "Contacts"; """
            self.cur.execute(query)
        except Exception as e:
            print(e)
            return False
        return True

    def createContactList(self):
        try:
            query = """CREATE TABLE IF NOT EXISTS "Contacts" (
                "index" SERIAL UNIQUE,
                "name" TEXT,
                "email" TEXT,
                "phone" TEXT,
	            "person" TEXT,
	            "trekname" TEXT,
	            "message" TEXT
            );"""
            self.cur.execute(query)
            print("contact table created succefully")
        except Exception as e:
            print("Error in create table",e)
            return False
        return True

    def addcontacts(self, name, email, phone, person, trekname, message):
        try:
            query = """INSERT INTO "Contacts" ( "name" ,"email","phone","person", "trekname", "message") VALUES ('{}','{}','{}','{}','{}','{}');""".format(name, email, phone, person, trekname, message)
            self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            print("error in add contacts ", e)
            # with open("logs.txt", 'a', encoding='utf-8') as f:
            #     f.write(e + "\n")
            print(e)
            return False
        return True

    def getcontacts(self):
        try:
            query = """ SELECT * from "Contacts"; """
            self.cur.execute(query)
            table = self.cur.fetchall()
        except Exception as e:
            print(e)
            return [False, None]
        destinations = []
        for data in table:
            d = {}
            d["name"] = data[1]
            d["email"] = data[2]
            d["phone"] = data[3]
            d["person"] = data[4]
            d["trekname"] = data[5]
            d["message"] = data[6]
            destinations.append(d)
        return  destinations
