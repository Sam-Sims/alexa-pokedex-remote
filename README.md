# Alexa Pokedex

This project contains source code and supporting files for a serverless alexa skill deployed via the SAM CLI. It includes the following files and folders.

- alexa-pokedex - Code for the application's Lambda function and supporting logic.
- events - Invocation events that you can use to invoke the function locally.
- template.yaml - A template that defines the application's AWS resources.

This project uses the alexa ask-sdk and python to create an alexa skill that allows you to look up pokemon information like a pokedex.

## Deploy the sample application

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

Refer to the SAM CLI documentation - [Here](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-reference.html)

You can find your API Gateway Endpoint URL after deployment.

## Usage

"alexa ask pokedex tools to give me a pokemon"

## TODO
* Create a models.json to define the alexa intents rather than manually creating them
