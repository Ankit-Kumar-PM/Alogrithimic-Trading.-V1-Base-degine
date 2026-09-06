import yfinance as yf
import numpy as np
import pandas as pd

# <<=============== DEMO ALGORITHIC TRADING PYTHON CODE =========================>>

print("\n<=--- WELCOME TO THE ALGORITHMIC TRADING SIMULATION ---=>")
print("YOU CAN BUY AND SELL STOCKS USING THIS ALGORITHMIC SIMULATION\n")

while True:
    try:
        cash = int(input("PLEASE ENTER THE AMOUNT OF MONEY YOU WANT TO TRADE WITH ($) ==> "))
        if cash <= 0:
            print("Please enter an amount greater than 0.")
            continue
        break
    except ValueError:
        print("Invalid entry! Please enter a whole number (e.g., 5000, 10000).")
while True:
    print("\nWHICH ASSET WOULD YOU LIKE TO TRADE?")
    print("1) Apple (AAPL)")
    print("2) Bitcoin (BTC-USD)")
    print("3) Microsoft (MSFT)")
    print("4) Amazon (AMZN)")
    print("5) NVIDIA (NVDA)")
    print("6) Tesla (TSLA)")
    print("7) Ethereum (ETH-USD)")
    print("8) Gold (GC=F)")
    print("9) S&P 500 ETF (SPY)")
    print("10) Exit\n")
    a=input("YOUR CHOICE ===> ")
    Stock_choice=a.lower().strip()
    match Stock_choice:
       case '1' | 'apple' :
        sts = 'AAPL'
        break
       case '2' | 'bitcoin' | 'btc':
        sts = 'BTC-USD'
        break
       case '3' | 'microsoft' | 'msft':
        sts = 'MSFT'
        break
       case '4' | 'amazon' | 'amzn':
        sts = 'AMZN'
        break
       case '5' | 'nvidia' | 'nvda':
        sts = 'NVDA'
        break
       case '6' | 'tesla' | 'tsla':
        sts = 'TSLA'
        break
       case '7' | 'ethereum' | 'eth':
        sts = 'ETH-USD'
        break
       case '8' | 'gold':
        sts = 'GC=F'
        break
       case '9' | 's&p 500' | 'spy':
        sts = 'SPY'
        break
       case '10' | 'exit':
        print("Exiting program...")
        exit()
       case _:
        print("Invalid choice!")

class protfolio:
    def __init__(self,cash):
        self.cash=cash
        self.shares=0
        self.history=[]

    def buy_shared(self,cp):
        if self.cash<cp:
            print("<---- INSUFFICENT FUNDS ----> ")
            return
        share_buy=self.cash//cp
        total_money_req=share_buy*cp
        self.shares+=share_buy
        self.cash-=total_money_req

        trade_record = {
    'action': 'BUY',
    'price': cp,
    'shares': share_buy,
    'total_cost': total_money_req,
    'remaining_cash': self.cash
}
        self.history.append(trade_record)
        print('sussesfuly buy')

    def sell_share(self,cp):
        if self.shares==0 :
            print("YOU DO NOT OWN ANY SHARES")
            return
        revenue=self.shares*cp
        self.cash+=revenue
        shares_sold=self.shares
        self.shares=0

        trade_record = {
    'action': 'SELL',
    'price': cp,
    'shares': shares_sold,
    'cash_gained': revenue,
    'remaining_cash': self.cash
                            }
        self.history.append(trade_record)
    print('sussesfuly sell')
   
    def show(self):
        a=self.history
        print(a)

# <<<============import_data==============>>>
Stock=yf.Ticker(sts)
df = Stock.history(period="60d")

# <<<============Data_Cleaning==============>>>

df.sort_index(ascending=False)
df.drop(columns=['Open','High','Low','Dividends','Stock Splits'],inplace=True)
df['5_day_SMA']=df['Close'].rolling(window=5).mean()
df.dropna(inplace=True)

# <<<============Condition (BUY\\SELL)==============>>>

df['Signal']=np.where(df['Close']<df['5_day_SMA'],'BUY','SELL')


ankit = protfolio(cash)

# <<============conditon chekcer ===============>
for index, row in df.iterrows():
    cp = row['Close']  
    
    if row['Signal'] == 'BUY' and ankit.shares == 0:  
        ankit.buy_shared(cp) 
    elif row['Signal'] == 'SELL' and ankit.shares > 0: 
        ankit.sell_share(cp)

if ankit.shares > 0:
    last_price = df.iloc[-1]['Close']
    ankit.sell_share(last_price)

print("\n" + "===+++==="*5 + " FINAL RESULTS " + "===+++==="*5)


trade_report = pd.DataFrame(ankit.history)
trade_report.round()
trade_report.fillna(0,inplace=True)
columns_to_convert = ['price', 'shares', 'total_cost', 'remaining_cash', 'cash_gained']
trade_report[columns_to_convert] = trade_report[columns_to_convert].astype(int)
print(trade_report)

trade_report.to_csv('my_trading_log.csv', index=False)
print("\nYour trading log has been successfully saved to 'my_trading_log.csv'!")

                                                                                                             
                                                                                                             