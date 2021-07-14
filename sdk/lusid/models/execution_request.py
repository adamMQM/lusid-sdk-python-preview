# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3264
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class ExecutionRequest(object):
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
        'id': 'ResourceId',
        'placement_id': 'ResourceId',
        'properties': 'dict(str, PerpetualProperty)',
        'instrument_identifiers': 'dict(str, str)',
        'quantity': 'float',
        'state': 'str',
        'side': 'str',
        'type': 'str',
        'created_date': 'datetime',
        'settlement_date': 'datetime',
        'price': 'CurrencyAndAmount',
        'settlement_currency': 'str',
        'settlement_currency_fx_rate': 'float',
        'counterparty': 'str'
    }

    attribute_map = {
        'id': 'id',
        'placement_id': 'placementId',
        'properties': 'properties',
        'instrument_identifiers': 'instrumentIdentifiers',
        'quantity': 'quantity',
        'state': 'state',
        'side': 'side',
        'type': 'type',
        'created_date': 'createdDate',
        'settlement_date': 'settlementDate',
        'price': 'price',
        'settlement_currency': 'settlementCurrency',
        'settlement_currency_fx_rate': 'settlementCurrencyFxRate',
        'counterparty': 'counterparty'
    }

    required_map = {
        'id': 'required',
        'placement_id': 'required',
        'properties': 'optional',
        'instrument_identifiers': 'required',
        'quantity': 'required',
        'state': 'required',
        'side': 'required',
        'type': 'required',
        'created_date': 'required',
        'settlement_date': 'optional',
        'price': 'required',
        'settlement_currency': 'required',
        'settlement_currency_fx_rate': 'required',
        'counterparty': 'required'
    }

    def __init__(self, id=None, placement_id=None, properties=None, instrument_identifiers=None, quantity=None, state=None, side=None, type=None, created_date=None, settlement_date=None, price=None, settlement_currency=None, settlement_currency_fx_rate=None, counterparty=None):  # noqa: E501
        """
        ExecutionRequest - a model defined in OpenAPI

        :param id:  (required)
        :type id: lusid.ResourceId
        :param placement_id:  (required)
        :type placement_id: lusid.ResourceId
        :param properties:  Client-defined properties associated with this execution.
        :type properties: dict[str, lusid.PerpetualProperty]
        :param instrument_identifiers:  The instrument ordered. (required)
        :type instrument_identifiers: dict(str, str)
        :param quantity:  The quantity of given instrument ordered. (required)
        :type quantity: float
        :param state:  The state of this execution (typically a FIX state; Open, Filled, etc). (required)
        :type state: str
        :param side:  The side (Buy, Sell, ...) of this execution. (required)
        :type side: str
        :param type:  The type of this execution (Market, Limit, etc). (required)
        :type type: str
        :param created_date:  The active date of this execution. (required)
        :type created_date: datetime
        :param settlement_date:  The (optional) settlement date for this execution
        :type settlement_date: datetime
        :param price:  (required)
        :type price: lusid.CurrencyAndAmount
        :param settlement_currency:  The execution's settlement currency. (required)
        :type settlement_currency: str
        :param settlement_currency_fx_rate:  The exectuion's settlement currency rate. (required)
        :type settlement_currency_fx_rate: float
        :param counterparty:  The market entity this placement is placed with. (required)
        :type counterparty: str

        """  # noqa: E501

        self._id = None
        self._placement_id = None
        self._properties = None
        self._instrument_identifiers = None
        self._quantity = None
        self._state = None
        self._side = None
        self._type = None
        self._created_date = None
        self._settlement_date = None
        self._price = None
        self._settlement_currency = None
        self._settlement_currency_fx_rate = None
        self._counterparty = None
        self.discriminator = None

        self.id = id
        self.placement_id = placement_id
        self.properties = properties
        self.instrument_identifiers = instrument_identifiers
        self.quantity = quantity
        self.state = state
        self.side = side
        self.type = type
        self.created_date = created_date
        if settlement_date is not None:
            self.settlement_date = settlement_date
        self.price = price
        self.settlement_currency = settlement_currency
        self.settlement_currency_fx_rate = settlement_currency_fx_rate
        self.counterparty = counterparty

    @property
    def id(self):
        """Gets the id of this ExecutionRequest.  # noqa: E501


        :return: The id of this ExecutionRequest.  # noqa: E501
        :rtype: ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExecutionRequest.


        :param id: The id of this ExecutionRequest.  # noqa: E501
        :type: ResourceId
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def placement_id(self):
        """Gets the placement_id of this ExecutionRequest.  # noqa: E501


        :return: The placement_id of this ExecutionRequest.  # noqa: E501
        :rtype: ResourceId
        """
        return self._placement_id

    @placement_id.setter
    def placement_id(self, placement_id):
        """Sets the placement_id of this ExecutionRequest.


        :param placement_id: The placement_id of this ExecutionRequest.  # noqa: E501
        :type: ResourceId
        """
        if placement_id is None:
            raise ValueError("Invalid value for `placement_id`, must not be `None`")  # noqa: E501

        self._placement_id = placement_id

    @property
    def properties(self):
        """Gets the properties of this ExecutionRequest.  # noqa: E501

        Client-defined properties associated with this execution.  # noqa: E501

        :return: The properties of this ExecutionRequest.  # noqa: E501
        :rtype: dict(str, PerpetualProperty)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ExecutionRequest.

        Client-defined properties associated with this execution.  # noqa: E501

        :param properties: The properties of this ExecutionRequest.  # noqa: E501
        :type: dict(str, PerpetualProperty)
        """

        self._properties = properties

    @property
    def instrument_identifiers(self):
        """Gets the instrument_identifiers of this ExecutionRequest.  # noqa: E501

        The instrument ordered.  # noqa: E501

        :return: The instrument_identifiers of this ExecutionRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._instrument_identifiers

    @instrument_identifiers.setter
    def instrument_identifiers(self, instrument_identifiers):
        """Sets the instrument_identifiers of this ExecutionRequest.

        The instrument ordered.  # noqa: E501

        :param instrument_identifiers: The instrument_identifiers of this ExecutionRequest.  # noqa: E501
        :type: dict(str, str)
        """
        if instrument_identifiers is None:
            raise ValueError("Invalid value for `instrument_identifiers`, must not be `None`")  # noqa: E501

        self._instrument_identifiers = instrument_identifiers

    @property
    def quantity(self):
        """Gets the quantity of this ExecutionRequest.  # noqa: E501

        The quantity of given instrument ordered.  # noqa: E501

        :return: The quantity of this ExecutionRequest.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ExecutionRequest.

        The quantity of given instrument ordered.  # noqa: E501

        :param quantity: The quantity of this ExecutionRequest.  # noqa: E501
        :type: float
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def state(self):
        """Gets the state of this ExecutionRequest.  # noqa: E501

        The state of this execution (typically a FIX state; Open, Filled, etc).  # noqa: E501

        :return: The state of this ExecutionRequest.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ExecutionRequest.

        The state of this execution (typically a FIX state; Open, Filled, etc).  # noqa: E501

        :param state: The state of this ExecutionRequest.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def side(self):
        """Gets the side of this ExecutionRequest.  # noqa: E501

        The side (Buy, Sell, ...) of this execution.  # noqa: E501

        :return: The side of this ExecutionRequest.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this ExecutionRequest.

        The side (Buy, Sell, ...) of this execution.  # noqa: E501

        :param side: The side of this ExecutionRequest.  # noqa: E501
        :type: str
        """
        if side is None:
            raise ValueError("Invalid value for `side`, must not be `None`")  # noqa: E501

        self._side = side

    @property
    def type(self):
        """Gets the type of this ExecutionRequest.  # noqa: E501

        The type of this execution (Market, Limit, etc).  # noqa: E501

        :return: The type of this ExecutionRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExecutionRequest.

        The type of this execution (Market, Limit, etc).  # noqa: E501

        :param type: The type of this ExecutionRequest.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def created_date(self):
        """Gets the created_date of this ExecutionRequest.  # noqa: E501

        The active date of this execution.  # noqa: E501

        :return: The created_date of this ExecutionRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this ExecutionRequest.

        The active date of this execution.  # noqa: E501

        :param created_date: The created_date of this ExecutionRequest.  # noqa: E501
        :type: datetime
        """
        if created_date is None:
            raise ValueError("Invalid value for `created_date`, must not be `None`")  # noqa: E501

        self._created_date = created_date

    @property
    def settlement_date(self):
        """Gets the settlement_date of this ExecutionRequest.  # noqa: E501

        The (optional) settlement date for this execution  # noqa: E501

        :return: The settlement_date of this ExecutionRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, settlement_date):
        """Sets the settlement_date of this ExecutionRequest.

        The (optional) settlement date for this execution  # noqa: E501

        :param settlement_date: The settlement_date of this ExecutionRequest.  # noqa: E501
        :type: datetime
        """

        self._settlement_date = settlement_date

    @property
    def price(self):
        """Gets the price of this ExecutionRequest.  # noqa: E501


        :return: The price of this ExecutionRequest.  # noqa: E501
        :rtype: CurrencyAndAmount
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this ExecutionRequest.


        :param price: The price of this ExecutionRequest.  # noqa: E501
        :type: CurrencyAndAmount
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def settlement_currency(self):
        """Gets the settlement_currency of this ExecutionRequest.  # noqa: E501

        The execution's settlement currency.  # noqa: E501

        :return: The settlement_currency of this ExecutionRequest.  # noqa: E501
        :rtype: str
        """
        return self._settlement_currency

    @settlement_currency.setter
    def settlement_currency(self, settlement_currency):
        """Sets the settlement_currency of this ExecutionRequest.

        The execution's settlement currency.  # noqa: E501

        :param settlement_currency: The settlement_currency of this ExecutionRequest.  # noqa: E501
        :type: str
        """
        if settlement_currency is None:
            raise ValueError("Invalid value for `settlement_currency`, must not be `None`")  # noqa: E501

        self._settlement_currency = settlement_currency

    @property
    def settlement_currency_fx_rate(self):
        """Gets the settlement_currency_fx_rate of this ExecutionRequest.  # noqa: E501

        The exectuion's settlement currency rate.  # noqa: E501

        :return: The settlement_currency_fx_rate of this ExecutionRequest.  # noqa: E501
        :rtype: float
        """
        return self._settlement_currency_fx_rate

    @settlement_currency_fx_rate.setter
    def settlement_currency_fx_rate(self, settlement_currency_fx_rate):
        """Sets the settlement_currency_fx_rate of this ExecutionRequest.

        The exectuion's settlement currency rate.  # noqa: E501

        :param settlement_currency_fx_rate: The settlement_currency_fx_rate of this ExecutionRequest.  # noqa: E501
        :type: float
        """
        if settlement_currency_fx_rate is None:
            raise ValueError("Invalid value for `settlement_currency_fx_rate`, must not be `None`")  # noqa: E501

        self._settlement_currency_fx_rate = settlement_currency_fx_rate

    @property
    def counterparty(self):
        """Gets the counterparty of this ExecutionRequest.  # noqa: E501

        The market entity this placement is placed with.  # noqa: E501

        :return: The counterparty of this ExecutionRequest.  # noqa: E501
        :rtype: str
        """
        return self._counterparty

    @counterparty.setter
    def counterparty(self, counterparty):
        """Sets the counterparty of this ExecutionRequest.

        The market entity this placement is placed with.  # noqa: E501

        :param counterparty: The counterparty of this ExecutionRequest.  # noqa: E501
        :type: str
        """
        if counterparty is None:
            raise ValueError("Invalid value for `counterparty`, must not be `None`")  # noqa: E501

        self._counterparty = counterparty

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExecutionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
