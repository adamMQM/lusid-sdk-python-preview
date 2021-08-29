# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3440
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


class CustomEntityDefinitionRequest(object):
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
        'custom_entity_id': 'str',
        'display_name': 'str',
        'description': 'str',
        'field_schema': 'list[CustomEntityFieldDefinition]'
    }

    attribute_map = {
        'custom_entity_id': 'customEntityId',
        'display_name': 'displayName',
        'description': 'description',
        'field_schema': 'fieldSchema'
    }

    required_map = {
        'custom_entity_id': 'required',
        'display_name': 'required',
        'description': 'optional',
        'field_schema': 'optional'
    }

    def __init__(self, custom_entity_id=None, display_name=None, description=None, field_schema=None, local_vars_configuration=None):  # noqa: E501
        """CustomEntityDefinitionRequest - a model defined in OpenAPI"
        
        :param custom_entity_id:  (required)
        :type custom_entity_id: str
        :param display_name:  (required)
        :type display_name: str
        :param description: 
        :type description: str
        :param field_schema: 
        :type field_schema: list[lusid.CustomEntityFieldDefinition]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._custom_entity_id = None
        self._display_name = None
        self._description = None
        self._field_schema = None
        self.discriminator = None

        self.custom_entity_id = custom_entity_id
        self.display_name = display_name
        self.description = description
        self.field_schema = field_schema

    @property
    def custom_entity_id(self):
        """Gets the custom_entity_id of this CustomEntityDefinitionRequest.  # noqa: E501


        :return: The custom_entity_id of this CustomEntityDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._custom_entity_id

    @custom_entity_id.setter
    def custom_entity_id(self, custom_entity_id):
        """Sets the custom_entity_id of this CustomEntityDefinitionRequest.


        :param custom_entity_id: The custom_entity_id of this CustomEntityDefinitionRequest.  # noqa: E501
        :type custom_entity_id: str
        """
        if self.local_vars_configuration.client_side_validation and custom_entity_id is None:  # noqa: E501
            raise ValueError("Invalid value for `custom_entity_id`, must not be `None`")  # noqa: E501

        self._custom_entity_id = custom_entity_id

    @property
    def display_name(self):
        """Gets the display_name of this CustomEntityDefinitionRequest.  # noqa: E501


        :return: The display_name of this CustomEntityDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CustomEntityDefinitionRequest.


        :param display_name: The display_name of this CustomEntityDefinitionRequest.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this CustomEntityDefinitionRequest.  # noqa: E501


        :return: The description of this CustomEntityDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CustomEntityDefinitionRequest.


        :param description: The description of this CustomEntityDefinitionRequest.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def field_schema(self):
        """Gets the field_schema of this CustomEntityDefinitionRequest.  # noqa: E501


        :return: The field_schema of this CustomEntityDefinitionRequest.  # noqa: E501
        :rtype: list[lusid.CustomEntityFieldDefinition]
        """
        return self._field_schema

    @field_schema.setter
    def field_schema(self, field_schema):
        """Sets the field_schema of this CustomEntityDefinitionRequest.


        :param field_schema: The field_schema of this CustomEntityDefinitionRequest.  # noqa: E501
        :type field_schema: list[lusid.CustomEntityFieldDefinition]
        """

        self._field_schema = field_schema

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
        if not isinstance(other, CustomEntityDefinitionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomEntityDefinitionRequest):
            return True

        return self.to_dict() != other.to_dict()
