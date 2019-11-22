"""
Connects to the Alpha Vantage API to retrieve stocks information.
"""

from typing import List

import json

import requests

API_KEY = '5IPQ89L576QGG667'


class StockQuote:
	"""
	Encapsulates a single stock quote for a given stock on
	a single day. The price for the stock is the closing
	price of the stock on day date.
	"""
	def __init__(self, symbol, date, price) -> None:
		self.symbol = symbol
		self.date = date
		self.price = price


def get_stock_history(symbol) -> List[StockQuote]:
	"""
	Retrieves the stock quote history for the specified quote and
	returns a list of StockQuote objects for the past 20+ years.
	TODO: Cache the results to prevent repeated API calls.
	"""
	response = requests.get(
		'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&outputsize=full&apikey={}'.format(
			symbol,
			API_KEY
		))

	payload = json.loads(response.text)
	ts_key = 'Time Series (Daily)'
	if not ts_key in payload:
		raise Exception('Invalid response from API request (bad body)')

	history = dict(payload[ts_key])
	stock_quotes = []
	for date, quotes in history.items():
		price = quotes['4. close']
		quote = StockQuote(symbol, date, price)
		stock_quotes.append(quote)

	return stock_quotes


def get_stock_quote(symbol) -> StockQuote:
	"""
	Returns the latest stock quote of a stock. Note that the stock price
	returned is not the intraday stock quote, but the closing price for
	the previous day.
	TODO: Consider using a different API call to speed it up.
	"""
	print('finding: ' + symbol)
	response = requests.get('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey={}'.format(
		symbol,
		API_KEY
	))

	try:
		print(response.text)
		data_key = 'Global Quote'
		data = dict(json.loads(response.text))[data_key]
	except:
		raise Exception('Bad symbol given') # TODO: Bad idea

	date = data['07. latest trading day'] # TODO: Improve date formatting
	price = data['05. price']
	return StockQuote(symbol, date, price)


def search_stock_quote(keywords) -> List[StockQuote]:
	"""
	Searches for the specified text, keywords using the AlphaVantage API and
	returns the quotes for any stock quotes that match the text (even partially).

	Returns an empty List if nothing is found.
	"""
	response = requests.get('https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={}&apikey={}'.format(
		keywords,
		API_KEY
	))

	try:
		data_key = 'bestMatches'
		data = dict(json.loads(response.text))[data_key]
	except:
		return []

	results = []
	for r in data:
		# TODO: For each quote, get the information
		try:
			quote = get_stock_quote(r['1. symbol'])
		except:
			# Probably AlphaVantage rate limiting
			continue
		results.append(quote)

	return results