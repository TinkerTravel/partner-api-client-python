# tinker_partner_api_wrapper.CustomerApi

All URIs are relative to *https://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customer_new_customer**](CustomerApi.md#customer_new_customer) | **POST** /v2/partner/customers | Create a Tinker Customer


# **customer_new_customer**
> InlineResponse200 customer_new_customer(app_id, api_key, email, gender, language, phone_country_code, phone, first_name, last_name)

Create a Tinker Customer

### Example 
```python
import time
import tinker_partner_api_wrapper
from tinker_partner_api_wrapper.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = tinker_partner_api_wrapper.CustomerApi()
app_id = 'app_id_example' # str | the partners appId
api_key = 'api_key_example' # str | the partners apiKey
email = 'email_example' # str | Email address of the customer
gender = 'gender_example' # str | Gender of the customer (M or F)
language = 'language_example' # str | ISO 3166 alpha 2 language code
phone_country_code = 'phone_country_code_example' # str | Country code for the phone number
phone = 'phone_example' # str | Phone number of the customer
first_name = 'first_name_example' # str | First name of the customer
last_name = 'last_name_example' # str | Last name of the customer

try: 
    # Create a Tinker Customer
    api_response = api_instance.customer_new_customer(app_id, api_key, email, gender, language, phone_country_code, phone, first_name, last_name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CustomerApi->customer_new_customer: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| the partners appId | 
 **api_key** | **str**| the partners apiKey | 
 **email** | **str**| Email address of the customer | 
 **gender** | **str**| Gender of the customer (M or F) | 
 **language** | **str**| ISO 3166 alpha 2 language code | 
 **phone_country_code** | **str**| Country code for the phone number | 
 **phone** | **str**| Phone number of the customer | 
 **first_name** | **str**| First name of the customer | 
 **last_name** | **str**| Last name of the customer | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/xml
 - **Accept**: application/json, application/xml, text/xml, application/javascript, text/javascript

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

