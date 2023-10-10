# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.597
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


class Abor(object):
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
        'id': 'ResourceId',
        'display_name': 'str',
        'description': 'str',
        'portfolio_ids': 'list[PortfolioEntityId]',
        'abor_configuration_id': 'ResourceId',
        'properties': 'dict(str, ModelProperty)',
        'version': 'Version',
        'links': 'list[Link]'
    }

    attribute_map = {
        'href': 'href',
        'id': 'id',
        'display_name': 'displayName',
        'description': 'description',
        'portfolio_ids': 'portfolioIds',
        'abor_configuration_id': 'aborConfigurationId',
        'properties': 'properties',
        'version': 'version',
        'links': 'links'
    }

    required_map = {
        'href': 'optional',
        'id': 'required',
        'display_name': 'optional',
        'description': 'optional',
        'portfolio_ids': 'required',
        'abor_configuration_id': 'optional',
        'properties': 'optional',
        'version': 'optional',
        'links': 'optional'
    }

    def __init__(self, href=None, id=None, display_name=None, description=None, portfolio_ids=None, abor_configuration_id=None, properties=None, version=None, links=None, local_vars_configuration=None):  # noqa: E501
        """Abor - a model defined in OpenAPI"
        
        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param id:  (required)
        :type id: lusid.ResourceId
        :param display_name:  The name of the Abor.
        :type display_name: str
        :param description:  The description for the Abor.
        :type description: str
        :param portfolio_ids:  The list with the portfolio ids which are part of the Abor. (required)
        :type portfolio_ids: list[lusid.PortfolioEntityId]
        :param abor_configuration_id: 
        :type abor_configuration_id: lusid.ResourceId
        :param properties:  A set of properties for the Abor.
        :type properties: dict[str, lusid.ModelProperty]
        :param version: 
        :type version: lusid.Version
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._href = None
        self._id = None
        self._display_name = None
        self._description = None
        self._portfolio_ids = None
        self._abor_configuration_id = None
        self._properties = None
        self._version = None
        self._links = None
        self.discriminator = None

        self.href = href
        self.id = id
        self.display_name = display_name
        self.description = description
        self.portfolio_ids = portfolio_ids
        if abor_configuration_id is not None:
            self.abor_configuration_id = abor_configuration_id
        self.properties = properties
        if version is not None:
            self.version = version
        self.links = links

    @property
    def href(self):
        """Gets the href of this Abor.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this Abor.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Abor.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this Abor.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this Abor.  # noqa: E501


        :return: The id of this Abor.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Abor.


        :param id: The id of this Abor.  # noqa: E501
        :type id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this Abor.  # noqa: E501

        The name of the Abor.  # noqa: E501

        :return: The display_name of this Abor.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Abor.

        The name of the Abor.  # noqa: E501

        :param display_name: The display_name of this Abor.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this Abor.  # noqa: E501

        The description for the Abor.  # noqa: E501

        :return: The description of this Abor.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Abor.

        The description for the Abor.  # noqa: E501

        :param description: The description of this Abor.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def portfolio_ids(self):
        """Gets the portfolio_ids of this Abor.  # noqa: E501

        The list with the portfolio ids which are part of the Abor.  # noqa: E501

        :return: The portfolio_ids of this Abor.  # noqa: E501
        :rtype: list[lusid.PortfolioEntityId]
        """
        return self._portfolio_ids

    @portfolio_ids.setter
    def portfolio_ids(self, portfolio_ids):
        """Sets the portfolio_ids of this Abor.

        The list with the portfolio ids which are part of the Abor.  # noqa: E501

        :param portfolio_ids: The portfolio_ids of this Abor.  # noqa: E501
        :type portfolio_ids: list[lusid.PortfolioEntityId]
        """
        if self.local_vars_configuration.client_side_validation and portfolio_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `portfolio_ids`, must not be `None`")  # noqa: E501

        self._portfolio_ids = portfolio_ids

    @property
    def abor_configuration_id(self):
        """Gets the abor_configuration_id of this Abor.  # noqa: E501


        :return: The abor_configuration_id of this Abor.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._abor_configuration_id

    @abor_configuration_id.setter
    def abor_configuration_id(self, abor_configuration_id):
        """Sets the abor_configuration_id of this Abor.


        :param abor_configuration_id: The abor_configuration_id of this Abor.  # noqa: E501
        :type abor_configuration_id: lusid.ResourceId
        """

        self._abor_configuration_id = abor_configuration_id

    @property
    def properties(self):
        """Gets the properties of this Abor.  # noqa: E501

        A set of properties for the Abor.  # noqa: E501

        :return: The properties of this Abor.  # noqa: E501
        :rtype: dict[str, lusid.ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Abor.

        A set of properties for the Abor.  # noqa: E501

        :param properties: The properties of this Abor.  # noqa: E501
        :type properties: dict[str, lusid.ModelProperty]
        """

        self._properties = properties

    @property
    def version(self):
        """Gets the version of this Abor.  # noqa: E501


        :return: The version of this Abor.  # noqa: E501
        :rtype: lusid.Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Abor.


        :param version: The version of this Abor.  # noqa: E501
        :type version: lusid.Version
        """

        self._version = version

    @property
    def links(self):
        """Gets the links of this Abor.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this Abor.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Abor.

        Collection of links.  # noqa: E501

        :param links: The links of this Abor.  # noqa: E501
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
        if not isinstance(other, Abor):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Abor):
            return True

        return self.to_dict() != other.to_dict()
