team-v README

To set up your environment:
    python setup.py develop
To run:
    python runapp.py

You can also do ./run to run the bash script and combine these actions into one.

TODO:
    WEBEX:
        - See if there is a way to change the webex plugin to call our server when the meeting is formed
    FRONT END:
        - wrapper.mak needs to be done (header/footer)
        - main_styles.css needs to be done so that there is a consistant syle across all pages
        - All javascript/jquery work needs to be done
        - Voice to text API integration
        - More beautiful/efficient way of viewing transcripts (search by name/content/time, name highlighting, etc.)
    BACK END:
        - User nicknames
        - Different meetings based on meeting_number
        - Meeting transcript security (possibly, so random people can't just see the transcript)
        - Meeting timestamps need to be altered
        - Meeting start/end times based on WEBEX meeting creation/finishing
        - Meeting start/end tags
