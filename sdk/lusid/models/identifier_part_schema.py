# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3132
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class IdentifierPartSchema(object):
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
        'index': 'int',
        'name': 'str',
        'display_name': 'str',
        'description': 'str',
        'required': 'bool',
        'links': 'list[Link]'
    }

    attribute_map = {
        'index': 'index',
        'name': 'name',
        'display_name': 'displayName',
        'description': 'description',
        'required': 'required',
        'links': 'links'
    }

    required_map = {
        'index': 'required',
        'name': 'required',
        'display_name': 'required',
        'description': 'required',
        'required': 'required',
        'links': 'optional'
    }

    def __init__(self, index=None, name=None, display_name=None, description=None, required=None, links=None):  # noqa: E501
        """
        IdentifierPartSchema - a model defined in OpenAPI

        :param index:  (required)
        :type index: int
        :param name:  (required)
        :type name: str
        :param display_name:  (required)
        :type display_name: str
        :param description:  (required)
        :type description: str
        :param required:  (required)
        :type required: bool
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501

        self._index = None
        self._name = None
        self._display_name = None
        self._description = None
        self._required = None
        self._links = None
        self.discriminator = None

        self.index = index
        self.name = name
        self.display_name = display_name
        self.description = description
        self.required = required
        self.links = links

    @property
    def index(self):
        """Gets the index of this IdentifierPartSchema.  # noqa: E501


        :return: The index of this IdentifierPartSchema.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this IdentifierPartSchema.


        :param index: The index of this IdentifierPartSchema.  # noqa: E501
        :type: int
        """
        if index is None:
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501

        self._index = index

    @property
    def name(self):
        """Gets the name of this IdentifierPartSchema.  # noqa: E501


        :return: The name of this IdentifierPartSchema.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IdentifierPartSchema.


        :param name: The name of this IdentifierPartSchema.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this IdentifierPartSchema.  # noqa: E501


        :return: The display_name of this IdentifierPartSchema.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this IdentifierPartSchema.


        :param display_name: The display_name of this IdentifierPartSchema.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this IdentifierPartSchema.  # noqa: E501


        :return: The description of this IdentifierPartSchema.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IdentifierPartSchema.


        :param description: The description of this IdentifierPartSchema.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def required(self):
        """Gets the required of this IdentifierPartSchema.  # noqa: E501


        :return: The required of this IdentifierPartSchema.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this IdentifierPartSchema.


        :param required: The required of this IdentifierPartSchema.  # noqa: E501
        :type: bool
        """
        if required is None:
            raise ValueError("Invalid value for `required`, must not be `None`")  # noqa: E501

        self._required = required

    @property
    def links(self):
        """Gets the links of this IdentifierPartSchema.  # noqa: E501


        :return: The links of this IdentifierPartSchema.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this IdentifierPartSchema.


        :param links: The links of this IdentifierPartSchema.  # noqa: E501
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
        if not isinstance(other, IdentifierPartSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
