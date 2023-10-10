# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.597
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


class TrialBalance(object):
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
        'general_ledger_account_code': 'str',
        'description': 'str',
        'levels': 'list[str]',
        'account_type': 'str',
        'opening': 'float',
        'closing': 'float',
        'debit': 'float',
        'credit': 'float',
        'links': 'list[Link]'
    }

    attribute_map = {
        'general_ledger_account_code': 'generalLedgerAccountCode',
        'description': 'description',
        'levels': 'levels',
        'account_type': 'accountType',
        'opening': 'opening',
        'closing': 'closing',
        'debit': 'debit',
        'credit': 'credit',
        'links': 'links'
    }

    required_map = {
        'general_ledger_account_code': 'required',
        'description': 'required',
        'levels': 'required',
        'account_type': 'required',
        'opening': 'required',
        'closing': 'required',
        'debit': 'required',
        'credit': 'required',
        'links': 'optional'
    }

    def __init__(self, general_ledger_account_code=None, description=None, levels=None, account_type=None, opening=None, closing=None, debit=None, credit=None, links=None, local_vars_configuration=None):  # noqa: E501
        """TrialBalance - a model defined in OpenAPI"
        
        :param general_ledger_account_code:  The Account code that the trial balance results have been grouped against (required)
        :type general_ledger_account_code: str
        :param description:  The description of the record (required)
        :type description: str
        :param levels:  The levels that have been derived from the specified General Ledger Profile (required)
        :type levels: list[str]
        :param account_type:  The account type attributed to the record (required)
        :type account_type: str
        :param opening:  The opening balance at the start of the period (required)
        :type opening: float
        :param closing:  The closing balance at the end of the period (required)
        :type closing: float
        :param debit:  All debits that occured in the period (required)
        :type debit: float
        :param credit:  All credits that occured in the period (required)
        :type credit: float
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._general_ledger_account_code = None
        self._description = None
        self._levels = None
        self._account_type = None
        self._opening = None
        self._closing = None
        self._debit = None
        self._credit = None
        self._links = None
        self.discriminator = None

        self.general_ledger_account_code = general_ledger_account_code
        self.description = description
        self.levels = levels
        self.account_type = account_type
        self.opening = opening
        self.closing = closing
        self.debit = debit
        self.credit = credit
        self.links = links

    @property
    def general_ledger_account_code(self):
        """Gets the general_ledger_account_code of this TrialBalance.  # noqa: E501

        The Account code that the trial balance results have been grouped against  # noqa: E501

        :return: The general_ledger_account_code of this TrialBalance.  # noqa: E501
        :rtype: str
        """
        return self._general_ledger_account_code

    @general_ledger_account_code.setter
    def general_ledger_account_code(self, general_ledger_account_code):
        """Sets the general_ledger_account_code of this TrialBalance.

        The Account code that the trial balance results have been grouped against  # noqa: E501

        :param general_ledger_account_code: The general_ledger_account_code of this TrialBalance.  # noqa: E501
        :type general_ledger_account_code: str
        """
        if self.local_vars_configuration.client_side_validation and general_ledger_account_code is None:  # noqa: E501
            raise ValueError("Invalid value for `general_ledger_account_code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                general_ledger_account_code is not None and len(general_ledger_account_code) < 1):
            raise ValueError("Invalid value for `general_ledger_account_code`, length must be greater than or equal to `1`")  # noqa: E501

        self._general_ledger_account_code = general_ledger_account_code

    @property
    def description(self):
        """Gets the description of this TrialBalance.  # noqa: E501

        The description of the record  # noqa: E501

        :return: The description of this TrialBalance.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TrialBalance.

        The description of the record  # noqa: E501

        :param description: The description of this TrialBalance.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def levels(self):
        """Gets the levels of this TrialBalance.  # noqa: E501

        The levels that have been derived from the specified General Ledger Profile  # noqa: E501

        :return: The levels of this TrialBalance.  # noqa: E501
        :rtype: list[str]
        """
        return self._levels

    @levels.setter
    def levels(self, levels):
        """Sets the levels of this TrialBalance.

        The levels that have been derived from the specified General Ledger Profile  # noqa: E501

        :param levels: The levels of this TrialBalance.  # noqa: E501
        :type levels: list[str]
        """
        if self.local_vars_configuration.client_side_validation and levels is None:  # noqa: E501
            raise ValueError("Invalid value for `levels`, must not be `None`")  # noqa: E501

        self._levels = levels

    @property
    def account_type(self):
        """Gets the account_type of this TrialBalance.  # noqa: E501

        The account type attributed to the record  # noqa: E501

        :return: The account_type of this TrialBalance.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this TrialBalance.

        The account type attributed to the record  # noqa: E501

        :param account_type: The account_type of this TrialBalance.  # noqa: E501
        :type account_type: str
        """
        if self.local_vars_configuration.client_side_validation and account_type is None:  # noqa: E501
            raise ValueError("Invalid value for `account_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                account_type is not None and len(account_type) < 1):
            raise ValueError("Invalid value for `account_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._account_type = account_type

    @property
    def opening(self):
        """Gets the opening of this TrialBalance.  # noqa: E501

        The opening balance at the start of the period  # noqa: E501

        :return: The opening of this TrialBalance.  # noqa: E501
        :rtype: float
        """
        return self._opening

    @opening.setter
    def opening(self, opening):
        """Sets the opening of this TrialBalance.

        The opening balance at the start of the period  # noqa: E501

        :param opening: The opening of this TrialBalance.  # noqa: E501
        :type opening: float
        """
        if self.local_vars_configuration.client_side_validation and opening is None:  # noqa: E501
            raise ValueError("Invalid value for `opening`, must not be `None`")  # noqa: E501

        self._opening = opening

    @property
    def closing(self):
        """Gets the closing of this TrialBalance.  # noqa: E501

        The closing balance at the end of the period  # noqa: E501

        :return: The closing of this TrialBalance.  # noqa: E501
        :rtype: float
        """
        return self._closing

    @closing.setter
    def closing(self, closing):
        """Sets the closing of this TrialBalance.

        The closing balance at the end of the period  # noqa: E501

        :param closing: The closing of this TrialBalance.  # noqa: E501
        :type closing: float
        """
        if self.local_vars_configuration.client_side_validation and closing is None:  # noqa: E501
            raise ValueError("Invalid value for `closing`, must not be `None`")  # noqa: E501

        self._closing = closing

    @property
    def debit(self):
        """Gets the debit of this TrialBalance.  # noqa: E501

        All debits that occured in the period  # noqa: E501

        :return: The debit of this TrialBalance.  # noqa: E501
        :rtype: float
        """
        return self._debit

    @debit.setter
    def debit(self, debit):
        """Sets the debit of this TrialBalance.

        All debits that occured in the period  # noqa: E501

        :param debit: The debit of this TrialBalance.  # noqa: E501
        :type debit: float
        """
        if self.local_vars_configuration.client_side_validation and debit is None:  # noqa: E501
            raise ValueError("Invalid value for `debit`, must not be `None`")  # noqa: E501

        self._debit = debit

    @property
    def credit(self):
        """Gets the credit of this TrialBalance.  # noqa: E501

        All credits that occured in the period  # noqa: E501

        :return: The credit of this TrialBalance.  # noqa: E501
        :rtype: float
        """
        return self._credit

    @credit.setter
    def credit(self, credit):
        """Sets the credit of this TrialBalance.

        All credits that occured in the period  # noqa: E501

        :param credit: The credit of this TrialBalance.  # noqa: E501
        :type credit: float
        """
        if self.local_vars_configuration.client_side_validation and credit is None:  # noqa: E501
            raise ValueError("Invalid value for `credit`, must not be `None`")  # noqa: E501

        self._credit = credit

    @property
    def links(self):
        """Gets the links of this TrialBalance.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this TrialBalance.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this TrialBalance.

        Collection of links.  # noqa: E501

        :param links: The links of this TrialBalance.  # noqa: E501
        :type links: list[lusid.Link]
        """

        self._links = links

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
        if not isinstance(other, TrialBalance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrialBalance):
            return True

        return self.to_dict() != other.to_dict()
