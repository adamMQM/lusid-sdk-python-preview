# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2723
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class Change(object):
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
        'href': 'str',
        'entity_id': 'ResourceId',
        'corrected': 'bool',
        'correction_effective_at': 'datetime',
        'correction_as_at': 'datetime',
        'amended': 'bool',
        'amendment_effective_at': 'datetime',
        'amendment_as_at': 'datetime',
        'links': 'list[Link]'
    }

    attribute_map = {
        'href': 'href',
        'entity_id': 'entityId',
        'corrected': 'corrected',
        'correction_effective_at': 'correctionEffectiveAt',
        'correction_as_at': 'correctionAsAt',
        'amended': 'amended',
        'amendment_effective_at': 'amendmentEffectiveAt',
        'amendment_as_at': 'amendmentAsAt',
        'links': 'links'
    }

    required_map = {
        'href': 'optional',
        'entity_id': 'required',
        'corrected': 'required',
        'correction_effective_at': 'optional',
        'correction_as_at': 'optional',
        'amended': 'required',
        'amendment_effective_at': 'optional',
        'amendment_as_at': 'optional',
        'links': 'optional'
    }

    def __init__(self, href=None, entity_id=None, corrected=None, correction_effective_at=None, correction_as_at=None, amended=None, amendment_effective_at=None, amendment_as_at=None, links=None):  # noqa: E501
        """
        Change - a model defined in OpenAPI

        :param href: 
        :type href: str
        :param entity_id:  (required)
        :type entity_id: lusid.ResourceId
        :param corrected:  (required)
        :type corrected: bool
        :param correction_effective_at: 
        :type correction_effective_at: datetime
        :param correction_as_at: 
        :type correction_as_at: datetime
        :param amended:  (required)
        :type amended: bool
        :param amendment_effective_at: 
        :type amendment_effective_at: datetime
        :param amendment_as_at: 
        :type amendment_as_at: datetime
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501

        self._href = None
        self._entity_id = None
        self._corrected = None
        self._correction_effective_at = None
        self._correction_as_at = None
        self._amended = None
        self._amendment_effective_at = None
        self._amendment_as_at = None
        self._links = None
        self.discriminator = None

        self.href = href
        self.entity_id = entity_id
        self.corrected = corrected
        self.correction_effective_at = correction_effective_at
        self.correction_as_at = correction_as_at
        self.amended = amended
        self.amendment_effective_at = amendment_effective_at
        self.amendment_as_at = amendment_as_at
        self.links = links

    @property
    def href(self):
        """Gets the href of this Change.  # noqa: E501


        :return: The href of this Change.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Change.


        :param href: The href of this Change.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def entity_id(self):
        """Gets the entity_id of this Change.  # noqa: E501


        :return: The entity_id of this Change.  # noqa: E501
        :rtype: ResourceId
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this Change.


        :param entity_id: The entity_id of this Change.  # noqa: E501
        :type: ResourceId
        """
        if entity_id is None:
            raise ValueError("Invalid value for `entity_id`, must not be `None`")  # noqa: E501

        self._entity_id = entity_id

    @property
    def corrected(self):
        """Gets the corrected of this Change.  # noqa: E501


        :return: The corrected of this Change.  # noqa: E501
        :rtype: bool
        """
        return self._corrected

    @corrected.setter
    def corrected(self, corrected):
        """Sets the corrected of this Change.


        :param corrected: The corrected of this Change.  # noqa: E501
        :type: bool
        """
        if corrected is None:
            raise ValueError("Invalid value for `corrected`, must not be `None`")  # noqa: E501

        self._corrected = corrected

    @property
    def correction_effective_at(self):
        """Gets the correction_effective_at of this Change.  # noqa: E501


        :return: The correction_effective_at of this Change.  # noqa: E501
        :rtype: datetime
        """
        return self._correction_effective_at

    @correction_effective_at.setter
    def correction_effective_at(self, correction_effective_at):
        """Sets the correction_effective_at of this Change.


        :param correction_effective_at: The correction_effective_at of this Change.  # noqa: E501
        :type: datetime
        """

        self._correction_effective_at = correction_effective_at

    @property
    def correction_as_at(self):
        """Gets the correction_as_at of this Change.  # noqa: E501


        :return: The correction_as_at of this Change.  # noqa: E501
        :rtype: datetime
        """
        return self._correction_as_at

    @correction_as_at.setter
    def correction_as_at(self, correction_as_at):
        """Sets the correction_as_at of this Change.


        :param correction_as_at: The correction_as_at of this Change.  # noqa: E501
        :type: datetime
        """

        self._correction_as_at = correction_as_at

    @property
    def amended(self):
        """Gets the amended of this Change.  # noqa: E501


        :return: The amended of this Change.  # noqa: E501
        :rtype: bool
        """
        return self._amended

    @amended.setter
    def amended(self, amended):
        """Sets the amended of this Change.


        :param amended: The amended of this Change.  # noqa: E501
        :type: bool
        """
        if amended is None:
            raise ValueError("Invalid value for `amended`, must not be `None`")  # noqa: E501

        self._amended = amended

    @property
    def amendment_effective_at(self):
        """Gets the amendment_effective_at of this Change.  # noqa: E501


        :return: The amendment_effective_at of this Change.  # noqa: E501
        :rtype: datetime
        """
        return self._amendment_effective_at

    @amendment_effective_at.setter
    def amendment_effective_at(self, amendment_effective_at):
        """Sets the amendment_effective_at of this Change.


        :param amendment_effective_at: The amendment_effective_at of this Change.  # noqa: E501
        :type: datetime
        """

        self._amendment_effective_at = amendment_effective_at

    @property
    def amendment_as_at(self):
        """Gets the amendment_as_at of this Change.  # noqa: E501


        :return: The amendment_as_at of this Change.  # noqa: E501
        :rtype: datetime
        """
        return self._amendment_as_at

    @amendment_as_at.setter
    def amendment_as_at(self, amendment_as_at):
        """Sets the amendment_as_at of this Change.


        :param amendment_as_at: The amendment_as_at of this Change.  # noqa: E501
        :type: datetime
        """

        self._amendment_as_at = amendment_as_at

    @property
    def links(self):
        """Gets the links of this Change.  # noqa: E501


        :return: The links of this Change.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Change.


        :param links: The links of this Change.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

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
        if not isinstance(other, Change):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
