team-v README
--------------------------------------------------------------------------------
Our server: team-v.herokuapp.com
--------------------------------------------------------------------------------
SETUP AND RUNNING THE APP:
To set up your environment, run the following commands (on Ubuntu):
    sudo apt-get install python-dev
    sudo apt-get install postgresql
    sudo apt-get install python-psycopg2
    sudo apt-get install libpq-dev

To install required libraries:
    python setup.py develop
To run:
    python runapp.py

You can also do ./run to run the bash script and combine these actions into one.
--------------------------------------------------------------------------------
SQL DATABASE:
    For now, this project uses a heroku PostgreSQL server. Currently, there is no local development (working on it, lol). If you have the heroku toolbelt installed and setup, you can use the following command to initialize the database (DO NOT RUN UNLESS YOU WANT TO DELETE EVERYTHING):
    cat init.sql | heroku pg:psql 
--------------------------------------------------------------------------------
TODO:
    WEBEX:
        - See if there is a way to change the webex plugin to call our server when the meeting is formed
    FRONT END:
        - wrapper.mak needs to be done (header/footer)
        - main_styles.css needs to be done so that there is a consistant syle across all pages
        - All javascript/jquery work needs to be done (login script, script notify others when someone is speaking, etc.)
        - Voice to text API integration
          highlighting, etc.)
        - Templates need to connect to CDN and pull files from them (or from local location if the meeting is not done)
    BACK END:
        - User nicknames
        - Different meetings based on meeting_number
        - Meeting timestamps need to be altered
        - Meeting start/end times based on WEBEX meeting creation/finishing
    DATABASE:
        - Possibly: Find a way to locally develop (write a script, make local db)
