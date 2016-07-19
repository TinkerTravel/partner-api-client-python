# test id's
from tinker_partner_api import TinkerPartnerAPI

appId = 'YOUR_APP_ID'
apiKey = 'YOUR_API_KEY'

from datetime import datetime

tinker = TinkerPartnerAPI(app_id=appId, api_key=apiKey, production=False)

# query airports
airports = tinker.airports()

print("Total airports", len(airports))
# => Total airports 425

def is_airport(iata_code):
    return lambda ap: ap['iata'] == iata_code

# pick the first (python2 compatible)
schiphol = list(filter(is_airport('AMS'), airports))[0]

print(schiphol)
# => {'geoloc': 262374, 'nr': '1', 'name': 'Schiphol Airport', 'iata': 'AMS'}

# get a home address
geo_completions = tinker.location(country='nl', city='amsterdam', street='nieuwezijds voorburgwal')

# pick the first, this is an example, your user should decide here
my_street = geo_completions[0]

print(my_street)
# => {'geoloc': 3646111, 'suggestion': 'Netherlands,Amsterdam,Amsterdam,Van der Hoopstraat'}

# these are internal id's
a_loc = schiphol['geoloc']
b_loc = my_street['geoloc']
print(a_loc, b_loc)
# => 262374 3646111

quote_to = tinker.quote_to_airport(
    passengers=1,
    checkin_luggage=0,
    customer_geoloc=my_street['geoloc'],
    customer_street_nr='15',
    airport_arrival_time=datetime(2016, 7, 26, hour=10, minute=00),
    airport_geoloc=schiphol['geoloc']
)

quote_from = tinker.quote_from_airport(
    passengers=1,
    checkin_luggage=0,
    airport_geoloc=schiphol['geoloc'],
    customer_geoloc=my_street['geoloc'],
    customer_street_nr='15',
    plane_landing_time=datetime(2016, 7, 26, hour=10, minute=00)
)


print(quote_to, quote_from)
# [{'quote_id': 82325448, 'amount': '33.99', 'travelClass': 'COMFORT'},
#  {'quote_id': 82325447, 'amount': '30.99', 'travelClass': 'ECONOMY'},
#  {'quote_id': 82325449, 'amount': '40.99', 'travelClass': 'BUSINESS'}]
#
# [{'quote_id': 82325452, 'amount': '37.99', 'travelClass': 'BUSINESS'},
#  {'quote_id': 82325451, 'amount': '31.99', 'travelClass': 'COMFORT'},
#  {'quote_id': 82325450, 'amount': '29.99', 'travelClass': 'ECONOMY'}]

customer = tinker.create_customer(
    email='test@defekt.nl',
    first_name='Test',
    last_name='Test',
    gender='F',
    language='nl',
    phone='+31612345678',
    phone_country_code='nl'
)
print(customer)
# {'customerId': 119826}

leg1 = {
    "quoteId": quote_to[0]['quote_id'],
    "flightNumber": 'KL-2345'
}

leg2 = {
    "quoteId": quote_to[0]['quote_id'],
    "flightNumber": 'KL-2345'
}

booking = tinker.confirm_booking(
    customer_id=customer['customerId'],
    selected_price_quotes=[leg1, leg2]
)

print(booking)
