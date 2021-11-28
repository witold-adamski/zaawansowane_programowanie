import requests


class Brewery:
    def __init__(self, id: str, name: str, brewery_type: str,
                 street: str, address_2: str, address_3: str,
                 city: str, state: str, county_province: str, postal_code: str,
                 country: str, longitude: str, latitude: str, phone: str,
                 website_url: str, updated_at: str, created_at: str):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state = state
        self.county_province = county_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.updated_at = updated_at
        self.created_at = created_at

    def __str__(self):
        return f'Id: {self.id}, ' \
               f'nazwa: {self.name}, ' \
               f'typ: {self.brewery_type}, ' \
               f'ulica: {self.street}, ' \
               f'reszta adresu: {self.address_2} {self.address_3}, ' \
               f'miasto: {self.city}, stan: {self.state}, ' \
               f'prowincja {self.county_province}, ' \
               f'kod pocztowy: {self.postal_code}, ' \
               f'kraj: {self.country}, ' \
               f'współrzędne: {self.longitude} - {self.latitude}, ' \
               f'telefon: {self.phone}, www: {self.website_url}, ' \
               f'aktualizacja: {self.updated_at}, ' \
               f'data utworzenia: {self.created_at}.'


response = requests.get('https://api.openbrewerydb.org/breweries').json()
for index, value in enumerate(response):
    print(f'{index}: {Brewery(**response[index])}')
