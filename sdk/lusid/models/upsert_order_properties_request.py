# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2514
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class UpsertOrderPropertiesRequest(object):
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
        'properties': 'list[ModelProperty]',
        'id': 'str'
    }

    attribute_map = {
        'properties': 'properties',
        'id': 'id'
    }

    required_map = {
        'properties': 'required',
        'id': 'required'
    }

    def __init__(self, properties=None, id=None):  # noqa: E501
        """
        UpsertOrderPropertiesRequest - a model defined in OpenAPI

        :param properties:  Client-defined properties associated with this order. (required)
        :type properties: list[lusid.ModelProperty]
        :param id:  Uniquely identifies this order. (required)
        :type id: str

        """  # noqa: E501

        self._properties = None
        self._id = None
        self.discriminator = None

        self.properties = properties
        self.id = id

    @property
    def properties(self):
        """Gets the properties of this UpsertOrderPropertiesRequest.  # noqa: E501

        Client-defined properties associated with this order.  # noqa: E501

        :return: The properties of this UpsertOrderPropertiesRequest.  # noqa: E501
        :rtype: list[ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this UpsertOrderPropertiesRequest.

        Client-defined properties associated with this order.  # noqa: E501

        :param properties: The properties of this UpsertOrderPropertiesRequest.  # noqa: E501
        :type: list[ModelProperty]
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")  # noqa: E501

        self._properties = properties

    @property
    def id(self):
        """Gets the id of this UpsertOrderPropertiesRequest.  # noqa: E501

        Uniquely identifies this order.  # noqa: E501

        :return: The id of this UpsertOrderPropertiesRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpsertOrderPropertiesRequest.

        Uniquely identifies this order.  # noqa: E501

        :param id: The id of this UpsertOrderPropertiesRequest.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

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
        if not isinstance(other, UpsertOrderPropertiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
