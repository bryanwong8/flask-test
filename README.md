# Part 1
1. Download Pycharm professional build. https://www.jetbrains.com/pycharm/download/#section=windows
2. Download Postgresql https://www.postgresql.org/download/
3. Download the latest version of python
4. Clone this repo into any directory that you want
5. Open Pycharm and open flask-test folder
6. Set up project interpreter to the latest version of python in settings

# Part 2 (For Mac/Linux)
7. Do this in terminal: mac/linux run: pip3 install virtualenv
8. Run this in terminal: virtualenv venv
9. Run this in terminal: venv\bin\activate to activate the virtual environment
10. Run this in terminal: pip3 install -r requirements.txt for mac/linux
11. If you get a psycopg2 error: pip3 install psycopg2-binary for mac/linux
12. If you get the above error, delete psycopg2 in requirements.txt then run pip3 install -r requirements.txt

# Part 2 (For Windows)
1. Download git and the git bash shell
7. Go to settings
8. Go to project interpreter and press the three dots on the top right and click add
9. Click on create a new virtual environment
10. Select python 3.7 for the Base interpreter and click ok
11. In the git bash shell cd to the project
12. Run: source venv\Scripts\activate
13. Run pip install -r requirements.txt

# Part 3
1. Click the rectangle box to the left of the play button and select edit configurations
2. Make your python interpreter the same as your project interpreter in settings
1. In the python console in Pycharm run: from flaskblog import db
2. Then run: db.create_all()
2. Click the play button in the top right of the Pycharm IDE
3. Go to localhost:5000 to see if the web page works
4. Try to register a user and log in. If you get a green flash message after logging in, you have set up everything correctly.
