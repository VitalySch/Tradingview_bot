from tradetool import TradeTool
from functions import checking
import time
from create_bot import send_msg


forex_list = {
    'EURUSD': ["forex", "FX_IDC"],
    'GBPUSD': ["forex", "FX_IDC"],
    'USDCHF': ["forex", "FX_IDC"],
    'USDJPY': ["forex", "FX_IDC"],
    'USDCAD': ["forex", "FX_IDC"],
    'AUDUSD': ["forex", "FX_IDC"],
    'NZDUSD': ["forex", "FX_IDC"],
    'EURJPY': ["forex", "FX_IDC"],
    'EURGBP': ["forex", "FX_IDC"],
    'GBPJPY': ["forex", "FX_IDC"],
    'EURCAD': ["forex", "FX_IDC"],
    'EURAUD': ["forex", "FX_IDC"],
    'AUDJPY': ["forex", "FX_IDC"],
    'GBPAUD': ["forex", "FX_IDC"],
    'GBPCAD': ["forex", "FX_IDC"],
    'GBPCHF': ["forex", "FX_IDC"],
    'NZDJPY': ["forex", "FX_IDC"],
    
}


def Forex_trade():
  for stock, market in forex_list.items():
      try:
        trade = TradeTool(stock, market[0], market[1])
        
        if trade.monitoring():
          if checking(stock, trade.result):
            text = f'{stock}, {trade.price}, {trade.result}'
            print(text)            
            send_msg(text)
      except:
        print(stock, "Данные не получены")
      time.sleep(0.5)