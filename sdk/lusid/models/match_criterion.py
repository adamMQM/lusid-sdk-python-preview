# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.5295
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


class MatchCriterion(object):
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
        'criterion_type': 'str'
    }

    attribute_map = {
        'criterion_type': 'criterionType'
    }

    required_map = {
        'criterion_type': 'required'
    }

    discriminator_value_class_map = {
        'PropertyValueIn': 'PropertyValueIn',
        'PropertyValueEquals': 'PropertyValueEquals'
    }

    def __init__(self, criterion_type=None, local_vars_configuration=None):  # noqa: E501
        """MatchCriterion - a model defined in OpenAPI"
        
        :param criterion_type:  The available values are: PropertyValueEquals, PropertyValueIn (required)
        :type criterion_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._criterion_type = None
        self.discriminator = 'criterion_type'

        self.criterion_type = criterion_type

    @property
    def criterion_type(self):
        """Gets the criterion_type of this MatchCriterion.  # noqa: E501

        The available values are: PropertyValueEquals, PropertyValueIn  # noqa: E501

        :return: The criterion_type of this MatchCriterion.  # noqa: E501
        :rtype: str
        """
        return self._criterion_type

    @criterion_type.setter
    def criterion_type(self, criterion_type):
        """Sets the criterion_type of this MatchCriterion.

        The available values are: PropertyValueEquals, PropertyValueIn  # noqa: E501

        :param criterion_type: The criterion_type of this MatchCriterion.  # noqa: E501
        :type criterion_type: str
        """
        if self.local_vars_configuration.client_side_validation and criterion_type is None:  # noqa: E501
            raise ValueError("Invalid value for `criterion_type`, must not be `None`")  # noqa: E501
        allowed_values = ["PropertyValueEquals", "PropertyValueIn"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and criterion_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `criterion_type` ({0}), must be one of {1}"  # noqa: E501
                .format(criterion_type, allowed_values)
            )

        self._criterion_type = criterion_type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, MatchCriterion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MatchCriterion):
            return True

        return self.to_dict() != other.to_dict()
