# Stock Prediction

## Setting up the project
Before setting up the project, make sure that you have Python 3.* installed. Then install Django using one of the following commands (`pip` or `pip3`):

```
pip3 install django
```

## Running the application server locally
To run the server locally, use the following command (`python`/`python3`):

```
python3 manage.py runserver
```

## Authors
* Katrina Bueno
* Pratik Patel
* Payal Pawar
* Ukoh Ndukwo
* John Yucetas
* Michael Kiros


## How it works

The stock prediction tool works such that when a user logs in, they will see the dashboard of the tool. From here, the user can navigate to the following pages:  saved stocks, stock history, search/details page, and prediction page.  

* Saved Stocks:  this page will show the user their saved stocks and will be unique to their log-in

* Stock History:  this page will show the user the history of the stock price over time.  They must select a certain stock to see the                     history, but by default they will see the recent trend of only their saved stocks.  

* Search/Details Page:  this page will allow the user to search for stocks and interest and possibly see the details of the stock as to                         what the company is about and how long they have been on the stock market.  

* Prediction Page:  this page is the entire basis for our project, since it will show the predicted future stock price for a particular                     stock according to the previous stock changes and news surrounding the company, CEO, etc.  
