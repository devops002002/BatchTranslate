from enum import Enum


class Country(Enum):
    English = 'en'
    ChinaSimple = 'zh-CN'
    ChinaTran = 'zh-TW'
    Koren = 'ko'
    Germany = 'de'
    Japanese = 'jp'
    Russian = 'ru'
    Spain = 'es'
    Italy = 'it'
    Franch = 'fr'
    Vietnam = 'vi'
    Portugal = 'pt'
    Persian = 'fa'


def get_country_list():
    list_country = []
    list_country.append(Country.English)
    list_country.append(Country.ChinaSimple)
    list_country.append(Country.ChinaTran)
    list_country.append(Country.Koren)
    list_country.append(Country.Germany)
    list_country.append(Country.Japanese)
    list_country.append(Country.Russian)
    list_country.append(Country.Spain)
    list_country.append(Country.Italy)
    list_country.append(Country.Franch)
    list_country.append(Country.Vietnam)
    list_country.append(Country.Portugal)
    list_country.append(Country.Persian)
    return list_country
