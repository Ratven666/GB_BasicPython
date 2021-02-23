import requests
from decimal import Decimal
import datetime


def currency_rates(val_code: str):
    """
    Возвращвет дату и курс запрашиваемой валюты по отношению к 1 рублю
    :param val_code: (str) Код валюты
    :return: (tuple) (datetime.date) Дата курса, (decimal.Decimal) Значение курса
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

    date_str = content[content.find("<ValCurs Date=") + 15: content.find("<ValCurs Date=") + 25]
    date = date_str.split(".")
    date = datetime.date(year=int(date[2]), month=int(date[1]), day=int(date[0]))

    return date, value / nominal


print(currency_rates("eur"))
print(currency_rates("USD"))

print(currency_rates("INR"))
print(currency_rates("Nuke_Cola_caps"))
