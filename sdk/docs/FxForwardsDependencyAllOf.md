# FxForwardsDependencyAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domestic_currency** | **str** | DomesticCurrency is the first currency in a currency pair quote e.g. eur-gbp, eur is the domestic currency. | 
**foreign_currency** | **str** | ForeignCurrency is the second currency in a currency pair quote e.g. eur-gbp, gbp is the foreign currency. | 
**curve_type** | **str** | Used to describe the format in which the curve is expressed  e.g. FxFwdCurve (general term to describe any representation), TenorFxFwdCurve, PipsFxFwdCurve. | 
**date** | **datetime** | The effectiveDate of the entity that this is a dependency for.  Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date. | 
**dependency_type** | **str** | The available values are: OpaqueDependency, CashDependency, DiscountingDependency, EquityCurveDependency, EquityVolDependency, FxDependency, FxForwardsDependency, FxVolDependency, IndexProjectionDependency, IrVolDependency, QuoteDependency, Vendor, CalendarDependency, InflationFixingDependency | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


