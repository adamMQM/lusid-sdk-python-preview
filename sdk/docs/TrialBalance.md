# TrialBalance

A TrialBalance entity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general_ledger_account_code** | **str** | The Account code that the trial balance results have been grouped against | 
**description** | **str** | The description of the record | 
**levels** | **list[str]** | The levels that have been derived from the specified General Ledger Profile | 
**account_type** | **str** | The account type attributed to the record | 
**opening** | **float** | The opening balance at the start of the period | 
**closing** | **float** | The closing balance at the end of the period | 
**debit** | **float** | All debits that occured in the period | 
**credit** | **float** | All credits that occured in the period | 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


