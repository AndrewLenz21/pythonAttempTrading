import ccxt
import hashlib
import json
import pybit   #usaremos la libreria bybit de python
from pybit import usdt_perpetual #USDT perpetual
from pybit import HTTP
import pandas as pd
import numpy as np
import time
import schedule
import requests
from datetime import date, datetime, timezone, tzinfo

ccxt=ccxt.bybit({
    'apiKey': 'yourAPIKey',
    'secret': 'yourSecret',
    'enableRateLimit': True
})
bybit=usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com",
    api_key='yourAPIKey',
    api_secret='yourSecret',
)

#Funcion de enviar mensajes a Telegram //BOT FATHER telegram
def telegram_send(bot_message):
    bot_token = 'token_bot'
    bot_chatID= 'id_bot'
    send_text = 'https://api.telegram.org.bot' + bot_token + 'sendMessage?chat_id' + bot_chatID + \
                '&parse_mode=MarkdownV2&text=' + bot_message
    responde = requests.get(send_text)
    return response.json()

#symbol='BTCUSDT'
class user():
    url_main = 'https://api.bybit.com'
    url_test = 'https://api-testnet.bybit.com'
    ws_url_main = 'wss://stream.bybit.com/realtime'
    ws_url_test = 'wss://stream-testnet.bybit.com/realtime'
    headers = {'Content-Type': 'application/json'}
#-----------------------------------------------------------------------------
#Funcion abrir LONG position, con Stop Loss y Targets
    def open_long(symbol,price,size):
        symbol=symbol
        price=price
        qty=size
        
        bybit.place_active_order(symbol=symbol,
                                 order_type='Limit',
                                 side='Buy',
                                 qty=qty,
                                 price=price,
                                 time_in_force='GoodTillCancel',
                                 reduce_only=False,
                                 close_on_trigger=False)
#----------------------------------------------------------------------------------
#Funcion abrir SHORT position, con Stop Loss y Targets
    def open_short(symbol,price,size):
        symbol=symbol
        price=price
        qty=size
        
        bybit.place_active_order(symbol=symbol,
                                 order_type='Limit',
                                 side='Sell',
                                 qty=qty,
                                 price=price,
                                 time_in_force='GoodTillCancel',
                                 reduce_only=False,
                                 close_on_trigger=False)
#--------------------------------------------------------------------------------
#Definir posiciones abiertas
    def current_positions(symbol):
        symbol=symbol
        positions=bybit.my_position(symbol=symbol)        
        results=positions['result']
        
        #Datos de posicion LONG
        long_size=results[0]['size']
        long_leverage=results[0]['leverage']
        long_entry=results[0]['entry_price']
        long_stop=results[0]['trailing_stop']
        long_takeprofit=results[0]['take_profit']
        #Datos de posicion SHORT
        short_size=results[1]['size']
        short_leverage=results[1]['leverage']
        short_entry=results[1]['entry_price']
        short_stop=results[1]['trailing_stop']
        short_takeprofit=results[1]['take_profit']
        
        return long_size,long_leverage,long_entry,long_stop,short_size,short_leverage,short_entry,short_stop,long_takeprofit,short_takeprofit
#---------------------------------------------------------------------------------
#Definir Trailing stop
    def set_trailing_stop(symbol, price, long_size, short_size, porcentaje):
        symbol = symbol
        price = price
        long_size = long_size
        short_size = short_size
        porcentaje = porcentaje
        clave = porcentaje / 100
        if long_size > 0 and short_size == 0:
            #Stop Loss Price para LONG
            sl_price = round(price * clave, 1)
            bybit.set_trading_stop(symbol=symbol,
                                   side='Buy',
                                   tp_sl_mode='Full',
                                   trailing_stop=sl_price)
            print(f'Trailing stop: {sl_price}')
        elif long_size == 0 and short_size > 0:
            #Stop Loss Price
            sl_price = round(price * clave, 1)
            bybit.set_trading_stop(symbol=symbol,
                                   side='Sell',
                                   tp_sl_mode='Full',
                                   trailing_stop=sl_price)
            print(f'Trailing stop: {sl_price}')
#---------------------------------------------------------------------------------
#Definir Targets para las posiciones abiertas
    def set_position_targets(symbol, price, long_size, short_size):
        symbol = symbol
        price = price
        long_size = long_size
        short_size = short_size
        #Para LONG position
        if long_size > 0 and short_size == 0:
            #Definir target 1
            t1_price = round(price * 1.0047, 1)
            t1_qty = round(long_size * 0.5, 3)
            bybit.place_active_order(symbol=symbol,
                                     order_type='Limit',
                                     side='Sell',
                                     qty=t1_qty,
                                     price=t1_price,
                                     time_in_force='GoodTillCancel',
                                     reduce_only=True,
                                     close_on_trigger=False)
            print(f"Target 1: {t1_price}")
            #Definir target 2
            t2_price = round(price * 1.0093, 1)
            t2_qty = round(long_size * 0.25, 3)
            bybit.place_active_order(symbol=symbol,
                                     order_type='Limit',
                                     side='Sell',
                                     qty=t2_qty,
                                     price=t2_price,
                                     time_in_force='GoodTillCancel',
                                     reduce_only=True,
                                     close_on_trigger=False)
            print(f"Target 2: {t2_price}")
        #Para SHORT position
        elif long_size == 0 and short_size > 0:
            #Definir target 1
            t1_price = round(price * 0.9953, 1)
            t1_qty = round(short_size * 0.5, 3)
            bybit.place_active_order(symbol=symbol,
                                     order_type='Limit',
                                     side='Buy',
                                     qty=t1_qty,
                                     price=t1_price,
                                     time_in_force='GoodTillCancel',
                                     reduce_only=True,
                                     close_on_trigger=False)
            print(f"Target 1: {t1_price}")
            #Definir target 2
            t2_price = round(price * 0.9907, 1)
            t2_qty = round(short_size * 0.25, 3)
            bybit.place_active_order(symbol=symbol,
                                     order_type='Limit',
                                     side='Buy',
                                     qty=t2_qty,
                                     price=t2_price,
                                     time_in_force='GoodTillCancel',
                                     reduce_only=True,
                                     close_on_trigger=False)
            print(f"Target 2: {t2_price}")
        else:
            print("No fui capaz de meter los targets.... OPS")
#--------------------------------------------------------------------------------
#Definir Targets de salida al detectar tendencia en contra  LONG
    def set_long_takeprofit(symbol, entry_price, long_size, exit_long):
        symbol = symbol
        entry_price = entry_price
        long_size = long_size
        exit_long = exit_long
        #Para LONG position
        #print("Preparing Exit for Long position")
        #Take Profit
        profit_exit = round(exit_long * 0.9994, 1)
        bybit.set_trading_stop(symbol=symbol,
                               side='Buy',
                               tp_sl_mode='Full',
                               take_profit=profit_exit)
#--------------------------------------------------------------------------------
#Definir Targets de salida al detectar tendencia en contra SHORT
    def set_short_takeprofit(symbol, entry_price, short_size, exit_short):
        symbol = symbol
        entry_price = entry_price
        short_size = short_size
        exit_short = exit_short
        #Para LONG position
        #print("Preparing Exit for Long position")
        #Take Profit
        profit_exit = round(exit_short * 1.0006, 1)
        bybit.set_trading_stop(symbol=symbol,
                               side='Sell',
                               tp_sl_mode='Full',
                               take_profit=profit_exit)
#-------------------------------------------------------------------------------
#Definir quitar Targets de salida al detectar tendencia a favor
    def remove_takeprofit(symbol, long_size, short_size):
        symbol = symbol
        long_size = long_size
        short_size = short_size
        if long_size > 0 and short_size == 0:
            print("Tendencia ALCISTA de vuelta a favor, take profit removed")
            bybit.set_trading_stop(symbol=symbol,
                                   side='Buy',
                                   tp_sl_mode='Full',
                                   take_profit=0)
        elif long_size == 0 and short_size > 0:
            print("Tendencia BAJISTA de vuelta a favor, take profit removed")
            bybit.set_trading_stop(symbol=symbol,
                                   side='Sell',
                                   tp_sl_mode='Full',
                                   take_profit=0)
        else:
            print('There was a mistake with exit targets...OOOPS')
#----------------------------------------------------------------------------
#Definir funcion para cerrar posiciones
    def close_position(symbol,long_size,short_size):
        symbol=symbol
        long_size=long_size
        short_size=short_size
        if long_size==0 and short_size==0:
            print("There is no open positions")
        elif long_size > 0 and short_size==0:
            print("Closing LONG position")
            bybit.place_active_order(symbol=symbol,
                                     order_type='Market',
                                     side='Sell',
                                     qty=long_size,
                                     time_in_force='GoodTillCancel',
                                     reduce_only=True,
                                     close_on_trigger=False)
        elif long_size==0 and short_size > 0:
            print("Closing SHORT position")
            bybit.place_active_order(symbol=symbol,
                                     order_type='Market',
                                     side='Buy',
                                     qty=short_size,
                                     time_in_force='GoodTillCancel',
                                     reduce_only=True,
                                     close_on_trigger=False)
        else:
            print("Closing all positions")
            #Closing LONG
            bybit.place_active_order(symbol=symbol,
                                     order_type='Market',
                                     side='Sell',
                                     qty=long_size,
                                     time_in_force='GoodTillCancel',
                                     reduce_only=True,
                                     close_on_trigger=False)
            #Closing SHORT
            bybit.place_active_order(symbol=symbol,
                                     order_type='Market',
                                     side='Buy',
                                     qty=short_size,
                                     time_in_force='GoodTillCancel',
                                     reduce_only=True,
                                     close_on_trigger=False)
#---------------------------------------------------------------------------------
#Definir funcion para cancelar ordenes
    def close_orders(symbol):
        symbol=symbol
        bybit.cancel_all_active_orders(symbol=symbol)
        
        
#Calculos de GANANCIAS
#profits=bybit.closed_profit_and_loss(symbol='BTCUSDT')
#datos1=profits['result']['data'][0]['closed_pnl']
#print(datos1)


#url_main = 'https://api.bybit.com'
#url_test = 'https://api-testnet.bybit.com'
#ws_url_main = 'wss://stream.bybit.com/realtime'
#ws_url_test = 'wss://stream-testnet.bybit.com/realtime'
#headers = {'Content-Type': 'application/json'}
#bybit.set_trading_stop(symbol='BTCUSDT',side='Buy', tp_sl_mode='Full' ,stop_loss=0)