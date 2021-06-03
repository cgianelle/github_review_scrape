# github_review_scrape
Scrapes provided Github repos, looking for pull requests that been an individual has been tagged as a reviewer, and sends an SMS message to a provided telephone number for alerting via Twilio. Useful for the times were there are lots of emails indicating pull requests but few with you as the reviewer. This is to cut through the noise.

## Install
~~~~
pip3 install PyGithub
pip3 install pyyaml
pip3 install twilio
~~~~

## Library Documentation
- https://pygithub.readthedocs.io/en/latest/index.html
- https://pyyaml.org/wiki/PyYAMLDocumentation
- https://www.twilio.com/docs/libraries/python

## Configuration
1. Create a Github personal access token and add the repos you wanted monitored
2. Create a Twilio account, register a telephone number (see `from_phone_number` below), and provide a phone number to where the SMS messages should be sent (see `to_phone_number`)
3. Create a config.yml file
~~~~
github:
  personal_access_token: 'dfhds;jfhrjhjf;djsf;djhf;jdhfjdfhruywufhwc'
  repos:
    - 'Project/repo1'
    - 'Project/repo2'
  login: 'your_username'
twilio:
  from_phone_number: '+12345678901'
  to_phone_number: '+13456789012'
  account_sid: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678'
  auth_token:  '0123456789abcdefghijklmnopqrstuv'
~~~~

## Execution
Crontab
The setting below runs M-F from 8am until 6PM
~~~~
0 8-18 * * 1-5 cd <path/to/github_review_scrape> && ./pull_request.py
~~~~