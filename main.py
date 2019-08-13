import numpy as np
import pandas as pd
import json
import urllib
import urllib.request as requests
from tkinter import ttk
import tkinter as tk
from matplotlib import style
import matplotlib.animation as animation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib
from datetime import datetime
from matplotlib import pyplot as plt

matplotlib.use("TkAgg")
LARGE_FONT = ("Verdanda", 12)
NORM_FONT = ("Verdanda", 10)
SMALL_FONT = ("Verdanda", 8)
style.use("ggplot")

f = Figure()
a = f.add_subplot(111)

exchange = "Bitbay"
DatCounter = 9000
programName = "btce"
resampleSize = "15Min"
DataPace = "1d"
candleWidth = 0.008
topIndicator = "none"
bottomIndicator = "none"
middleIndicator = "none"
EMAs = []
SMAs = []


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
    dataLink = "https://api.bitbay.net/rest/trading/transactions/ETH-USD?limit=300"
    data = urllib.request.urlopen(dataLink)
    datastr = data.read().decode("utf-8")
    data = json.loads(datastr)
    data = data["items"]
    print("Ticker data \n")
    print(data)

    data = pd.DataFrame(data)
    print('\n\n')
    print(data)

    buys = data[(data['ty'] == "Buy")]

    timestamps = []
    for date in buys['t']:
        timestamps.append(np.float64(date[:-3]))

    buys["datestamp"] = np.asarray(timestamps).astype('datetime64[s]')

    buyDates = (buys["datestamp"]).tolist()
    print('\nBuy Data\n')
    print(buys)
    print(buyDates)
    print("\n\n")
    # datetimes = np.asarray(datetimes, dtype='datetime64[m]')
    # buys["datestamp"] = np.asarray(datetimes).astype('datetime64[m]')
    # buys["datestamp"] = np.array()
    # buyDates = (buys["datestamp"]).tolist()
    # print(buyDates)

    sells = data[(data['ty'] == "Sell")]

    timeStampsSell = []
    for date in sells['t']:
        timeStampsSell.append(np.float64(date[:-3]))

    sells["datestamp"] = np.asarray(timeStampsSell).astype('datetime64[s]')

    sellDates = (sells["datestamp"]).tolist()
    print(sells)
    print(sellDates)
    print("\n")

    a.clear()
    a.plot_date(buyDates, buys["r"], "#00A3E0", label="buys")
    a.plot_date(sellDates, sells["r"], "#183A54", label="sells")
    a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2, borderaxespad=0)
    title = "BITBAY ETH-USD Prices\nLast Price: "+str(data["r"][299])
    a.set_title(title)


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
                                   command=lambda: changeExchange("ETH","ETH-USD"))
        exchangeChoice.add_command(label="Kraken",
                                   command= lambda: changeExchange("ETH", "ETH-USD"))
        exchangeChoice.add_command(label="Coinbase",
                                   command=lambda: changeExchange("ETH","ETH-USD"))
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
ani = animation.FuncAnimation(f, animate, interval=5000)
app.mainloop()
