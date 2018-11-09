# Challenge 1 - Serverless Ipsum generator

Build a Serverless Ipsum generator. Build a simple serverless-backed web app that displays Serverless Ipsum when it is loaded. Or Tony Danza Ipsum. Or The Office Ipsum. Or Reasons-I-Can’t-Take-Out-The-Trash Ipsum. As long as it looks like Lorem Ipsum, but uses different words, we’re good. The page doesn’t have to look fancy, and you can do this even if you’ve never coded anything in your life!

See this page: [NoServerNovember](https://serverless.com/blog/no-server-november-challenge/)  

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
cd serverless-ipsum-generator/
```

3. Run Serverless function locally

```bash
serverless invoke local --function impsum_generator
```

## Web Demo
To try out this example, visit
https://vaibhavsingh97.com/serverless-enigma/serverless-ipsum-generator/web/index.html
