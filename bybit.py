import json
from pybit.unified_trading import HTTP
import os

class BybitInstrumentDL:
	def __init__(self, config_file):
		self.config_file = config_file

	def download_data(self):
		session = HTTP(testnet=True)

		script_path = os.path.join(os.path.dirname(__file__))
		print(script_path)

		with open(os.path.join(script_path,self.config_file), 'r') as f:
			self.config = json.load(f)

		category = self.config.get('category')
		interval = self.config.get('interval')
		symbol = self.config.get('symbol')
		limit = self.config.get('limit')

		instrument_data = session.get_kline(category=category, interval=interval, symbol=symbol, limit=limit)
		instrument_info = session.get_instruments_info(category=category,symbol=symbol)
		
		#JSON
		with open(os.path.join(script_path,f'{symbol}_data.json'), 'w') as f:
			json.dump(instrument_data, f)

		with open(os.path.join(script_path,f'{symbol}_info.json'), 'w') as f:
			json.dump(instrument_info, f)
		
		return json.dumps(instrument_data), json.dumps(instrument_info)

class Data_Result_entry:
	"""
	Pagal https://bybit-exchange.github.io/docs/v5/market/kline grąžina parametrus
	result { category, symbol }
	"""
	def __init__(self, category, symbol):
		self.category = 	category
		self.symbol = 		symbol

class Data_List_entry:
	"""
	Pagal https://bybit-exchange.github.io/docs/v5/market/kline grąžina parametrus
	list: [[ 
			list[0]: list[1]: openPrice, list[2]: highPrice, list[3]: lowPrice,
			list[4]: closePrice, list[5]: volume, list[6]: turnover
		]]
	"""
	def __init__(self, startTime, openPrice, highPrice, lowPrice, closePrice, volume, turnover):
		self.startTime = 	int(startTime)
		self.openPrice = 	openPrice
		self.highPrice = 	highPrice
		self.lowPrice = 	lowPrice
		self.closePrice = 	closePrice
		self.volume = 		volume
		self.turnover = 	turnover

class Data_Response_entry:
	"""
	Pagal https://bybit-exchange.github.io/docs/v5/market/kline grąžina parametrus
	{ retCode, retMsg, retExtInfo, time }
	"""
	def __init__(self, retCode, retMsg, retExtInfo, time):
		self.retCode = 		retCode
		self.retMsg = 		retMsg
		self.retExtInfo = 	retExtInfo
		self.time = 		int(time)

class Info_Result_entry:
	"""
	Pagal https://bybit-exchange.github.io/docs/v5/market/instrument grąžina parametrus
	result: { category },
	"""
	def __init__(self, category):
		self.category = category

class Info_List_entry:
	"""
	Pagal https://bybit-exchange.github.io/docs/v5/market/instrument grąžina parametrus
	list: [{
		 symbol, baseCoin, quoteCoin, innovation, status,
		 lotSizeFilter: {
			basePrecision, quotePrecision, minOrderQty,
		 	maxOrderQty, minOrderAmt, maxOrderAmt},
		 priceFilter: { tickSize },
		 }]
	"""
	def __init__(self, symbol, baseCoin, quoteCoin, innovation, status, basePrecision,
		quotePrecision, minOrderQty, maxOrderQty, minOrderAmt, maxOrderAmt, tickSize):
		self.symbol = 			symbol
		self.baseCoin = 		baseCoin
		self.quoteCoin = 		quoteCoin
		self.innovation = 		bool(innovation)
		self.status = 			status
		self.basePrecision = 	basePrecision
		self.quotePrecision = 	quotePrecision
		self.minOrderQty = 		minOrderQty
		self.maxOrderQty = 		maxOrderQty
		self.minOrderAmt = 		minOrderAmt
		self.maxOrderAmt = 		maxOrderAmt
		self.tickSize = 		tickSize

class Info_Response_entry:
	"""
	Pagal https://bybit-exchange.github.io/docs/v5/market/instrument grąžina parametrus
	{ retCode, retMsg, retExtInfo, time }
	"""
	def __init__(self, retCode, retMsg, retExtInfo, time):
		self.retCode = 		retCode
		self.retMsg = 		retMsg
		self.retExtInfo = 	retExtInfo
		self.time = 		int(time)