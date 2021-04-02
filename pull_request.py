from github import Github
import yaml
from twilio.rest import Client

class TwilioUtils:
    def __init__(self, sid, token):
        self.acct_sid = sid
        self.acct_token = token
        self._to_phone_number = None
        self._from_phone_number = None

    @property
    def to_phone_number(self):
        return self._to_phone_number

    @to_phone_number.setter
    def to_phone_number(self, phone_number):
        self._to_phone_number = phone_number

    @to_phone_number.deleter
    def to_phone_number(self):
        del self._to_phone_number

    @property
    def from_phone_number(self):
        return self._from_phone_number

    @from_phone_number.setter
    def from_phone_number(self, phone_number):
        self._from_phone_number = phone_number

    @from_phone_number.deleter
    def from_phone_number(self):
        del self._from_phone_number

    def connectToTwilio(self):
        self.twilio_client = Client(self.acct_sid, self.acct_token)

    def sendSMS(self, message):
        return self.twilio_client.messages.create(
                     body=message,
                     from_=self._from_phone_number,
                     to=self._to_phone_number
                 )


class GithubUtils:
    def __init__(self, personal_access_token, base_url=None):
        self.personal_access_token = personal_access_token
        self.base_url = base_url

    def connectToGithub(self):
        if not self.base_url:
            self.github = Github(self.personal_access_token)
        else:
            self.github = Github(base_url=self.base_url, login_or_token=self.personal_access_token)

    def findReviewer(self, repo, user):
        repo = self.github.get_repo(repo)
        pulls = repo.get_pulls(state='open', sort='created')
        pull_request_titles = []
        for pr in pulls:
            requests = pr.get_review_requests()
            for request in requests:
                for r in request:
                    if r.login == user:
                        pull_request_titles.append(pr.title)
        return pull_request_titles
     
if __name__ == '__main__':
    stream = open("config.yml", 'r')
    dictionary = yaml.safe_load(stream)
    try:
        github_utils = GithubUtils(dictionary['github']['personal_access_token'])
        twilio_utils = TwilioUtils(dictionary['twilio']['account_sid'], dictionary['twilio']['auth_token'])
        github_utils.connectToGithub()
        twilio_utils.from_phone_number = dictionary['twilio']['from_phone_number']
        twilio_utils.to_phone_number = dictionary['twilio']['to_phone_number']
        twilio_utils.connectToTwilio()

        for repo in dictionary['github']['repos']:
            print("Checking repo",repo)
            pulls = github_utils.findReviewer(repo, dictionary['github']['login'])
            for pull in pulls:
                print("sending {0}".format(pull))
                twilio_utils.sendSMS(pull)

    except Exception as e:
        print(e)
        print("Check your configuration file and make sure that you have configured your personal_access_token under github")
        