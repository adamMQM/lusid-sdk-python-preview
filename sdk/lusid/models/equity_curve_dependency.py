# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4853
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


class EquityCurveDependency(object):
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
        'market_identifier': 'str',
        'code': 'str',
        'curve_type': 'str',
        'date': 'datetime',
        'dependency_type': 'str'
    }

    attribute_map = {
        'market_identifier': 'marketIdentifier',
        'code': 'code',
        'curve_type': 'curveType',
        'date': 'date',
        'dependency_type': 'dependencyType'
    }

    required_map = {
        'market_identifier': 'required',
        'code': 'required',
        'curve_type': 'required',
        'date': 'required',
        'dependency_type': 'required'
    }

    def __init__(self, market_identifier=None, code=None, curve_type=None, date=None, dependency_type=None, local_vars_configuration=None):  # noqa: E501
        """EquityCurveDependency - a model defined in OpenAPI"
        
        :param market_identifier:  Type of the code identifying the corresponding equity, e.g. ISIN or CUSIP (required)
        :type market_identifier: str
        :param code:  The code identifying the corresponding equity, e.g. US0378331005 if the MarketIdentifier was set to ISIN (required)
        :type code: str
        :param curve_type:  The curve type of the EquityCurve required. E.g. EquityCurveByPrices (required)
        :type curve_type: str
        :param date:  The effectiveDate of the entity that this is a dependency for.  Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date. (required)
        :type date: datetime
        :param dependency_type:  The available values are: Opaque, Cash, Discounting, EquityCurve, EquityVol, Fx, FxForwards, FxVol, IndexProjection, IrVol, Quote, Vendor (required)
        :type dependency_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._market_identifier = None
        self._code = None
        self._curve_type = None
        self._date = None
        self._dependency_type = None
        self.discriminator = None

        self.market_identifier = market_identifier
        self.code = code
        self.curve_type = curve_type
        self.date = date
        self.dependency_type = dependency_type

    @property
    def market_identifier(self):
        """Gets the market_identifier of this EquityCurveDependency.  # noqa: E501

        Type of the code identifying the corresponding equity, e.g. ISIN or CUSIP  # noqa: E501

        :return: The market_identifier of this EquityCurveDependency.  # noqa: E501
        :rtype: str
        """
        return self._market_identifier

    @market_identifier.setter
    def market_identifier(self, market_identifier):
        """Sets the market_identifier of this EquityCurveDependency.

        Type of the code identifying the corresponding equity, e.g. ISIN or CUSIP  # noqa: E501

        :param market_identifier: The market_identifier of this EquityCurveDependency.  # noqa: E501
        :type market_identifier: str
        """
        if self.local_vars_configuration.client_side_validation and market_identifier is None:  # noqa: E501
            raise ValueError("Invalid value for `market_identifier`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                market_identifier is not None and len(market_identifier) > 50):
            raise ValueError("Invalid value for `market_identifier`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                market_identifier is not None and len(market_identifier) < 0):
            raise ValueError("Invalid value for `market_identifier`, length must be greater than or equal to `0`")  # noqa: E501

        self._market_identifier = market_identifier

    @property
    def code(self):
        """Gets the code of this EquityCurveDependency.  # noqa: E501

        The code identifying the corresponding equity, e.g. US0378331005 if the MarketIdentifier was set to ISIN  # noqa: E501

        :return: The code of this EquityCurveDependency.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this EquityCurveDependency.

        The code identifying the corresponding equity, e.g. US0378331005 if the MarketIdentifier was set to ISIN  # noqa: E501

        :param code: The code of this EquityCurveDependency.  # noqa: E501
        :type code: str
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) > 50):
            raise ValueError("Invalid value for `code`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) < 0):
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `0`")  # noqa: E501

        self._code = code

    @property
    def curve_type(self):
        """Gets the curve_type of this EquityCurveDependency.  # noqa: E501

        The curve type of the EquityCurve required. E.g. EquityCurveByPrices  # noqa: E501

        :return: The curve_type of this EquityCurveDependency.  # noqa: E501
        :rtype: str
        """
        return self._curve_type

    @curve_type.setter
    def curve_type(self, curve_type):
        """Sets the curve_type of this EquityCurveDependency.

        The curve type of the EquityCurve required. E.g. EquityCurveByPrices  # noqa: E501

        :param curve_type: The curve_type of this EquityCurveDependency.  # noqa: E501
        :type curve_type: str
        """
        if self.local_vars_configuration.client_side_validation and curve_type is None:  # noqa: E501
            raise ValueError("Invalid value for `curve_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                curve_type is not None and len(curve_type) > 50):
            raise ValueError("Invalid value for `curve_type`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                curve_type is not None and len(curve_type) < 0):
            raise ValueError("Invalid value for `curve_type`, length must be greater than or equal to `0`")  # noqa: E501

        self._curve_type = curve_type

    @property
    def date(self):
        """Gets the date of this EquityCurveDependency.  # noqa: E501

        The effectiveDate of the entity that this is a dependency for.  Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date.  # noqa: E501

        :return: The date of this EquityCurveDependency.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this EquityCurveDependency.

        The effectiveDate of the entity that this is a dependency for.  Unless there is an obvious date this should be, like for a historic reset, then this is the valuation date.  # noqa: E501

        :param date: The date of this EquityCurveDependency.  # noqa: E501
        :type date: datetime
        """
        if self.local_vars_configuration.client_side_validation and date is None:  # noqa: E501
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def dependency_type(self):
        """Gets the dependency_type of this EquityCurveDependency.  # noqa: E501

        The available values are: Opaque, Cash, Discounting, EquityCurve, EquityVol, Fx, FxForwards, FxVol, IndexProjection, IrVol, Quote, Vendor  # noqa: E501

        :return: The dependency_type of this EquityCurveDependency.  # noqa: E501
        :rtype: str
        """
        return self._dependency_type

    @dependency_type.setter
    def dependency_type(self, dependency_type):
        """Sets the dependency_type of this EquityCurveDependency.

        The available values are: Opaque, Cash, Discounting, EquityCurve, EquityVol, Fx, FxForwards, FxVol, IndexProjection, IrVol, Quote, Vendor  # noqa: E501

        :param dependency_type: The dependency_type of this EquityCurveDependency.  # noqa: E501
        :type dependency_type: str
        """
        if self.local_vars_configuration.client_side_validation and dependency_type is None:  # noqa: E501
            raise ValueError("Invalid value for `dependency_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Opaque", "Cash", "Discounting", "EquityCurve", "EquityVol", "Fx", "FxForwards", "FxVol", "IndexProjection", "IrVol", "Quote", "Vendor"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and dependency_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `dependency_type` ({0}), must be one of {1}"  # noqa: E501
                .format(dependency_type, allowed_values)
            )

        self._dependency_type = dependency_type

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
        if not isinstance(other, EquityCurveDependency):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EquityCurveDependency):
            return True

        return self.to_dict() != other.to_dict()
