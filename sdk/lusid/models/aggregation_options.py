# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3003
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class AggregationOptions(object):
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
        'use_ansi_like_syntax': 'bool'
    }

    attribute_map = {
        'use_ansi_like_syntax': 'useAnsiLikeSyntax'
    }

    required_map = {
        'use_ansi_like_syntax': 'optional'
    }

    def __init__(self, use_ansi_like_syntax=None):  # noqa: E501
        """
        AggregationOptions - a model defined in OpenAPI

        :param use_ansi_like_syntax:  Should the aggregation behave like ANSI Sql or MySql with respect to a conceptual request which is equivalent to \"select a,sum(a) from results\";  ANSI Sql would report an error if a was not unique where MySql would simply view a,suma(a) as equivalent to firstof(a),sum(a).
        :type use_ansi_like_syntax: bool

        """  # noqa: E501

        self._use_ansi_like_syntax = None
        self.discriminator = None

        if use_ansi_like_syntax is not None:
            self.use_ansi_like_syntax = use_ansi_like_syntax

    @property
    def use_ansi_like_syntax(self):
        """Gets the use_ansi_like_syntax of this AggregationOptions.  # noqa: E501

        Should the aggregation behave like ANSI Sql or MySql with respect to a conceptual request which is equivalent to \"select a,sum(a) from results\";  ANSI Sql would report an error if a was not unique where MySql would simply view a,suma(a) as equivalent to firstof(a),sum(a).  # noqa: E501

        :return: The use_ansi_like_syntax of this AggregationOptions.  # noqa: E501
        :rtype: bool
        """
        return self._use_ansi_like_syntax

    @use_ansi_like_syntax.setter
    def use_ansi_like_syntax(self, use_ansi_like_syntax):
        """Sets the use_ansi_like_syntax of this AggregationOptions.

        Should the aggregation behave like ANSI Sql or MySql with respect to a conceptual request which is equivalent to \"select a,sum(a) from results\";  ANSI Sql would report an error if a was not unique where MySql would simply view a,suma(a) as equivalent to firstof(a),sum(a).  # noqa: E501

        :param use_ansi_like_syntax: The use_ansi_like_syntax of this AggregationOptions.  # noqa: E501
        :type: bool
        """

        self._use_ansi_like_syntax = use_ansi_like_syntax

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
        if not isinstance(other, AggregationOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
