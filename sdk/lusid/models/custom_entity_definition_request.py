# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4024
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
        'entity_type_name': 'str',
        'display_name': 'str',
        'description': 'str',
        'field_schema': 'list[CustomEntityFieldDefinition]'
    }

    attribute_map = {
        'entity_type_name': 'entityTypeName',
        'display_name': 'displayName',
        'description': 'description',
        'field_schema': 'fieldSchema'
    }

    required_map = {
        'entity_type_name': 'required',
        'display_name': 'required',
        'description': 'optional',
        'field_schema': 'optional'
    }

    def __init__(self, entity_type_name=None, display_name=None, description=None, field_schema=None, local_vars_configuration=None):  # noqa: E501
        """CustomEntityDefinitionRequest - a model defined in OpenAPI"
        
        :param entity_type_name:  (required)
        :type entity_type_name: str
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

        self._entity_type_name = None
        self._display_name = None
        self._description = None
        self._field_schema = None
        self.discriminator = None

        self.entity_type_name = entity_type_name
        self.display_name = display_name
        self.description = description
        self.field_schema = field_schema

    @property
    def entity_type_name(self):
        """Gets the entity_type_name of this CustomEntityDefinitionRequest.  # noqa: E501


        :return: The entity_type_name of this CustomEntityDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._entity_type_name

    @entity_type_name.setter
    def entity_type_name(self, entity_type_name):
        """Sets the entity_type_name of this CustomEntityDefinitionRequest.


        :param entity_type_name: The entity_type_name of this CustomEntityDefinitionRequest.  # noqa: E501
        :type entity_type_name: str
        """
        if self.local_vars_configuration.client_side_validation and entity_type_name is None:  # noqa: E501
            raise ValueError("Invalid value for `entity_type_name`, must not be `None`")  # noqa: E501

        self._entity_type_name = entity_type_name

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
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and not re.search(r'^[\s\S]*$', display_name)):  # noqa: E501
            raise ValueError(r"Invalid value for `display_name`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

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
        if (self.local_vars_configuration.client_side_validation and
                description is not None and not re.search(r'^[\s\S]*$', description)):  # noqa: E501
            raise ValueError(r"Invalid value for `description`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

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
