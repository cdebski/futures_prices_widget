import tkinter as tk
from pandas_datareader import data as pdr


def pull_data(ticker):
    """pulls futures data from yahoo finance"""

    return pdr.DataReader(ticker.upper(), data_source='yahoo')


def price_change(data):
    """calculates daily change in futures price"""

    return (data / data.shift(1)) - 1


def format(float):
    """formats float as string that is a percentage 
    multiplied by 100 rounded to two decimals ('xx.yy')"""

    return str(round(float * 100, 2))


def futures_movement(ticker):
    """returns the movement of the provided futures 
    contract and names it given it's ticker"""

    data = pull_data(ticker)
    movement = format(price_change(data)['Adj Close']
                      .iloc[-1])

    if ticker == 'ES=F':
        symbol = '$SPX'
    elif ticker == 'YM=F':
        symbol = '$DOW'
    elif ticker == 'NQ=F':
        symbol = '$IXIC'
    elif ticker == 'CL=F':
        symbol = 'Crude'
    elif ticker == 'GC=F':
        symbol = 'Gold'
    else:
        symbol = '10-Year'

    movement = f'{symbol}: {movement}%'
    return movement


def color_scheme(ticker):
    """assigns a color to the movement of each futures
    contract"""

    data = pull_data(ticker)
    movement = price_change(data)['Adj Close'].iloc[-1]

    if movement > 0:
        color = 'green'
        return color
    elif movement == 0:
        color = 'black'
        return color
    else:
        color = 'red'
        return color


# pulls futures contract data, calculates daily change
# returns change as a %, and assigns it a color based on movement
spx_movement = futures_movement('ES=F')
spx_color = color_scheme('ES=F')

dow_movement = futures_movement('YM=F')
dow_color = color_scheme('YM=F')

nsdq_movement = futures_movement('NQ=F')
nsdq_color = color_scheme('NQ=F')

oil_movement = futures_movement('CL=F')
oil_color = color_scheme('CL=F')

gold_movement = futures_movement('GC=F')
gold_color = color_scheme('GC=F')

treas_movement = futures_movement('^TNX')
treas_color = color_scheme('^TNX')

# creates widget window
window = tk.Tk()

# assigns labels for each futures contract
spx_lbl = tk.Label(window, text=spx_movement,
                   fg=spx_color, font=('Verdana', 14))
spx_lbl.place(x=20, y=20)

dow_lbl = tk.Label(window, text=dow_movement,
                   fg=dow_color, font=('Verdana', 14))
dow_lbl.place(x=20, y=45)

nsdq_lbl = tk.Label(window, text=nsdq_movement,
                    fg=nsdq_color, font=('Verdana', 14))
nsdq_lbl.place(x=20, y=70)

oil_lbl = tk.Label(window, text=oil_movement,
                   fg=oil_color, font=('Verdana', 14))
oil_lbl.place(x=20, y=95)

gold_lbl = tk.Label(window, text=gold_movement,
                    fg=gold_color, font=('Verdana', 14))
gold_lbl.place(x=20, y=120)

treas_lbl = tk.Label(window, text=treas_movement,
                     fg=treas_color, font=('Verdana', 14))
treas_lbl.place(x=20, y=145)

# gives widget metrics
window.title('FUTURES PRICES')
window.geometry('200x200+5+20')
window.mainloop()
