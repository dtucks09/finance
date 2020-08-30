from risk_ranges import trends
import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 500)

car_dealerships = ['kmx', 'cvna', 'vrm']
sectors = ['XLF', 'XLI', 'XLU', 'XLK', 'XLC', 'XLY', 'XLE', 'IYR', 'XLV', 'XOP', 'XRT', 'IBB', 'XAR', 'XLB', 'XSD', 'XME']
countries = ['EEM', 'EWI', 'EWG', 'EWZ', 'EWA', 'DXJ', 'EIDO', 'EWP', 'EWT', 'EPHE', 'EWQ', 'EWW', 'EWY', 'PIN', 'RSX', 'TUR']
big_tech = ['GOOGL', 'TWTR', 'FB', 'NFLX', 'AAPL', 'MSFT', 'AMZN', 'BABA']
currencies = ['UUP', 'FXE', 'FXA', 'FXB', 'GLD']
commodities = ['GLD', 'USO', 'UNG', 'XOP', 'COPX', 'CORN', 'COW', 'DBA', 'DBC', 'GDX', 'JJC', 'JO', 'NIB', 'SOYB', 'WEAT', 'WOOD']
small_cap_tech = ['ANGI', 'SQ', 'MTCH', 'GRUB', 'BYND', 'CHWY', 'CRWD', 'LYFT', 'PINS', 'TW', 'UBER', 'WORK', 'YETI', 'ZM', 'BOX', 'DBX', 'DOCU', 'ETSY', 'SHOP', 'ZEN']
equity_indices = ['IWM', 'IWO', 'QQQ', 'SPY', 'GDX', 'XOP', 'HYG', 'MCHI']
fixed_income = ['TLT', 'IEF']
stocks = ['CMG', 'WMT', 'DIS', 'DELL', 'IAC', 'TSLA']
wfh_enablement = ['CLDX', 'INTU', 'XOUP', 'BILL', 'SMAR', 'WORK', 'PLAN', 'SQ', 'BL', 'AVLR', 'QTWO', 'SHOP', 'APPN', 'PAGS', 'WK', 'WIX']

selected_list = sectors

column_names = ['ticker',
                'last_price',
                '5d_sma',
                '10d_sma',
                '50d_sma',
                '200d_sma',
                '5v20_trend',
                '10v50_trend',
                'Closev200_trend',
                'RSI'
                ]

output_df = pd.DataFrame(columns=column_names)

for ticker in selected_list:
    series = pd.Series(trends(ticker), index=output_df.columns)
    output_df = output_df.append(series, ignore_index=True)

print(output_df)
