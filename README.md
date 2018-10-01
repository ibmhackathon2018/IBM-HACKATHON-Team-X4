# Help me with my mood (SHADE), IBM HACKATHON 2018, by Team X4 
# Video of the Solution on YouTube ("https://youtu.be/0uErPRpO_Oo")
<details>
  <summary>Table of Contents</summary>

  * [Video of the solution]
  * [Before you begin]
  * [Installation]
  * [Authentication]
    * [Getting credentials]
  * [Python version]
  * [How to run this application]

</details>

## Video of the Solution
* Click here("https://youtu.be/0uErPRpO_Oo")

## Before you begin
* You need an internet connection.
* You need a browser.
* You need an Twitter's developer account
* You need an [IBM Cloud] account.

## Installation
```Windows
To install Python visit(https://www.python.org/downloads/)

```
To install Django, use `pip` :
```windows
pip install django
```

To install IBM DB2, use `pip`:
```windows
pip install ibmdb
```

To install IBM watson cloud, use `pip`:
```windows
pip install --upgrade watson-developer-cloud
```

To install Tweepy,use `pip`:
```windows
pip install tweepy
```

Note the following:

a) In case you run into problems installing the SDK, try
```
!pip install --upgrade pip
```


### Getting credentials
To find out which authentication to use, view the service credentials:
```IBMWatson
1. Go to the IBM Cloud [Dashboard](https://console.bluemix.net/dashboard/apps?category=ai) page.
2. Either click an existing Watson service instance or click [**Create resource > AI**](https://console.bluemix.net/catalog/?category=ai) and create a service instance.
3. Copy the `url` and either `apikey` or `username` and `password`. Click **Show** if the credentials are masked.
```
```Twitter
1. Go to https://dev.twitter.com/apps/new and log in, if necessary
2. Enter your Application Name, Description and your website address. You can leave the callback URL empty.
3. Accept the TOS, and solve the CAPTCHA.
4. Submit the form by clicking the Create your Twitter Application
5. Copy the consumer key (API key) and consumer secret from the screen into your application
6. In order to access the Twitter, that is to get recent tweets, you need the four keys such as Consumer Key, Consumer Secret, Acess token, Access Token Secret.
7. To get all these keys, click the OAuth Tool tab in your Twitter Application and copy those keys.
```

## Python version

Tested on Python 3.4, 3.5, and 3.6.

## How to run this application.
1. Go to .\Problem3\util.py\
2. Replace all twitter and IBM credentials from xxxx with yours
eg:
```Twitter
  CONSUMER_KEY = 'xxxx'
  CONSUMER_SECRET = 'xxxx'
  OAUTH_TOKEN = 'xxxx'
  OAUTH_TOKEN_SECRET = 'xxxx'
```

```IBMWatson
  url='https://gateway.watsonplatform.net/tone-analyzer/api',
  username='xxxx',
  password='xxxx',
  version='2017-09-21')
```

```IBMDB2
"DRIVER={{IBM DB2 ODBC DRIVER}};"
    "DATABASE=BLUDB;"
    "HOSTNAME=dashdb-txn-sbox-yp-lon02-01.services.eu-gb.bluemix.net;"  
    "PORT=50000;"
    "PROTOCOL=TCPIP;"
    "UID=xxxx;"
    "PWD=xxxx;")
```

3. Goto to console and reach to the application root folder.
4. Type python manage.py runserver localhost:8080
5. Application will be available on the mentioned address("http://localhost:8080/HelpMeWithMyMood/")
