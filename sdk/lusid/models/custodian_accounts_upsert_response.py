# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.568
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


class CustodianAccountsUpsertResponse(object):
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
        'href': 'str',
        'version': 'Version',
        'custodian_accounts': 'list[CustodianAccount]',
        'links': 'list[Link]'
    }

    attribute_map = {
        'href': 'href',
        'version': 'version',
        'custodian_accounts': 'custodianAccounts',
        'links': 'links'
    }

    required_map = {
        'href': 'optional',
        'version': 'optional',
        'custodian_accounts': 'optional',
        'links': 'optional'
    }

    def __init__(self, href=None, version=None, custodian_accounts=None, links=None, local_vars_configuration=None):  # noqa: E501
        """CustodianAccountsUpsertResponse - a model defined in OpenAPI"
        
        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param version: 
        :type version: lusid.Version
        :param custodian_accounts:  The Custodian Accounts which have been upserted.
        :type custodian_accounts: list[lusid.CustodianAccount]
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._href = None
        self._version = None
        self._custodian_accounts = None
        self._links = None
        self.discriminator = None

        self.href = href
        if version is not None:
            self.version = version
        self.custodian_accounts = custodian_accounts
        self.links = links

    @property
    def href(self):
        """Gets the href of this CustodianAccountsUpsertResponse.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this CustodianAccountsUpsertResponse.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this CustodianAccountsUpsertResponse.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this CustodianAccountsUpsertResponse.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def version(self):
        """Gets the version of this CustodianAccountsUpsertResponse.  # noqa: E501


        :return: The version of this CustodianAccountsUpsertResponse.  # noqa: E501
        :rtype: lusid.Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CustodianAccountsUpsertResponse.


        :param version: The version of this CustodianAccountsUpsertResponse.  # noqa: E501
        :type version: lusid.Version
        """

        self._version = version

    @property
    def custodian_accounts(self):
        """Gets the custodian_accounts of this CustodianAccountsUpsertResponse.  # noqa: E501

        The Custodian Accounts which have been upserted.  # noqa: E501

        :return: The custodian_accounts of this CustodianAccountsUpsertResponse.  # noqa: E501
        :rtype: list[lusid.CustodianAccount]
        """
        return self._custodian_accounts

    @custodian_accounts.setter
    def custodian_accounts(self, custodian_accounts):
        """Sets the custodian_accounts of this CustodianAccountsUpsertResponse.

        The Custodian Accounts which have been upserted.  # noqa: E501

        :param custodian_accounts: The custodian_accounts of this CustodianAccountsUpsertResponse.  # noqa: E501
        :type custodian_accounts: list[lusid.CustodianAccount]
        """

        self._custodian_accounts = custodian_accounts

    @property
    def links(self):
        """Gets the links of this CustodianAccountsUpsertResponse.  # noqa: E501


        :return: The links of this CustodianAccountsUpsertResponse.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CustodianAccountsUpsertResponse.


        :param links: The links of this CustodianAccountsUpsertResponse.  # noqa: E501
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
        if not isinstance(other, CustodianAccountsUpsertResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustodianAccountsUpsertResponse):
            return True

        return self.to_dict() != other.to_dict()
