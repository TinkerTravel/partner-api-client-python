# Tinker Partner API, Python Client

This is a *beta-*Python client for the Tinker Partner-API (`api.tinker.taxi`).

Feel free to contact us at `api@tinker.travel` or file a github issue, or PR ;-)

## Overview

First create a client object you pass it your `appId` and `apiKey` tokens.

```python
from tinker_partner_api import TinkerPartnerAPI

tinker = TinkerPartnerAPI(
    app_id='b8f61abc9164ae96bc6f1bc4',
    api_key='9ba26ef96f3e96fa23b0a6fe6f0e26f3ab6,
    # use the sandbox (this is the default, anyway)
    production=False
)
```

Then you can call:

1. `tinker.airports` - the airports we support
2. `tinker.location` - geolocation lookup of customer address
3. `tinker.quote_from_airport` - get a price quote for `customer => airport`
4. `tinker.quote_to_airport` - get a price qupte for `aiport => customer`
5. `tinker.create_customer` - create the customer contact details
6. `tinker.confirm_booking` - confirm the booking

See below for details.

## Installation

This works best with Python 3.2 and upwards. It also supports Python 2.7 and
later with an up to date pyOpenSSL.

### Installation (Python 3)

You can install directly from Github via pip:

```sh
pip install git+https://github.com/TinkerTravel/tinker-partner-api-python.git
```

To use the bindings, import the package:

```python
import tinker_partner_api as tinker
```

You can also install the API client via [Setuptools](http://pypi.python.org/pypi/setuptools),
by cloning and running:

```sh
python setup.py install
```

### Installation (Python 2.7)

For Python 2.7+ you need to put some more effort, sorry.

You need to install recent versions of

- `ndg-httpsclient`, `pyopenssl` and `pyasn` ; using a recent version of `openssl`.

On Mac you can install this using homebrew:

```sh
brew update
brew install openssl
```

Then you use this library in your Python builds like so (see `brew info openssl`):

```sh
# install cryptography with newer openssl library
LDFLAGS="-L/usr/local/opt/openssl/lib" pip install cryptography --no-use-wheel

# install rest of dependencies
pip install ndg-httpsclient pyopenssl
```

Phew! Now the example should be working.

## Getting Started

First create a client object you pass it your `appId` and `apiKey` tokens.

```python 
from tinker_partner_api import TinkerPartnerAPI

tinker = TinkerPartnerAPI(
    app_id='b8f61abc9164ae96bc6f1bc4',
    api_key='9ba26ef96f3e96fa23b0a6fe6f0e26f3ab6,
    # use the sandbox (this is the default, anyway)
    production=False
)
```

You can now request a list of supported airports, like so:
 
```python
airports = tinkerAPI.airports()
print("Total airports", len(airports))
# => Total airports 425
```

As an example, let's pick Schiphol from it,

```python
schiphol = list(filter(lambda ap: ap['iata'] == "AMS", airports))[0]

print(schiphol)
# => {'geoloc': 262374, 'nr': '1', 'name': 'Schiphol Airport', 'iata': 'AMS'}
```

And lookup a customer address

```python

# get a home address
geo_completions = tinkerAPI.location(country='nl', city='amsterdam', street='nieuwezijds voorburgwal')

# pick the first, this is an example, your user should decide here
customer_geoloc = geo_completions[0]

print(customer_geoloc)
# => {u'geoloc': 3646119, u'suggestion': u'Netherlands,Amsterdam,Amsterdam,Nieuwezijds Voorburgwal'}
```

Great, lets get a quote in both directions. First "to the airport", notice the `airport_arrival_time` parameter.

```python
quote_to = tinkerAPI.quote_to_airport(
    passengers=1,
    checkin_luggage=0,
    customer_geoloc=my_street['geoloc'],
    customer_street_nr='15',
    airport_arrival_time=datetime(2016, 7, 26, hour=10, minute=00),
    airport_geoloc=schiphol['geoloc']
)
```

The two directions are slightly different, for the "from the aiport" direction
we pass `plane_landing_time`. Please refer to http://developer.tinker.travel
for the details on their meaning.

Times passed should be always *local to the location you are referring to*
(due to general relativity and curved space-time and such.. just kidding).

```python
quote_from = tinkerAPI.quote_from_airport(
    passengers=1,
    checkin_luggage=0,
    airport_geoloc=schiphol['geoloc'],
    customer_geoloc=my_street['geoloc'],
    customer_street_nr='15',
    plane_landing_time=datetime(2016, 7, 26, hour=10, minute=00)
)
```

Example output:

```python
print(quote_to, quote_from)
# [{'quote_id': 82325448, 'amount': '33.99', 'travelClass': 'COMFORT'},
#  {'quote_id': 82325447, 'amount': '30.99', 'travelClass': 'ECONOMY'},
#  {'quote_id': 82325449, 'amount': '40.99', 'travelClass': 'BUSINESS'}]
#
# [{'quote_id': 82325452, 'amount': '37.99', 'travelClass': 'BUSINESS'},
#  {'quote_id': 82325451, 'amount': '31.99', 'travelClass': 'COMFORT'},
#  {'quote_id': 82325450, 'amount': '29.99', 'travelClass': 'ECONOMY'}]
```


Okay, now if you want to confirm this, first create the customer details.

```python
customer = tinkerAPI.create_customer(
    email='customer@gmail.com',
    first_name='The',
    last_name='Customer',
    gender='F',
    language='nl',
    phone='+31612345678',
    phone_country_code='nl'
)
print(customer)
# {'customerId': 119826}
```

Then *collect some legs* (selected quotes) and confirm the booking.

```python
leg1 = {
    "quoteId": quote_to[0]['quote_id'],
    "flightNumber": 'KL-2345'
}

leg2 = {
    "quoteId": quote_to[0]['quote_id'],
    "flightNumber": 'KL-2345'
}

booking = tinkerAPI.confirm_booking(
    customer_id=customer['customerId'],
    selected_price_quotes=[leg1, leg2]
)
```

And you get a confirmation stating the number of legs booked.

```
print(booking)
# => [{u'bkg_confirm_booking': 2}]
```

Hurray! Trip booked!