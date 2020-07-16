import json
import sys

import requests


def currencyConverter(currencyFrom, currencyTo, amount):
    apiKey = '7c49c4cc89f8aa74e06b'
    convert = currencyFrom + "_" + currencyTo
    revert = currencyTo + "_" + currencyFrom
    convert_url = 'https://free.currconv.com/api/v7/convert?q=' + convert + "," + revert + '&compact=ultra&apiKey=' + apiKey
    response = requests.get(convert_url)
    response.raise_for_status()

    url = 'https://free.currconv.com/api/v7/currencies?apiKey=' + apiKey
    response2 = requests.get(url)
    response2.raise_for_status()

    currencyRate = json.loads(response.text)
    all = json.loads(response2.text)

    print("Amount = " + amount)
    print(
        convert + " : " + str(currencyRate[convert] * int(amount)) + " " + all["results"][currencyTo]["currencySymbol"])
    print(
        revert + " : " + str(currencyRate[revert] * int(amount)) + " " + all["results"][currencyFrom]["currencySymbol"])


# change to "countries" if you want to see list of countries currencies
def allCurrencies(option="currencies"):
    apiKey = '7c49c4cc89f8aa74e06b'
    url = 'https://free.currconv.com/api/v7/' + option + '?apiKey=' + apiKey
    response = requests.get(url)
    response.raise_for_status()

    all = json.loads(response.text)
    for currency in all["results"].values():
        try:
            print(currency["id"] + " -- " + currency["currencyName"] + " : " +
                  currency["currencySymbol"])
        except KeyError:
            print(currency["id"] + " -- " + currency["currencyName"] + " : " + "No symbol")


if __name__ == '__main__':
    if len(sys.argv) == 4:
        currencyConverter(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        allCurrencies()  # add "countries" if you want to see list of currencies' countries
