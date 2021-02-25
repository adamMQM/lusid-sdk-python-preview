# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2646
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class CreditDefaultSwap(object):
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
        'ticker': 'str',
        'start_date': 'datetime',
        'maturity_date': 'datetime',
        'flow_conventions': 'CdsFlowConventions',
        'coupon_rate': 'float',
        'protection_detail_specification': 'CdsProtectionDetailSpecification',
        'instrument_type': 'str'
    }

    attribute_map = {
        'ticker': 'ticker',
        'start_date': 'startDate',
        'maturity_date': 'maturityDate',
        'flow_conventions': 'flowConventions',
        'coupon_rate': 'couponRate',
        'protection_detail_specification': 'protectionDetailSpecification',
        'instrument_type': 'instrumentType'
    }

    required_map = {
        'ticker': 'required',
        'start_date': 'required',
        'maturity_date': 'required',
        'flow_conventions': 'required',
        'coupon_rate': 'required',
        'protection_detail_specification': 'required',
        'instrument_type': 'required'
    }

    def __init__(self, ticker=None, start_date=None, maturity_date=None, flow_conventions=None, coupon_rate=None, protection_detail_specification=None, instrument_type=None):  # noqa: E501
        """
        CreditDefaultSwap - a model defined in OpenAPI

        :param ticker:  A ticker to uniquely specify then entity against which the cds is written (required)
        :type ticker: str
        :param start_date:  The start date of the instrument. This is normally synonymous with the trade-date. (required)
        :type start_date: datetime
        :param maturity_date:  The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.              For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as              Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date (required)
        :type maturity_date: datetime
        :param flow_conventions:  (required)
        :type flow_conventions: lusid.CdsFlowConventions
        :param coupon_rate:  The coupon rate paid on each payment date of the premium leg as a fraction of 100 percent, e.g. \"0.05\" meaning 500 basis points or 5%.              For a standard corporate CDS (North American) this must be either 100bps or 500bps. (required)
        :type coupon_rate: float
        :param protection_detail_specification:  (required)
        :type protection_detail_specification: lusid.CdsProtectionDetailSpecification
        :param instrument_type:  The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashflowLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap (required)
        :type instrument_type: str

        """  # noqa: E501

        self._ticker = None
        self._start_date = None
        self._maturity_date = None
        self._flow_conventions = None
        self._coupon_rate = None
        self._protection_detail_specification = None
        self._instrument_type = None
        self.discriminator = None

        self.ticker = ticker
        self.start_date = start_date
        self.maturity_date = maturity_date
        self.flow_conventions = flow_conventions
        self.coupon_rate = coupon_rate
        self.protection_detail_specification = protection_detail_specification
        self.instrument_type = instrument_type

    @property
    def ticker(self):
        """Gets the ticker of this CreditDefaultSwap.  # noqa: E501

        A ticker to uniquely specify then entity against which the cds is written  # noqa: E501

        :return: The ticker of this CreditDefaultSwap.  # noqa: E501
        :rtype: str
        """
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        """Sets the ticker of this CreditDefaultSwap.

        A ticker to uniquely specify then entity against which the cds is written  # noqa: E501

        :param ticker: The ticker of this CreditDefaultSwap.  # noqa: E501
        :type: str
        """
        if ticker is None:
            raise ValueError("Invalid value for `ticker`, must not be `None`")  # noqa: E501

        self._ticker = ticker

    @property
    def start_date(self):
        """Gets the start_date of this CreditDefaultSwap.  # noqa: E501

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :return: The start_date of this CreditDefaultSwap.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this CreditDefaultSwap.

        The start date of the instrument. This is normally synonymous with the trade-date.  # noqa: E501

        :param start_date: The start_date of this CreditDefaultSwap.  # noqa: E501
        :type: datetime
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def maturity_date(self):
        """Gets the maturity_date of this CreditDefaultSwap.  # noqa: E501

        The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.              For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as              Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date  # noqa: E501

        :return: The maturity_date of this CreditDefaultSwap.  # noqa: E501
        :rtype: datetime
        """
        return self._maturity_date

    @maturity_date.setter
    def maturity_date(self, maturity_date):
        """Sets the maturity_date of this CreditDefaultSwap.

        The final maturity date of the instrument. This means the last date on which the instruments makes a payment of any amount.              For the avoidance of doubt, that is not necessarily prior to its last sensitivity date for the purposes of risk; e.g. instruments such as              Constant Maturity Swaps (CMS) often have sensitivities to rates beyond their last payment date  # noqa: E501

        :param maturity_date: The maturity_date of this CreditDefaultSwap.  # noqa: E501
        :type: datetime
        """
        if maturity_date is None:
            raise ValueError("Invalid value for `maturity_date`, must not be `None`")  # noqa: E501

        self._maturity_date = maturity_date

    @property
    def flow_conventions(self):
        """Gets the flow_conventions of this CreditDefaultSwap.  # noqa: E501


        :return: The flow_conventions of this CreditDefaultSwap.  # noqa: E501
        :rtype: CdsFlowConventions
        """
        return self._flow_conventions

    @flow_conventions.setter
    def flow_conventions(self, flow_conventions):
        """Sets the flow_conventions of this CreditDefaultSwap.


        :param flow_conventions: The flow_conventions of this CreditDefaultSwap.  # noqa: E501
        :type: CdsFlowConventions
        """
        if flow_conventions is None:
            raise ValueError("Invalid value for `flow_conventions`, must not be `None`")  # noqa: E501

        self._flow_conventions = flow_conventions

    @property
    def coupon_rate(self):
        """Gets the coupon_rate of this CreditDefaultSwap.  # noqa: E501

        The coupon rate paid on each payment date of the premium leg as a fraction of 100 percent, e.g. \"0.05\" meaning 500 basis points or 5%.              For a standard corporate CDS (North American) this must be either 100bps or 500bps.  # noqa: E501

        :return: The coupon_rate of this CreditDefaultSwap.  # noqa: E501
        :rtype: float
        """
        return self._coupon_rate

    @coupon_rate.setter
    def coupon_rate(self, coupon_rate):
        """Sets the coupon_rate of this CreditDefaultSwap.

        The coupon rate paid on each payment date of the premium leg as a fraction of 100 percent, e.g. \"0.05\" meaning 500 basis points or 5%.              For a standard corporate CDS (North American) this must be either 100bps or 500bps.  # noqa: E501

        :param coupon_rate: The coupon_rate of this CreditDefaultSwap.  # noqa: E501
        :type: float
        """
        if coupon_rate is None:
            raise ValueError("Invalid value for `coupon_rate`, must not be `None`")  # noqa: E501

        self._coupon_rate = coupon_rate

    @property
    def protection_detail_specification(self):
        """Gets the protection_detail_specification of this CreditDefaultSwap.  # noqa: E501


        :return: The protection_detail_specification of this CreditDefaultSwap.  # noqa: E501
        :rtype: CdsProtectionDetailSpecification
        """
        return self._protection_detail_specification

    @protection_detail_specification.setter
    def protection_detail_specification(self, protection_detail_specification):
        """Sets the protection_detail_specification of this CreditDefaultSwap.


        :param protection_detail_specification: The protection_detail_specification of this CreditDefaultSwap.  # noqa: E501
        :type: CdsProtectionDetailSpecification
        """
        if protection_detail_specification is None:
            raise ValueError("Invalid value for `protection_detail_specification`, must not be `None`")  # noqa: E501

        self._protection_detail_specification = protection_detail_specification

    @property
    def instrument_type(self):
        """Gets the instrument_type of this CreditDefaultSwap.  # noqa: E501

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashflowLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap  # noqa: E501

        :return: The instrument_type of this CreditDefaultSwap.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this CreditDefaultSwap.

        The available values are: QuotedSecurity, InterestRateSwap, FxForward, Future, ExoticInstrument, FxOption, CreditDefaultSwap, InterestRateSwaption, Bond, EquityOption, FixedLeg, FloatingLeg, BespokeCashflowLeg, Unknown, TermDeposit, ContractForDifference, EquitySwap  # noqa: E501

        :param instrument_type: The instrument_type of this CreditDefaultSwap.  # noqa: E501
        :type: str
        """
        if instrument_type is None:
            raise ValueError("Invalid value for `instrument_type`, must not be `None`")  # noqa: E501
        allowed_values = ["QuotedSecurity", "InterestRateSwap", "FxForward", "Future", "ExoticInstrument", "FxOption", "CreditDefaultSwap", "InterestRateSwaption", "Bond", "EquityOption", "FixedLeg", "FloatingLeg", "BespokeCashflowLeg", "Unknown", "TermDeposit", "ContractForDifference", "EquitySwap"]  # noqa: E501
        if instrument_type not in allowed_values:
            raise ValueError(
                "Invalid value for `instrument_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instrument_type, allowed_values)
            )

        self._instrument_type = instrument_type

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
        if not isinstance(other, CreditDefaultSwap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
