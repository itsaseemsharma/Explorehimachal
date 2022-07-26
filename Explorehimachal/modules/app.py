import MainRepo


from flask import Flask, render_template, redirect, session, send_file, request
from flask_mail import Mail, Message
from flask.helpers import url_for

import os

app = Flask(__name__)
app.salt = 'super secret key'
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


# if(os.environ.get('ENV') == "Production"):
#     app.config.from_object("config.ProductionConfig")
# else:
#     app.config.from_object("config.DevelopmentConfig")

mail = Mail(app)
db = MainRepo.Repo()

from User import UserServices
from TouristsDestination import TouristDestinationServices
from User.UserController import user
#from Hotel.HotelController import hotel
from TouristsDestination.TouristDestinationController import touristdestination

app.register_blueprint(user, url_prefix="/user")
#app.register_blueprint(hotel, url_prefix="/hotel")
app.register_blueprint(touristdestination, url_prefix="/touristdestination")


@app.route('/home', methods=['GET'])
def home():
    print("db",db)

    userService = UserServices.UserServices(db)
    touristServices = TouristDestinationServices.Services(db)
    #
    # if(app.config["ENV"] == "production"):
    #     userService.addView()
    totalVisits = userService.getTotalVisits()
    print("totalVisits",totalVisits)
    plans = 0
    noOfusers = userService.getNumberOfUsers()
    print(" noOfusers ",  noOfusers)
    # places = touristServices.getCountOfDestinations()
    # print(" places ", places)
    places = 1
    print(" userData ",session)
    if (not session.get("index") is None):
         userData = userService.getUserSession(session.get("index"))
         print(" userData ",userData)
         # if (userData[0]):
    #         name = userData[1].name
    #         firstname = name
    #         if " " in name:
    #             firstname = name.split()[0]
    #         return render_template("home.html", firstname=firstname, loggedIn=True, type=userData[1].usertype, visits=totalVisits, plans=plans, noOfusers=noOfusers, places=places)

    return render_template('home1.html', loggedIn=False, visits=1, plans=plans, noOfusers=10, places=places)


@app.route('/logo', methods=['GET'])
def logo():
    return send_file('static/assets/img/hero-img2.png')

@app.route('/', methods=['GET'])
@app.route('/Home', methods=['GET'])
def redir():
    return redirect(url_for('home'))

# @app.route('/event', methods=['GET'])
# def event():
#     return render_template('home1.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8090))
    app.run(host='localhost', port=port)
