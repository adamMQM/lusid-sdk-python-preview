# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.606
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


class DeleteAccountsResponse(object):
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
        'version': 'Version',
        'account_ids': 'list[str]',
        'links': 'list[Link]'
    }

    attribute_map = {
        'version': 'version',
        'account_ids': 'accountIds',
        'links': 'links'
    }

    required_map = {
        'version': 'optional',
        'account_ids': 'optional',
        'links': 'optional'
    }

    def __init__(self, version=None, account_ids=None, links=None, local_vars_configuration=None):  # noqa: E501
        """DeleteAccountsResponse - a model defined in OpenAPI"
        
        :param version: 
        :type version: lusid.Version
        :param account_ids:  The Accounts which have been soft/hard deleted.
        :type account_ids: list[str]
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._version = None
        self._account_ids = None
        self._links = None
        self.discriminator = None

        if version is not None:
            self.version = version
        self.account_ids = account_ids
        self.links = links

    @property
    def version(self):
        """Gets the version of this DeleteAccountsResponse.  # noqa: E501


        :return: The version of this DeleteAccountsResponse.  # noqa: E501
        :rtype: lusid.Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DeleteAccountsResponse.


        :param version: The version of this DeleteAccountsResponse.  # noqa: E501
        :type version: lusid.Version
        """

        self._version = version

    @property
    def account_ids(self):
        """Gets the account_ids of this DeleteAccountsResponse.  # noqa: E501

        The Accounts which have been soft/hard deleted.  # noqa: E501

        :return: The account_ids of this DeleteAccountsResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._account_ids

    @account_ids.setter
    def account_ids(self, account_ids):
        """Sets the account_ids of this DeleteAccountsResponse.

        The Accounts which have been soft/hard deleted.  # noqa: E501

        :param account_ids: The account_ids of this DeleteAccountsResponse.  # noqa: E501
        :type account_ids: list[str]
        """

        self._account_ids = account_ids

    @property
    def links(self):
        """Gets the links of this DeleteAccountsResponse.  # noqa: E501


        :return: The links of this DeleteAccountsResponse.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this DeleteAccountsResponse.


        :param links: The links of this DeleteAccountsResponse.  # noqa: E501
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
        if not isinstance(other, DeleteAccountsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeleteAccountsResponse):
            return True

        return self.to_dict() != other.to_dict()
