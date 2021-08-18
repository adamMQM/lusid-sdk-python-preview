# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3400
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class CounterpartySignatory(object):
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
        'name': 'str',
        'legal_entity_identifier': 'TypedResourceId'
    }

    attribute_map = {
        'name': 'name',
        'legal_entity_identifier': 'legalEntityIdentifier'
    }

    required_map = {
        'name': 'required',
        'legal_entity_identifier': 'required'
    }

    def __init__(self, name=None, legal_entity_identifier=None):  # noqa: E501
        """
        CounterpartySignatory - a model defined in OpenAPI

        :param name:  A user-defined name or label for the counterparty signatory.  There is no requirement for this to match the \"displayName\" of the legal entity. (required)
        :type name: str
        :param legal_entity_identifier:  (required)
        :type legal_entity_identifier: lusid.TypedResourceId

        """  # noqa: E501

        self._name = None
        self._legal_entity_identifier = None
        self.discriminator = None

        self.name = name
        self.legal_entity_identifier = legal_entity_identifier

    @property
    def name(self):
        """Gets the name of this CounterpartySignatory.  # noqa: E501

        A user-defined name or label for the counterparty signatory.  There is no requirement for this to match the \"displayName\" of the legal entity.  # noqa: E501

        :return: The name of this CounterpartySignatory.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CounterpartySignatory.

        A user-defined name or label for the counterparty signatory.  There is no requirement for this to match the \"displayName\" of the legal entity.  # noqa: E501

        :param name: The name of this CounterpartySignatory.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def legal_entity_identifier(self):
        """Gets the legal_entity_identifier of this CounterpartySignatory.  # noqa: E501


        :return: The legal_entity_identifier of this CounterpartySignatory.  # noqa: E501
        :rtype: TypedResourceId
        """
        return self._legal_entity_identifier

    @legal_entity_identifier.setter
    def legal_entity_identifier(self, legal_entity_identifier):
        """Sets the legal_entity_identifier of this CounterpartySignatory.


        :param legal_entity_identifier: The legal_entity_identifier of this CounterpartySignatory.  # noqa: E501
        :type: TypedResourceId
        """
        if legal_entity_identifier is None:
            raise ValueError("Invalid value for `legal_entity_identifier`, must not be `None`")  # noqa: E501

        self._legal_entity_identifier = legal_entity_identifier

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
        if not isinstance(other, CounterpartySignatory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
