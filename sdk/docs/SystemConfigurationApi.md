# lusid.SystemConfigurationApi

All URIs are relative to *http://localhost:38075*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_configuration_transaction_type**](SystemConfigurationApi.md#create_configuration_transaction_type) | **POST** /api/systemconfiguration/transactions/type | [EARLY ACCESS] Create transaction type
[**create_side_definition**](SystemConfigurationApi.md#create_side_definition) | **POST** /api/systemconfiguration/transactions/side | [EXPERIMENTAL] Create side definition
[**list_configuration_transaction_types**](SystemConfigurationApi.md#list_configuration_transaction_types) | **GET** /api/systemconfiguration/transactions | [EARLY ACCESS] List transaction types
[**set_configuration_transaction_types**](SystemConfigurationApi.md#set_configuration_transaction_types) | **PUT** /api/systemconfiguration/transactions | [EXPERIMENTAL] Set transaction types


# **create_configuration_transaction_type**
> TransactionSetConfigurationData create_configuration_transaction_type(transaction_configuration_data_request=transaction_configuration_data_request)

[EARLY ACCESS] Create transaction type

Create a new transaction type by specifying a definition and the mappings to movements

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost:38075
configuration.host = "http://localhost:38075"
# Create an instance of the API class
api_instance = lusid.SystemConfigurationApi(lusid.ApiClient(configuration))
transaction_configuration_data_request = {"aliases":[{"type":"Another-Sell","description":"Sale","transactionClass":"MyDefault","transactionGroup":"MyGroup","transactionRoles":"LongShorter"}],"movements":[{"movementTypes":"StockMovement","side":"Side1","direction":-1,"properties":{},"mappings":[]},{"movementTypes":"CashCommitment","side":"Side2","direction":1,"properties":{},"mappings":[]}],"properties":{}} # TransactionConfigurationDataRequest | A transaction type definition (optional)

try:
    # [EARLY ACCESS] Create transaction type
    api_response = api_instance.create_configuration_transaction_type(transaction_configuration_data_request=transaction_configuration_data_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemConfigurationApi->create_configuration_transaction_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_configuration_data_request** | [**TransactionConfigurationDataRequest**](TransactionConfigurationDataRequest.md)| A transaction type definition | [optional] 

### Return type

[**TransactionSetConfigurationData**](TransactionSetConfigurationData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_side_definition**
> TransactionSetConfigurationData create_side_definition(side_configuration_data_request=side_configuration_data_request)

[EXPERIMENTAL] Create side definition

Create a new side definition for us in transaction type configuration

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost:38075
configuration.host = "http://localhost:38075"
# Create an instance of the API class
api_instance = lusid.SystemConfigurationApi(lusid.ApiClient(configuration))
side_configuration_data_request = {"side":"Side1","security":"security","currency":"currency","rate":"0.5","units":"500","amount":"1000"} # SideConfigurationDataRequest | The definition of the side to be created. (optional)

try:
    # [EXPERIMENTAL] Create side definition
    api_response = api_instance.create_side_definition(side_configuration_data_request=side_configuration_data_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemConfigurationApi->create_side_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **side_configuration_data_request** | [**SideConfigurationDataRequest**](SideConfigurationDataRequest.md)| The definition of the side to be created. | [optional] 

### Return type

[**TransactionSetConfigurationData**](TransactionSetConfigurationData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_configuration_transaction_types**
> TransactionSetConfigurationData list_configuration_transaction_types()

[EARLY ACCESS] List transaction types

Get the list of persisted transaction types

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost:38075
configuration.host = "http://localhost:38075"
# Create an instance of the API class
api_instance = lusid.SystemConfigurationApi(lusid.ApiClient(configuration))

try:
    # [EARLY ACCESS] List transaction types
    api_response = api_instance.list_configuration_transaction_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemConfigurationApi->list_configuration_transaction_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TransactionSetConfigurationData**](TransactionSetConfigurationData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_configuration_transaction_types**
> TransactionSetConfigurationData set_configuration_transaction_types(transaction_set_configuration_data_request=transaction_set_configuration_data_request)

[EXPERIMENTAL] Set transaction types

Set all transaction types to be used by the movements engine, for the organisation                WARNING! Changing these mappings will have a material impact on how data, new and old, is processed and aggregated by LUSID. This will affect your whole organisation. Only change if you are fully aware of the implications of the change.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid
from lusid.rest import ApiException
from pprint import pprint
configuration = lusid.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost:38075
configuration.host = "http://localhost:38075"
# Create an instance of the API class
api_instance = lusid.SystemConfigurationApi(lusid.ApiClient(configuration))
transaction_set_configuration_data_request = {"transactionConfigRequests":[{"aliases":[{"type":"Simple-Sell","description":"Sale","transactionClass":"MyDefault","transactionGroup":"MyGroup","transactionRoles":"LongShorter"}],"movements":[{"movementTypes":"StockMovement","side":"Side1","direction":-1,"properties":{},"mappings":[]},{"movementTypes":"CashCommitment","side":"Side2","direction":1,"properties":{},"mappings":[]}],"properties":{}},{"aliases":[{"type":"Sell-FIFO","description":"Sale using FIFO logic","transactionClass":"FIFO","transactionGroup":"MyGroup","transactionRoles":"LongShorter"}],"movements":[{"movementTypes":"StockMovement","side":"Side1","direction":-1,"properties":{"transactionConfiguration/default/TaxLotSelectionMethod":{"key":"TransactionConfiguration/default/TaxLotSelectionMethod","value":{"labelValue":"FirstInFirstOut"}}},"mappings":[]},{"movementTypes":"CashCommitment","side":"Side2","direction":1,"properties":{},"mappings":[]}],"properties":{"transactionConfiguration/default/Example":{"key":"TransactionConfiguration/default/Example","value":{"labelValue":"Value"}}}}],"sideConfigRequests":[{"side":"Side1","security":"security","currency":"currency","rate":"0.5","units":"500","amount":"1000"},{"side":"Side2","security":"security","currency":"currency","rate":"0.75","units":"250","amount":"2000"}]} # TransactionSetConfigurationDataRequest | The complete set of transaction type definitions (optional)

try:
    # [EXPERIMENTAL] Set transaction types
    api_response = api_instance.set_configuration_transaction_types(transaction_set_configuration_data_request=transaction_set_configuration_data_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemConfigurationApi->set_configuration_transaction_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_set_configuration_data_request** | [**TransactionSetConfigurationDataRequest**](TransactionSetConfigurationDataRequest.md)| The complete set of transaction type definitions | [optional] 

### Return type

[**TransactionSetConfigurationData**](TransactionSetConfigurationData.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

