import logging
from emoji import emojize


logger = logging.getLogger()
logger.setLevel(logging.INFO)

Closing_keywords = [
    "close",
    "closes",
    "closed",
    "fix",
    "fixes",
    "fixed",
    "resolve",
    "resolves",
    "resolved"
]


def isValidPullRequest(body):
    pr_body = body['pull_request']['body']
    for words in Closing_keywords:
        if str(words) in pr_body.lower() and len(pr_body.split("#")) > 1:
            return True
    return False


def eventIsPullRequest(event):
    if event['headers']['X-GitHub-Event'] == 'pull_request' and 'pull_request' in event['body']:
        return True
    return False


def updatePullRequestStatus(githubClient, payload, repository, pullRequest):
    repository_name = repository['full_name']
    sha = pullRequest['head']['sha']
    try:
        githubClient.get_repo(repository_name).get_commit(sha).create_status(
            payload['state'], payload['target_url'], payload['description'], payload['context'])
    except RuntimeError as e:
        logging.error("Error: {}".format(e))
    return


def createPullRequestComment(githubClient, repository, pullRequest):
    repository_name = repository['full_name']
    sha = pullRequest['head']['sha']
    body = "Thanks for creating Pull Request {} but closing issue keywords \
are missing.You can include these closing keywords in your pull request descriptions, \
as well as commit messages, to automatically close issues in GitHub. To know more, please visit https://help.github.com/articles/closing-issues-using-keywords/".format(
        emojize(":hugs:", use_aliases=True))
    try:
        githubClient.get_repo(repository_name).get_commit(
            sha).create_comment(body)
    except RuntimeError as e:
        logging.error("Error: {}".format(e))
    return
