# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.5178
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


class FxRateSchedule(object):
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
        'fixing_lag': 'int',
        'fx_conversion_types': 'list[str]',
        'rate': 'float',
        'to_currency': 'str',
        'schedule_type': 'str'
    }

    attribute_map = {
        'fixing_lag': 'fixingLag',
        'fx_conversion_types': 'fxConversionTypes',
        'rate': 'rate',
        'to_currency': 'toCurrency',
        'schedule_type': 'scheduleType'
    }

    required_map = {
        'fixing_lag': 'optional',
        'fx_conversion_types': 'optional',
        'rate': 'optional',
        'to_currency': 'optional',
        'schedule_type': 'required'
    }

    def __init__(self, fixing_lag=None, fx_conversion_types=None, rate=None, to_currency=None, schedule_type=None, local_vars_configuration=None):  # noqa: E501
        """FxRateSchedule - a model defined in OpenAPI"
        
        :param fixing_lag:  If rate is not known upfront then will need a fixing rate. Can be fixed x number of days before payment date.
        :type fixing_lag: int
        :param fx_conversion_types:  List of flags to indicate if coupon payments, principal payments or both are converted
        :type fx_conversion_types: list[str]
        :param rate:  FxRate used to convert payments. Assumed to be in units of the ToCurrency so conversion is paymentAmount x fxRate
        :type rate: float
        :param to_currency:  Currency that payments are converted to
        :type to_currency: str
        :param schedule_type:  The available values are: Fixed, Float, Optionality, Step, Exercise, FxRate, Invalid (required)
        :type schedule_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._fixing_lag = None
        self._fx_conversion_types = None
        self._rate = None
        self._to_currency = None
        self._schedule_type = None
        self.discriminator = None

        if fixing_lag is not None:
            self.fixing_lag = fixing_lag
        self.fx_conversion_types = fx_conversion_types
        if rate is not None:
            self.rate = rate
        self.to_currency = to_currency
        self.schedule_type = schedule_type

    @property
    def fixing_lag(self):
        """Gets the fixing_lag of this FxRateSchedule.  # noqa: E501

        If rate is not known upfront then will need a fixing rate. Can be fixed x number of days before payment date.  # noqa: E501

        :return: The fixing_lag of this FxRateSchedule.  # noqa: E501
        :rtype: int
        """
        return self._fixing_lag

    @fixing_lag.setter
    def fixing_lag(self, fixing_lag):
        """Sets the fixing_lag of this FxRateSchedule.

        If rate is not known upfront then will need a fixing rate. Can be fixed x number of days before payment date.  # noqa: E501

        :param fixing_lag: The fixing_lag of this FxRateSchedule.  # noqa: E501
        :type fixing_lag: int
        """

        self._fixing_lag = fixing_lag

    @property
    def fx_conversion_types(self):
        """Gets the fx_conversion_types of this FxRateSchedule.  # noqa: E501

        List of flags to indicate if coupon payments, principal payments or both are converted  # noqa: E501

        :return: The fx_conversion_types of this FxRateSchedule.  # noqa: E501
        :rtype: list[str]
        """
        return self._fx_conversion_types

    @fx_conversion_types.setter
    def fx_conversion_types(self, fx_conversion_types):
        """Sets the fx_conversion_types of this FxRateSchedule.

        List of flags to indicate if coupon payments, principal payments or both are converted  # noqa: E501

        :param fx_conversion_types: The fx_conversion_types of this FxRateSchedule.  # noqa: E501
        :type fx_conversion_types: list[str]
        """

        self._fx_conversion_types = fx_conversion_types

    @property
    def rate(self):
        """Gets the rate of this FxRateSchedule.  # noqa: E501

        FxRate used to convert payments. Assumed to be in units of the ToCurrency so conversion is paymentAmount x fxRate  # noqa: E501

        :return: The rate of this FxRateSchedule.  # noqa: E501
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this FxRateSchedule.

        FxRate used to convert payments. Assumed to be in units of the ToCurrency so conversion is paymentAmount x fxRate  # noqa: E501

        :param rate: The rate of this FxRateSchedule.  # noqa: E501
        :type rate: float
        """

        self._rate = rate

    @property
    def to_currency(self):
        """Gets the to_currency of this FxRateSchedule.  # noqa: E501

        Currency that payments are converted to  # noqa: E501

        :return: The to_currency of this FxRateSchedule.  # noqa: E501
        :rtype: str
        """
        return self._to_currency

    @to_currency.setter
    def to_currency(self, to_currency):
        """Sets the to_currency of this FxRateSchedule.

        Currency that payments are converted to  # noqa: E501

        :param to_currency: The to_currency of this FxRateSchedule.  # noqa: E501
        :type to_currency: str
        """

        self._to_currency = to_currency

    @property
    def schedule_type(self):
        """Gets the schedule_type of this FxRateSchedule.  # noqa: E501

        The available values are: Fixed, Float, Optionality, Step, Exercise, FxRate, Invalid  # noqa: E501

        :return: The schedule_type of this FxRateSchedule.  # noqa: E501
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """Sets the schedule_type of this FxRateSchedule.

        The available values are: Fixed, Float, Optionality, Step, Exercise, FxRate, Invalid  # noqa: E501

        :param schedule_type: The schedule_type of this FxRateSchedule.  # noqa: E501
        :type schedule_type: str
        """
        if self.local_vars_configuration.client_side_validation and schedule_type is None:  # noqa: E501
            raise ValueError("Invalid value for `schedule_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Fixed", "Float", "Optionality", "Step", "Exercise", "FxRate", "Invalid"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and schedule_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `schedule_type` ({0}), must be one of {1}"  # noqa: E501
                .format(schedule_type, allowed_values)
            )

        self._schedule_type = schedule_type

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
        if not isinstance(other, FxRateSchedule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FxRateSchedule):
            return True

        return self.to_dict() != other.to_dict()
