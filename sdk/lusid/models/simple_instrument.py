# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4044
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


class SimpleInstrument(object):
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
        'maturity_date': 'datetime',
        'dom_ccy': 'str',
        'asset_class': 'str',
        'fgn_ccys': 'list[str]',
        'simple_instrument_type': 'str',
        'instrument_type': 'str'
    }

    attribute_map = {
        'maturity_date': 'maturityDate',
        'dom_ccy': 'domCcy',
        'asset_class': 'assetClass',
        'fgn_ccys': 'fgnCcys',
        'simple_instrument_type': 'simpleInstrumentType',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'maturity_date': 'optional',
        'dom_ccy': 'required',
        'asset_class': 'required',
        'fgn_ccys': 'optional',
        'simple_instrument_type': 'required',
        'instrument_type': 'required'
    }

    def __init__(self, maturity_date=None, dom_ccy=None, asset_class=None, fgn_ccys=None, simple_instrument_type=None, instrument_type=None, local_vars_configuration=None):  # noqa: E501
        """SimpleInstrument - a model defined in OpenAPI"
        
        :param maturity_date:  The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date.
        :type maturity_date: datetime
        :param dom_ccy:  The domestic currency. (required)
        :type dom_ccy: str
        :param asset_class:  The available values are: InterestRates, FX, Inflation, Equities, Credit, Commodities, Money, Unknown (required)
        :type asset_class: str
        :param fgn_ccys:  The set of foreign currencies, if any (optional).
        :type fgn_ccys: list[str]
        :param simple_instrument_type:  The Instrument type of the simple instrument. (required)
        :type simple_instrument_type: str
        :param instrument_type:  The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption (required)
        :type instrument_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._maturity_date = None
        self._dom_ccy = None
        self._asset_class = None
        self._fgn_ccys = None
        self._simple_instrument_type = None
        self._instrument_type = None
        self.discriminator = None

        if maturity_date is not None:
            self.maturity_date = maturity_date
        self.dom_ccy = dom_ccy
        self.asset_class = asset_class
        self.fgn_ccys = fgn_ccys
        self.simple_instrument_type = simple_instrument_type
        self.instrument_type = instrument_type

    @property
    def maturity_date(self):
        """Gets the maturity_date of this SimpleInstrument.  # noqa: E501

        The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date.  # noqa: E501

        :return: The maturity_date of this SimpleInstrument.  # noqa: E501
        :rtype: datetime
        """
        return self._maturity_date

    @maturity_date.setter
    def maturity_date(self, maturity_date):
        """Sets the maturity_date of this SimpleInstrument.

        The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.  For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as  Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date.  # noqa: E501

        :param maturity_date: The maturity_date of this SimpleInstrument.  # noqa: E501
        :type maturity_date: datetime
        """

        self._maturity_date = maturity_date

    @property
    def dom_ccy(self):
        """Gets the dom_ccy of this SimpleInstrument.  # noqa: E501

        The domestic currency.  # noqa: E501

        :return: The dom_ccy of this SimpleInstrument.  # noqa: E501
        :rtype: str
        """
        return self._dom_ccy

    @dom_ccy.setter
    def dom_ccy(self, dom_ccy):
        """Sets the dom_ccy of this SimpleInstrument.

        The domestic currency.  # noqa: E501

        :param dom_ccy: The dom_ccy of this SimpleInstrument.  # noqa: E501
        :type dom_ccy: str
        """
        if self.local_vars_configuration.client_side_validation and dom_ccy is None:  # noqa: E501
            raise ValueError("Invalid value for `dom_ccy`, must not be `None`")  # noqa: E501

        self._dom_ccy = dom_ccy

    @property
    def asset_class(self):
        """Gets the asset_class of this SimpleInstrument.  # noqa: E501

        The available values are: InterestRates, FX, Inflation, Equities, Credit, Commodities, Money, Unknown  # noqa: E501

        :return: The asset_class of this SimpleInstrument.  # noqa: E501
        :rtype: str
        """
        return self._asset_class

    @asset_class.setter
    def asset_class(self, asset_class):
        """Sets the asset_class of this SimpleInstrument.

        The available values are: InterestRates, FX, Inflation, Equities, Credit, Commodities, Money, Unknown  # noqa: E501

        :param asset_class: The asset_class of this SimpleInstrument.  # noqa: E501
        :type asset_class: str
        """
        if self.local_vars_configuration.client_side_validation and asset_class is None:  # noqa: E501
            raise ValueError("Invalid value for `asset_class`, must not be `None`")  # noqa: E501
        allowed_values = ["InterestRates", "FX", "Inflation", "Equities", "Credit", "Commodities", "Money", "Unknown"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and asset_class not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `asset_class` ({0}), must be one of {1}"  # noqa: E501
                .format(asset_class, allowed_values)
            )

        self._asset_class = asset_class

    @property
    def fgn_ccys(self):
        """Gets the fgn_ccys of this SimpleInstrument.  # noqa: E501

        The set of foreign currencies, if any (optional).  # noqa: E501

        :return: The fgn_ccys of this SimpleInstrument.  # noqa: E501
        :rtype: list[str]
        """
        return self._fgn_ccys

    @fgn_ccys.setter
    def fgn_ccys(self, fgn_ccys):
        """Sets the fgn_ccys of this SimpleInstrument.

        The set of foreign currencies, if any (optional).  # noqa: E501

        :param fgn_ccys: The fgn_ccys of this SimpleInstrument.  # noqa: E501
        :type fgn_ccys: list[str]
        """

        self._fgn_ccys = fgn_ccys

    @property
    def simple_instrument_type(self):
        """Gets the simple_instrument_type of this SimpleInstrument.  # noqa: E501

        The Instrument type of the simple instrument.  # noqa: E501

        :return: The simple_instrument_type of this SimpleInstrument.  # noqa: E501
        :rtype: str
        """
        return self._simple_instrument_type

    @simple_instrument_type.setter
    def simple_instrument_type(self, simple_instrument_type):
        """Sets the simple_instrument_type of this SimpleInstrument.

        The Instrument type of the simple instrument.  # noqa: E501

        :param simple_instrument_type: The simple_instrument_type of this SimpleInstrument.  # noqa: E501
        :type simple_instrument_type: str
        """
        if self.local_vars_configuration.client_side_validation and simple_instrument_type is None:  # noqa: E501
            raise ValueError("Invalid value for `simple_instrument_type`, must not be `None`")  # noqa: E501

        self._simple_instrument_type = simple_instrument_type

    @property
    def instrument_type(self):
        """Gets the instrument_type of this SimpleInstrument.  # noqa: E501

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption  # noqa: E501

        :return: The instrument_type of this SimpleInstrument.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this SimpleInstrument.

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashFlowsLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap, CashPerpetual, CapFloor, CashSettled, CdsIndex, Basket, FundingLeg, FxSwap, ForwardRateAgreement, SimpleInstrument, Repo, Equity, ExchangeTradedOption  # noqa: E501

        :param instrument_type: The instrument_type of this SimpleInstrument.  # noqa: E501
        :type instrument_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501
        allowed_values = ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashFlowsLeg", "Unknown", "TermDeposit", "ContractForDifference", "EquitySwap", "CashPerpetual", "CapFloor", "CashSettled", "CdsIndex", "Basket", "FundingLeg", "FxSwap", "ForwardRateAgreement", "SimpleInstrument", "Repo", "Equity", "ExchangeTradedOption"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and instrument_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `instrument_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instrument_type, allowed_values)
            )

        self._instrument_type = instrument_type

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
        if not isinstance(other, SimpleInstrument):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimpleInstrument):
            return True

        return self.to_dict() != other.to_dict()
