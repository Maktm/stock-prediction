# Stock Prediction
A tool to view current and future stock prices based on simple
machine learning.

## How it works
The stock prediction tool works such that when a user logs in, they
will see the dashboard of the tool. From here, the user can navigate
to the following pages: saved stocks, stock history, search/details
page, and prediction page.

* *Saved Stocks*: this page will show the user their saved stocks and
will be unique to their log-in

* *Stock History*: this page will show the user the history of the stock
price over time. They must select a certain stock to see the history,
but by default they will see the recent trend of only their saved
stocks.

* *Search/Details Page*: this page will allow the user to search for
stocks and interest and possibly see the details of the stock as
to what the company is about and how long they have been on the
stock market.

* *Help Page*: this page will guide the user on how to use our tool,
much like this section of the README file.

* *Prediction Page*: this page is the entire basis for our project,
since it will show the predicted future stock price for a particular
stock according to the previous stock changes and news surrounding
the company, CEO, etc.

## Getting started
To set up the project, first clone the repository into your
local drive. After, use the following steps to set up the
Django web application.

For uses of Python, make sure to use the appropriate version
(i.e. `python` or `python3`).

### Installing dependencies
```shell script
pip3 install -r requirements.txt
```

### Create the migrations
```shell script
python3 manage.py makemigration stock_prediction
```

### Migrate the tables/models
```shell script
python3 manage.py migrate
```

## Running the web application
Use the following command to run the Django web application
on `localhost:8000`.

```shell script
python3 manage.py runserver
```

## Making changes
When making changes *please do not commit the SQLite database*. The
database contains a single table/entity with the admin user for
adding new users on new instances but that's about it.

The login credentials for the admin interface are:

```
username: admin
password: Password123!
```

## Authors
* Katrina Bueno
* Pratik Patel
* Michael Kiros
* Payal Pawar
* Ukoh Ndukwo
* John Yucetas
