# import numpy as np
# import pandas as pd


send_list = {'OZON': None,
            'SBERP': None,
            'MTSS': None,
            'GAZP': None,
            'SIBN': None,
            'TATN': None,
            'VTBR': None,
            'FIVE': None,
            'HYDR': None,
            'SNGS': None,
            'VKCO': None,
            'ROSN': None,
            'PHOR': None,
            'LKOH': None,
            'GMKN': None,
            'NLMK': None,
            'ALRS': None,
            'YNDX': None,
            'SBER': None,
            'MGNT': None,
            'PLZL': None,
            'POLY': None,
            'FEES': None,
            'MOEX': None,
            'NVTK': None,
            'CHMF': None,
            'EURUSD': None,
            'GBPUSD': None,
            'USDCHF': None,
            'USDJPY': None,
            'USDCAD': None,
            'AUDUSD': None,
            'NZDUSD': None,
            'EURJPY': None,
            'EURGBP': None,
            'GBPJPY': None,
            'EURCAD': None,
            'EURAUD': None,
            'AUDJPY': None,
            'GBPAUD': None,
            'GBPCAD': None,
            'GBPCHF': None,
            'NZDJPY': None,
            }





def cheking(tool, advice):
  '''
  Функция проверяет есть данные в списке. Неодходима для того, чтобы не спамить одним и тем же результатом
  '''
  if send_list[tool] == advice:
    send_list[tool] = advice
    return False
  else:
    send_list[tool] = advice
    return True
    