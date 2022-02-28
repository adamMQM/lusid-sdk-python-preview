# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4024
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class FeeRuleUpsertRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'code': 'str',
        'transaction_property_key': 'str',
        'transaction_type': 'str',
        'country': 'str',
        'counterparty': 'str',
        'transaction_currency': 'str',
        'settlement_currency': 'str',
        'execution_broker': 'str',
        'custodian': 'str',
        'exchange': 'str',
        'fee': 'CalculationInfo',
        'min_fee': 'CalculationInfo',
        'max_fee': 'CalculationInfo',
        'additional_keys': 'dict(str, str)',
        'description': 'str'
    }

    attribute_map = {
        'code': 'code',
        'transaction_property_key': 'transactionPropertyKey',
        'transaction_type': 'transactionType',
        'country': 'country',
        'counterparty': 'counterparty',
        'transaction_currency': 'transactionCurrency',
        'settlement_currency': 'settlementCurrency',
        'execution_broker': 'executionBroker',
        'custodian': 'custodian',
        'exchange': 'exchange',
        'fee': 'fee',
        'min_fee': 'minFee',
        'max_fee': 'maxFee',
        'additional_keys': 'additionalKeys',
        'description': 'description'
    }

    required_map = {
        'code': 'required',
        'transaction_property_key': 'required',
        'transaction_type': 'required',
        'country': 'required',
        'counterparty': 'required',
        'transaction_currency': 'required',
        'settlement_currency': 'required',
        'execution_broker': 'required',
        'custodian': 'required',
        'exchange': 'required',
        'fee': 'required',
        'min_fee': 'optional',
        'max_fee': 'optional',
        'additional_keys': 'optional',
        'description': 'optional'
    }

    def __init__(self, code=None, transaction_property_key=None, transaction_type=None, country=None, counterparty=None, transaction_currency=None, settlement_currency=None, execution_broker=None, custodian=None, exchange=None, fee=None, min_fee=None, max_fee=None, additional_keys=None, description=None, local_vars_configuration=None):  # noqa: E501
        """FeeRuleUpsertRequest - a model defined in OpenAPI"
        
        :param code:  (required)
        :type code: str
        :param transaction_property_key:  (required)
        :type transaction_property_key: str
        :param transaction_type:  (required)
        :type transaction_type: str
        :param country:  (required)
        :type country: str
        :param counterparty:  (required)
        :type counterparty: str
        :param transaction_currency:  (required)
        :type transaction_currency: str
        :param settlement_currency:  (required)
        :type settlement_currency: str
        :param execution_broker:  (required)
        :type execution_broker: str
        :param custodian:  (required)
        :type custodian: str
        :param exchange:  (required)
        :type exchange: str
        :param fee:  (required)
        :type fee: lusid.CalculationInfo
        :param min_fee: 
        :type min_fee: lusid.CalculationInfo
        :param max_fee: 
        :type max_fee: lusid.CalculationInfo
        :param additional_keys: 
        :type additional_keys: dict(str, str)
        :param description: 
        :type description: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._transaction_property_key = None
        self._transaction_type = None
        self._country = None
        self._counterparty = None
        self._transaction_currency = None
        self._settlement_currency = None
        self._execution_broker = None
        self._custodian = None
        self._exchange = None
        self._fee = None
        self._min_fee = None
        self._max_fee = None
        self._additional_keys = None
        self._description = None
        self.discriminator = None

        self.code = code
        self.transaction_property_key = transaction_property_key
        self.transaction_type = transaction_type
        self.country = country
        self.counterparty = counterparty
        self.transaction_currency = transaction_currency
        self.settlement_currency = settlement_currency
        self.execution_broker = execution_broker
        self.custodian = custodian
        self.exchange = exchange
        self.fee = fee
        if min_fee is not None:
            self.min_fee = min_fee
        if max_fee is not None:
            self.max_fee = max_fee
        self.additional_keys = additional_keys
        self.description = description

    @property
    def code(self):
        """Gets the code of this FeeRuleUpsertRequest.  # noqa: E501


        :return: The code of this FeeRuleUpsertRequest.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this FeeRuleUpsertRequest.


        :param code: The code of this FeeRuleUpsertRequest.  # noqa: E501
        :type code: str
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) > 64):
            raise ValueError("Invalid value for `code`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) < 1):
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', code)):  # noqa: E501
            raise ValueError(r"Invalid value for `code`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._code = code

    @property
    def transaction_property_key(self):
        """Gets the transaction_property_key of this FeeRuleUpsertRequest.  # noqa: E501


        :return: The transaction_property_key of this FeeRuleUpsertRequest.  # noqa: E501
        :rtype: str
        """
        return self._transaction_property_key

    @transaction_property_key.setter
    def transaction_property_key(self, transaction_property_key):
        """Sets the transaction_property_key of this FeeRuleUpsertRequest.


        :param transaction_property_key: The transaction_property_key of this FeeRuleUpsertRequest.  # noqa: E501
        :type transaction_property_key: str
        """
        if self.local_vars_configuration.client_side_validation and transaction_property_key is None:  # noqa: E501
            raise ValueError("Invalid value for `transaction_property_key`, must not be `None`")  # noqa: E501

        self._transaction_property_key = transaction_property_key

    @property
    def transaction_type(self):
        """Gets the transaction_type of this FeeRuleUpsertRequest.  # noqa: E501


        :return: The transaction_type of this FeeRuleUpsertRequest.  # noqa: E501
        :rtype: str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this FeeRuleUpsertRequest.


        :param transaction_type: The transaction_type of this FeeRuleUpsertRequest.  # noqa: E501
        :type transaction_type: str
        """
        if self.local_vars_configuration.client_side_validation and transaction_type is None:  # noqa: E501
            raise ValueError("Invalid value for `transaction_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                transaction_type is not None and len(transaction_type) > 64):
            raise ValueError("Invalid value for `transaction_type`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                transaction_type is not None and len(transaction_type) < 1):
            raise ValueError("Invalid value for `transaction_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._transaction_type = transaction_type

    @property
    def country(self):
        """Gets the country of this FeeRuleUpsertRequest.  # noqa: E501


        :return: The country of this FeeRuleUpsertRequest.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this FeeRuleUpsertRequest.


        :param country: The country of this FeeRuleUpsertRequest.  # noqa: E501
        :type country: str
        """
        if self.local_vars_configuration.client_side_validation and country is None:  # noqa: E501
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                country is not None and len(country) > 64):
            raise ValueError("Invalid value for `country`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                country is not None and len(country) < 1):
            raise ValueError("Invalid value for `country`, length must be greater than or equal to `1`")  # noqa: E501

        self._country = country

    @property
    def counterparty(self):
        """Gets the counterparty of this FeeRuleUpsertRequest.  # noqa: E501


        :return: The counterparty of this FeeRuleUpsertRequest.  # noqa: E501
        :rtype: str
        """
        return self._counterparty

    @counterparty.setter
    def counterparty(self, counterparty):
        """Sets the counterparty of this FeeRuleUpsertRequest.


        :param counterparty: The counterparty of this FeeRuleUpsertRequest.  # noqa: E501
        :type counterparty: str
        """
        if self.local_vars_configuration.client_side_validation and counterparty is None:  # noqa: E501
            raise ValueError("Invalid value for `counterparty`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                counterparty is not None and len(counterparty) > 64):
            raise ValueError("Invalid value for `counterparty`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                counterparty is not None and len(counterparty) < 1):
            raise ValueError("Invalid value for `counterparty`, length must be greater than or equal to `1`")  # noqa: E501

        self._counterparty = counterparty

    @property
    def transaction_currency(self):
        """Gets the transaction_currency of this FeeRuleUpsertRequest.  # noqa: E501


        :return: The transaction_currency of this FeeRuleUpsertRequest.  # noqa: E501
        :rtype: str
        """
        return self._transaction_currency

    @transaction_currency.setter
    def transaction_currency(self, transaction_currency):
        """Sets the transaction_currency of this FeeRuleUpsertRequest.


        :param transaction_currency: The transaction_currency of this FeeRuleUpsertRequest.  # noqa: E501
        :type transaction_currency: str
        """
        if self.local_vars_configuration.client_side_validation and transaction_currency is None:  # noqa: E501
            raise ValueError("Invalid value for `transaction_currency`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                transaction_currency is not None and len(transaction_currency) > 64):
            raise ValueError("Invalid value for `transaction_currency`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                transaction_currency is not None and len(transaction_currency) < 1):
            raise ValueError("Invalid value for `transaction_currency`, length must be greater than or equal to `1`")  # noqa: E501

        self._transaction_currency = transaction_currency

    @property
    def settlement_currency(self):
        """Gets the settlement_currency of this FeeRuleUpsertRequest.  # noqa: E501


        :return: The settlement_currency of this FeeRuleUpsertRequest.  # noqa: E501
        :rtype: str
        """
        return self._settlement_currency

    @settlement_currency.setter
    def settlement_currency(self, settlement_currency):
        """Sets the settlement_currency of this FeeRuleUpsertRequest.


        :param settlement_currency: The settlement_currency of this FeeRuleUpsertRequest.  # noqa: E501
        :type settlement_currency: str
        """
        if self.local_vars_configuration.client_side_validation and settlement_currency is None:  # noqa: E501
            raise ValueError("Invalid value for `settlement_currency`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                settlement_currency is not None and len(settlement_currency) > 64):
            raise ValueError("Invalid value for `settlement_currency`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                settlement_currency is not None and len(settlement_currency) < 1):
            raise ValueError("Invalid value for `settlement_currency`, length must be greater than or equal to `1`")  # noqa: E501

        self._settlement_currency = settlement_currency

    @property
    def execution_broker(self):
        """Gets the execution_broker of this FeeRuleUpsertRequest.  # noqa: E501


        :return: The execution_broker of this FeeRuleUpsertRequest.  # noqa: E501
        :rtype: str
        """
        return self._execution_broker

    @execution_broker.setter
    def execution_broker(self, execution_broker):
        """Sets the execution_broker of this FeeRuleUpsertRequest.


        :param execution_broker: The execution_broker of this FeeRuleUpsertRequest.  # noqa: E501
        :type execution_broker: str
        """
        if self.local_vars_configuration.client_side_validation and execution_broker is None:  # noqa: E501
            raise ValueError("Invalid value for `execution_broker`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                execution_broker is not None and len(execution_broker) > 64):
            raise ValueError("Invalid value for `execution_broker`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                execution_broker is not None and len(execution_broker) < 1):
            raise ValueError("Invalid value for `execution_broker`, length must be greater than or equal to `1`")  # noqa: E501

        self._execution_broker = execution_broker

    @property
    def custodian(self):
        """Gets the custodian of this FeeRuleUpsertRequest.  # noqa: E501


        :return: The custodian of this FeeRuleUpsertRequest.  # noqa: E501
        :rtype: str
        """
        return self._custodian

    @custodian.setter
    def custodian(self, custodian):
        """Sets the custodian of this FeeRuleUpsertRequest.


        :param custodian: The custodian of this FeeRuleUpsertRequest.  # noqa: E501
        :type custodian: str
        """
        if self.local_vars_configuration.client_side_validation and custodian is None:  # noqa: E501
            raise ValueError("Invalid value for `custodian`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                custodian is not None and len(custodian) > 64):
            raise ValueError("Invalid value for `custodian`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                custodian is not None and len(custodian) < 1):
            raise ValueError("Invalid value for `custodian`, length must be greater than or equal to `1`")  # noqa: E501

        self._custodian = custodian

    @property
    def exchange(self):
        """Gets the exchange of this FeeRuleUpsertRequest.  # noqa: E501


        :return: The exchange of this FeeRuleUpsertRequest.  # noqa: E501
        :rtype: str
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this FeeRuleUpsertRequest.


        :param exchange: The exchange of this FeeRuleUpsertRequest.  # noqa: E501
        :type exchange: str
        """
        if self.local_vars_configuration.client_side_validation and exchange is None:  # noqa: E501
            raise ValueError("Invalid value for `exchange`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                exchange is not None and len(exchange) > 64):
            raise ValueError("Invalid value for `exchange`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                exchange is not None and len(exchange) < 1):
            raise ValueError("Invalid value for `exchange`, length must be greater than or equal to `1`")  # noqa: E501

        self._exchange = exchange

    @property
    def fee(self):
        """Gets the fee of this FeeRuleUpsertRequest.  # noqa: E501


        :return: The fee of this FeeRuleUpsertRequest.  # noqa: E501
        :rtype: lusid.CalculationInfo
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this FeeRuleUpsertRequest.


        :param fee: The fee of this FeeRuleUpsertRequest.  # noqa: E501
        :type fee: lusid.CalculationInfo
        """
        if self.local_vars_configuration.client_side_validation and fee is None:  # noqa: E501
            raise ValueError("Invalid value for `fee`, must not be `None`")  # noqa: E501

        self._fee = fee

    @property
    def min_fee(self):
        """Gets the min_fee of this FeeRuleUpsertRequest.  # noqa: E501


        :return: The min_fee of this FeeRuleUpsertRequest.  # noqa: E501
        :rtype: lusid.CalculationInfo
        """
        return self._min_fee

    @min_fee.setter
    def min_fee(self, min_fee):
        """Sets the min_fee of this FeeRuleUpsertRequest.


        :param min_fee: The min_fee of this FeeRuleUpsertRequest.  # noqa: E501
        :type min_fee: lusid.CalculationInfo
        """

        self._min_fee = min_fee

    @property
    def max_fee(self):
        """Gets the max_fee of this FeeRuleUpsertRequest.  # noqa: E501


        :return: The max_fee of this FeeRuleUpsertRequest.  # noqa: E501
        :rtype: lusid.CalculationInfo
        """
        return self._max_fee

    @max_fee.setter
    def max_fee(self, max_fee):
        """Sets the max_fee of this FeeRuleUpsertRequest.


        :param max_fee: The max_fee of this FeeRuleUpsertRequest.  # noqa: E501
        :type max_fee: lusid.CalculationInfo
        """

        self._max_fee = max_fee

    @property
    def additional_keys(self):
        """Gets the additional_keys of this FeeRuleUpsertRequest.  # noqa: E501


        :return: The additional_keys of this FeeRuleUpsertRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._additional_keys

    @additional_keys.setter
    def additional_keys(self, additional_keys):
        """Sets the additional_keys of this FeeRuleUpsertRequest.


        :param additional_keys: The additional_keys of this FeeRuleUpsertRequest.  # noqa: E501
        :type additional_keys: dict(str, str)
        """

        self._additional_keys = additional_keys

    @property
    def description(self):
        """Gets the description of this FeeRuleUpsertRequest.  # noqa: E501


        :return: The description of this FeeRuleUpsertRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FeeRuleUpsertRequest.


        :param description: The description of this FeeRuleUpsertRequest.  # noqa: E501
        :type description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 1024):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and not re.search(r'^[\s\S]*$', description)):  # noqa: E501
            raise ValueError(r"Invalid value for `description`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._description = description

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FeeRuleUpsertRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FeeRuleUpsertRequest):
            return True

        return self.to_dict() != other.to_dict()
