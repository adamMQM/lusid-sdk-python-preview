# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2987
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class DeletedOrdersEntitiesResponse(object):
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
        'failures': 'list[ValueTupleOfResourceIdToString]',
        'deletes': 'list[ValueTupleOfResourceIdToDeletedEntityResponse]'
    }

    attribute_map = {
        'failures': 'failures',
        'deletes': 'deletes'
    }

    required_map = {
        'failures': 'optional',
        'deletes': 'optional'
    }

    def __init__(self, failures=None, deletes=None):  # noqa: E501
        """
        DeletedOrdersEntitiesResponse - a model defined in OpenAPI

        :param failures:  Failed resource IDs, with their associated failures.
        :type failures: list[lusid.ValueTupleOfResourceIdToString]
        :param deletes:  Successfully deleted resource IDs, with associated responses.
        :type deletes: list[lusid.ValueTupleOfResourceIdToDeletedEntityResponse]

        """  # noqa: E501

        self._failures = None
        self._deletes = None
        self.discriminator = None

        self.failures = failures
        self.deletes = deletes

    @property
    def failures(self):
        """Gets the failures of this DeletedOrdersEntitiesResponse.  # noqa: E501

        Failed resource IDs, with their associated failures.  # noqa: E501

        :return: The failures of this DeletedOrdersEntitiesResponse.  # noqa: E501
        :rtype: list[ValueTupleOfResourceIdToString]
        """
        return self._failures

    @failures.setter
    def failures(self, failures):
        """Sets the failures of this DeletedOrdersEntitiesResponse.

        Failed resource IDs, with their associated failures.  # noqa: E501

        :param failures: The failures of this DeletedOrdersEntitiesResponse.  # noqa: E501
        :type: list[ValueTupleOfResourceIdToString]
        """

        self._failures = failures

    @property
    def deletes(self):
        """Gets the deletes of this DeletedOrdersEntitiesResponse.  # noqa: E501

        Successfully deleted resource IDs, with associated responses.  # noqa: E501

        :return: The deletes of this DeletedOrdersEntitiesResponse.  # noqa: E501
        :rtype: list[ValueTupleOfResourceIdToDeletedEntityResponse]
        """
        return self._deletes

    @deletes.setter
    def deletes(self, deletes):
        """Sets the deletes of this DeletedOrdersEntitiesResponse.

        Successfully deleted resource IDs, with associated responses.  # noqa: E501

        :param deletes: The deletes of this DeletedOrdersEntitiesResponse.  # noqa: E501
        :type: list[ValueTupleOfResourceIdToDeletedEntityResponse]
        """

        self._deletes = deletes

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
        if not isinstance(other, DeletedOrdersEntitiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
