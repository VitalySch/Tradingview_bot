from tradingview_ta import TA_Handler, Interval, Exchange
''' 
Создание класса для сбора информации по торговым инструментам для выдачи рекомендации на покупку или продажу
'''
class TradeTool:
  def __init__(self, ticker, screener, exchange):
    self.ticker = ticker
    
    self.price = TA_Handler(symbol=ticker, screener=screener,exchange=exchange, interval=Interval.INTERVAL_1_MINUTE).get_analysis().indicators["open"] # цена открытия на данную минуту для ориентира
    self.interval_1_min = TA_Handler(symbol=ticker, screener=screener,exchange=exchange, interval=Interval.INTERVAL_1_MINUTE).get_analysis()
    self.interval_5_min = TA_Handler(symbol=ticker, screener=screener,exchange=exchange, interval=Interval.INTERVAL_5_MINUTES).get_analysis()
    self.interval_15_min = TA_Handler(symbol=ticker, screener=screener,exchange=exchange, interval=Interval.INTERVAL_15_MINUTES).get_analysis()
    self.interval_30_min = TA_Handler(symbol=ticker, screener=screener,exchange=exchange, interval=Interval.INTERVAL_30_MINUTES).get_analysis()
    self.interval_1_hour = TA_Handler(symbol=ticker, screener=screener,exchange=exchange, interval=Interval.INTERVAL_1_HOUR).get_analysis()
    self.interval_4_hours = TA_Handler(symbol=ticker, screener=screener,exchange=exchange, interval=Interval.INTERVAL_4_HOURS).get_analysis()
    self.interval_1_day = TA_Handler(symbol=ticker, screener=screener,exchange=exchange, interval=Interval.INTERVAL_1_DAY).get_analysis()
    self.interval_1_week = TA_Handler(symbol=ticker, screener=screener,exchange=exchange, interval=Interval.INTERVAL_1_WEEK).get_analysis()
    self.interval_1_month = TA_Handler(symbol=ticker, screener=screener,exchange=exchange, interval=Interval.INTERVAL_1_MONTH).get_analysis()
    self.recommended_stop_loss = self.interval_1_hour.indicators['Pivot.M.Woodie.Middle'] # прогнозируемая точка разворота, которую можно использовать в качестве стоплосса
    self.result = self.monitoring()
    self.scalping_result = self.scalping()
  
  def monitoring(self) -> tuple:
    '''Функция проверки совпадения по рекомендациям на старшем и младших таймфреймах и возвращает результат'''
    if self.interval_1_month.summary['RECOMMENDATION'] == 'STRONG_SELL' or self.interval_1_month.summary['RECOMMENDATION'] == 'STRONG_BUY':
      if self.interval_1_month.summary['RECOMMENDATION'] == self.interval_1_week.summary['RECOMMENDATION'] == self.interval_1_day.summary['RECOMMENDATION'] == self.interval_4_hours.summary['RECOMMENDATION'] == self.interval_1_hour.summary['RECOMMENDATION']:
        result = self.interval_1_month.summary['RECOMMENDATION']
        return (f'1 month, {result}')
    
    elif self.interval_1_week.summary['RECOMMENDATION'] == 'STRONG_SELL' or self.interval_1_week.summary['RECOMMENDATION'] == 'STRONG_BUY':
      if self.interval_1_week.summary['RECOMMENDATION'] == self.interval_1_day.summary['RECOMMENDATION'] == self.interval_4_hours.summary['RECOMMENDATION'] == self.interval_1_hour.summary['RECOMMENDATION']:
        result = self.interval_1_week.summary['RECOMMENDATION']
        return (f'1 week , {result}')
        # self.result = ('1 week',self.interval_1_week.summary['RECOMMENDATION'])
  
    elif self.interval_1_day.summary['RECOMMENDATION'] == 'STRONG_SELL' or self.interval_1_day.summary['RECOMMENDATION'] == 'STRONG_BUY':
      if self.interval_1_day.summary['RECOMMENDATION'] == self.interval_4_hours.summary['RECOMMENDATION'] == self.interval_1_hour.summary['RECOMMENDATION'] == self.interval_30_min.summary['RECOMMENDATION']:
        result = self.interval_1_day.summary['RECOMMENDATION']
        return (f'1 day, {result}')
        # self.result = ('1 day',self.interval_1_day.summary['RECOMMENDATION'])
 
    elif self.interval_4_hours.summary['RECOMMENDATION'] == 'STRONG_SELL' or self.interval_4_hours.summary['RECOMMENDATION'] == 'STRONG_BUY':
      if self.interval_4_hours.summary['RECOMMENDATION'] == self.interval_1_hour.summary['RECOMMENDATION'] == self.interval_30_min.summary['RECOMMENDATION'] == self.interval_15_min.summary['RECOMMENDATION']:
        result = self.interval_4_hours.summary['RECOMMENDATION']
        return (f'4 hours, {result}')
        # self.result = ('4 hours',self.interval_4_hours.summary['RECOMMENDATION'])
  
  
    # elif self.interval_1_hour.summary['RECOMMENDATION'] == 'STRONG_SELL' or self.interval_1_hour.summary['RECOMMENDATION'] == 'STRONG_BUY':
    #   if self.interval_1_hour.summary['RECOMMENDATION'] == self.interval_30_min.summary['RECOMMENDATION'] == self.interval_15_min.summary['RECOMMENDATION'] == self.interval_5_min.summary['RECOMMENDATION']:
    #     return ('1 hour',self.interval_1_hour.summary['RECOMMENDATION'])
    #     # self.result = ('1 hour',self.interval_1_hour.summary['RECOMMENDATION'])

  def scalping(self):
    # if self.interval_15_min.moving_averages['COMPUTE']['Ichimoku'] == 'BUY' and self.interval_15_min.oscillators['COMPUTE']['CCI'] == 'BUY':
    #   if self.interval_15_min.moving_averages['COMPUTE']['Ichimoku'] == self.self.interval_5_min.moving_averages['COMPUTE']['Ichimoku'] == self.self.interval_1_min.moving_averages['COMPUTE']['Ichimoku'] and self.interval_15_min.oscillators['COMPUTE']['CCI'] == self.self.interval_5_min.oscillators['COMPUTE']['CCI'] == self.self.interval_1_min.oscillators['COMPUTE']['CCI']:
    #     return "Scalping Buy"
    # elif self.interval_15_min.moving_averages['COMPUTE']['Ichimoku'] == 'SELL' and self.interval_15_min.oscillators['COMPUTE']['CCI'] == 'SELL':
    #   if self.interval_15_min.moving_averages['COMPUTE']['Ichimoku'] == self.self.interval_5_min.moving_averages['COMPUTE']['Ichimoku'] == self.self.interval_1_min.moving_averages['COMPUTE']['Ichimoku'] and self.interval_15_min.oscillators['COMPUTE']['CCI'] == self.self.interval_5_min.oscillators['COMPUTE']['CCI'] == self.self.interval_1_min.oscillators['COMPUTE']['CCI']:
    #     return "Scalping Sell"
    if self.interval_15_min.moving_averages['RECOMMENDATION'] == 'STRONG_BUY' and self.interval_15_min.oscillators['COMPUTE']['CCI'] == 'BUY':
      # if self.interval_15_min.moving_averages['RECOMMENDATION'] == self.self.interval_5_min.moving_averages['RECOMMENDATION'] == self.self.interval_1_min.moving_averages['RECOMMENDATION'] and self.interval_15_min.oscillators['COMPUTE']['CCI'] == self.self.interval_5_min.oscillators['COMPUTE']['CCI'] == self.self.interval_1_min.oscillators['COMPUTE']['CCI']:
        return "Scalping Buy"
    elif self.interval_15_min.moving_averages['RECOMMENDATION'] == 'STRONG_SELL' and self.interval_15_min.oscillators['COMPUTE']['CCI'] == 'SELL':
      # if self.interval_15_min.moving_averages['RECOMMENDATION'] == self.self.interval_5_min.moving_averages['RECOMMENDATION'] == self.self.interval_1_min.moving_averages['RECOMMENDATION'] and self.interval_15_min.oscillators['COMPUTE']['CCI'] == self.self.interval_5_min.oscillators['COMPUTE']['CCI'] == self.self.interval_1_min.oscillators['COMPUTE']['CCI']:
        return "Scalping Sell"

  