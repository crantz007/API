import requests
import json


def main():
    # methods
    bitcoin = get_bitcoin()
    rate = get_bitcoin_rate()
    converted = convert(rate, bitcoin)
    display(bitcoin, converted)


# get bitcoin amount from user
def get_bitcoin():
    while True:
        # exceptions check if input data are numbers
        try:
            bitcoin = float(input('Enter the amount of bitcoin: '))
            break
        except:
            print('amount should be numbers')
    return bitcoin


# get bitcoin rate by request from url
def get_bitcoin_rate():
    data2 = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
    rate = data2['bpi']['USD']['rate']
    return rate


# calculations and formatting data type for rate
def convert(rate, bitcoin):
    try:
        formatting_rate = float(rate)
    except:
        formatting_rate = float(rate.replace(',', ''))
    converted = (bitcoin * formatting_rate)
    return converted


# display result
def display(bitcoin, converted):
    print(f'{bitcoin}  bitcoin is equivalent to {converted:.2f} in USD')


if __name__ == '__main__':
    main()
