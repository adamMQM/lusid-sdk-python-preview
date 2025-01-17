# CompletePortfolio


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**href** | **str** | The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime. | [optional] 
**description** | **str** | The long form description of the portfolio. | [optional] 
**display_name** | **str** | The name of the portfolio. | [optional] 
**created** | **datetime** | The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date. | [optional] 
**parent_portfolio_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**is_derived** | **bool** | Whether or not this is a derived portfolio. | [optional] [readonly] 
**type** | **str** | The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction | [optional] 
**version** | [**Version**](Version.md) |  | 
**properties** | [**list[ModelProperty]**](ModelProperty.md) | The requested portfolio properties. These will be from the &#39;Portfolio&#39; domain. | [optional] 
**base_currency** | **str** | If the portfolio is a transaction portfolio or derived transaction portfolio, this is the base currency of the portfolio. | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


