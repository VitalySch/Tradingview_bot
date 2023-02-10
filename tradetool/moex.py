from tradetool import TradeTool
from functions import checking
import time
from create_bot import send_msg




moex_list = {
            'OZON': ["russia", "MOEX"],
            'SBERP': ["russia", "MOEX"],
            'MTSS': ["russia", "MOEX"],
            'GAZP': ["russia", "MOEX"],
            'SIBN': ["russia", "MOEX"],
            'TATN': ["russia", "MOEX"],
            'VTBR': ["russia", "MOEX"],
            'FIVE': ["russia", "MOEX"],
            'HYDR': ["russia", "MOEX"],
            'SNGS': ["russia", "MOEX"],
            'VKCO': ["russia", "MOEX"],
            'ROSN': ["russia", "MOEX"],
            'PHOR': ["russia", "MOEX"],
            'LKOH': ["russia", "MOEX"],
            'GMKN': ["russia", "MOEX"],
            'NLMK': ["russia", "MOEX"],
            'ALRS': ["russia", "MOEX"],
            'YNDX': ["russia", "MOEX"],
            'SBER': ["russia", "MOEX"],
            'MGNT': ["russia", "MOEX"],
            'PLZL': ["russia", "MOEX"],
            'POLY': ["russia", "MOEX"],
            'FEES': ["russia", "MOEX"],
            'MOEX': ["russia", "MOEX"],
            'NVTK': ["russia", "MOEX"],
            'CHMF': ["russia", "MOEX"],
}


def Moex_trade():
  for stock, market in moex_list.items():
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