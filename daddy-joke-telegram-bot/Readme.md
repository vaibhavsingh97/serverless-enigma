# Challenge 2 - Serverless Daddy Jokes telegram bot

Write a serverless-backed Twitter bot. Make it tweet dad jokes. Instead of twitter, I choose telegram bot fo daddy jokes

See this page: [NoServerNovember](https://serverless.com/blog/no-server-november-challenge/)

## Demo

Try the bot here :robot: : [t.me/daddyjokebot](t.me/daddyjokebot)

![Day 2 demo gif](/daddy-joke-telegram-bot/demo/demo.gif)

## Prerequisites

1. Node.js v6.5.0 or later.
2. Serverless CLI v1.9.0 or later. You can run `npm install -g serverless` to install it.
3. An AWS account. If you don't already have one, you can sign up for a free trial that includes 1 million free Lambda requests per month.
4. [Set-up your Provider Credentials.](https://serverless.com/framework/docs/providers/aws/guide/credentials/)

## Run

1. Clone the repository by using this link :

```bash
$ git clone https://github.com/vaibhavsingh97/serverless-enigma.git
```

2. Go to `serverless-ipsum-generator/`

```bash
$ cd daddy-joke-telegram-bot/
```

3. Get a bot from Telegram, sending this message to @BotFather

```bash
$ /newbot
```

4. Put the token received into a file called serverless.env.yml, like this

```bash
$ cat serverless.env.yml
TELEGRAM_TOKEN: <your_token>
```

5. Deploy it

```bash
$ serverless deploy
```

6. With the URL returned in the output, configure the Webhook

```bash
$ curl -X POST https://<your_url>.amazonaws.com/dev/set_webhook
```

7. With the URL returned in the output, check the Webhook is successfully set or not

```bash
$ curl -X POST https://<your_url>.amazonaws.com/dev/get_webhook_info
```

It should output the above URL returned in the output

Now, you can ask bot to get new jokes :wink:
