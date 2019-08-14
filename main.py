import json
import tkinter as tk
import urllib
import urllib.request as requests
from datetime import datetime
from tkinter import ttk

import matplotlib
import matplotlib.animation as animation
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
#from matplotlib.figure import Figure

matplotlib.use("TkAgg")
LARGE_FONT = ("Verdanda", 12)
NORM_FONT = ("Verdanda", 10)
SMALL_FONT = ("Verdanda", 8)
style.use("ggplot")

f = plt.figure()
#a = f.add_subplot(111)
paneCount = 1
exchange = "bitbay"
DatCounter = 9000
programName = "btce"
resampleSize = "15Min"
DataPace = "tick"
candleWidth = 0.008
topIndicator = "none"
bottomIndicator = "none"
middleIndicator = "none"
chartLoad = True

darkColor = "#183A54"
lightColor = "#00A3E0"

EMAs = []
SMAs = []

def tutorial():
    #def leavemini(what):
        # what.destroy()
    def page2():
        tut.destroy()
        tut2 = tk.Tk()
        def page3():
            tut2.destroy()
            tut3 = tk.Tk()
            tut3.wm_title("Part 3!")
            label = ttk.Label(tut3, text="Part 3", font=NORM_FONT)
            label.pack(side="top", fill="x", pady=10)
            B1 = ttk.Button(tut3, text="Done!", command= tut3.destroy)
            B1.pack()
            tut3.mainloop()
        tut2.wm_title("Part 2!")
        label = ttk.Label(tut2, text="Part 2", font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(tut2, text="Next!", command= page3)
        B1.pack()
        tut2.mainloop()
    tut = tk.Tk()
    tut.wm_title("Tutorial")
    label = ttk.Label(tut, text="What do you need help with?", font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(tut, text="Overview of the application", command=page2)
    B1.pack()
    B2 = ttk.Button(tut, text="How do I trade with this client?", command=lambda: popupmsg("Not yet Completed"))
    B2.pack()
    B3 = ttk.Button(tut, text="Indicator Questions/Help", command=lambda: popupmsg("Not yet completed "))
    B3.pack()
    
    tut.mainloop()



    
def loadChart(run):
    global chartLoad

    if run == "start":
        chartLoad = True
    elif run == "stop":
        chartload = False

def addMiddleIndicator(what):
    global middleIndicator
    global DatCounter
    if DataPace == "tick":
        popupmsg("Indicators in Tick Data not available")
    
    if what != "none":
        if middleIndicator == "none":
            if what == "sma":
                midIQ = tk.Tk()
                midIQ.wm_title("Periods?")
                label = ttk.Label(midIQ, text="Choose how many periods how many you want your sma to be")
                label.pack(side="top", fill="x", pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0, 10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global DatCounter

                    middleIndicator = []
                    periods = (e.get())
                    group = []
                    group.append("sma")
                    group.append(int(periods))
                    middleIndicator.append(group)
                    DatCounter = 9000
                    print("middle Indicator set to: ", middleIndicator)
                    midIQ.destroy()
                b = ttk.Button(midIQ, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop()


            if what == "ema":
                midIQ = tk.Tk()
                midIQ.wm_title("Periods?")
                label = ttk.Label(midIQ, text="Choose how many periods how many you want your sma to be")
                label.pack(side="top", fill="x", pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0, 10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global DatCounter

                    middleIndicator = []
                    periods = (e.get())
                    group = []
                    group.append("ema")
                    group.append(int(periods))
                    middleIndicator.append(group)
                    DatCounter = 9000
                    print("middle Indicator set to: ", middleIndicator)
                    midIQ.destroy()
                b = ttk.Button(midIQ, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop()
        else:
            if what == "sma":
                midIQ = tk.Tk()
                midIQ.wm_title("Periods?")
                label = ttk.Label(midIQ, text="Choose how many periods how many you want your sma to be")
                label.pack(side="top", fill="x", pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0, 10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global DatCounter

                    #middleIndicator = []
                    periods = (e.get())
                    group = []
                    group.append("sma")
                    group.append(int(periods))
                    middleIndicator.append(group)
                    DatCounter = 9000
                    print("middle Indicator set to: ", middleIndicator)
                    midIQ.destroy()
                b = ttk.Button(midIQ, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop()


            if what == "ema":
                midIQ = tk.Tk()
                midIQ.wm_title("Periods?")
                label = ttk.Label(midIQ, text="Choose how many periods how many you want your sma to be")
                label.pack(side="top", fill="x", pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0, 10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global DatCounter

                    #middleIndicator = []
                    periods = (e.get())
                    group = []
                    group.append("ema")
                    group.append(int(periods))
                    middleIndicator.append(group)
                    DatCounter = 9000
                    print("middle Indicator set to: ", middleIndicator)
                    midIQ.destroy()
                b = ttk.Button(midIQ, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop()
    else:
        addMiddleIndicator = None




def addTopIndicator(what):
    global topIndicator
    global DatCounter

    if DataPace == "tick":
        popupmsg("Indicators in Tick Data not available")
    elif what == "none":
        topIndicator = what
        DatCounter = 9000
    elif what == "rsi":
        rsiQ = tk.Tk()
        rsiQ.wm_title("Periods?")
        label = ttk.Label(rsiQ, text="Choose how many periods you want each RSI calculation to consider.")
        label.pack(side="top", fill="x", pady=10)

        e = ttk.Entry(rsiQ)
        e.insert(0, 14)
        e.pack()
        e.focus_set()

        def callback():
            global topIndicator
            global DatCounter

            periods = (e.get())
            group = []
            group.append("rsi")
            group.append(periods)
            
            topIndicator = group
            DatCounter = 9000
            print("Set top Indicator to", group)
            rsiQ.destroy()
        b = ttk.Button(rsiQ, text="Submit", width=10, command=callback)
        b.pack()
        tk.mainloop()
    elif what == "macd":
        # global topIndicator
        # global DatCounter
        topIndicator = "macd"
        DatCounter = 9000

def addBottomIndicator(what):
    global bottomIndicator
    global DatCounter

    if DataPace == "tick":
        popupmsg("Indicators in Tick Data not available")
    elif what == "none":
        bottomIndicator = what
        DatCounter = 9000
    elif what == "rsi":
        rsiQ = tk.Tk()
        rsiQ.wm_title("Periods?")
        label = ttk.Label(rsiQ, text="Choose how many periods you want each RSI calculation to consider.")
        label.pack(side="top", fill="x", pady=10)

        e = ttk.Entry(rsiQ)
        e.insert(0, 14)
        e.pack()
        e.focus_set()

        def callback():
            global bottomIndicator
            global DatCounter

            periods = (e.get())
            group = []
            group.append("rsi")
            group.append(periods)
            
            bottomIndicator = group
            DatCounter = 9000
            print("Set bottom Indicator to", group)
            rsiQ.destroy()
        b = ttk.Button(rsiQ, text="Submit", width=10, command=callback)
        b.pack()
        tk.mainloop()
    elif what == "macd":
        # global topIndicator
        # global DatCounter
        bottomIndicator = "macd"
        DatCounter = 9000

def changeTimeFrame(tf):
    global DataPace
    global DatCounter
    if tf == "7d" and resampleSize == "1Min":
        popupmsg("Too muhc data chosen, choose a smaller time frame or higher OHLC sample size")
    else:
        DataPace = tf
        DatCounter = 9000

def changeSampleSize(size, width):
    global resampleSize
    global DatCounter
    global candleWidth
    if DataPace == "7d" and resampleSize == "1Min":
        popupmsg("Too muhc data chosen, choose a smaller time frame or higher OHLC sample size")
    if DataPace == "tick": 
        popupmsg("Your currently viewing tick data, not OHLC.")
    else:
        resampleSize = size
        DatCounter = 9000
        candleWidth = width

    

def changeExchange(towhat, pn):
    global exchange
    global DatCounter
    global programName

    exchange = towhat
    programName = pn
    DatCounter = 9000

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command=popup.destory())
    B1.pack()
    popup.mainloop()


def animate(i):
    global refreshRate
    global DatCounter

    if chartLoad: 
        if paneCount ==1:
            if DataPace == "tick":
                try:
                    
                    if exchange == "bitbay":
                        a = plt.subplot2grid((6,4), (0,0), rowspan= 5, colspan= 4)
                        a2 = plt.subplot2grid((6,4), (5,0), rowspan=1, colspan=4, sharex= a)

                        dataLink = "https://api.bitbay.net/rest/trading/transactions/ETH-USD?limit=300"
                        data = urllib.request.urlopen(dataLink)
                        datastr = data.read().decode("utf-8")
                        data = json.loads(datastr)
                        data = data["items"]
                        print("Ticker data  Bitbay \n")
                        data = pd.DataFrame(data)
                        print('\n\n')
                        print(data)

                    
                        timestamps = []
                        for date in data['t']:
                            timestamps.append(np.float64(date[:-3]))
                        data["dateStamp"] = np.asarray(timestamps).astype('datetime64[s]')
                        print('\n\n','Data', data, '\n\n')
                        buys = data[(data['ty'] == "Buy")]
                        allDates = data["dateStamp"].tolist()

                        #buys["datestamp"] = np.asarray(timestamps).astype('datetime64[s]')
                        buyDates = (buys["dateStamp"]).tolist()
                        print('\nBuy Data\n')
                        print(buys)
                        print("\n\n")
                        # datetimes = np.asarray(datetimes, dtype='datetime64[m]')
                        # buys["datestamp"] = np.asarray(datetimes).astype('datetime64[m]')
                        # buys["datestamp"] = np.array()
                        # buyDates = (buys["datestamp"]).tolist()
                        # print(buyDates)

                        
                        #timeStampsSell = []
                        #for date in sells['t']:
                            #timeStampsSell.append(np.float64(date[:-3]))
                        #sells["datestamp"] = np.asarray(timeStampsSell).astype('datetime64[s]')
                        #sellDates = (sells["datestamp"]).tolist()
                        sells = data[(data['ty'] == "Sell")]
                        sellDates =  (sells["dateStamp"]).tolist()
                        print("\nSell Data\n")
                        print(sells)
                        print("\n")
                        
                        volume = data["a"]
                        a.clear()
                        a.plot_date(buyDates, buys["r"], lightColor, label="buys")
                        a.plot_date(sellDates, sells["r"], darkColor, label="sells")
                        a2.fill_between(allDates, 0, volume, facecolor= darkColor)
                        a.xaxis.set_major_locator(mticker.MaxNLocator(5))
                        a.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H-%M-%S"))
                        plt.setp(a.get_xticklabels(), visible=False)
                        a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2, borderaxespad=0)
                        title = "BITBAY ETH-USD Prices\nLast Price: "+str(data["r"][299])
                        a.set_title(title)
                        print('\nGraph Loaded!!!!\n')


                    if exchange == "kraken":
                        a = plt.subplot2grid((6,4), (0,0), rowspan= 5, colspan= 4)
                        a2 = plt.subplot2grid((6,4), (5,0), rowspan=1, colspan=4, sharex= a)

                        dataLink = "https://api.kraken.com/0/public/Trades?pair=ETHUSD"
                        data = urllib.request.urlopen(dataLink)
                        datastr = data.read().decode("utf-8")
                        data = json.loads(datastr)
                        data = data["result"]
                        data = data["XETHZUSD"]
                        print("Ticker data for Kraken \n")
                        data = pd.DataFrame(data ,columns=["price", "volume","timestamp","buy/sell", "market/limit", 'other'])
                        data = data[(data['market/limit'] == 'm')]
                        print('\n\n', 'Printing Cleaned Data:\n')
                        print(data)
                        timestamps = []
                        for date in data['timestamp']:
                            timestamps.append(np.float64(date))
                        data['dateStamp'] = np.array(timestamps).astype('datetime64[s]')
                        print('\nConverted Unix Timestamps to Datetime', data['dateStamp'])
                        buys = data[(data['buy/sell'] == 'b')]
                        #buys["dateStamp"] = np.asarray(timestamps).astype('datetime64[s]')
                        print('\n\n','Data', data, '\n\n')
                        buys = buys.sort_values('dateStamp')
                        buyDates = buys["dateStamp"].tolist()
                        print('\nBuy Data\n')
                        print(buys)
                        print("\n\n")
                        
                        
                        sells = data[(data['buy/sell']=='s')]
                        # timestamps = []
                        # for date in sells['timestamp']:
                        #     timestamps.append(np.float64(date[:-3]))
                        # sells['dateStamp'] = np.array(timestamps).astype('datetime64[s]')
                        sells = sells.sort_values('dateStamp')
                        sellDates =  sells["dateStamp"].tolist()
                        print("\nSell Data\n")
                        print(sells)
                        print("\n")
                            
                       
                        data = data.sort_values('dateStamp')

                        print('\n', data['dateStamp'], '\n')
                        allDates = buys['dateStamp'].tolist()
                        
                        volume = buys["volume"].tolist()
                        print('\n\n', 'Fresh Data\n', data, '\n\n')
                        print('Sell Data\n' ,sells)
                        print('\nBuy Data\n', buys)
                        a.clear()
                        a.plot_date(buyDates, buys["price"], lightColor, label="buys")
                        a.plot_date(sellDates, sells["price"], darkColor, label="sells")
                        a2.fill_between(allDates, 0, volume, facecolor= darkColor)
                        a.xaxis.set_major_locator(mticker.MaxNLocator(5))
                        a.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H-%M-%S"))
                        plt.setp(a.get_xticklabels(), visible=False)
                        a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2, borderaxespad=0)
                      
                        title = "BITBAY ETH-USD Prices\nLast Price: "+str(buys['price'].iloc[-1])
                        a.set_title(title)
                        print('\nGraph Loaded!!!!\n')


                    if exchange == "bitfinex":
                        a = plt.subplot2grid((6,4), (0,0), rowspan= 5, colspan= 4)
                        a2 = plt.subplot2grid((6,4), (5,0), rowspan=1, colspan=4, sharex= a)

                        dataLink = "https://api.bitfinex.com/v1/trades/btcusd?limit=2000"
                        data = urllib.request.urlopen(dataLink)
                        datastr = data.read().decode("utf-8")
                        data = json.loads(datastr)
                        print("Ticker data for bitfinex \n")
                        data = pd.DataFrame(data)
                        print('\n\n', 'Printing Cleaned Data:\n')
                        print(data)
                        timestamps = []
                        for date in data['timestamp']:
                            timestamps.append(np.float64(date))
                        data['dateStamp'] = np.array(timestamps).astype('datetime64[s]')
                        print('\nConverted Unix Timestamps to Datetime', data['dateStamp'])
                        buys = data[(data['type'] == 'buy')]
                        #buys["dateStamp"] = np.asarray(timestamps).astype('datetime64[s]')
                        print('\n\n','Data', data, '\n\n')
                        buys = buys.sort_values('dateStamp')
                        buyDates = buys["dateStamp"].tolist()
                        print('\nBuy Data\n')
                        print(buys)
                        print("\n\n")
                        
                        
                        sells = data[(data['type']=='sell')]
                        # timestamps = []
                        # for date in sells['timestamp']:
                        #     timestamps.append(np.float64(date[:-3]))
                        # sells['dateStamp'] = np.array(timestamps).astype('datetime64[s]')
                        sells = sells.sort_values('dateStamp')
                        sellDates =  sells["dateStamp"].tolist()
                        print("\nSell Data\n")
                        print(sells)
                        print("\n")
                            
                       
                        data = data.sort_values('dateStamp')

                        print('\n', data['dateStamp'], '\n')
                        allDates = buys['dateStamp'].tolist()
                        
                        volume = buys["amount"].apply(float).tolist()
                        print('\n\n', 'Fresh Data\n', data, '\n\n')
                        print('Sell Data\n' ,sells)
                        print('\nBuy Data\n', buys)
                        a.clear()
                        a.plot_date(buyDates, buys["price"], lightColor, label="buys")
                        a.plot_date(sellDates, sells["price"], darkColor, label="sells")
                        a2.fill_between(allDates, 0, volume, facecolor= darkColor)
                        a.xaxis.set_major_locator(mticker.MaxNLocator(5))
                        a.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H-%M-%S"))
                        plt.setp(a.get_xticklabels(), visible=False)
                        a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2, borderaxespad=0)
                      
                        title = "Bitfinex ETH-USD Prices\nLast Price: "+str(buys['price'].iloc[-1])
                        a.set_title(title)
                        print('\nGraph Loaded!!!!\n')
                except Exception as e:
                    print(e)
                # else:
                #     if DatCounter > 12:
                #         try:
                #             if exchange =='Huboi':
                #                 if topIndicator != "none":
                #                     a = plt.subplot2grid((6,4),(1,0), rowspan=5, colspan=4)
                #                     a2 = plt.subplot2grind((6,4), (0,0), sharex=a, rowspan=1, colspan=4)
                #                 else:
                #                     a = plt.subplot2grid((6,4), (0,0), rowspan=6, colspan=4)
                #             else:
                #                 if topIndicator != "none" and bottomIndicator != "none":
                #                     #Main Graph
                #                     a = plt.subplot2grid((6,4), (1,0), sharex= a,rowspan=3, colspan=4)
                #                     #Volume
                #                     a2 = plt.subplot2grid((6,4), (4,0), sharex= a,rowspan=1, colspan=4)
                #                     # Bottom Indicator
                #                     a3 = plt.subplot2grid((6,4), (5,0), sharex= a,rowspan=1, colspan=4)

                #                     # top Indicator
                #                     a0 = plt.subplot2grid((6,4), (0,0), sharex= a, rowspan=4, colspan=4)
                #                 elif topIndicator != "none":
                #                     #Main Graph
                #                     a = plt.subplot2grid((6,4), (1,0), sharex= a,rowspan=1, colspan=4)
                #                     #Volume
                #                     a2 = plt.subplot2grid((6,4), (5,0), sharex= a,rowspan=1, colspan=4)
                #                     # Top Indicator
                #                     a0 = plt.subplot2grid((6,4), (0,0), sharex= a, rowspan=1, colspan=4)
                #                 elif bottomIndicator !="none":
                #                     #Main Graph
                #                     a = plt.subplot2grid((6,4), (0,0), sharex= a,rowspan=4, colspan=4)
                #                     #Volume
                #                     a2 = plt.subplot2grid((6,4), (4,0), sharex= a,rowspan=1, colspan=4)
                #                     # Top Indicator
                #                     a3 = plt.subplot2grid((6,4), (5,0), sharex= a,rowspan=1, colspan=4)
                #                 else:
                #                     #Main Graph
                #                     a = plt.subplot2grid((6,4), (0,0), sharex= a,rowspan=5, colspan=4)
                #                     #Volume
                #                     a2 = plt.subplot2grid((6,4), (5,0), sharex= a,rowspan=1, colspan=4)
                            
                #             data = urllib.request.urlopen("http://seaofbtc.com/api/basic/price?key=1&tf="+DataPace+"&exchange="+programName).read()
                #             data =  data.decode()
                #             data = json.loads(data)
                #             dateStamp = np.array(data[0]).astype("datetime64[s]")
                #             dateStamp = dateStamp.tolist()

                #             df = pd.DataFrame({'Datetime':dateStamp})
                #             df['Price'] = data[1]
                #             df['Volume'] = data[2]
                #             df['Symbol'] = 'BTCUSD'
                #             df['MPLDate'] = df['Datetime'].apply(lambda date: mdates.date2num(date.to_pydatetime()))
                #             df = df.set_index("Datetime")


                        # except Exception as e:
                        #     print('failed in the non tick animate:', str(e))

class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.title(self, "TrewCyptoGraph")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(
            label="Save settings", command=lambda: popupmsg("Not supported just yet!"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)

        exchangeChoice = tk.Menu(menubar, tearoff=1)
        exchangeChoice.add_command(label="Bitbay",
                                   command=lambda: changeExchange("bitbay","ETH-USD"))
        exchangeChoice.add_command(label="Kraken",
                                   command= lambda: changeExchange("kraken", "ETH-USD"))
        exchangeChoice.add_command(label="Bitfinex",
                                   command=lambda: changeExchange("bitfinex","ETH-USD"))
        menubar.add_cascade(label="Exchange", menu=exchangeChoice)

        dataTF = tk.Menu(menubar, tearoff=1)
        dataTF.add_command(label="Tick", 
                           command= lambda: changeTimeFrame('tick'))
        dataTF.add_command(label="1 Day", 
                    command= lambda: changeTimeFrame('1d'))
        dataTF.add_command(label="3 Day ", 
                    command= lambda: changeTimeFrame('3d'))
        dataTF.add_command(label="1 Week ", 
            command= lambda: changeTimeFrame('7d'))
        menubar.add_cascade(label="Data Time Frame", menu=dataTF)

        OHLCI = tk.Menu(menubar, tearoff=1)
        OHLCI.add_command(label="Tick", 
                        command= lambda: changeTimeFrame('tick'))
        OHLCI.add_command(label="1 minute", 
                        command= lambda: changeSampleSize('1Min', 0.005))
        OHLCI.add_command(label="5 minute", 
                        command= lambda: changeSampleSize('5Min', 0.003))
        OHLCI.add_command(label="15 minute", 
                        command= lambda: changeSampleSize('15Min', 0.008))
        OHLCI.add_command(label="30 minute", 
                        command= lambda: changeSampleSize('30Min', 0.016))
        OHLCI.add_command(label="1 Hour", 
                        command= lambda: changeSampleSize('1H', 0.032))
        OHLCI.add_command(label="3 Hour", 
                        command= lambda: changeSampleSize('3H', 0.096))

        menubar.add_cascade(label="OHLC Interval", menu=OHLCI)

        topIndi = tk.Menu(menubar, tearoff=1)
        topIndi.add_command(label="None",
        command = lambda: addTopIndicator('none'))
        topIndi.add_command(label="RSI",
        command = lambda: addTopIndicator('rsi'))
        topIndi.add_command(label="MACD",
        command = lambda: addTopIndicator('macd'))
        menubar.add_cascade(label="Top Indicator", menu=topIndi)



        mainIndi = tk.Menu(menubar, tearoff=1)
        mainIndi.add_command(label="None",
        command = lambda: addMiddleIndicator('none'))
        mainIndi.add_command(label="SMA",
        command = lambda: addMiddleIndicator('sma'))
        mainIndi.add_command(label="EMA",
        command = lambda: addMiddleIndicator('ema'))
        menubar.add_cascade(label="Main/middle Indicator", menu=mainIndi)


        bottomIndi = tk.Menu(menubar, tearoff=1)
        bottomIndi.add_command(label="None",
        command = lambda: addBottomIndicator('none'))
        bottomIndi.add_command(label="RSI",
        command = lambda: addBottomIndicator('rsi'))
        bottomIndi.add_command(label="MACD",
        command = lambda: addBottomIndicator('macd'))
        menubar.add_cascade(label="Bottom Indicator", menu=bottomIndi)
        
        
        tradeButton = tk.Menu(menubar, tearoff=1)
        tradeButton.add_command(label="Manual Trading", 
        command= lambda: popupmsg("This is not live yet"))

        tradeButton.add_command(label="Automated Trading", command= lambda: popupmsg("This is not live yet"))

        tradeButton.add_separator()
        tradeButton.add_command(label="Quick Buy", 
        command= lambda: popupmsg("This is not live yet"))

        tradeButton.add_command(label="Quick Sell", command= lambda: popupmsg("This is not live yet"))


        tradeButton.add_separator()
        tradeButton.add_command(label="Setup Quick Buy/Sell", command=lambda: popupmsg("This is not live  yet"))

        menubar.add_cascade(label="Trading", menu=tradeButton)

        startStop = tk.Menu(menubar, tearoff=1)
        startStop.add_command(label="Resume", command= lambda: loadChart('start'))
        startStop.add_command(label="Pause", command= lambda: loadChart('stop'))
        menubar.add_cascade(label="Resume/Pause Client", menu =startStop)

        helpMenu = tk.Menu(menubar, tearoff=0)
        helpMenu.add_command(label="Tutorial", command=tutorial)
        menubar.add_cascade(label="Help", menu=helpMenu)













        tk.Tk.config(self, menu=menubar)

        self.frames = {}

        for F in (StartPage, BTC_Page):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(
            self,
            text="""ALPHA Bitcoin Trading Application use at your own risk. There is no promise of warranty""",
            font=LARGE_FONT,
        )
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(
            self, text="Agree", command=lambda: controller.show_frame(BTC_Page)
        )
        button1.pack()

        button2 = ttk.Button(self, text="Disagree", command=quit)
        button2.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page one", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(
            self, text="Back to Home", command=lambda: controller.show_frame(StartPage)
        )
        button1.pack()


class BTC_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page three", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = ttk.Button(
            self, text="Back to Home", command=lambda: controller.show_frame(StartPage)
        )
        button1.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


app = SeaofBTCapp()
app.geometry("1920x1080")
app.attributes('-fullscreen', True)
app.attributes('-topmost', True)
ani = animation.FuncAnimation(f, animate, interval=3000)
app.mainloop()
