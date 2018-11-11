import os
import json
import logging
import yaml
from github import Github
from libs import github_service
from libs import response

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def github_check(event, context):

    logger.info('Event: {}'.format(event))
    github_client = Github(os.environ.get('GITHUB_TOKEN'))
    body = yaml.load(event["body"])
    target_url = body['pull_request']['html_url']
    if not github_service.eventIsPullRequest(event):
        return response.success('Event is not a Pull Request')
    if github_service.isValidPullRequest(body):
        payload = response.githubSuccessPayload(target_url)
    else:
        payload = response.githubFailurePayload(target_url)
        try:
            github_service.createPullRequestComment(
                github_client, body['repository'], body['pull_request'])
        except RuntimeError as e:
            logging.error("Error: {}".format(e))
            logging.error("Failed to comment")
    try:
        github_service.updatePullRequestStatus(
            github_client, payload, body['repository'], body['pull_request'])
        response.success(
            'Process finished with state: {}'.format(payload['state']))
        logger.info('Process finished with state: {}'.format(payload['state']))
    except RuntimeError as e:
        logging.error("Error: {}".format(e))
        response.failure('Process finished with error.')
