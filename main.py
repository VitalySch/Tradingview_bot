from tradetool import TradeTool, moex_list, forex_list, other_list, america_list
import time
from create_bot import send_msg
from functions import cheking

  
  
def main():  
  
  while True: 
    
    # for stock, market in moex_list.items():
    #   try:
    #     trade = TradeTool(stock, market[0], market[1])
        
    #     if trade.monitoring():
    #       if cheking(stock, trade.result):
    #         result = trade.result
    #         text = stock + ', ' + str(trade.price) + ', ' + str(result)
    #         print(text)            
    #         # send_msg(text)
    #   except:
    #     print(stock, "Данные не получены")
    #   time.sleep(1)

    # for stock, market in forex_list.items():
    #   try:
    #     trade = TradeTool(stock, market[0], market[1])
    #     if trade.monitoring():
    #       if cheking(stock, trade.result):
    #         result = trade.result
    #         text = stock + ', ' + str(trade.price) + ', ' + str(result)
    #         print(text)            
    #         send_msg(text)
    #   except:
    #     print(stock, "Данные не получены")
    #   time.sleep(1)

    #   for stock, market in other_list.items():
    #     try:
    #       trade = TradeTool(stock, market[0], market[1])
    #       if trade.monitoring():
    #         if cheking(stock, trade.result):
    #           result = trade.result
    #           text = stock + ', ' + str(trade.price) + ', ' + str(result)
    #           print(text)            
    #           # send_msg(text)
    #     except:
    #       print(stock, "Данные не получены")
    #     time.sleep(1)
    for stock, market in america_list.items():
      try:
        trade = TradeTool(stock, market[0], market[1])
        if trade.monitoring():
          if cheking(stock, trade.result):
            result = trade.result
            text = f'{stock}, {trade.price}, {result}'
            print(text)            
            # send_msg(text)
      except:
        print(stock, "Данные не получены")
      time.sleep(1)

    
    
     
 


if __name__ == '__main__':
  main()