from bybit import *

config_file = 'bybit.json'
lookback = 0

downloader = BybitInstrumentDL(config_file)
data, info = downloader.download_data()
json_data = json.loads(data)
json_info = json.loads(info)

data_result = Data_Result_entry(
	category = 	json_data['result']['category'],
	symbol = 	json_data['result']['symbol']
	)

data_response = Data_Response_entry(
	retCode = 	json_data['retCode'],
	retMsg = 	json_data['retMsg'],
	retExtInfo = 	json_data['retExtInfo'],
	time = 		json_data['time']
	)

data_list = Data_List_entry(
	startTime = 	json_data['result']['list'][lookback][0],
	openPrice = 	json_data['result']['list'][lookback][1],
	highPrice = 	json_data['result']['list'][lookback][2],
	lowPrice = 	json_data['result']['list'][lookback][3],
	closePrice = 	json_data['result']['list'][lookback][4],
	volume = 	json_data['result']['list'][lookback][5],
	turnover = 	json_data['result']['list'][lookback][6]
	)

info_result = Info_Result_entry(
	category = 		json_info['result']['category']
)

info_response = Info_Response_entry(
	retCode = 	json_info['retCode'],
	retMsg = 	json_info['retMsg'],
	retExtInfo = 	json_info['retExtInfo'],
	time = 		json_info['time']
	)

info_list = Info_List_entry(
	symbol = 	json_info['result']['list'][0]['symbol'],
	baseCoin = 	json_info['result']['list'][0]['baseCoin'],
	quoteCoin = 	json_info['result']['list'][0]['quoteCoin'],
	innovation = 	json_info['result']['list'][0]['innovation'],
	status = 	json_info['result']['list'][0]['status'],
	basePrecision = json_info['result']['list'][0]['lotSizeFilter']['basePrecision'],
	quotePrecision = json_info['result']['list'][0]['lotSizeFilter']['quotePrecision'],
	minOrderQty = 	json_info['result']['list'][0]['lotSizeFilter']['minOrderQty'],
	maxOrderQty = 	json_info['result']['list'][0]['lotSizeFilter']['maxOrderQty'],
	minOrderAmt = 	json_info['result']['list'][0]['lotSizeFilter']['minOrderAmt'],
	maxOrderAmt = 	json_info['result']['list'][0]['lotSizeFilter']['maxOrderAmt'],
	tickSize = 	json_info['result']['list'][0]['priceFilter']['tickSize'],
	)

#data
print(f'==============================Data')
print(f'retCode:	{data_response.retCode}')
print(f'retMsg:		{data_response.retMsg}')
print(f'retExtInfo:	{data_response.retExtInfo}')
print(f'time:		{data_response.time}')
print(f'category:	{data_result.category}')
print(f'symbol:		{data_result.symbol}')
print(f'startTime:	{data_list.startTime}')
print(f'openPrice:	{data_list.openPrice}')
print(f'highPrice:	{data_list.highPrice}')
print(f'lowPrice:	{data_list.lowPrice}')
print(f'closePrice:	{data_list.closePrice}')
print(f'volume:		{data_list.volume}')
print(f'turnover:	{data_list.turnover}')

#info
print('==============================Info')
print(f'retCode:	{info_response.retCode}')
print(f'retMsg:		{info_response.retMsg}')
print(f'retExtInfo:	{info_response.retExtInfo}')
print(f'time:		{info_response.time}')
print(f'category:	{info_result.category}')
print(f'symbol:		{info_list.symbol}')
print(f'baseCoin:	{info_list.baseCoin}')
print(f'quoteCoin:	{info_list.quoteCoin}')
print(f'innovation:	{info_list.innovation}')
print(f'status:		{info_list.status}')
print(f'basePrecision:	{info_list.basePrecision}')
print(f'quotePrecision:	{info_list.quotePrecision}')
print(f'minOrderQty:	{info_list.minOrderQty}')
print(f'maxOrderQty:	{info_list.maxOrderQty}')
print(f'minOrderAmt:	{info_list.minOrderAmt}')
print(f'maxOrderAmt:	{info_list.maxOrderAmt}')
print(f'tickSize:	{info_list.tickSize}')

