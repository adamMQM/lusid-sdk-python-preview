# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4017
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


class CreditSpreadCurveDataAllOf(object):
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
        'base_date': 'datetime',
        'dom_ccy': 'str',
        'tenors': 'list[str]',
        'spreads': 'list[float]',
        'recovery_rate': 'float',
        'reference_date': 'datetime',
        'maturities': 'list[datetime]',
        'market_data_type': 'str'
    }

    attribute_map = {
        'base_date': 'baseDate',
        'dom_ccy': 'domCcy',
        'tenors': 'tenors',
        'spreads': 'spreads',
        'recovery_rate': 'recoveryRate',
        'reference_date': 'referenceDate',
        'maturities': 'maturities',
        'market_data_type': 'marketDataType'
    }

    required_map = {
        'base_date': 'required',
        'dom_ccy': 'required',
        'tenors': 'required',
        'spreads': 'required',
        'recovery_rate': 'required',
        'reference_date': 'optional',
        'maturities': 'optional',
        'market_data_type': 'required'
    }

    def __init__(self, base_date=None, dom_ccy=None, tenors=None, spreads=None, recovery_rate=None, reference_date=None, maturities=None, market_data_type=None, local_vars_configuration=None):  # noqa: E501
        """CreditSpreadCurveDataAllOf - a model defined in OpenAPI"
        
        :param base_date:  EffectiveAt date of the quoted rates (required)
        :type base_date: datetime
        :param dom_ccy:  Domestic currency of the curve (required)
        :type dom_ccy: str
        :param tenors:  The tenors for which the rates apply (required)
        :type tenors: list[str]
        :param spreads:  Par spread quotes corresponding to the tenors. (required)
        :type spreads: list[float]
        :param recovery_rate:  The recovery rate in default. (required)
        :type recovery_rate: float
        :param reference_date:  If tenors are provided, this is the date against which the tenors will be resolved.  This is of importance to CDX spread quotes, which are usually quoted in tenors relative to the CDX start date.  In this case, the ReferenceDate would be equal to the CDX start date, and the BaseDate would be the date for which the spreads are valid.  If not provided, this defaults to the BaseDate of the curve.
        :type reference_date: datetime
        :param maturities:  The maturity dates for which the rates apply.  Either tenors or maturities should be provided, not both.
        :type maturities: list[datetime]
        :param market_data_type:  The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData (required)
        :type market_data_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._base_date = None
        self._dom_ccy = None
        self._tenors = None
        self._spreads = None
        self._recovery_rate = None
        self._reference_date = None
        self._maturities = None
        self._market_data_type = None
        self.discriminator = None

        self.base_date = base_date
        self.dom_ccy = dom_ccy
        self.tenors = tenors
        self.spreads = spreads
        self.recovery_rate = recovery_rate
        self.reference_date = reference_date
        self.maturities = maturities
        self.market_data_type = market_data_type

    @property
    def base_date(self):
        """Gets the base_date of this CreditSpreadCurveDataAllOf.  # noqa: E501

        EffectiveAt date of the quoted rates  # noqa: E501

        :return: The base_date of this CreditSpreadCurveDataAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._base_date

    @base_date.setter
    def base_date(self, base_date):
        """Sets the base_date of this CreditSpreadCurveDataAllOf.

        EffectiveAt date of the quoted rates  # noqa: E501

        :param base_date: The base_date of this CreditSpreadCurveDataAllOf.  # noqa: E501
        :type base_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and base_date is None:  # noqa: E501
            raise ValueError("Invalid value for `base_date`, must not be `None`")  # noqa: E501

        self._base_date = base_date

    @property
    def dom_ccy(self):
        """Gets the dom_ccy of this CreditSpreadCurveDataAllOf.  # noqa: E501

        Domestic currency of the curve  # noqa: E501

        :return: The dom_ccy of this CreditSpreadCurveDataAllOf.  # noqa: E501
        :rtype: str
        """
        return self._dom_ccy

    @dom_ccy.setter
    def dom_ccy(self, dom_ccy):
        """Sets the dom_ccy of this CreditSpreadCurveDataAllOf.

        Domestic currency of the curve  # noqa: E501

        :param dom_ccy: The dom_ccy of this CreditSpreadCurveDataAllOf.  # noqa: E501
        :type dom_ccy: str
        """
        if self.local_vars_configuration.client_side_validation and dom_ccy is None:  # noqa: E501
            raise ValueError("Invalid value for `dom_ccy`, must not be `None`")  # noqa: E501

        self._dom_ccy = dom_ccy

    @property
    def tenors(self):
        """Gets the tenors of this CreditSpreadCurveDataAllOf.  # noqa: E501

        The tenors for which the rates apply  # noqa: E501

        :return: The tenors of this CreditSpreadCurveDataAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._tenors

    @tenors.setter
    def tenors(self, tenors):
        """Sets the tenors of this CreditSpreadCurveDataAllOf.

        The tenors for which the rates apply  # noqa: E501

        :param tenors: The tenors of this CreditSpreadCurveDataAllOf.  # noqa: E501
        :type tenors: list[str]
        """
        if self.local_vars_configuration.client_side_validation and tenors is None:  # noqa: E501
            raise ValueError("Invalid value for `tenors`, must not be `None`")  # noqa: E501

        self._tenors = tenors

    @property
    def spreads(self):
        """Gets the spreads of this CreditSpreadCurveDataAllOf.  # noqa: E501

        Par spread quotes corresponding to the tenors.  # noqa: E501

        :return: The spreads of this CreditSpreadCurveDataAllOf.  # noqa: E501
        :rtype: list[float]
        """
        return self._spreads

    @spreads.setter
    def spreads(self, spreads):
        """Sets the spreads of this CreditSpreadCurveDataAllOf.

        Par spread quotes corresponding to the tenors.  # noqa: E501

        :param spreads: The spreads of this CreditSpreadCurveDataAllOf.  # noqa: E501
        :type spreads: list[float]
        """
        if self.local_vars_configuration.client_side_validation and spreads is None:  # noqa: E501
            raise ValueError("Invalid value for `spreads`, must not be `None`")  # noqa: E501

        self._spreads = spreads

    @property
    def recovery_rate(self):
        """Gets the recovery_rate of this CreditSpreadCurveDataAllOf.  # noqa: E501

        The recovery rate in default.  # noqa: E501

        :return: The recovery_rate of this CreditSpreadCurveDataAllOf.  # noqa: E501
        :rtype: float
        """
        return self._recovery_rate

    @recovery_rate.setter
    def recovery_rate(self, recovery_rate):
        """Sets the recovery_rate of this CreditSpreadCurveDataAllOf.

        The recovery rate in default.  # noqa: E501

        :param recovery_rate: The recovery_rate of this CreditSpreadCurveDataAllOf.  # noqa: E501
        :type recovery_rate: float
        """
        if self.local_vars_configuration.client_side_validation and recovery_rate is None:  # noqa: E501
            raise ValueError("Invalid value for `recovery_rate`, must not be `None`")  # noqa: E501

        self._recovery_rate = recovery_rate

    @property
    def reference_date(self):
        """Gets the reference_date of this CreditSpreadCurveDataAllOf.  # noqa: E501

        If tenors are provided, this is the date against which the tenors will be resolved.  This is of importance to CDX spread quotes, which are usually quoted in tenors relative to the CDX start date.  In this case, the ReferenceDate would be equal to the CDX start date, and the BaseDate would be the date for which the spreads are valid.  If not provided, this defaults to the BaseDate of the curve.  # noqa: E501

        :return: The reference_date of this CreditSpreadCurveDataAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._reference_date

    @reference_date.setter
    def reference_date(self, reference_date):
        """Sets the reference_date of this CreditSpreadCurveDataAllOf.

        If tenors are provided, this is the date against which the tenors will be resolved.  This is of importance to CDX spread quotes, which are usually quoted in tenors relative to the CDX start date.  In this case, the ReferenceDate would be equal to the CDX start date, and the BaseDate would be the date for which the spreads are valid.  If not provided, this defaults to the BaseDate of the curve.  # noqa: E501

        :param reference_date: The reference_date of this CreditSpreadCurveDataAllOf.  # noqa: E501
        :type reference_date: datetime
        """

        self._reference_date = reference_date

    @property
    def maturities(self):
        """Gets the maturities of this CreditSpreadCurveDataAllOf.  # noqa: E501

        The maturity dates for which the rates apply.  Either tenors or maturities should be provided, not both.  # noqa: E501

        :return: The maturities of this CreditSpreadCurveDataAllOf.  # noqa: E501
        :rtype: list[datetime]
        """
        return self._maturities

    @maturities.setter
    def maturities(self, maturities):
        """Sets the maturities of this CreditSpreadCurveDataAllOf.

        The maturity dates for which the rates apply.  Either tenors or maturities should be provided, not both.  # noqa: E501

        :param maturities: The maturities of this CreditSpreadCurveDataAllOf.  # noqa: E501
        :type maturities: list[datetime]
        """

        self._maturities = maturities

    @property
    def market_data_type(self):
        """Gets the market_data_type of this CreditSpreadCurveDataAllOf.  # noqa: E501

        The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData  # noqa: E501

        :return: The market_data_type of this CreditSpreadCurveDataAllOf.  # noqa: E501
        :rtype: str
        """
        return self._market_data_type

    @market_data_type.setter
    def market_data_type(self, market_data_type):
        """Sets the market_data_type of this CreditSpreadCurveDataAllOf.

        The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData  # noqa: E501

        :param market_data_type: The market_data_type of this CreditSpreadCurveDataAllOf.  # noqa: E501
        :type market_data_type: str
        """
        if self.local_vars_configuration.client_side_validation and market_data_type is None:  # noqa: E501
            raise ValueError("Invalid value for `market_data_type`, must not be `None`")  # noqa: E501
        allowed_values = ["DiscountFactorCurveData", "EquityVolSurfaceData", "FxVolSurfaceData", "IrVolCubeData", "OpaqueMarketData", "YieldCurveData", "FxForwardCurveData", "FxForwardPipsCurveData", "FxForwardTenorCurveData", "FxForwardTenorPipsCurveData", "FxForwardCurveByQuoteReference", "CreditSpreadCurveData"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and market_data_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `market_data_type` ({0}), must be one of {1}"  # noqa: E501
                .format(market_data_type, allowed_values)
            )

        self._market_data_type = market_data_type

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
        if not isinstance(other, CreditSpreadCurveDataAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreditSpreadCurveDataAllOf):
            return True

        return self.to_dict() != other.to_dict()
