import requests
from decimal import Decimal


def currency_rates(val_code: str):
    """
    Возвращвет текущий курс валюты по отношению к 1 рублю
    :param val_code: (str) Код валюты
    :return: (decimal.Decimal) Значение курса
    """
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    start_index = content.find(val_code.upper())
    if start_index == -1:
        return None
    end_index = start_index + content[start_index:].find("</Valute>")

    sub_s = content[start_index:end_index]
    nominal = int(sub_s[sub_s.find("<Nominal>") + 9: sub_s.find("</Nominal>")])
    value = sub_s[sub_s.find("<Value>") + 7: sub_s.find("</Value>")]
    value = Decimal(value.replace(",", "."))

    return value / nominal


print(currency_rates("eur"))
print(currency_rates("USD"))

print(currency_rates("INR"))
print(currency_rates("Nuke_Cola_caps"))
