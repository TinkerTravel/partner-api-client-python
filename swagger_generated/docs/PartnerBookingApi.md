# tinker_partner_api_wrapper.PartnerBookingApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**partner_booking_airports**](PartnerBookingApi.md#partner_booking_airports) | **GET** /v2/partner/bookings/airports | Retrieves a list of all tinker-activated airports
[**partner_booking_confirm**](PartnerBookingApi.md#partner_booking_confirm) | **POST** /v2/partner/bookings/confirm | Confirm a previously created set of price quotes
[**partner_booking_locations**](PartnerBookingApi.md#partner_booking_locations) | **GET** /v2/partner/bookings/locations | Retrieves a geoloc-id for a given location
[**partner_booking_request_from_airport_booking**](PartnerBookingApi.md#partner_booking_request_from_airport_booking) | **POST** /v2/partner/bookings/from/airport | Request a price quote for a trip starting FROM an airport.
[**partner_booking_request_to_airport_booking**](PartnerBookingApi.md#partner_booking_request_to_airport_booking) | **POST** /v2/partner/bookings/to/airport | Request a price quote for a trip TO an airport


# **partner_booking_airports**
> InlineResponse200 partner_booking_airports(app_id, api_key)

Retrieves a list of all tinker-activated airports

### Example 
```python
import time
import tinker_partner_api_wrapper
from tinker_partner_api_wrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = tinker_partner_api_wrapper.PartnerBookingApi()
app_id = 'app_id_example' # str | the partners appId
api_key = 'api_key_example' # str | the partners apiKey

try: 
    # Retrieves a list of all tinker-activated airports
    api_response = api_instance.partner_booking_airports(app_id, api_key)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PartnerBookingApi->partner_booking_airports: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| the partners appId | 
 **api_key** | **str**| the partners apiKey | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partner_booking_confirm**
> InlineResponse200 partner_booking_confirm(app_id, api_key, customer_id, price_quotes, comment=comment)

Confirm a previously created set of price quotes

### Example 
```python
import time
import tinker_partner_api_wrapper
from tinker_partner_api_wrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = tinker_partner_api_wrapper.PartnerBookingApi()
app_id = 'app_id_example' # str | the partners appId
api_key = 'api_key_example' # str | the partners apiKey
customer_id = 1.2 # float | The id of a newly created customer of the customers endpoint
price_quotes = 'price_quotes_example' # str | A list of price quote objects: [ {quoteId: Number, flightNumber: String} ]
comment = 'comment_example' # str | An optional comment (optional)

try: 
    # Confirm a previously created set of price quotes
    api_response = api_instance.partner_booking_confirm(app_id, api_key, customer_id, price_quotes, comment=comment)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PartnerBookingApi->partner_booking_confirm: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| the partners appId | 
 **api_key** | **str**| the partners apiKey | 
 **customer_id** | **float**| The id of a newly created customer of the customers endpoint | 
 **price_quotes** | **str**| A list of price quote objects: [ {quoteId: Number, flightNumber: String} ] | 
 **comment** | **str**| An optional comment | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partner_booking_locations**
> InlineResponse200 partner_booking_locations(app_id, api_key, country, city, street)

Retrieves a geoloc-id for a given location

### Example 
```python
import time
import tinker_partner_api_wrapper
from tinker_partner_api_wrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = tinker_partner_api_wrapper.PartnerBookingApi()
app_id = 'app_id_example' # str | the partners appId
api_key = 'api_key_example' # str | the partners apiKey
country = 'country_example' # str | ISO 3166 alpha 2 country code
city = 'city_example' # str | City name
street = 'street_example' # str | Street name

try: 
    # Retrieves a geoloc-id for a given location
    api_response = api_instance.partner_booking_locations(app_id, api_key, country, city, street)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PartnerBookingApi->partner_booking_locations: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| the partners appId | 
 **api_key** | **str**| the partners apiKey | 
 **country** | **str**| ISO 3166 alpha 2 country code | 
 **city** | **str**| City name | 
 **street** | **str**| Street name | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partner_booking_request_from_airport_booking**
> InlineResponse200 partner_booking_request_from_airport_booking(app_id, api_key, passengers, checkin_luggage, airport_geoloc, location_geoloc, location_number, plane_landing_time)

Request a price quote for a trip starting FROM an airport.

### Example 
```python
import time
import tinker_partner_api_wrapper
from tinker_partner_api_wrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = tinker_partner_api_wrapper.PartnerBookingApi()
app_id = 'app_id_example' # str | the partners appId
api_key = 'api_key_example' # str | the partners apiKey
passengers = 'passengers_example' # str | Passengers definition There are three types of passengers available:  [A]dult, [B]aby and [C]hild A valid definition would be: A1B1C0 for example Regular expression: ^A[0-8]B[0-8]C[0-8]$
checkin_luggage = 1.2 # float | the number of checkin luggage pieces
airport_geoloc = 1.2 # float | the geoloc for the airport, obtained from the airports endpoint
location_geoloc = 1.2 # float | the geoloc for a location, obtained from the locations endpoint
location_number = 'location_number_example' # str | the house number (incl. extensions) for the location
plane_landing_time = 'plane_landing_time_example' # str | The date-time the plane will land Regular expression: /^20[1-9]{2}-((0[1-9])|(1[0-2]))-((0[1-9])|([12][0-9])|(3[01])) (([01][0-9])|(2[0-3])):(00|30):00$/

try: 
    # Request a price quote for a trip starting FROM an airport.
    api_response = api_instance.partner_booking_request_from_airport_booking(app_id, api_key, passengers, checkin_luggage, airport_geoloc, location_geoloc, location_number, plane_landing_time)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PartnerBookingApi->partner_booking_request_from_airport_booking: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| the partners appId | 
 **api_key** | **str**| the partners apiKey | 
 **passengers** | **str**| Passengers definition There are three types of passengers available:  [A]dult, [B]aby and [C]hild A valid definition would be: A1B1C0 for example Regular expression: ^A[0-8]B[0-8]C[0-8]$ | 
 **checkin_luggage** | **float**| the number of checkin luggage pieces | 
 **airport_geoloc** | **float**| the geoloc for the airport, obtained from the airports endpoint | 
 **location_geoloc** | **float**| the geoloc for a location, obtained from the locations endpoint | 
 **location_number** | **str**| the house number (incl. extensions) for the location | 
 **plane_landing_time** | **str**| The date-time the plane will land Regular expression: /^20[1-9]{2}-((0[1-9])|(1[0-2]))-((0[1-9])|([12][0-9])|(3[01])) (([01][0-9])|(2[0-3])):(00|30):00$/ | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partner_booking_request_to_airport_booking**
> InlineResponse200 partner_booking_request_to_airport_booking(app_id, api_key, passengers, checkin_luggage, airport_geoloc, location_geoloc, location_number, airport_arrival_time)

Request a price quote for a trip TO an airport

### Example 
```python
import time
import tinker_partner_api_wrapper
from tinker_partner_api_wrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = tinker_partner_api_wrapper.PartnerBookingApi()
app_id = 'app_id_example' # str | the partners appId
api_key = 'api_key_example' # str | the partners apiKey
passengers = 'passengers_example' # str | Passengers definition There are three types of passengers available:  [A]dult, [B]aby and [C]hild A valid definition would be: A1B1C0 for example Regular expression: ^A[0-8]B[0-8]C[0-8]$
checkin_luggage = 1.2 # float | the number of checkin luggage pieces
airport_geoloc = 1.2 # float | the geoloc for the airport, obtained from the airports endpoint
location_geoloc = 1.2 # float | the geoloc for a location, obtained from the locations endpoint
location_number = 'location_number_example' # str | the house number (incl. extensions) for the location
airport_arrival_time = 'airport_arrival_time_example' # str | The date-time the passenger desires to be at the airport Regular expression: /^20[1-9]{2}-((0[1-9])|(1[0-2]))-((0[1-9])|([12][0-9])|(3[01])) (([01][0-9])|(2[0-3])):(00|30):00$/

try: 
    # Request a price quote for a trip TO an airport
    api_response = api_instance.partner_booking_request_to_airport_booking(app_id, api_key, passengers, checkin_luggage, airport_geoloc, location_geoloc, location_number, airport_arrival_time)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PartnerBookingApi->partner_booking_request_to_airport_booking: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| the partners appId | 
 **api_key** | **str**| the partners apiKey | 
 **passengers** | **str**| Passengers definition There are three types of passengers available:  [A]dult, [B]aby and [C]hild A valid definition would be: A1B1C0 for example Regular expression: ^A[0-8]B[0-8]C[0-8]$ | 
 **checkin_luggage** | **float**| the number of checkin luggage pieces | 
 **airport_geoloc** | **float**| the geoloc for the airport, obtained from the airports endpoint | 
 **location_geoloc** | **float**| the geoloc for a location, obtained from the locations endpoint | 
 **location_number** | **str**| the house number (incl. extensions) for the location | 
 **airport_arrival_time** | **str**| The date-time the passenger desires to be at the airport Regular expression: /^20[1-9]{2}-((0[1-9])|(1[0-2]))-((0[1-9])|([12][0-9])|(3[01])) (([01][0-9])|(2[0-3])):(00|30):00$/ | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

