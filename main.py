from tradetool import TradeTool
from tradetool import moex_list
from tradetool import forex_list
import time
from create_bot import send_msg
from functions import cheking





  


if __name__ == '__main__':
  
  
  
  
  while True:
   
    for stock in moex_list:      
      for key, value in stock.items():  
        trade = TradeTool(key, "russia", "MOEX")
        print(key, trade.price)
        if trade.monitoring():
          if cheking(key, trade.result):
            # print(trade.result)
            text = value + ', ' + str(trade.price) + ', ' + str(trade.result)
            print(text)        
            send_msg(text)
    
      

    

    for ticker in forex_list:
      
      trade = TradeTool(ticker, "forex", "FX_IDC")
      print(ticker, trade.price)
      if trade.monitoring():
          if cheking(ticker, trade.result):
             text = ticker + ', ' + str(trade.price) + ', ' + str(trade.result)
             print(text)        
             send_msg(text)

            
    time.sleep(60)
    
    

    

  
 
  