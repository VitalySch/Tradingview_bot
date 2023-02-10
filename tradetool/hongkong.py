from tradetool import TradeTool
from functions import checking
import time
from create_bot import send_msg




hongkong_list = {
            '1': ["hongkong", "HKEX", "CK Hutchison"],  # CK Hutchison
            '288': ["hongkong", "HKEX", "WH Group"], # WH Group
            '9988': ["hongkong", "HKEX", "ALIBABA GROUP"], # ALIBABA GROUP
            '2020': ["hongkong", "HKEX", "Anta Sports"], # Anta Sports
            '175': ["hongkong", "HKEX", "Geely Automobile"], # Geely Automobile
            '9999': ["hongkong", "HKEX", "NetEase"], # NetEase
            '9888': ["hongkong", "HKEX"], # Baidu
            '2269': ["hongkong", "HKEX", "Baidu"], # Wuxi Biologics
            '669': ["hongkong", "HKEX", "Techtronic Industries"], # Techtronic Industries
            '2628': ["hongkong", "HKEX", "China Life Insurance"], # China Life Insurance
            '6690': ["hongkong", "HKEX", "Haier Smart Home Co"], # Haier Smart Home Co 
}


def HongKong_trade():
  for stock, market in hongkong_list.items():
      try:
        trade = TradeTool(stock, market[0], market[1])
        
        if trade.monitoring():
          if checking(stock, trade.result):
            text = f'{market[2]}, {trade.price}, {trade.result}'
            print(text)            
            send_msg(text)
      except:
        print(stock, "Данные не получены")
      time.sleep(0.5)