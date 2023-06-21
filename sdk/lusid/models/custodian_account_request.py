# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.273
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


class CustodianAccountRequest(object):
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
        'scope': 'str',
        'code': 'str',
        'status': 'str',
        'account_number': 'str',
        'account_name': 'str',
        'accounting_method': 'str',
        'currency': 'str',
        'properties': 'dict(str, ModelProperty)',
        'custodian_identifier': 'TypedResourceId',
        'account_type': 'str'
    }

    attribute_map = {
        'scope': 'scope',
        'code': 'code',
        'status': 'status',
        'account_number': 'accountNumber',
        'account_name': 'accountName',
        'accounting_method': 'accountingMethod',
        'currency': 'currency',
        'properties': 'properties',
        'custodian_identifier': 'custodianIdentifier',
        'account_type': 'accountType'
    }

    required_map = {
        'scope': 'optional',
        'code': 'required',
        'status': 'optional',
        'account_number': 'required',
        'account_name': 'required',
        'accounting_method': 'required',
        'currency': 'required',
        'properties': 'optional',
        'custodian_identifier': 'required',
        'account_type': 'optional'
    }

    def __init__(self, scope=None, code=None, status=None, account_number=None, account_name=None, accounting_method=None, currency=None, properties=None, custodian_identifier=None, account_type=None, local_vars_configuration=None):  # noqa: E501
        """CustodianAccountRequest - a model defined in OpenAPI"
        
        :param scope:  The Scope assigned to the Custodian Account, where left blank the parent Portfolio Scope will be used
        :type scope: str
        :param code:  Unique Code representing the Custodian Account (required)
        :type code: str
        :param status:  The account status. Can be Active, Inactive or Deleted. Defaults to Active.
        :type status: str
        :param account_number:  The Custodian Account Number (required)
        :type account_number: str
        :param account_name:  The identifiable name given to the Custodian Account (required)
        :type account_name: str
        :param accounting_method:  The Accounting method to be used (required)
        :type accounting_method: str
        :param currency:  The Currency for the Account (required)
        :type currency: str
        :param properties:  Set of unique Custodian Account properties and associated values to store with the Custodian Account. Each property must be from the 'CustodianAccount' domain.
        :type properties: dict[str, lusid.ModelProperty]
        :param custodian_identifier:  (required)
        :type custodian_identifier: lusid.TypedResourceId
        :param account_type:  The Type of the Custodian Account. Can be Margin, Cash or Swap. Defaults to Margin.
        :type account_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._scope = None
        self._code = None
        self._status = None
        self._account_number = None
        self._account_name = None
        self._accounting_method = None
        self._currency = None
        self._properties = None
        self._custodian_identifier = None
        self._account_type = None
        self.discriminator = None

        self.scope = scope
        self.code = code
        self.status = status
        self.account_number = account_number
        self.account_name = account_name
        self.accounting_method = accounting_method
        self.currency = currency
        self.properties = properties
        self.custodian_identifier = custodian_identifier
        self.account_type = account_type

    @property
    def scope(self):
        """Gets the scope of this CustodianAccountRequest.  # noqa: E501

        The Scope assigned to the Custodian Account, where left blank the parent Portfolio Scope will be used  # noqa: E501

        :return: The scope of this CustodianAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this CustodianAccountRequest.

        The Scope assigned to the Custodian Account, where left blank the parent Portfolio Scope will be used  # noqa: E501

        :param scope: The scope of this CustodianAccountRequest.  # noqa: E501
        :type scope: str
        """
        if (self.local_vars_configuration.client_side_validation and
                scope is not None and len(scope) > 64):
            raise ValueError("Invalid value for `scope`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                scope is not None and len(scope) < 1):
            raise ValueError("Invalid value for `scope`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                scope is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', scope)):  # noqa: E501
            raise ValueError(r"Invalid value for `scope`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._scope = scope

    @property
    def code(self):
        """Gets the code of this CustodianAccountRequest.  # noqa: E501

        Unique Code representing the Custodian Account  # noqa: E501

        :return: The code of this CustodianAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CustodianAccountRequest.

        Unique Code representing the Custodian Account  # noqa: E501

        :param code: The code of this CustodianAccountRequest.  # noqa: E501
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
    def status(self):
        """Gets the status of this CustodianAccountRequest.  # noqa: E501

        The account status. Can be Active, Inactive or Deleted. Defaults to Active.  # noqa: E501

        :return: The status of this CustodianAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CustodianAccountRequest.

        The account status. Can be Active, Inactive or Deleted. Defaults to Active.  # noqa: E501

        :param status: The status of this CustodianAccountRequest.  # noqa: E501
        :type status: str
        """

        self._status = status

    @property
    def account_number(self):
        """Gets the account_number of this CustodianAccountRequest.  # noqa: E501

        The Custodian Account Number  # noqa: E501

        :return: The account_number of this CustodianAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this CustodianAccountRequest.

        The Custodian Account Number  # noqa: E501

        :param account_number: The account_number of this CustodianAccountRequest.  # noqa: E501
        :type account_number: str
        """
        if self.local_vars_configuration.client_side_validation and account_number is None:  # noqa: E501
            raise ValueError("Invalid value for `account_number`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                account_number is not None and len(account_number) > 64):
            raise ValueError("Invalid value for `account_number`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                account_number is not None and len(account_number) < 1):
            raise ValueError("Invalid value for `account_number`, length must be greater than or equal to `1`")  # noqa: E501

        self._account_number = account_number

    @property
    def account_name(self):
        """Gets the account_name of this CustodianAccountRequest.  # noqa: E501

        The identifiable name given to the Custodian Account  # noqa: E501

        :return: The account_name of this CustodianAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this CustodianAccountRequest.

        The identifiable name given to the Custodian Account  # noqa: E501

        :param account_name: The account_name of this CustodianAccountRequest.  # noqa: E501
        :type account_name: str
        """
        if self.local_vars_configuration.client_side_validation and account_name is None:  # noqa: E501
            raise ValueError("Invalid value for `account_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                account_name is not None and len(account_name) > 512):
            raise ValueError("Invalid value for `account_name`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                account_name is not None and len(account_name) < 1):
            raise ValueError("Invalid value for `account_name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                account_name is not None and not re.search(r'^[\s\S]*$', account_name)):  # noqa: E501
            raise ValueError(r"Invalid value for `account_name`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._account_name = account_name

    @property
    def accounting_method(self):
        """Gets the accounting_method of this CustodianAccountRequest.  # noqa: E501

        The Accounting method to be used  # noqa: E501

        :return: The accounting_method of this CustodianAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._accounting_method

    @accounting_method.setter
    def accounting_method(self, accounting_method):
        """Sets the accounting_method of this CustodianAccountRequest.

        The Accounting method to be used  # noqa: E501

        :param accounting_method: The accounting_method of this CustodianAccountRequest.  # noqa: E501
        :type accounting_method: str
        """
        if self.local_vars_configuration.client_side_validation and accounting_method is None:  # noqa: E501
            raise ValueError("Invalid value for `accounting_method`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                accounting_method is not None and len(accounting_method) < 1):
            raise ValueError("Invalid value for `accounting_method`, length must be greater than or equal to `1`")  # noqa: E501

        self._accounting_method = accounting_method

    @property
    def currency(self):
        """Gets the currency of this CustodianAccountRequest.  # noqa: E501

        The Currency for the Account  # noqa: E501

        :return: The currency of this CustodianAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CustodianAccountRequest.

        The Currency for the Account  # noqa: E501

        :param currency: The currency of this CustodianAccountRequest.  # noqa: E501
        :type currency: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def properties(self):
        """Gets the properties of this CustodianAccountRequest.  # noqa: E501

        Set of unique Custodian Account properties and associated values to store with the Custodian Account. Each property must be from the 'CustodianAccount' domain.  # noqa: E501

        :return: The properties of this CustodianAccountRequest.  # noqa: E501
        :rtype: dict[str, lusid.ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this CustodianAccountRequest.

        Set of unique Custodian Account properties and associated values to store with the Custodian Account. Each property must be from the 'CustodianAccount' domain.  # noqa: E501

        :param properties: The properties of this CustodianAccountRequest.  # noqa: E501
        :type properties: dict[str, lusid.ModelProperty]
        """

        self._properties = properties

    @property
    def custodian_identifier(self):
        """Gets the custodian_identifier of this CustodianAccountRequest.  # noqa: E501


        :return: The custodian_identifier of this CustodianAccountRequest.  # noqa: E501
        :rtype: lusid.TypedResourceId
        """
        return self._custodian_identifier

    @custodian_identifier.setter
    def custodian_identifier(self, custodian_identifier):
        """Sets the custodian_identifier of this CustodianAccountRequest.


        :param custodian_identifier: The custodian_identifier of this CustodianAccountRequest.  # noqa: E501
        :type custodian_identifier: lusid.TypedResourceId
        """
        if self.local_vars_configuration.client_side_validation and custodian_identifier is None:  # noqa: E501
            raise ValueError("Invalid value for `custodian_identifier`, must not be `None`")  # noqa: E501

        self._custodian_identifier = custodian_identifier

    @property
    def account_type(self):
        """Gets the account_type of this CustodianAccountRequest.  # noqa: E501

        The Type of the Custodian Account. Can be Margin, Cash or Swap. Defaults to Margin.  # noqa: E501

        :return: The account_type of this CustodianAccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this CustodianAccountRequest.

        The Type of the Custodian Account. Can be Margin, Cash or Swap. Defaults to Margin.  # noqa: E501

        :param account_type: The account_type of this CustodianAccountRequest.  # noqa: E501
        :type account_type: str
        """

        self._account_type = account_type

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
        if not isinstance(other, CustodianAccountRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustodianAccountRequest):
            return True

        return self.to_dict() != other.to_dict()
