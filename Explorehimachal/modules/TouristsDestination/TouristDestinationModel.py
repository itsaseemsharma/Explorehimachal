class TouristDestination:
    def __init__(self, index, name, state, city, type, openingTime, closingTime, spendingForIndian, isMedCondAllowed, location, longitude, latitude, timeRequired, blockData) -> None:
        self.index = index
        self.name = name
        self.state = state
        self.city = city
        self.type = type
        self.openingTime = openingTime
        self.closingTime = closingTime
        self.spendingForIndian = spendingForIndian
        self.location = location
        self.longitude = longitude
        self.latitude = latitude
        self.timeRequired = timeRequired
        self.isMedCondAllowed = isMedCondAllowed
        self.blockData = blockData
