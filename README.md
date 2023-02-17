# pythonAttempTrading
The day I tried to do automated trading using the order book

ATTENTION: Trading is risky and much more so if you let a robot do it for you.

Evaluate the algorithm that I am giving you and use some functions that are inside, I hope it will help you. Good luck
## How did the robot work?
The robot was receiving data from Binance's order book through the CCXT API and placing orders for position opening using the Pybit API from Bybit.
## What conditions should the robot have to open an order?

In price ranges of 100 increments, the robot would aggregate the total amount of BTC it found within those ranges and store them in an array. 

It would then calculate the total buy and sell volume within a price range that varied from 6 to 7%. When it found a difference of 2770 BTC, and the imbalance favored buying, it would open a LONG position, and if it favored selling, it would open a SHORT position. 

The robot would open the position at the price it found within the range that had the highest amount of BTC.

This means that:
- If it detected buying force, it looked for the entry price in the ranges of 100 in 100 that were below the current price. Using the element of the array that had the highest amount of BTC.
- If it detected a sales force, it looked for the entry price in the ranges of 100 in 100 that were below the current price. Using the element of the array that had the highest amount of BTC.

## Did the robot have other functionalities?

Yes, every time it detected a large amount of BTC, or when it opened a trading position, it recorded everything via Telegram messages. The robot ran continuously on a Replit virtual machine.

## Is the robot currently functional?

At the moment the robot does not work correctly, because before, I used the order book of FTX and Binance together to calculate the sum of volumes. Apart from the fact that the robot, despite the fact that at the time (7 months ago) it worked perfectly and met all the conditions that I have programmed for it, IT WAS NOT PROFITABLE.
However, it was a nice experience making the algorithm and programming it.

## Will you try to create something similar?

In the future, yes, I plan to create an improved robot, using some features that I have created in it, but using more concrete and advanced strategies, adding technical analysis, indicators and exponential sums.
