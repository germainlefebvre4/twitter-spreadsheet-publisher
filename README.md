# Twitter Spreadsheet Publisher
Automatically publish tweets contained in a structures Google Spreadsheet document. Only focus on content and we manage publication and continuous rollover publishing.

## Getting started

```bash
pip install -r requirements.txt
python main.py
```


## Environment variables

The application works with `.env` (or `dotenv`) system that isolate env vars in the `.env` file.

The `.env` parameters are:
* Google Spreadsheet
  * `SPREADSHEET_ID`
  * `SPREADSHEET_RANGE`
* Twitter
  * `TWITTER_CONSUMER_KEY`
  * `TWITTER_CONSUMER_SECRET`
  * `TWITTER_ACCESS_TOKEN`
  * `TWITTER_ACCESS_TOKEN_SECRET`

A template `.env.template` and an example `.env.example` are present to help you.


## Requirements

A few actions are required to use this applciation.

### Google Spreadsheet API

Enable the Google Spreadsheet API.

### Google Service Account

Create a Google Service Account.

* Create a service account
* Generate an API KEY for this service account in JSON format
* Download it as `credentials.json` in the root directory's application

### Google Spreadsheet Content

Create a Google Spreadsheet.

Invite the Service account (previously created) to your Google Spreadsheet with its email.

Create the Google Spreadsheet content:
```
   | A    | B       | C     | D                |
---|------|---------|-------|------------------|
 1 | Next | Message | Image | Publication date |
---|------|---------|-------|------------------|
 2 |      | Oh my ! |       |                  |
 3 | x    | Okey ;) |       |                  |
 4 |      | Good !! |       |                  |
```

Columns to be filled:
* `Next` focus the next line to tweet
* `Message` contains the tweet message
* `Image` gives the iamge to attach to the tweet (not implemented yet)

Columns not to be filled:
* `Publication date` informs the last tweeted post for this message

Mind to retrieve the Spreadsheet ID located in the address bar. (e.g. For document located at `https://docs.google.com/spreadsheets/d/18t7uSkPqg2hJnJzRww7q5xoyiy21UozFoZ9DKfzUE7b/edit#gid=0` the ID is `18t7uSkPqg2hJnJzRww7q5xoyiy21UozFoZ9DKfzUE7b`)


### Create a Twitter App

* Create a Twitter App at [https://apps.twitter.com/](https://apps.twitter.com/) (app v1 or v2 does not matter)
* Generate the Consumer keys: `Api key` and `Api key secret` from your App
* Generate the Authentication tokens: `Access toekn` and `Access toekn secret` from your App


### Fill the authentication informations

#### Google Spreadsheet

* Retrieve the service account Api key JSON file as `credentials.json`
* Retrieve the Google Spreadsheet ID and paste it in the `.env` file


#### Twitter

* Retrieve the Twitter Authentication informations and paste them in the `.env` file:


## Compatibility

Python version:
* 3.x


## Local development

Setup your local development environment with `pipenv` utility:
```bash
pipenv update
```

And run it as well:
```bash
pipenv run python main.py
```
