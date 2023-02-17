# pythonAttempTrading
The day I tried to do automated trading using the order book
## How did the robot work?
The robot was receiving data from Binance's order book through the CCXT API and placing orders for position opening using the Pybit API from Bybit.
## What conditions should the robot have to open an order?

In price ranges of 100 increments, the robot would aggregate the total amount of BTC it found within those ranges and store them in an array. 

It would then calculate the total buy and sell volume within a price range that varied from 6 to 7%. When it found a difference of 2770 BTC, and the imbalance favored buying, it would open a LONG position, and if it favored selling, it would open a SHORT position. 

The robot would open the position at the price it found within the range that had the highest amount of BTC.

This means that:
- If it detected buying pressure, it would look for the entry price within the ranges that were 100 BTC below the current price, using the array element that had the highest amount of BTC. 
- If it detected selling pressure, it would look for the entry price within the ranges that were 100 BTC above the current price, using the array element that had the highest amount of BTC.
