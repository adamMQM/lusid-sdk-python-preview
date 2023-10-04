# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.568
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


class AllocationServiceRunResponse(object):
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
        'values': 'list[ResourceId]',
        'failed': 'dict(str, ErrorDetail)'
    }

    attribute_map = {
        'values': 'values',
        'failed': 'failed'
    }

    required_map = {
        'values': 'optional',
        'failed': 'optional'
    }

    def __init__(self, values=None, failed=None, local_vars_configuration=None):  # noqa: E501
        """AllocationServiceRunResponse - a model defined in OpenAPI"
        
        :param values: 
        :type values: list[lusid.ResourceId]
        :param failed: 
        :type failed: dict[str, lusid.ErrorDetail]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._values = None
        self._failed = None
        self.discriminator = None

        self.values = values
        self.failed = failed

    @property
    def values(self):
        """Gets the values of this AllocationServiceRunResponse.  # noqa: E501


        :return: The values of this AllocationServiceRunResponse.  # noqa: E501
        :rtype: list[lusid.ResourceId]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this AllocationServiceRunResponse.


        :param values: The values of this AllocationServiceRunResponse.  # noqa: E501
        :type values: list[lusid.ResourceId]
        """

        self._values = values

    @property
    def failed(self):
        """Gets the failed of this AllocationServiceRunResponse.  # noqa: E501


        :return: The failed of this AllocationServiceRunResponse.  # noqa: E501
        :rtype: dict[str, lusid.ErrorDetail]
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this AllocationServiceRunResponse.


        :param failed: The failed of this AllocationServiceRunResponse.  # noqa: E501
        :type failed: dict[str, lusid.ErrorDetail]
        """

        self._failed = failed

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
        if not isinstance(other, AllocationServiceRunResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AllocationServiceRunResponse):
            return True

        return self.to_dict() != other.to_dict()
