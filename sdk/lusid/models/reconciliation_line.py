# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.5122
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


class ReconciliationLine(object):
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
        'left': 'dict(str, object)',
        'right': 'dict(str, object)',
        'difference': 'dict(str, object)',
        'result_comparison': 'dict(str, object)'
    }

    attribute_map = {
        'left': 'left',
        'right': 'right',
        'difference': 'difference',
        'result_comparison': 'resultComparison'
    }

    required_map = {
        'left': 'optional',
        'right': 'optional',
        'difference': 'optional',
        'result_comparison': 'optional'
    }

    def __init__(self, left=None, right=None, difference=None, result_comparison=None, local_vars_configuration=None):  # noqa: E501
        """ReconciliationLine - a model defined in OpenAPI"
        
        :param left:  Left hand side of the comparison
        :type left: dict(str, object)
        :param right:  Right hand side of the comparison
        :type right: dict(str, object)
        :param difference:  Difference between LHS and RHS of comparison
        :type difference: dict(str, object)
        :param result_comparison:  The logical or semantic description of the difference, e.g. \"Matches\" or \"MatchesWithTolerance\" or \"Failed\".
        :type result_comparison: dict(str, object)

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._left = None
        self._right = None
        self._difference = None
        self._result_comparison = None
        self.discriminator = None

        self.left = left
        self.right = right
        self.difference = difference
        self.result_comparison = result_comparison

    @property
    def left(self):
        """Gets the left of this ReconciliationLine.  # noqa: E501

        Left hand side of the comparison  # noqa: E501

        :return: The left of this ReconciliationLine.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this ReconciliationLine.

        Left hand side of the comparison  # noqa: E501

        :param left: The left of this ReconciliationLine.  # noqa: E501
        :type left: dict(str, object)
        """

        self._left = left

    @property
    def right(self):
        """Gets the right of this ReconciliationLine.  # noqa: E501

        Right hand side of the comparison  # noqa: E501

        :return: The right of this ReconciliationLine.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._right

    @right.setter
    def right(self, right):
        """Sets the right of this ReconciliationLine.

        Right hand side of the comparison  # noqa: E501

        :param right: The right of this ReconciliationLine.  # noqa: E501
        :type right: dict(str, object)
        """

        self._right = right

    @property
    def difference(self):
        """Gets the difference of this ReconciliationLine.  # noqa: E501

        Difference between LHS and RHS of comparison  # noqa: E501

        :return: The difference of this ReconciliationLine.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._difference

    @difference.setter
    def difference(self, difference):
        """Sets the difference of this ReconciliationLine.

        Difference between LHS and RHS of comparison  # noqa: E501

        :param difference: The difference of this ReconciliationLine.  # noqa: E501
        :type difference: dict(str, object)
        """

        self._difference = difference

    @property
    def result_comparison(self):
        """Gets the result_comparison of this ReconciliationLine.  # noqa: E501

        The logical or semantic description of the difference, e.g. \"Matches\" or \"MatchesWithTolerance\" or \"Failed\".  # noqa: E501

        :return: The result_comparison of this ReconciliationLine.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._result_comparison

    @result_comparison.setter
    def result_comparison(self, result_comparison):
        """Sets the result_comparison of this ReconciliationLine.

        The logical or semantic description of the difference, e.g. \"Matches\" or \"MatchesWithTolerance\" or \"Failed\".  # noqa: E501

        :param result_comparison: The result_comparison of this ReconciliationLine.  # noqa: E501
        :type result_comparison: dict(str, object)
        """

        self._result_comparison = result_comparison

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
        if not isinstance(other, ReconciliationLine):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReconciliationLine):
            return True

        return self.to_dict() != other.to_dict()
