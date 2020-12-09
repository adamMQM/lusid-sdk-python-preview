# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2376
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class DataDefinition(object):
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
        'name': 'str',
        'data_type': 'str',
        'key_type': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'name': 'name',
        'data_type': 'dataType',
        'key_type': 'keyType',
        'links': 'links'
    }

    required_map = {
        'name': 'optional',
        'data_type': 'optional',
        'key_type': 'optional',
        'links': 'optional'
    }

    def __init__(self, name=None, data_type=None, key_type=None, links=None):  # noqa: E501
        """
        DataDefinition - a model defined in OpenAPI

        :param name:  The name of the data item. This is the name that will appear
        :type name: str
        :param data_type:  A member of the set of possible data types, that all data passed under that key is expected to be of.  Currently limited to one of [string, integer, decimal].
        :type data_type: str
        :param key_type:  Is the item either a unique key for the dictionary, i.e. does it identify a unique index or conceptual 'row' within the list of dictionaries,  or a partial key or is it simply a data item within that dictionary. Must be one of [Unique,PartOfUnique,Leaf]
        :type key_type: str
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501

        self._name = None
        self._data_type = None
        self._key_type = None
        self._links = None
        self.discriminator = None

        self.name = name
        self.data_type = data_type
        self.key_type = key_type
        self.links = links

    @property
    def name(self):
        """Gets the name of this DataDefinition.  # noqa: E501

        The name of the data item. This is the name that will appear  # noqa: E501

        :return: The name of this DataDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataDefinition.

        The name of the data item. This is the name that will appear  # noqa: E501

        :param name: The name of this DataDefinition.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def data_type(self):
        """Gets the data_type of this DataDefinition.  # noqa: E501

        A member of the set of possible data types, that all data passed under that key is expected to be of.  Currently limited to one of [string, integer, decimal].  # noqa: E501

        :return: The data_type of this DataDefinition.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this DataDefinition.

        A member of the set of possible data types, that all data passed under that key is expected to be of.  Currently limited to one of [string, integer, decimal].  # noqa: E501

        :param data_type: The data_type of this DataDefinition.  # noqa: E501
        :type: str
        """

        self._data_type = data_type

    @property
    def key_type(self):
        """Gets the key_type of this DataDefinition.  # noqa: E501

        Is the item either a unique key for the dictionary, i.e. does it identify a unique index or conceptual 'row' within the list of dictionaries,  or a partial key or is it simply a data item within that dictionary. Must be one of [Unique,PartOfUnique,Leaf]  # noqa: E501

        :return: The key_type of this DataDefinition.  # noqa: E501
        :rtype: str
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type):
        """Sets the key_type of this DataDefinition.

        Is the item either a unique key for the dictionary, i.e. does it identify a unique index or conceptual 'row' within the list of dictionaries,  or a partial key or is it simply a data item within that dictionary. Must be one of [Unique,PartOfUnique,Leaf]  # noqa: E501

        :param key_type: The key_type of this DataDefinition.  # noqa: E501
        :type: str
        """

        self._key_type = key_type

    @property
    def links(self):
        """Gets the links of this DataDefinition.  # noqa: E501


        :return: The links of this DataDefinition.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this DataDefinition.


        :param links: The links of this DataDefinition.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

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
        if not isinstance(other, DataDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
