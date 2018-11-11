import json


def buildResponse(statusCode, body):
    return {
        'statusCode': statusCode,
        'body': json.dumps(body)
    }


def githubPayload(state, target_url, description):
    return {
        'state': state,
        'target_url': target_url,
        'description': description,
        'context': 'serverless-webhook/closing-issue-checker'
    }


def success(body):
    return buildResponse(200, body)


def failure(body):
    return buildResponse(400, body)


def githubSuccessPayload(target_url):
    return githubPayload('success', target_url, 'PR body is according to standard format.')


def githubFailurePayload(target_url):
    return githubPayload('failure', target_url, 'PR body should contain closing keywords.')
