# github_review_scrape
Scrapes Github repos, looking for pull requests that I've been tagged as a reviewer. Useful for the times were there are lots of emails indicating pull requests but few with me as the review. This is to cut through the noise.

## Install
~~~~
pip3 install PyGithub
pip3 install pyyaml
~~~~

## Library Documentation
- https://pygithub.readthedocs.io/en/latest/index.html
- https://pyyaml.org/wiki/PyYAMLDocumentation

## Configuration
1. Create a Github personal access token

~~~~
github:
  personal_access_token: 'dfhds;jfhrjhjf;djsf;djhf;jdhfjdfhruywufhwc'
  repos:
    - 'Project/repo1'
    - 'Project/repo2'
  login: 'your_username'
~~~~
