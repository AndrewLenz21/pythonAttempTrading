def describe(self):
        return self.deep_extend(super(bybit, self).describe(), {
            'id': 'bybit',
            'name': 'Bybit',
            'countries': ['VG'],  # British Virgin Islands
            'version': 'v2',
            'userAgent': None,
            # 50 requests per second for GET requests, 1000ms / 50 = 20ms between requests
            # 20 requests per second for POST requests, cost = 50 / 20 = 2.5
            'rateLimit': 20,
            'hostname': 'bybit.com',  # bybit.com, bytick.com
            'pro': True,
            'has': {
                'CORS': True,
                'spot': True,
                'margin': False,
                'swap': True,
                'future': True,
                'option': None,
                'cancelAllOrders': True,
                'cancelOrder': True,
                'createOrder': True,
                'createStopLimitOrder': True,
                'createStopMarketOrder': True,
                'createStopOrder': True,
                'editOrder': True,
                'fetchBalance': True,
                'fetchBorrowInterest': True,
                'fetchBorrowRate': False,
                'fetchBorrowRates': False,
                'fetchClosedOrders': True,
                'fetchCurrencies': True,
                'fetchDepositAddress': True,
                'fetchDepositAddresses': False,
                'fetchDepositAddressesByNetwork': True,
                'fetchDeposits': True,
                'fetchFundingRate': True,
                'fetchFundingRateHistory': False,
                'fetchIndexOHLCV': True,
                'fetchLedger': True,
                'fetchMarketLeverageTiers': True,
                'fetchMarkets': True,
                'fetchMarkOHLCV': True,
                'fetchMyTrades': True,
                'fetchOHLCV': True,
                'fetchOpenInterestHistory': True,
                'fetchOpenOrders': True,
                'fetchOrder': True,
                'fetchOrderBook': True,
                'fetchOrders': True,
                'fetchOrderTrades': True,
                'fetchPositions': True,
                'fetchPremiumIndexOHLCV': True,
                'fetchTicker': True,
                'fetchTickers': True,
                'fetchTime': True,
                'fetchTrades': True,
                'fetchTradingFee': False,
                'fetchTradingFees': False,
                'fetchTransactions': None,
                'fetchTransfers': True,
                'fetchWithdrawals': True,
                'setLeverage': True,
                'setMarginMode': True,
                'setPositionMode': True,
                'transfer': True,
                'withdraw': True,
            },
            'timeframes': {
                '1m': '1',
                '3m': '3',
                '5m': '5',
                '15m': '15',
                '30m': '30',
                '1h': '60',
                '2h': '120',
                '4h': '240',
                '6h': '360',
                '12h': '720',
                '1d': 'D',
                '1w': 'W',
                '1M': 'M',
                '1y': 'Y',
            },
            'urls': {
                'test': {
                    'spot': 'https://api-testnet.{hostname}',
                    'futures': 'https://api-testnet.{hostname}',
                    'v2': 'https://api-testnet.{hostname}',
                    'public': 'https://api-testnet.{hostname}',
                    'private': 'https://api-testnet.{hostname}',
                },
                'logo': 'https://user-images.githubusercontent.com/51840849/76547799-daff5b80-649e-11ea-87fb-3be9bac08954.jpg',
                'api': {
                    'spot': 'https://api.{hostname}',
                    'futures': 'https://api.{hostname}',
                    'v2': 'https://api.{hostname}',
                    'public': 'https://api.{hostname}',
                    'private': 'https://api.{hostname}',
                },
                'www': 'https://www.bybit.com',
                'doc': [
                    'https://bybit-exchange.github.io/docs/inverse/',
                    'https://bybit-exchange.github.io/docs/linear/',
                    'https://github.com/bybit-exchange',
                ],
                'fees': 'https://help.bybit.com/hc/en-us/articles/360039261154',
                'referral': 'https://partner.bybit.com/b/ccxt',
            },
            'api': {
                'public': {
                    'get': {
                        # inverse swap
                        'v2/public/orderBook/L2': 1,
                        'v2/public/kline/list': 3,
                        'v2/public/tickers': 1,
                        'v2/public/trading-records': 1,
                        'v2/public/symbols': 1,
                        'v2/public/mark-price-kline': 3,
                        'v2/public/index-price-kline': 3,
                        'v2/public/premium-index-kline': 2,
                        'v2/public/open-interest': 1,
                        'v2/public/big-deal': 1,
                        'v2/public/account-ratio': 1,
                        'v2/public/funding-rate': 1,
                        'v2/public/elite-ratio': 1,
                        'v2/public/funding/prev-funding-rate': 1,
                        'v2/public/risk-limit/list': 1,
                        # linear swap USDT
                        'public/linear/kline': 3,
                        'public/linear/recent-trading-records': 1,
                        'public/linear/risk-limit': 1,
                        'public/linear/funding/prev-funding-rate': 1,
                        'public/linear/mark-price-kline': 1,
                        'public/linear/index-price-kline': 1,
                        'public/linear/premium-index-kline': 1,
                        # spot
                        'spot/v1/time': 1,
                        'spot/v1/symbols': 1,
                        'spot/quote/v1/depth': 1,
                        'spot/quote/v1/depth/merged': 1,
                        'spot/quote/v1/trades': 1,
                        'spot/quote/v1/kline': 1,
                        'spot/quote/v1/ticker/24hr': 1,
                        'spot/quote/v1/ticker/price': 1,
                        'spot/quote/v1/ticker/book_ticker': 1,
                        # data
                        'v2/public/time': 1,
                        'v2/public/announcement': 1,
                        # USDC endpoints
                        # option USDC
                        'option/usdc/openapi/public/v1/order-book': 1,
                        'option/usdc/openapi/public/v1/symbols': 1,
                        'option/usdc/openapi/public/v1/tick': 1,
                        'option/usdc/openapi/public/v1/delivery-price': 1,
                        'option/usdc/openapi/public/v1/query-trade-latest': 1,
                        # perpetual swap USDC
                        'perpetual/usdc/openapi/public/v1/order-book': 1,
                        'perpetual/usdc/openapi/public/v1/symbols': 1,
                        'perpetual/usdc/openapi/public/v1/tick': 1,
                        'perpetual/usdc/openapi/public/v1/kline/list': 1,
                        'perpetual/usdc/openapi/public/v1/mark-price-kline': 1,
                        'perpetual/usdc/openapi/public/v1/index-price-kline': 1,
                        'perpetual/usdc/openapi/public/v1/premium-index-kline': 1,
                        'perpetual/usdc/openapi/public/v1/open-interest': 1,
                        'perpetual/usdc/openapi/public/v1/big-deal': 1,
                        'perpetual/usdc/openapi/public/v1/account-ratio': 1,
                        'perpetual/usdc/openapi/public/v1/prev-funding-rate': 1,
                        'perpetual/usdc/openapi/public/v1/risk-limit/list': 1,
                        # account
                        'asset/v1/public/deposit/allowed-deposit-list': 1,
                        'contract/v3/public/copytrading/symbol/list': 1,
                    },
                },
                'private': {
                    'get': {
                        # inverse swap
                        'v2/private/order/list': 5,
                        'v2/private/order': 5,
                        'v2/private/stop-order/list': 5,
                        'v2/private/stop-order': 1,
                        'v2/private/position/list': 25,
                        'v2/private/position/fee-rate': 40,
                        'v2/private/execution/list': 25,
                        'v2/private/trade/closed-pnl/list': 1,
                        'v2/public/risk-limit/list': 1,  # TODO check
                        'v2/public/funding/prev-funding-rate': 25,  # TODO check
                        'v2/private/funding/prev-funding': 25,
                        'v2/private/funding/predicted-funding': 25,
                        'v2/private/account/api-key': 5,
                        'v2/private/account/lcp': 1,
                        'v2/private/wallet/balance': 25,  # 120 per minute = 2 per second => cost = 50 / 2 = 25
                        'v2/private/wallet/fund/records': 25,
                        'v2/private/wallet/withdraw/list': 25,
                        'v2/private/exchange-order/list': 1,
                        # linear swap USDT
                        'private/linear/order/list': 5,  # 600 per minute = 10 per second => cost = 50 / 10 =  5
                        'private/linear/order/search': 5,
                        'private/linear/stop-order/list': 5,
                        'private/linear/stop-order/search': 5,
                        'private/linear/position/list': 25,
                        'private/linear/trade/execution/list': 25,
                        'private/linear/trade/closed-pnl/list': 25,
                        'public/linear/risk-limit': 1,
                        'private/linear/funding/predicted-funding': 25,
                        'private/linear/funding/prev-funding': 25,
                        # inverse futures
                        'futures/private/order/list': 5,
                        'futures/private/order': 5,
                        'futures/private/stop-order/list': 5,
                        'futures/private/stop-order': 5,
                        'futures/private/position/list': 25,
                        'futures/private/execution/list': 25,
                        'futures/private/trade/closed-pnl/list': 1,
                        # spot
                        'spot/v1/account': 2.5,
                        'spot/v1/order': 2.5,
                        'spot/v1/open-orders': 2.5,
                        'spot/v1/history-orders': 2.5,
                        'spot/v1/myTrades': 2.5,
                        'spot/v1/cross-margin/order': 10,
                        'spot/v1/cross-margin/accounts/balance': 10,
                        'spot/v1/cross-margin/loan-info': 10,
                        'spot/v1/cross-margin/repay/history': 10,
                        # account
                        'asset/v1/private/transfer/list': 50,  # 60 per minute = 1 per second => cost = 50 / 1 = 50
                        'asset/v1/private/sub-member/transfer/list': 50,
                        'asset/v1/private/sub-member/member-ids': 50,
                        'asset/v1/private/deposit/record/query': 50,
                        'asset/v1/private/withdraw/record/query': 25,
                        'asset/v1/private/coin-info/query': 25,
                        'asset/v1/private/asset-info/query': 50,
                        'asset/v1/private/deposit/address': 100,
                        'asset/v1/private/universal/transfer/list': 50,
                        'contract/v3/private/copytrading/order/list': 1,
                        'contract/v3/private/copytrading/position/list': 1,
                        'contract/v3/private/copytrading/wallet/balance': 1,
                    },
                    'post': {
                        # inverse swap
                        'v2/private/order/create': 30,
                        'v2/private/order/cancel': 30,
                        'v2/private/order/cancelAll': 300,  # 100 per minute + 'consumes 10 requests'
                        'v2/private/order/replace': 30,
                        'v2/private/stop-order/create': 30,
                        'v2/private/stop-order/cancel': 30,
                        'v2/private/stop-order/cancelAll': 300,
                        'v2/private/stop-order/replace': 30,
                        'v2/private/position/change-position-margin': 40,
                        'v2/private/position/trading-stop': 40,
                        'v2/private/position/leverage/save': 40,
                        'v2/private/tpsl/switch-mode': 40,
                        'v2/private/position/switch-isolated': 2.5,
                        'v2/private/position/risk-limit': 2.5,
                        'v2/private/position/switch-mode': 2.5,
                        # linear swap USDT
                        'private/linear/order/create': 30,  # 100 per minute = 1.666 per second => cost = 50 / 1.6666 = 30
                        'private/linear/order/cancel': 30,
                        'private/linear/order/cancel-all': 300,  # 100 per minute + 'consumes 10 requests'
                        'private/linear/order/replace': 30,
                        'private/linear/stop-order/create': 30,
                        'private/linear/stop-order/cancel': 30,
                        'private/linear/stop-order/cancel-all': 300,
                        'private/linear/stop-order/replace': 30,
                        'private/linear/position/set-auto-add-margin': 40,
                        'private/linear/position/switch-isolated': 40,
                        'private/linear/position/switch-mode': 40,
                        'private/linear/tpsl/switch-mode': 2.5,
                        'private/linear/position/add-margin': 40,
                        'private/linear/position/set-leverage': 40,  # 75 per minute = 1.25 per second => cost = 50 / 1.25 = 40
                        'private/linear/position/trading-stop': 40,
                        'private/linear/position/set-risk': 2.5,
                        # inverse futures
                        'futures/private/order/create': 30,
                        'futures/private/order/cancel': 30,
                        'futures/private/order/cancelAll': 30,
                        'futures/private/order/replace': 30,
                        'futures/private/stop-order/create': 30,
                        'futures/private/stop-order/cancel': 30,
                        'futures/private/stop-order/cancelAll': 30,
                        'futures/private/stop-order/replace': 30,
                        'futures/private/position/change-position-margin': 40,
                        'futures/private/position/trading-stop': 40,
                        'futures/private/position/leverage/save': 40,
                        'futures/private/position/switch-mode': 40,
                        'futures/private/tpsl/switch-mode': 40,
                        'futures/private/position/switch-isolated': 40,
                        'futures/private/position/risk-limit': 2.5,
                        # spot
                        'spot/v1/order': 2.5,
                        'spot/v1/cross-margin/loan': 10,
                        'spot/v1/cross-margin/repay': 10,
                        # account
                        'asset/v1/private/transfer': 150,  # 20 per minute = 0.333 per second => cost = 50 / 0.3333 = 150
                        'asset/v1/private/sub-member/transfer': 150,
                        'asset/v1/private/withdraw': 50,
                        'asset/v1/private/withdraw/cancel': 50,
                        'asset/v1/private/transferable-subs/save': 3000,
                        'asset/v1/private/universal/transfer': 1500,
                        # USDC endpoints
                        # option USDC
                        'option/usdc/openapi/private/v1/place-order': 2.5,
                        'option/usdc/openapi/private/v1/batch-place-order': 2.5,
                        'option/usdc/openapi/private/v1/replace-order': 2.5,
                        'option/usdc/openapi/private/v1/batch-replace-orders': 2.5,
                        'option/usdc/openapi/private/v1/cancel-order': 2.5,
                        'option/usdc/openapi/private/v1/batch-cancel-orders': 2.5,
                        'option/usdc/openapi/private/v1/cancel-all': 2.5,
                        'option/usdc/openapi/private/v1/query-active-orders': 2.5,
                        'option/usdc/openapi/private/v1/query-order-history': 2.5,
                        'option/usdc/openapi/private/v1/execution-list': 2.5,
                        'option/usdc/openapi/private/v1/query-transaction-log': 2.5,
                        'option/usdc/openapi/private/v1/query-wallet-balance': 2.5,
                        'option/usdc/openapi/private/v1/query-asset-info': 2.5,
                        'option/usdc/openapi/private/v1/query-margin-info': 2.5,
                        'option/usdc/openapi/private/v1/query-position': 2.5,
                        'option/usdc/openapi/private/v1/query-delivery-list': 2.5,
                        'option/usdc/openapi/private/v1/query-position-exp-date': 2.5,
                        'option/usdc/openapi/private/v1/mmp-modify': 2.5,
                        'option/usdc/openapi/private/v1/mmp-reset': 2.5,
                        # perpetual swap USDC
                        'perpetual/usdc/openapi/private/v1/place-order': 2.5,
                        'perpetual/usdc/openapi/private/v1/replace-order': 2.5,
                        'perpetual/usdc/openapi/private/v1/cancel-order': 2.5,
                        'perpetual/usdc/openapi/private/v1/cancel-all': 2.5,
                        'perpetual/usdc/openapi/private/v1/position/leverage/save': 2.5,
                        'option/usdc/openapi/private/v1/session-settlement': 2.5,
                        'option/usdc/private/asset/account/setMarginMode': 2.5,
                        'perpetual/usdc/openapi/public/v1/risk-limit/list': 2.5,
                        'perpetual/usdc/openapi/private/v1/position/set-risk-limit': 2.5,
                        'perpetual/usdc/openapi/private/v1/predicted-funding': 2.5,
                        'contract/v3/private/copytrading/order/create': 2.5,
                        'contract/v3/private/copytrading/order/cancel': 2.5,
                        'contract/v3/private/copytrading/order/close': 2.5,
                        'contract/v3/private/copytrading/position/close': 2.5,
                        'contract/v3/private/copytrading/position/set-leverage': 2.5,
                        'contract/v3/private/copytrading/wallet/transfer': 2.5,
                    },
                    'delete': {
                        # spot
                        'spot/v1/order': 2.5,
                        'spot/v1/order/fast': 2.5,
                        'spot/order/batch-cancel': 2.5,
                        'spot/order/batch-fast-cancel': 2.5,
                        'spot/order/batch-cancel-by-ids': 2.5,
                    },
                },
            },
            'httpExceptions': {
                '403': RateLimitExceeded,  # Forbidden -- You request too many times
            },
            'exceptions': {
                # Uncodumented explanation of error strings:
                # - oc_diff: order cost needed to place self order
                # - new_oc: total order cost of open orders including the order you are trying to open
                # - ob: order balance - the total cost of current open orders
                # - ab: available balance
                'exact': {
                    '-10009': BadRequest,  # {"ret_code":-10009,"ret_msg":"Invalid period!","result":null,"token":null}
                    '-2013': InvalidOrder,  # {"ret_code":-2013,"ret_msg":"Order does not exist.","ext_code":null,"ext_info":null,"result":null}
                    '-2015': AuthenticationError,  # Invalid API-key, IP, or permissions for action.
                    '-1021': BadRequest,  # {"ret_code":-1021,"ret_msg":"Timestamp for self request is outside of the recvWindow.","ext_code":null,"ext_info":null,"result":null}
                    '-1004': BadRequest,  # {"ret_code":-1004,"ret_msg":"Missing required parameter \u0027symbol\u0027","ext_code":null,"ext_info":null,"result":null}
                    '7001': BadRequest,  # {"retCode":7001,"retMsg":"request params type error"}
                    '10001': BadRequest,  # parameter error
                    '10002': InvalidNonce,  # request expired, check your timestamp and recv_window
                    '10003': AuthenticationError,  # Invalid apikey
                    '10004': AuthenticationError,  # invalid sign
                    '10005': PermissionDenied,  # permission denied for current apikey
                    '10006': RateLimitExceeded,  # too many requests
                    '10007': AuthenticationError,  # api_key not found in your request parameters
                    '10010': PermissionDenied,  # request ip mismatch
                    '10016': ExchangeError,  # {"retCode":10016,"retMsg":"System error. Please try again later."}
                    '10017': BadRequest,  # request path not found or request method is invalid
                    '10018': RateLimitExceeded,  # exceed ip rate limit
                    '20001': OrderNotFound,  # Order not exists
                    '20003': InvalidOrder,  # missing parameter side
                    '20004': InvalidOrder,  # invalid parameter side
                    '20005': InvalidOrder,  # missing parameter symbol
                    '20006': InvalidOrder,  # invalid parameter symbol
                    '20007': InvalidOrder,  # missing parameter order_type
                    '20008': InvalidOrder,  # invalid parameter order_type
                    '20009': InvalidOrder,  # missing parameter qty
                    '20010': InvalidOrder,  # qty must be greater than 0
                    '20011': InvalidOrder,  # qty must be an integer
                    '20012': InvalidOrder,  # qty must be greater than zero and less than 1 million
                    '20013': InvalidOrder,  # missing parameter price
                    '20014': InvalidOrder,  # price must be greater than 0
                    '20015': InvalidOrder,  # missing parameter time_in_force
                    '20016': InvalidOrder,  # invalid value for parameter time_in_force
                    '20017': InvalidOrder,  # missing parameter order_id
                    '20018': InvalidOrder,  # invalid date format
                    '20019': InvalidOrder,  # missing parameter stop_px
                    '20020': InvalidOrder,  # missing parameter base_price
                    '20021': InvalidOrder,  # missing parameter stop_order_id
                    '20022': BadRequest,  # missing parameter leverage
                    '20023': BadRequest,  # leverage must be a number
                    '20031': BadRequest,  # leverage must be greater than zero
                    '20070': BadRequest,  # missing parameter margin
                    '20071': BadRequest,  # margin must be greater than zero
                    '20084': BadRequest,  # order_id or order_link_id is required
                    '30001': BadRequest,  # order_link_id is repeated
                    '30003': InvalidOrder,  # qty must be more than the minimum allowed
                    '30004': InvalidOrder,  # qty must be less than the maximum allowed
                    '30005': InvalidOrder,  # price exceeds maximum allowed
                    '30007': InvalidOrder,  # price exceeds minimum allowed
                    '30008': InvalidOrder,  # invalid order_type
                    '30009': ExchangeError,  # no position found
                    '30010': InsufficientFunds,  # insufficient wallet balance
                    '30011': PermissionDenied,  # operation not allowed as position is undergoing liquidation
                    '30012': PermissionDenied,  # operation not allowed as position is undergoing ADL
                    '30013': PermissionDenied,  # position is in liq or adl status
                    '30014': InvalidOrder,  # invalid closing order, qty should not greater than size
                    '30015': InvalidOrder,  # invalid closing order, side should be opposite
                    '30016': ExchangeError,  # TS and SL must be cancelled first while closing position
                    '30017': InvalidOrder,  # estimated fill price cannot be lower than current Buy liq_price
                    '30018': InvalidOrder,  # estimated fill price cannot be higher than current Sell liq_price
                    '30019': InvalidOrder,  # cannot attach TP/SL params for non-zero position when placing non-opening position order
                    '30020': InvalidOrder,  # position already has TP/SL params
                    '30021': InvalidOrder,  # cannot afford estimated position_margin
                    '30022': InvalidOrder,  # estimated buy liq_price cannot be higher than current mark_price
                    '30023': InvalidOrder,  # estimated sell liq_price cannot be lower than current mark_price
                    '30024': InvalidOrder,  # cannot set TP/SL/TS for zero-position
                    '30025': InvalidOrder,  # trigger price should bigger than 10% of last price
                    '30026': InvalidOrder,  # price too high
                    '30027': InvalidOrder,  # price set for Take profit should be higher than Last Traded Price
                    '30028': InvalidOrder,  # price set for Stop loss should be between Liquidation price and Last Traded Price
                    '30029': InvalidOrder,  # price set for Stop loss should be between Last Traded Price and Liquidation price
                    '30030': InvalidOrder,  # price set for Take profit should be lower than Last Traded Price
                    '30031': InsufficientFunds,  # insufficient available balance for order cost
                    '30032': InvalidOrder,  # order has been filled or cancelled
                    '30033': RateLimitExceeded,  # The number of stop orders exceeds maximum limit allowed
                    '30034': OrderNotFound,  # no order found
                    '30035': RateLimitExceeded,  # too fast to cancel
                    '30036': ExchangeError,  # the expected position value after order execution exceeds the current risk limit
                    '30037': InvalidOrder,  # order already cancelled
                    '30041': ExchangeError,  # no position found
                    '30042': InsufficientFunds,  # insufficient wallet balance
                    '30043': InvalidOrder,  # operation not allowed as position is undergoing liquidation
                    '30044': InvalidOrder,  # operation not allowed as position is undergoing AD
                    '30045': InvalidOrder,  # operation not allowed as position is not normal status
                    '30049': InsufficientFunds,  # insufficient available balance
                    '30050': ExchangeError,  # any adjustments made will trigger immediate liquidation
                    '30051': ExchangeError,  # due to risk limit, cannot adjust leverage
                    '30052': ExchangeError,  # leverage can not less than 1
                    '30054': ExchangeError,  # position margin is invalid
                    '30057': ExchangeError,  # requested quantity of contracts exceeds risk limit
                    '30063': ExchangeError,  # reduce-only rule not satisfied
                    '30067': InsufficientFunds,  # insufficient available balance
                    '30068': ExchangeError,  # exit value must be positive
                    '30074': InvalidOrder,  # can't create the stop order, because you expect the order will be triggered when the LastPrice(or IndexPrice、 MarkPrice, determined by trigger_by) is raising to stop_px, but the LastPrice(or IndexPrice、 MarkPrice) is already equal to or greater than stop_px, please adjust base_price or stop_px
                    '30075': InvalidOrder,  # can't create the stop order, because you expect the order will be triggered when the LastPrice(or IndexPrice、 MarkPrice, determined by trigger_by) is falling to stop_px, but the LastPrice(or IndexPrice、 MarkPrice) is already equal to or less than stop_px, please adjust base_price or stop_px
                    '30078': ExchangeError,  # {"ret_code":30078,"ret_msg":"","ext_code":"","ext_info":"","result":null,"time_now":"1644853040.916000","rate_limit_status":73,"rate_limit_reset_ms":1644853040912,"rate_limit":75}
                    # '30084': BadRequest,  # Isolated not modified, see handleErrors below
                    '33004': AuthenticationError,  # apikey already expired
                    '34026': ExchangeError,  # the limit is no change
                    '34036': BadRequest,  # {"ret_code":34036,"ret_msg":"leverage not modified","ext_code":"","ext_info":"","result":null,"time_now":"1652376449.258918","rate_limit_status":74,"rate_limit_reset_ms":1652376449255,"rate_limit":75}
                    '35015': BadRequest,  # {"ret_code":35015,"ret_msg":"Qty not in range","ext_code":"","ext_info":"","result":null,"time_now":"1652277215.821362","rate_limit_status":99,"rate_limit_reset_ms":1652277215819,"rate_limit":100}
                    '130006': InvalidOrder,  # {"ret_code":130006,"ret_msg":"The number of contracts exceeds maximum limit allowed: too large","ext_code":"","ext_info":"","result":null,"time_now":"1658397095.099030","rate_limit_status":99,"rate_limit_reset_ms":1658397095097,"rate_limit":100}
                    '130021': InsufficientFunds,  # {"ret_code":130021,"ret_msg":"orderfix price failed for CannotAffordOrderCost.","ext_code":"","ext_info":"","result":null,"time_now":"1644588250.204878","rate_limit_status":98,"rate_limit_reset_ms":1644588250200,"rate_limit":100} |  {"ret_code":130021,"ret_msg":"oc_diff[1707966351], new_oc[1707966351] with ob[....]+AB[....]","ext_code":"","ext_info":"","result":null,"time_now":"1658395300.872766","rate_limit_status":99,"rate_limit_reset_ms":1658395300855,"rate_limit":100} caused issues/9149#issuecomment-1146559498
                    '130074': InvalidOrder,  # {"ret_code":130074,"ret_msg":"expect Rising, but trigger_price[190000000] \u003c= current[211280000]??LastPrice","ext_code":"","ext_info":"","result":null,"time_now":"1655386638.067076","rate_limit_status":97,"rate_limit_reset_ms":1655386638065,"rate_limit":100}
                    '3100116': BadRequest,  # {"retCode":3100116,"retMsg":"Order quantity below the lower limit 0.01.","result":null,"retExtMap":{"key0":"0.01"}}
                    '3100198': BadRequest,  # {"retCode":3100198,"retMsg":"orderLinkId can not be empty.","result":null,"retExtMap":{}}
                    '3200300': InsufficientFunds,  # {"retCode":3200300,"retMsg":"Insufficient margin balance.","result":null,"retExtMap":{}}
                },
                'broad': {
                    'unknown orderInfo': OrderNotFound,  # {"ret_code":-1,"ret_msg":"unknown orderInfo","ext_code":"","ext_info":"","result":null,"time_now":"1584030414.005545","rate_limit_status":99,"rate_limit_reset_ms":1584030414003,"rate_limit":100}
                    'invalid api_key': AuthenticationError,  # {"ret_code":10003,"ret_msg":"invalid api_key","ext_code":"","ext_info":"","result":null,"time_now":"1599547085.415797"}
                    # the below two issues are caused as described: issues/9149#issuecomment-1146559498, when response is such:  {"ret_code":130021,"ret_msg":"oc_diff[1707966351], new_oc[1707966351] with ob[....]+AB[....]","ext_code":"","ext_info":"","result":null,"time_now":"1658395300.872766","rate_limit_status":99,"rate_limit_reset_ms":1658395300855,"rate_limit":100}
                    'oc_diff': InsufficientFunds,
                    'new_oc': InsufficientFunds,
                },
            },
            'precisionMode': TICK_SIZE,
            'options': {
                'createMarketBuyOrderRequiresPrice': True,
                'defaultType': 'swap',  # 'swap', 'future', 'option', 'spot'
                'defaultSubType': 'linear',  # 'linear', 'inverse'
                'defaultSettle': 'USDT',  # USDC for USDC settled markets
                'code': 'BTC',
                'recvWindow': 5 * 1000,  # 5 sec default
                'timeDifference': 0,  # the difference between system clock and exchange server clock
                'adjustForTimeDifference': False,  # controls the adjustment logic upon instantiation
                'brokerId': 'CCXT',
                'accountsByType': {
                    'spot': 'SPOT',
                    'margin': 'SPOT',
                    'future': 'CONTRACT',
                    'swap': 'CONTRACT',
                    'option': 'OPTION',
                },
                'accountsById': {
                    'SPOT': 'spot',
                    'MARGIN': 'spot',
                    'CONTRACT': 'contract',
                    'OPTION': 'option',
                },
            },
            'fees': {
                'trading': {
                    'feeSide': 'get',
                    'tierBased': True,
                    'percentage': True,
                    'taker': 0.00075,
                    'maker': 0.0001,
                },
                'funding': {
                    'tierBased': False,
                    'percentage': False,
                    'withdraw': {},
                    'deposit': {},
                },
            },
        })
