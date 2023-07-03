# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.307
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


class UpsertReconciliationRunRequest(object):
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
        'date': 'datetime',
        'version': 'int'
    }

    attribute_map = {
        'date': 'date',
        'version': 'version'
    }

    required_map = {
        'date': 'required',
        'version': 'required'
    }

    def __init__(self, date=None, version=None, local_vars_configuration=None):  # noqa: E501
        """UpsertReconciliationRunRequest - a model defined in OpenAPI"
        
        :param date:  The effective date of the reconciliation run (required)
        :type date: datetime
        :param version:  The version number for a run (required)
        :type version: int

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._date = None
        self._version = None
        self.discriminator = None

        self.date = date
        self.version = version

    @property
    def date(self):
        """Gets the date of this UpsertReconciliationRunRequest.  # noqa: E501

        The effective date of the reconciliation run  # noqa: E501

        :return: The date of this UpsertReconciliationRunRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this UpsertReconciliationRunRequest.

        The effective date of the reconciliation run  # noqa: E501

        :param date: The date of this UpsertReconciliationRunRequest.  # noqa: E501
        :type date: datetime
        """
        if self.local_vars_configuration.client_side_validation and date is None:  # noqa: E501
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def version(self):
        """Gets the version of this UpsertReconciliationRunRequest.  # noqa: E501

        The version number for a run  # noqa: E501

        :return: The version of this UpsertReconciliationRunRequest.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UpsertReconciliationRunRequest.

        The version number for a run  # noqa: E501

        :param version: The version of this UpsertReconciliationRunRequest.  # noqa: E501
        :type version: int
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

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
        if not isinstance(other, UpsertReconciliationRunRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpsertReconciliationRunRequest):
            return True

        return self.to_dict() != other.to_dict()
