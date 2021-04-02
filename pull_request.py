from github import Github
import yaml

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
        github_utils.connectToGithub()
        for repo in dictionary['github']['repos']:
            print("Checking repo",repo)
            pulls = github_utils.findReviewer(repo, dictionary['github']['login'])
            print(pulls)

    except:
        print("Check your configuration file and make sure that you have configured your personal_access_token under github")
        