#PRIMER PROTOTIPO DE ROBOT DE TRADING (BUENOS RESULTADOS)
#USANDO LIBRO DE ORDENES SPOT (FTX y BINANCE)
#Detectaremos un precio en donde exista una gran cantidad de volumen

#THIS IS THE MAIN FILE

#Ese precio lo usaremos como punto de rebote, o precio de entrada a LONG o SHORT
import ccxt
import hashlib
import json
import pybit
import pandas as pd
import numpy as np
import time
import schedule
import math
import telegram_send
#
from ComandosBybit import user
#
from datetime import date, datetime, timezone, tzinfo

#Datos principales retirados de Binance
import PrincipalDataCenter as data
#Usuario Api and Secret importados
import usuario1 as inf
#Si hay necesidad, usaremos los comandos de Pybit
#-----------------------------------------------
from ccxt.base.exchange import Exchange
from pprint import pprint

#Configurar Data Center (solo lectura, no operaciones)
#Binance
binance = ccxt.binance({
    'apiKey': data.apiKey,
    'secret': data.secretKey,
    'enableRateLimit': True
})
#FTX
ftx = ccxt.ftx({
    'apiKey': data.apiKeyFTX,
    'secret': data.secretKeyFTX,
    'enableRateLimit': True
})
#------------------------------------------------
#Configurar usuario (en este caso usa Bybit)
usuario = ccxt.bybit({
    'apiKey': inf.apiKey,
    'secret': inf.secretKey,
    'enableRateLimit': True
})
#En este caso sera para el par BTC:USDT futuros perpetuos con USDT
#Consideramos que cada contrato vale minimo 0,001 BTC
symbol = 'BTC/USDT'  #Analizar en dataCenter
symbolOP = 'BTC/USDT:USDT'  #Para ordenar posiciones
symbol_user = 'BTCUSDT'
symbol_FTX = 'BTC/USDT'

params = {'timeinForce': 'PostOnly'}

#-------------------------------------------------------------------------------------------------


#order_book_upgraded() DETECTOR de Tendencia y Precios de Entrada segun el volumen
#Usa datos del libro de ordenes de Binance y FTX
def order_book_upgraded():
    print('--------------------------')
    #print('Analisis OB upgraded, Binance and FTX')
    #print('-----------------------')
    #Datos Binance
    df_binance = pd.DataFrame()
    temp_df_binance = pd.DataFrame()
    #mercados=exchange_futuros.load_markets()
    params = {}
    ordenes_binance = binance.fetch_order_book(symbol=symbol, limit=1440)
    #Datos variables
    #Niveles de rangos
    r1=8
    r2=56
    #numero de decimales
    nd=0
    #----------------------------------------
    bids_binance = ordenes_binance['bids']
    asks_binance = ordenes_binance['asks']

    #bids = ordenes['bids']
    #asks = ordenes['asks']

    first_bid_binance = bids_binance[0]
    first_ask_binance = asks_binance[0]

    bid_vol_binance = []
    ask_vol_binance = []
    #----Suma de volumenes--------
    for x in range(11):

        for set in bids_binance:
            #print(set)
            #price = set [0]
            vol_binance = set[1]
            bid_vol_binance.append(vol_binance)

            #print(bid_vol_list)
            sum_bidvol_binance = sum(bid_vol_binance)
            #print(sum_bidvol)

        for set in asks_binance:
            #print(set)
            #price = set [0]
            vol_binance = set[1]
            ask_vol_binance.append(vol_binance)

            #print(ask_vol_list)
            sum_askvol_binance = sum(ask_vol_binance)
            #print(sum_askvol)
    #print('ASKS-VENTAS')

    first_bid_binance = bids_binance[0][0]*pow(10,nd)
    last_bid_binance = bids_binance[1439][0]*pow(10,nd)

    first_ask_binance = asks_binance[0][0]*pow(10,nd)
    last_ask_binance = asks_binance[1439][0]*pow(10,nd)

    #Datos FTX
    df_ftx = pd.DataFrame()
    temp_df_ftx = pd.DataFrame()
    #mercados=exchange_futuros.load_markets()
    #print(mercados)
    params = {}
    ordenes_ftx = ftx.fetch_order_book(symbol=symbol, limit=100)
    bids_ftx = ordenes_ftx['bids']
    asks_ftx = ordenes_ftx['asks']
    #print('BIDS-COMPRAS')
    #print(bids1[0])
    #print(bids1[1699])

    bids_ftx = ordenes_ftx['bids']
    asks_ftx = ordenes_ftx['asks']

    first_bid_ftx = bids_ftx[0]
    first_ask_ftx = asks_ftx[0]

    bid_vol_ftx = []
    ask_vol_ftx = []

    for y in range(11):

        for set in bids_ftx:
            #print(set)
            #price = set [0]
            vol_ftx = set[1]
            bid_vol_ftx.append(vol_ftx)

            #print(bid_vol_list)
            sum_bidvol_ftx = sum(bid_vol_ftx)
            #print(sum_bidvol)

        for set in asks_ftx:
            #print(set)
            #price = set [0]
            vol_ftx = set[1]
            ask_vol_ftx.append(vol_ftx)

            #print(ask_vol_list)
            sum_askvol_ftx = sum(ask_vol_ftx)
            #print(sum_askvol)

    #print('ASKS-VENTAS')
    first_bid_ftx = bids_ftx[0][0]*pow(10,nd)
    last_bid_ftx = bids_ftx[99][0]*pow(10,nd)

    first_ask_ftx = asks_ftx[0][0]*pow(10,nd)
    last_ask_ftx = asks_ftx[99][0]*pow(10,nd)

    #-----------------------------------------------------------------------------------------------------------
    #Generamos los rangos nivel 1 de BIDS usando el rango de BINANCE
    num_bids=(first_bid_binance-last_bid_binance)/r1
    grupos_bid=math.trunc(num_bids)+1  #numero de grupos BIDS
    rangos_bids=list(range(math.trunc(last_bid_binance),math.trunc(first_bid_binance+(r1-0.02)),r1)) #rangos definidos
    #Generamos los rangos nivel 2 de BIDS usnado el rango de BINANCE
    num2_bids=(first_bid_binance-last_bid_binance)/r2
    grupos2_bids=math.trunc(num2_bids)+1
    rangos2_bids=list(range(math.trunc(last_bid_binance),math.trunc(first_bid_binance+(r2-0.02)),r2)) #rangos nivel 2 definidos
    
    #Generamos los rangos nivel 1 de ASKS usando el rango de BINANCE
    num_asks=(last_ask_binance-first_ask_binance)/r1
    grupos_ask=math.trunc(num_asks)+1  #numero de grupos ASKS
    rangos_asks=list(range(math.trunc(first_ask_binance),math.trunc(last_ask_binance+(r1-0.02)),r1)) #rangos definidos 
    #Generamos los rangos nivel 2 de BIDS usnado el rango de BINANCE
    num2_asks=(last_ask_binance-first_ask_binance)/r2
    grupos2_asks=math.trunc(num2_asks)+1
    rangos2_asks=list(range(math.trunc(first_ask_binance),math.trunc(last_ask_binance+(r2-0.02)),r2)) #rangos nivel 2 definidos
    #-----------------------------------------------------------------------------------------------------------

    #Volumen total en un rango de r1 en r1 ASKS-VENTAS
    #print('Volumen de ventas')

    range_volask = []
    for a, b in zip(rangos_asks, rangos_asks[1:]):
        suma_binance = sum(x[1] for x in asks_binance if (x[0]*pow(10,nd) >= a and x[0]*pow(10,nd) < b))
        suma_ftx = sum(x[1] for x in asks_ftx if (x[0]*pow(10,nd) >= a and x[0]*pow(10,nd) < b))
        suma = suma_binance + suma_ftx
        vol10_ask = round(suma, 1)
        range_volask.append(vol10_ask)
    #Numero de dato donde se encuentra el mayor volumen en ASKS
    #print(range_volask)
    i_maxask = range_volask.index(max(range_volask))
    mayor_vol_ask = range_volask[i_maxask]/pow(10,nd)

    #Encontrar los precios donde esta el mayor volumen de ASK-VENTAS
    precio_ask1 = rangos_asks[i_maxask + 1]/pow(10,nd)
    precio_ask2 = rangos_asks[i_maxask]/pow(10,nd)

    range2_volask=[]
    for a, b in zip(rangos2_asks, rangos2_asks[1:]):
        suma_binance=sum(x[1] for x in asks_binance if (x[0]*pow(10,nd) >= a and x[0]*pow(10,nd) < b))
        suma_ftx=sum(x[1] for x in asks_ftx if (x[0]*pow(10,nd) >= a and x[0]*pow(10,nd) < b))
        suma = suma_binance+suma_ftx
        volr2_ask=round(suma,1)
        range2_volask.append(volr2_ask)
    #Numero de dato donde se encuentra el mayor volumen en ASKS
    #print(range_volask)
    i_maxask2=range2_volask.index(max(range2_volask))
    mayor2_vol_ask=range2_volask[i_maxask2]/pow(10,nd)
    
    #Encontrar los precios donde esta el mayor volumen de ASK-VENTAS
    precio2_ask1=rangos2_asks[i_maxask2+1]/pow(10,nd)
    precio2_ask2=rangos2_asks[i_maxask2]/pow(10,nd)
    

    #Volumen total en un rango de r1 en r1 BIDS-COMPRAS
    range_volbid = []
    for a, b in zip(rangos_bids, rangos_bids[1:]):
        suma_binance = sum(x[1] for x in bids_binance if (x[0]*pow(10,nd) >= a and x[0]*pow(10,nd) < b))
        suma_ftx = sum(x[1] for x in bids_ftx if (x[0]*pow(10,nd) >= a and x[0]*pow(10,nd) < b))
        suma = suma_binance + suma_ftx
        vol10_bid = round(suma, 1)
        range_volbid.append(vol10_bid)
    #Numero de dato donde se encuentra el mayor volumen en BIDS
    i_maxbid = range_volbid.index(max(range_volbid))
    mayor_vol_bid = range_volbid[i_maxbid]/pow(10,nd)

    #Encontrar los precios donde esta el mayor volumen de BID-COMPRAS
    precio_bid1 = rangos_bids[i_maxbid]/pow(10,nd)
    precio_bid2 = rangos_bids[i_maxbid + 1]/pow(10,nd)
    
    #Agrupacion nivel 2
    range2_volbid=[]
    for a, b in zip(rangos2_bids, rangos2_bids[1:]):
        suma_binance=sum(x[1] for x in bids_binance if (x[0]*pow(10,nd) >= a and x[0]*pow(10,nd) < b))
        suma_ftx=sum(x[1] for x in bids_ftx if (x[0]*pow(10,nd) >= a and x[0]*pow(10,nd) < b))
        suma=suma_binance+suma_ftx
        volr2_bid=round(suma,1)
        range2_volbid.append(volr2_bid)
    #Numero de dato donde se encuentra el mayor volumen en BIDS
    i_maxbid2=range2_volbid.index(max(range2_volbid))
    mayor2_vol_bid=range2_volbid[i_maxbid2]/pow(10,nd)
    
    #Encontrar los precios donde esta el mayor volumen de BID-COMPRAS
    precio2_bid1=rangos_bids[i_maxbid2]/pow(10,nd)
    precio2_bid2=rangos_bids[i_maxbid2+1]/pow(10,nd)


    #Definir tendencia

    sum_askvol = sum_askvol_binance + sum_askvol_ftx
    sum_bidvol = sum_bidvol_binance + sum_bidvol_ftx
    '''
    #Definimos el precio para el short y el long, ASK/VENTA 2  y BID/COMPRA 1
    if precio2_bid1+50 > precio_bid1:
        buy_price=precio_bid1
    else:
        buy_price=precio2_bid1
        
    if precio2_ask2-50 < precio_ask2:
        sell_price=precio_ask2
    else:
        sell_price=precio2_ask2
    '''
    fuerza_venta = round(sum_askvol, 1)
    fuerza_compra = round(sum_bidvol, 1)
    diff_vol = round(abs(fuerza_venta - fuerza_compra), 1)
    if fuerza_venta > fuerza_compra:
        indice = round(((fuerza_venta / fuerza_compra) * 100 - 100), 2)
        tendencia = False
        print(f"Tendencia BAJISTA---fuerza={indice}%  \nDiferencia Volumen={diff_vol} BTC")
    elif fuerza_compra > fuerza_venta:
        indice = round(((fuerza_compra / fuerza_venta) * 100 - 100), 2)
        tendencia = True
        print(f"Tendencia ALCISTA---fuerza={indice}%  \nDiferencia Volumen={diff_vol} BTC")
    else:
        print("No hay tendencia definida")

    #print('Buscando precio de VENTA...')
    #print(f'El mayor volumen ASK/VENTA es: {mayor_vol_ask}')
    #print(f'comprendido entre {precio_ask2} y {precio_ask1}')

    #print('Buscando precio de COMPRA...')
    #print(f'El mayor volumen BID/COMPRA es: {mayor_vol_bid}')
    #print(f'comprendido entre {precio_bid2} y {precio_bid1}')

    short_price = round(precio_ask1 * 0.99913, 1)
    long_price = round(precio_bid2 * 1.0005, 1)
    
    print('-----Analizando precios de entrada------')
    print(f'Short Entry:{short_price}   Long Entry:{long_price}')

    actual_price = (first_bid_binance + first_ask_binance) / 2

    return tendencia, indice, short_price, long_price, diff_vol, actual_price


#FUNCION PRINCIPAL 'order_book_upgraded()' returns tendencia,indice,short_price,long_price, actual_price
#Definidas en los Comandos Bybit por la funcion
#Abrir Posicion
def bot():
    numero_contratos = 0.004  #Cantidad a meter por operacion
    qty = numero_contratos
    #Contratos minimos son 4, es decir 0.004 BTC =  casi 90 dolares , con apalancamiento x3==30
    #Looking Positions

    #Posiciones abiertas:
    #Definidas en los Comandos Bybit por la funcion
    #current_positions(symbol)
    positions = user.current_positions(symbol=symbol_user)
    #Informacion LONG
    long_position = positions[0]
    long_leverage = positions[1]
    long_entry = positions[2]
    long_stop = positions[3]
    #Informacion SHORT
    short_position = positions[4]
    short_leverage = positions[5]
    short_entry = positions[6]
    short_stop = positions[7]
    #Informacion de salida
    long_takeprofit = positions[8]
    short_takeprofit = positions[9]

    #Variable bandera para saber si poner o no los targets de posicion
    if long_stop > 0 or short_stop > 0:
        targets_set = True
    else:
        targets_set = False
    #Variable bandera para saber si poner o no los targets de salida
    #Variable bandera que define si estamos en posicion
    if long_position > 0 and short_position == 0:
        in_pos = True
        posicion = 'LONG'
        if long_stop == 0 and targets_set == False:
            print('--------------------------------')
            print("We have a LONG position")
            print('Settings targets')
            user.set_trailing_stop(symbol=symbol_user,
                                    price=long_entry,
                                    long_size=long_position,
                                    short_size=short_position,
                                    porcentaje=1.75)
            user.set_position_targets(symbol=symbol_user,
                                    price=long_entry,
                                    long_size=long_position,
                                    short_size=short_position)
            telegram_send.send(messages=[f"\U0001F916#BTC/USDT\U000026A1(LONG \U0001F4C8 open)\U0001F525\n\nTrailing Stop: {round(long_entry*0.016,1)}\nEntry price:  {long_entry}\n\nTargets:\n 1) {round(long_entry*1.0047,1)} \n 2) {round(long_entry*1.0093,1)}\n 3)  \U0001F680"])
            targets_set = True
            print('Targets puestos correctamente')
            telegram_send.send(messages=[f"\U0001F916#BTC/USDT \U0001F5A5\n\n\U000026A1Targets programmed correctly \U000026A1"])
        else:
            print('--------------------------------')
            print("We have LONG position")
    elif short_position > 0 and long_position == 0:
        in_pos = True
        posicion = 'SHORT'
        if short_stop == 0 and targets_set == False:
            print('--------------------------------')
            print("We have a SHORT position")
            print('Settings targets')
            user.set_trailing_stop(symbol=symbol_user,
                                   price=short_entry,
                                   long_size=long_position,
                                   short_size=short_position,
                                   porcentaje=1.75)
            user.set_position_targets(symbol=symbol_user,
                                    price=short_entry,
                                    long_size=long_position,
                                    short_size=short_position)
            telegram_send.send(messages=[f"\U0001F916#BTC/USDT\U000026A1(SHORT \U0001F4C9 open)\U0001F525\n\nTrailing Stop: {round(short_entry*0.016,1)}\nEntry price:  {short_entry}\n\nTargets:\n 1) {round(short_entry*0.9953,1)} \n 2) {round(short_entry*0.9907,1)}\n 3)  \U0001F680"])
            targets_set = True
            print('Targets puestos correctamente')
            telegram_send.send(messages=[f"\U0001F916#BTC/USDT \U0001F5A5\n\n\U000026A1Targets programmed correctly \U000026A1"])
        else:
            print('--------------------------------')
            print("We have SHORT position")
    else:
        in_pos = False
        targets_set = False
        print('----------------------------')
        print("Waiting for an open position")

    #Definiendo tendencias y fuerzas con order_book_upgrade()
    order_book = order_book_upgraded()  #tendencia,fuerza,entrada short,entrada long
    tendencia = order_book[0]
    fuerza = order_book[1]
    entrada_short = order_book[2]
    entrada_long = order_book[3]
    diff_vol = order_book[4]
    actual_price = order_book[5]
    #Cantidad de contratos BTC 1 contract=0.001 BTC
    qty = qty
    #print(signal)
    if in_pos == False:
        #Condicion para orden LONG
        if tendencia == True and fuerza > 40 and diff_vol > 2770:
            #Precio condicion
            precio_condicion = abs((actual_price / entrada_long) - 1)
            bp = entrada_long
            long_price = round(bp, 1)
            if precio_condicion < 0.00055:
                #Cerrar orden actual
                print('Opening LONG order:')
                print(f'Buy price: {long_price}  Qty:{qty} ')
                user.open_long(symbol=symbol_user, 
                               price=long_price, 
                               size=qty)
                telegram_send.send(messages=[f'\U000026A1#BTC/USDT\U000026A1\U0001F9BE\n \n\U0001F916 Opening LONG order \n\U0001F4C8 Possible entry: {long_price}'])
                #Orden abierta solo por 9 segundos, para evitar el algoritmo de bloqueo de Bybit
                time.sleep(9)
                posicion_entrada=user.current_positions(symbol=symbol_user)
                order_long_qty=posicion_entrada[0]
                order_long_entry=posicion_entrada[2]
                if order_long_qty == 0:
                    user.close_orders(symbol=symbol_user)
                else:
                    print(f'Posicion abierta con exito en {order_long_entry}')
                    #Targets todavia no definidos
                    targets_set = False
            else:
                print('Movimiento fuerte detectado')
                if precio_condicion < 0.00075:
                    telegram_send.send(messages=[f'\U000026A1#BTC/USDT\U000026A1\n \n\U0001F4E1 Possible LONG order \U0001F4A1'])
                    print(f'Acercandose a una posicion LONG en {long_price}')
        #Condicion para orden SHORT
        elif tendencia == False and fuerza > 40 and diff_vol > 2770:
            #Precio condicion
            precio_condicion = abs((entrada_short / actual_price) - 1)
            sp = entrada_short
            short_price = round(sp, 1)
            if precio_condicion < 0.00055:
                print('Opening SHORT order:')
                print(f'Sell price: {short_price}  Qty:{qty} ')
                user.open_short(symbol=symbol_user,
                                price=short_price,
                                size=qty)
                telegram_send.send(messages=[f'\U000026A1#BTC/USDT\U000026A1\U0001F9BE\n \n\U0001F916 Opening SHORT order \n\U0001F4C9 Possible entry: {short_price}'])
                #Orden abierta solo por 9 segundos, para evitar el algoritmo de bloqueo de Bybit
                time.sleep(9)
                posicion_entrada=user.current_positions(symbol=symbol_user)
                order_short_qty=posicion_entrada[4]
                order_long_entry=posicion_entrada[6]
                if order_short_qty == 0:
                    user.close_orders(symbol=symbol_user)
                else:
                    print(f'Posicion abierta con exito en {order_short_entry}')
                    #Targets todavia no definidos
                    targets_set = False
            else:
                print('Movimiento fuerte detectado')
                if precio_condicion < 0.00075:
                    telegram_send.send(messages=[f'\U000026A1#BTC/USDT\U000026A1\n \n\U0001F4E1 Possible SHORT order \U0001F4A1'])
                    print(f'Acercandose a una posicion SHORT en {short_price}')
        else:
            print('Movimiento fuerte no detectado')
    #Definiendo condiciones para posiciones abiertas
    elif in_pos == True:
        condition_qty = (qty/2) + (qty/8)
        condition2_qty = (qty/4) + (qty/8)
        
        condition_stop_long = long_entry * 0.0081
        condition_stop_short = short_entry * 0.0081
        condition2_stop_long = long_entry * 0.0076
        condition2_stop_short = short_entry * 0.0076
        #Definiendo cuando se agarra el primer target
        if long_position > condition2_qty and long_position < condition_qty and short_position == 0:
            if condition_stop_long < long_stop:
                user.set_trailing_stop(symbol=symbol_user,
                                        price=long_entry,
                                        long_size=long_position,
                                        short_size=short_position,
                                        porcentaje=0.81)
                print('Primer target alcanzado, reduciendo stop_loss')
                telegram_send.send(messages=[f'\U0001F916#BTC/USDT\U000026A1(LONG \U0001F4C8)\n\n\U00002705Target 1: Hitted \U0001F4B5'])
            else:
                print('Posicion exitosa')
        elif short_position > condition2_qty and short_position < condition_qty and long_position == 0:
            if condition_stop_short < short_stop:
                user.set_trailing_stop(symbol=symbol_user,
                                        price=short_entry,
                                        long_size=long_position,
                                        short_size=short_position,
                                        porcentaje=0.81)
                print('Primer target alcanzado, reduciendo stop_loss')
                telegram_send.send(messages=[f'\U0001F916#BTC/USDT\U000026A1(SHORT \U0001F4C9)\n\n\U00002705Target 1: Hitted \U0001F4B5'])
            else:
                print('Posicion exitosa')
        elif long_position > 0 and long_position < condition2_qty and short_position == 0:
            if condition2_stop_long < long_stop:
                user.set_trailing_stop(symbol=symbol_user,
                                        price=long_entry,
                                        long_size=long_position,
                                        short_size=short_position,
                                        porcentaje=0.76)
                print('Segundo target alcanzado, reduciendo stop_loss')
                telegram_send.send(messages=[f'\U0001F916#BTC/USDT\U000026A1(LONG \U0001F4C8)\n\n\U00002705Target 2: Hitted \U0001F911'])
            else:
                print('Posicion exitosa')
        elif short_position > 0 and short_position < condition2_qty and long_position == 0:
            if condition2_stop_short < short_stop:
                user.set_trailing_stop(symbol=symbol_user,
                                        price=short_entry,
                                        long_size=long_position,
                                        short_size=short_position,
                                        porcentaje=0.76)
                print('Segundo target alcanzado, reduciendo stop_loss')
                telegram_send.send(messages=[f'\U0001F916#BTC/USDT\U000026A1(SHORT \U0001F4C9)\n\n\U00002705Target 2: Hitted \U0001F911'])
            else:
                print('Posicion exitosa')
        else:
            print('Posicion completa, aun no se alcanzan targets')
        #Definir condiciones para definir Take Profit
        if posicion == 'LONG' and tendencia == False and fuerza > 38 and diff_vol > 2700:
            precio_condicion2 = abs((entrada_short / actual_price) - 1)
            salida_long = round(entrada_short * 0.9993,1)
            if precio_condicion2 > 0.0005 and long_takeprofit == 0 and actual_price > (long_entry*1.003):
                user.set_long_takeprofit(symbol=symbol_user,
                                        entry_price=long_entry,
                                        long_size=long_position,
                                        exit_long=salida_long)
                print(f'Tendecia en contra detectada, Take Profit puesto en {salida_long}')
                telegram_send.send(messages=[f'\U0001F916#BTC/USDT\U000026A0(LONG \U0001F4C8)\U000026A0\n\nDowntrend detected \U0001F4C9\U0001F6A8\n\U0001F6F0 Take Profit: {salida_long}'])
            else:
                print(f'Posible cierre de posicion LONG en {salida_long}')
            if actual_price < (long_entry * 0.9855):
                user.close_position(symbol=symbol_user,
                                    long_size=long_position,
                                    short_size=short_position)
                print('Cerrado de emergencia, posicion LONG fallida')
                telegram_send.send(messages=[f'\U0001F916#BTC/USDT\U000026A0(LONG \U0001F4C8)\U000026A0\n\n\U0001F6A8Emergency exit\U0001F6A8 \nLONG position failed \U0001F625'])
        elif posicion == 'SHORT' and tendencia == True and fuerza > 38 and diff_vol > 2700:
            precio_condicion2 = abs((actual_price / entrada_long) - 1)
            salida_short = round(entrada_long * 1.0007,1)
            if precio_condicion2 > 0.0005 and short_takeprofit == 0 and actual_price < (short_entry*0.997):
                user.set_short_takeprofit(symbol=symbol_user,
                                        entry_price=short_entry,
                                        short_size=short_position,
                                        exit_short=salida_short)
                print(f'Tendecia en contra detectada, Take Profit puesto en {salida_short}')
                telegram_send.send(messages=[f'\U0001F916#BTC/USDT\U000026A0(SHORT \U0001F4C9)\U000026A0\n\nUptrend detected \U0001F4C8\U0001F6A8\n\U0001F6F0 Take Profit: {salida_short}'])
            else:
                print(f'Posible cierre de posicion SHORT en {salida_short}')
            if actual_price > (short_entry * 1.0145):
                user.close_position(symbol=symbol_user,
                                    long_size=long_position,
                                    short_size=short_position)
                print('Cerrado de emergencia, posicion SHORT fallida')
                telegram_send.send(messages=[f'\U0001F916#BTC/USDT\U000026A0(SHORT \U0001F4C9)\U000026A0\n\n\U0001F6A8Emergency exit\U0001F6A8 \nSHORT position failed \U0001F625'])
        elif long_takeprofit > 0 or short_takeprofit > 0:
            if posicion == 'LONG' and tendencia == True and fuerza > 40 and diff_vol > 2680:
                precio_condicion3 = abs((long_takeprofit / actual_price) - 1)
                if precio_condicion3 < 0.0009:
                    user.remove_takeprofit(symbol=symbol_user,
                                        long_size=long_position,
                                        short_size=short_position)
                    print('Tendencia a favor de vuelta, removing TP')
                    telegram_send.send(messages=[f'\U0001F916#BTC/USDT\U000026A1(LONG \U0001F4C8)\U000026A1\n\nUptrend is back \U0001F525 \nTake Profit removed \U0000274C'])
                else:
                    print('Tendencia a favor de vuelta, pero no se remueve el tp')
            elif posicion == 'SHORT' and tendencia == False and fuerza > 40 and diff_vol > 2680:
                precio_condicion3 = abs((actual_price / short_takeprofit) - 1)
                if precio_condicion3 < 0.0009:
                    user.remove_takeprofit(symbol=symbol_user,
                                        long_size=long_position,
                                        short_size=short_position)
                    print('Tendencia a favor de vuelta, removing TP')
                    telegram_send.send(messages=[f'\U0001F916#BTC/USDT\U000026A1(SHORT \U0001F4C9)\U000026A1\n\nDowntrend is back \U0001F525 \nTake Profit removed \U0000274C'])
                else:
                    print('Tendencia a favor de vuelta, pero no se remueve el tp')
        elif posicion == 'LONG':
            print('LONG position open, waiting for targets')
        elif posicion == 'SHORT':
            print('SHORT position open, waiting for targets')
        else:
            telegram_send.send(messages=[f"\U000026A1#BTC/USDT\U000026A1\U000026A0\n \n\U0000274C Error programming targets \U0000274C"])
            print('There was a mistake with the targeetss.....OOPPPSS')


#bot()
#Loop del bot
schedule.every(4).seconds.do(bot)
while True:
    try:
        schedule.run_pending()
    except:
        print('There was a mistake...OOPSS')
        telegram_send.send(messages=[f"\U0001F916#BTC/USDT \U0001F6A8 Bot message\n\n\U0001F449 INTERNAL ERROR \U0001F448 \nSleeping for 15 sec \U0001F4A4"])
        time.sleep(20)

#-------------------------------------
#Obtener Bid y Ask (Oferta y Demanda)
