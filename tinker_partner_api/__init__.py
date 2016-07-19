from __future__ import absolute_import

import sys
if sys.version_info <= (3,2):
    from urllib3.contrib import pyopenssl
    pyopenssl.inject_into_urllib3()

#!/usr/bin/env python3
from datetime import datetime

import swagger_generated.tinker_partner_api_wrapper as tinker

import json

# debugging off
if False:
    import logging
    logging.getLogger("urllib3").setLevel(logging.DEBUG)
    logging.getLogger("tinker_partner_api").setLevel(logging.DEBUG)

class TinkerPartnerAPI():
    def __init__(self, production=False, app_id=None, api_key=None):
        subdomain = production and 'api' or 'sandbox'
        self.baseUrl = 'https://{}.tinker.taxi/api'.format(subdomain)
        self.client = tinker.ApiClient(host=self.baseUrl)
        self.booking = tinker.PartnerBookingApi(api_client=self.client)
        self.contact = tinker.CustomerApi(api_client=self.client)
        self.app_id = app_id
        self.api_key = api_key

    def airports(self):
        return self.booking.partner_booking_airports(
            app_id=self.app_id, api_key=self.api_key
        ).result

    def location(self, country=None, city=None, street=None):
        return self.booking.partner_booking_locations(
            app_id=self.app_id, api_key=self.api_key,
            country=country, city=city, street=street
        ).result

    def quote_from_airport(self,
                           passengers=None,
                           checkin_luggage=None,
                           customer_geoloc=None,
                           customer_street_nr=None,
                           airport_geoloc=None,
                           plane_landing_time=None):

        # TODO check timezone = CET
        if not type(plane_landing_time) == datetime:
            raise ValueError('`plane_landing_time` argument must be a datetime object')

        return self.booking.partner_booking_request_from_airport_booking(
            app_id=self.app_id, api_key=self.api_key,
            passengers=passengers, checkin_luggage=checkin_luggage,
            airport_geoloc=airport_geoloc, location_geoloc=customer_geoloc,
            location_number=customer_street_nr, plane_landing_time=plane_landing_time
        ).result

    def quote_to_airport(self,
                         passengers=None,
                         checkin_luggage=None,
                         customer_geoloc=None,
                         customer_street_nr=None,
                         airport_geoloc=None,
                         airport_arrival_time=None):

        # TODO check timezone = CET
        if not type(airport_arrival_time) == datetime:
            raise ValueError('`airport_arrival_time` argument must be a datetime object')

        return self.booking.partner_booking_request_to_airport_booking(
            app_id=self.app_id, api_key=self.api_key,
            passengers=passengers, checkin_luggage=checkin_luggage,
            airport_geoloc=airport_geoloc, location_geoloc=customer_geoloc,
            location_number=customer_street_nr, airport_arrival_time=airport_arrival_time,
        ).result

    def create_customer(self,
                        email=None,
                        gender=None,
                        language=None,
                        phone_country_code=None,
                        phone=None,
                        first_name=None,
                        last_name=None):
        return self.contact.customer_new_customer(
            app_id=self.app_id, api_key=self.api_key,
            email=email, gender=gender, language=language,
            phone_country_code=phone_country_code, phone=phone,
            first_name=first_name, last_name=last_name
        ).result

#{quoteId: 1, flightNumber: 'XX-000'}
    def confirm_booking(self, customer_id=None, selected_price_quotes=None):
        return self.booking.partner_booking_confirm(
            app_id=self.app_id, api_key=self.api_key,
            customer_id=customer_id,
            price_quotes=json.dumps(selected_price_quotes)
        ).result

