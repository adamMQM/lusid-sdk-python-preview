# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4618
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


class Package(object):
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
        'id': 'ResourceId',
        'order_ids': 'list[ResourceId]',
        'order_instruction_ids': 'list[ResourceId]',
        'properties': 'dict(str, PerpetualProperty)',
        'version': 'Version',
        'links': 'list[Link]'
    }

    attribute_map = {
        'id': 'id',
        'order_ids': 'orderIds',
        'order_instruction_ids': 'orderInstructionIds',
        'properties': 'properties',
        'version': 'version',
        'links': 'links'
    }

    required_map = {
        'id': 'required',
        'order_ids': 'required',
        'order_instruction_ids': 'required',
        'properties': 'optional',
        'version': 'optional',
        'links': 'optional'
    }

    def __init__(self, id=None, order_ids=None, order_instruction_ids=None, properties=None, version=None, links=None, local_vars_configuration=None):  # noqa: E501
        """Package - a model defined in OpenAPI"
        
        :param id:  (required)
        :type id: lusid.ResourceId
        :param order_ids:  Related order ids. (required)
        :type order_ids: list[lusid.ResourceId]
        :param order_instruction_ids:  Related order instruction ids. (required)
        :type order_instruction_ids: list[lusid.ResourceId]
        :param properties:  Client-defined properties associated with this execution.
        :type properties: dict[str, lusid.PerpetualProperty]
        :param version: 
        :type version: lusid.Version
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._order_ids = None
        self._order_instruction_ids = None
        self._properties = None
        self._version = None
        self._links = None
        self.discriminator = None

        self.id = id
        self.order_ids = order_ids
        self.order_instruction_ids = order_instruction_ids
        self.properties = properties
        if version is not None:
            self.version = version
        self.links = links

    @property
    def id(self):
        """Gets the id of this Package.  # noqa: E501


        :return: The id of this Package.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Package.


        :param id: The id of this Package.  # noqa: E501
        :type id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def order_ids(self):
        """Gets the order_ids of this Package.  # noqa: E501

        Related order ids.  # noqa: E501

        :return: The order_ids of this Package.  # noqa: E501
        :rtype: list[lusid.ResourceId]
        """
        return self._order_ids

    @order_ids.setter
    def order_ids(self, order_ids):
        """Sets the order_ids of this Package.

        Related order ids.  # noqa: E501

        :param order_ids: The order_ids of this Package.  # noqa: E501
        :type order_ids: list[lusid.ResourceId]
        """
        if self.local_vars_configuration.client_side_validation and order_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `order_ids`, must not be `None`")  # noqa: E501

        self._order_ids = order_ids

    @property
    def order_instruction_ids(self):
        """Gets the order_instruction_ids of this Package.  # noqa: E501

        Related order instruction ids.  # noqa: E501

        :return: The order_instruction_ids of this Package.  # noqa: E501
        :rtype: list[lusid.ResourceId]
        """
        return self._order_instruction_ids

    @order_instruction_ids.setter
    def order_instruction_ids(self, order_instruction_ids):
        """Sets the order_instruction_ids of this Package.

        Related order instruction ids.  # noqa: E501

        :param order_instruction_ids: The order_instruction_ids of this Package.  # noqa: E501
        :type order_instruction_ids: list[lusid.ResourceId]
        """
        if self.local_vars_configuration.client_side_validation and order_instruction_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `order_instruction_ids`, must not be `None`")  # noqa: E501

        self._order_instruction_ids = order_instruction_ids

    @property
    def properties(self):
        """Gets the properties of this Package.  # noqa: E501

        Client-defined properties associated with this execution.  # noqa: E501

        :return: The properties of this Package.  # noqa: E501
        :rtype: dict[str, lusid.PerpetualProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Package.

        Client-defined properties associated with this execution.  # noqa: E501

        :param properties: The properties of this Package.  # noqa: E501
        :type properties: dict[str, lusid.PerpetualProperty]
        """

        self._properties = properties

    @property
    def version(self):
        """Gets the version of this Package.  # noqa: E501


        :return: The version of this Package.  # noqa: E501
        :rtype: lusid.Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Package.


        :param version: The version of this Package.  # noqa: E501
        :type version: lusid.Version
        """

        self._version = version

    @property
    def links(self):
        """Gets the links of this Package.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this Package.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Package.

        Collection of links.  # noqa: E501

        :param links: The links of this Package.  # noqa: E501
        :type links: list[lusid.Link]
        """

        self._links = links

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
        if not isinstance(other, Package):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Package):
            return True

        return self.to_dict() != other.to_dict()
