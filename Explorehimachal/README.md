# Description

<p align="center">
  <img src="modules/static/assets/img/hero-img.png" />
</p>

The Explore Himachal is a web based application. The main purpose 
of “Explore Himachal” is to provide a convenient way for a customer to 
book tours.This project is to develop a system that automates the processes and 
activities of a travelling. In this project, we will make an easier task of 
searching places and for booking of tour. This often requires a lot of time 
and effort.We provide approach skills to critically examine how a tourist visits and its 
ability to operate in an appropriate way when dealing with the 
consequences of tourism, locally, regionally, and nationally including visitor 
security and ecological influences.It is tedious for a customer to plan a particular journey and have it 
executed properly. The project ‘Explore Himachal’ is developed to 
replace the currently existing system, which helps in keeping records of the 
customer details of destination as well as payment received.
# Technologies

Backend is Developed in Python using Flask framework. Frontend is developed in HTML, CSS, JS using Bootstrap framework. 'SQLite' is used as database.

# Contact Us
You can contact us at 99aseem@gmail.com . 


#How to run:

Requirements:

1. Create a virtual environment for this project with the command python3 -m virtualenv venv
2. Create virtual environment via the command: source venv/bin/activate. If successful, your terminal will now say (sdd-venv) at the beginning of each line.
3. Install required packages and extensions, pip install -r requirements.txt, from within your Harvest Here directory containing the requirements.txt file (where you will be if you've followed the instructions up to this point). This will take several minutes.
Change to the "Explorehimachal" directory, cd modules.
Run the following two commands to get the database ready to go.
python3 manage.py makemigrations

python3 manage.py migrate

Everything should be ready! All that's left is to run the server via the command python3 manage.py runserver and the site will be available at http://localhost:8090.

