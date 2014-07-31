team-v README
--------------------------------------------------------------------------------
Our server: https://team-v.herokuapp.com
--------------------------------------------------------------------------------
SETUP AND RUNNING THE APP LOCALLY:
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

The main page should be at http://localhost:5000 (HTTP, NOT HTTPS for local).
--------------------------------------------------------------------------------
SQL DATABASE:
    This project uses a heroku PostgreSQL server. If you have the heroku toolbelt installed and setup, you can use the following command to initialize the database (DO NOT RUN UNLESS YOU WANT TO DELETE EVERYTHING):
    cat init.sql | heroku pg:psql 
AMAZON S3:
    For long-term storage of transcripts, the project uses an amazon S3 bucket. the bucket is teamvlogfiles, hosted in the Northern California (us-west-1) region. If you want to access the bucket on the server, use the environment variablesAWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. If you want to access the bucket on a client, make a post request to /auth with your meeting number. 
--------------------------------------------------------------------------------
TODO:
    WEBEX:
        - See if there is a way to change the webex plugin to call our server when the meeting is formed
    FRONT END:
        - wrapper.mak needs to be done (header/footer)
        - main_styles.css needs to be done so that there is a consistant syle across all pages
        - All javascript/jquery work needs to be done (login script, script notify others when someone is speaking, etc.)
          highlighting, etc.)
        - Error handling for transcript.mak javacript to retrieve files
    BACK END:
        - Error handling for /auth view
