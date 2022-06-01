# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4436
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


class ReconcileNumericRule(object):
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
        'comparison_type': 'str',
        'tolerance': 'float',
        'applies_to': 'AggregateSpec',
        'rule_type': 'str'
    }

    attribute_map = {
        'comparison_type': 'comparisonType',
        'tolerance': 'tolerance',
        'applies_to': 'appliesTo',
        'rule_type': 'ruleType'
    }

    required_map = {
        'comparison_type': 'required',
        'tolerance': 'optional',
        'applies_to': 'required',
        'rule_type': 'required'
    }

    def __init__(self, comparison_type=None, tolerance=None, applies_to=None, rule_type=None, local_vars_configuration=None):  # noqa: E501
        """ReconcileNumericRule - a model defined in OpenAPI"
        
        :param comparison_type:  The available values are: Exact, AbsoluteDifference, RelativeDifference (required)
        :type comparison_type: str
        :param tolerance:  For a numeric type only (i.e. decimal, integer, date or datetime offset possibly controversially), this is the quantity used in the comparison.  The units of the tolerance must be set appropriately for the item being compared.  For a number such as a currency or amount that will be a simple quantity, for a DateTime or DateTimeOffset it should be days. If fewer than a single day then this should be  passed as a fraction.
        :type tolerance: float
        :param applies_to:  (required)
        :type applies_to: lusid.AggregateSpec
        :param rule_type:  The available values are: ReconcileNumericRule, ReconcileDateTimeRule, ReconcileStringRule, ReconcileExact (required)
        :type rule_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._comparison_type = None
        self._tolerance = None
        self._applies_to = None
        self._rule_type = None
        self.discriminator = None

        self.comparison_type = comparison_type
        if tolerance is not None:
            self.tolerance = tolerance
        self.applies_to = applies_to
        self.rule_type = rule_type

    @property
    def comparison_type(self):
        """Gets the comparison_type of this ReconcileNumericRule.  # noqa: E501

        The available values are: Exact, AbsoluteDifference, RelativeDifference  # noqa: E501

        :return: The comparison_type of this ReconcileNumericRule.  # noqa: E501
        :rtype: str
        """
        return self._comparison_type

    @comparison_type.setter
    def comparison_type(self, comparison_type):
        """Sets the comparison_type of this ReconcileNumericRule.

        The available values are: Exact, AbsoluteDifference, RelativeDifference  # noqa: E501

        :param comparison_type: The comparison_type of this ReconcileNumericRule.  # noqa: E501
        :type comparison_type: str
        """
        if self.local_vars_configuration.client_side_validation and comparison_type is None:  # noqa: E501
            raise ValueError("Invalid value for `comparison_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Exact", "AbsoluteDifference", "RelativeDifference"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and comparison_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `comparison_type` ({0}), must be one of {1}"  # noqa: E501
                .format(comparison_type, allowed_values)
            )

        self._comparison_type = comparison_type

    @property
    def tolerance(self):
        """Gets the tolerance of this ReconcileNumericRule.  # noqa: E501

        For a numeric type only (i.e. decimal, integer, date or datetime offset possibly controversially), this is the quantity used in the comparison.  The units of the tolerance must be set appropriately for the item being compared.  For a number such as a currency or amount that will be a simple quantity, for a DateTime or DateTimeOffset it should be days. If fewer than a single day then this should be  passed as a fraction.  # noqa: E501

        :return: The tolerance of this ReconcileNumericRule.  # noqa: E501
        :rtype: float
        """
        return self._tolerance

    @tolerance.setter
    def tolerance(self, tolerance):
        """Sets the tolerance of this ReconcileNumericRule.

        For a numeric type only (i.e. decimal, integer, date or datetime offset possibly controversially), this is the quantity used in the comparison.  The units of the tolerance must be set appropriately for the item being compared.  For a number such as a currency or amount that will be a simple quantity, for a DateTime or DateTimeOffset it should be days. If fewer than a single day then this should be  passed as a fraction.  # noqa: E501

        :param tolerance: The tolerance of this ReconcileNumericRule.  # noqa: E501
        :type tolerance: float
        """

        self._tolerance = tolerance

    @property
    def applies_to(self):
        """Gets the applies_to of this ReconcileNumericRule.  # noqa: E501


        :return: The applies_to of this ReconcileNumericRule.  # noqa: E501
        :rtype: lusid.AggregateSpec
        """
        return self._applies_to

    @applies_to.setter
    def applies_to(self, applies_to):
        """Sets the applies_to of this ReconcileNumericRule.


        :param applies_to: The applies_to of this ReconcileNumericRule.  # noqa: E501
        :type applies_to: lusid.AggregateSpec
        """
        if self.local_vars_configuration.client_side_validation and applies_to is None:  # noqa: E501
            raise ValueError("Invalid value for `applies_to`, must not be `None`")  # noqa: E501

        self._applies_to = applies_to

    @property
    def rule_type(self):
        """Gets the rule_type of this ReconcileNumericRule.  # noqa: E501

        The available values are: ReconcileNumericRule, ReconcileDateTimeRule, ReconcileStringRule, ReconcileExact  # noqa: E501

        :return: The rule_type of this ReconcileNumericRule.  # noqa: E501
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """Sets the rule_type of this ReconcileNumericRule.

        The available values are: ReconcileNumericRule, ReconcileDateTimeRule, ReconcileStringRule, ReconcileExact  # noqa: E501

        :param rule_type: The rule_type of this ReconcileNumericRule.  # noqa: E501
        :type rule_type: str
        """
        if self.local_vars_configuration.client_side_validation and rule_type is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_type`, must not be `None`")  # noqa: E501
        allowed_values = ["ReconcileNumericRule", "ReconcileDateTimeRule", "ReconcileStringRule", "ReconcileExact"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and rule_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `rule_type` ({0}), must be one of {1}"  # noqa: E501
                .format(rule_type, allowed_values)
            )

        self._rule_type = rule_type

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
        if not isinstance(other, ReconcileNumericRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReconcileNumericRule):
            return True

        return self.to_dict() != other.to_dict()
