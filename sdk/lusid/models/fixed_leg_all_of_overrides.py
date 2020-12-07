# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2358
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class FixedLegAllOfOverrides(object):
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
        'amortization': 'list[float]',
        'spreads': 'list[float]'
    }

    attribute_map = {
        'amortization': 'Amortization',
        'spreads': 'Spreads'
    }

    required_map = {
        'amortization': 'optional',
        'spreads': 'optional'
    }

    def __init__(self, amortization=None, spreads=None):  # noqa: E501
        """
        FixedLegAllOfOverrides - a model defined in OpenAPI

        :param amortization: 
        :type amortization: list[float]
        :param spreads: 
        :type spreads: list[float]

        """  # noqa: E501

        self._amortization = None
        self._spreads = None
        self.discriminator = None

        if amortization is not None:
            self.amortization = amortization
        if spreads is not None:
            self.spreads = spreads

    @property
    def amortization(self):
        """Gets the amortization of this FixedLegAllOfOverrides.  # noqa: E501


        :return: The amortization of this FixedLegAllOfOverrides.  # noqa: E501
        :rtype: list[float]
        """
        return self._amortization

    @amortization.setter
    def amortization(self, amortization):
        """Sets the amortization of this FixedLegAllOfOverrides.


        :param amortization: The amortization of this FixedLegAllOfOverrides.  # noqa: E501
        :type: list[float]
        """

        self._amortization = amortization

    @property
    def spreads(self):
        """Gets the spreads of this FixedLegAllOfOverrides.  # noqa: E501


        :return: The spreads of this FixedLegAllOfOverrides.  # noqa: E501
        :rtype: list[float]
        """
        return self._spreads

    @spreads.setter
    def spreads(self, spreads):
        """Sets the spreads of this FixedLegAllOfOverrides.


        :param spreads: The spreads of this FixedLegAllOfOverrides.  # noqa: E501
        :type: list[float]
        """

        self._spreads = spreads

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
        if not isinstance(other, FixedLegAllOfOverrides):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
