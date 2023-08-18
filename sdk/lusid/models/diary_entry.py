# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.451
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


class DiaryEntry(object):
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
        'abor_id': 'ResourceId',
        'diary_entry_code': 'str',
        'type': 'str',
        'name': 'str',
        'status': 'str',
        'effective_at': 'datetime',
        'query_as_at': 'datetime',
        'previous_entry_time': 'datetime',
        'properties': 'dict(str, ModelProperty)',
        'version': 'Version',
        'links': 'list[Link]'
    }

    attribute_map = {
        'href': 'href',
        'abor_id': 'aborId',
        'diary_entry_code': 'diaryEntryCode',
        'type': 'type',
        'name': 'name',
        'status': 'status',
        'effective_at': 'effectiveAt',
        'query_as_at': 'queryAsAt',
        'previous_entry_time': 'previousEntryTime',
        'properties': 'properties',
        'version': 'version',
        'links': 'links'
    }

    required_map = {
        'href': 'optional',
        'abor_id': 'optional',
        'diary_entry_code': 'optional',
        'type': 'required',
        'name': 'optional',
        'status': 'required',
        'effective_at': 'required',
        'query_as_at': 'optional',
        'previous_entry_time': 'optional',
        'properties': 'optional',
        'version': 'optional',
        'links': 'optional'
    }

    def __init__(self, href=None, abor_id=None, diary_entry_code=None, type=None, name=None, status=None, effective_at=None, query_as_at=None, previous_entry_time=None, properties=None, version=None, links=None, local_vars_configuration=None):  # noqa: E501
        """DiaryEntry - a model defined in OpenAPI"
        
        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param abor_id: 
        :type abor_id: lusid.ResourceId
        :param diary_entry_code:  The code of the diary entry.
        :type diary_entry_code: str
        :param type:  The type of the diary entry. (required)
        :type type: str
        :param name:  The name of the diary entry.
        :type name: str
        :param status:  The status of the diary entry. Defaults to 'Undefined'. (required)
        :type status: str
        :param effective_at:  The effective time of the diary entry. (required)
        :type effective_at: datetime
        :param query_as_at:  The query time of the diary entry. Defaults to latest.
        :type query_as_at: datetime
        :param previous_entry_time:  The entry time of the previous diary entry.
        :type previous_entry_time: datetime
        :param properties:  Properties to add to the diary entry.
        :type properties: dict[str, lusid.ModelProperty]
        :param version: 
        :type version: lusid.Version
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._href = None
        self._abor_id = None
        self._diary_entry_code = None
        self._type = None
        self._name = None
        self._status = None
        self._effective_at = None
        self._query_as_at = None
        self._previous_entry_time = None
        self._properties = None
        self._version = None
        self._links = None
        self.discriminator = None

        self.href = href
        if abor_id is not None:
            self.abor_id = abor_id
        self.diary_entry_code = diary_entry_code
        self.type = type
        self.name = name
        self.status = status
        self.effective_at = effective_at
        if query_as_at is not None:
            self.query_as_at = query_as_at
        if previous_entry_time is not None:
            self.previous_entry_time = previous_entry_time
        self.properties = properties
        if version is not None:
            self.version = version
        self.links = links

    @property
    def href(self):
        """Gets the href of this DiaryEntry.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this DiaryEntry.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this DiaryEntry.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this DiaryEntry.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def abor_id(self):
        """Gets the abor_id of this DiaryEntry.  # noqa: E501


        :return: The abor_id of this DiaryEntry.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._abor_id

    @abor_id.setter
    def abor_id(self, abor_id):
        """Sets the abor_id of this DiaryEntry.


        :param abor_id: The abor_id of this DiaryEntry.  # noqa: E501
        :type abor_id: lusid.ResourceId
        """

        self._abor_id = abor_id

    @property
    def diary_entry_code(self):
        """Gets the diary_entry_code of this DiaryEntry.  # noqa: E501

        The code of the diary entry.  # noqa: E501

        :return: The diary_entry_code of this DiaryEntry.  # noqa: E501
        :rtype: str
        """
        return self._diary_entry_code

    @diary_entry_code.setter
    def diary_entry_code(self, diary_entry_code):
        """Sets the diary_entry_code of this DiaryEntry.

        The code of the diary entry.  # noqa: E501

        :param diary_entry_code: The diary_entry_code of this DiaryEntry.  # noqa: E501
        :type diary_entry_code: str
        """

        self._diary_entry_code = diary_entry_code

    @property
    def type(self):
        """Gets the type of this DiaryEntry.  # noqa: E501

        The type of the diary entry.  # noqa: E501

        :return: The type of this DiaryEntry.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DiaryEntry.

        The type of the diary entry.  # noqa: E501

        :param type: The type of this DiaryEntry.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) < 1):
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this DiaryEntry.  # noqa: E501

        The name of the diary entry.  # noqa: E501

        :return: The name of this DiaryEntry.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DiaryEntry.

        The name of the diary entry.  # noqa: E501

        :param name: The name of this DiaryEntry.  # noqa: E501
        :type name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 256):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[^\\<>&\"]+$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[^\\<>&\"]+$/`")  # noqa: E501

        self._name = name

    @property
    def status(self):
        """Gets the status of this DiaryEntry.  # noqa: E501

        The status of the diary entry. Defaults to 'Undefined'.  # noqa: E501

        :return: The status of this DiaryEntry.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DiaryEntry.

        The status of the diary entry. Defaults to 'Undefined'.  # noqa: E501

        :param status: The status of this DiaryEntry.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                status is not None and len(status) < 1):
            raise ValueError("Invalid value for `status`, length must be greater than or equal to `1`")  # noqa: E501

        self._status = status

    @property
    def effective_at(self):
        """Gets the effective_at of this DiaryEntry.  # noqa: E501

        The effective time of the diary entry.  # noqa: E501

        :return: The effective_at of this DiaryEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_at

    @effective_at.setter
    def effective_at(self, effective_at):
        """Sets the effective_at of this DiaryEntry.

        The effective time of the diary entry.  # noqa: E501

        :param effective_at: The effective_at of this DiaryEntry.  # noqa: E501
        :type effective_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and effective_at is None:  # noqa: E501
            raise ValueError("Invalid value for `effective_at`, must not be `None`")  # noqa: E501

        self._effective_at = effective_at

    @property
    def query_as_at(self):
        """Gets the query_as_at of this DiaryEntry.  # noqa: E501

        The query time of the diary entry. Defaults to latest.  # noqa: E501

        :return: The query_as_at of this DiaryEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._query_as_at

    @query_as_at.setter
    def query_as_at(self, query_as_at):
        """Sets the query_as_at of this DiaryEntry.

        The query time of the diary entry. Defaults to latest.  # noqa: E501

        :param query_as_at: The query_as_at of this DiaryEntry.  # noqa: E501
        :type query_as_at: datetime
        """

        self._query_as_at = query_as_at

    @property
    def previous_entry_time(self):
        """Gets the previous_entry_time of this DiaryEntry.  # noqa: E501

        The entry time of the previous diary entry.  # noqa: E501

        :return: The previous_entry_time of this DiaryEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._previous_entry_time

    @previous_entry_time.setter
    def previous_entry_time(self, previous_entry_time):
        """Sets the previous_entry_time of this DiaryEntry.

        The entry time of the previous diary entry.  # noqa: E501

        :param previous_entry_time: The previous_entry_time of this DiaryEntry.  # noqa: E501
        :type previous_entry_time: datetime
        """

        self._previous_entry_time = previous_entry_time

    @property
    def properties(self):
        """Gets the properties of this DiaryEntry.  # noqa: E501

        Properties to add to the diary entry.  # noqa: E501

        :return: The properties of this DiaryEntry.  # noqa: E501
        :rtype: dict[str, lusid.ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this DiaryEntry.

        Properties to add to the diary entry.  # noqa: E501

        :param properties: The properties of this DiaryEntry.  # noqa: E501
        :type properties: dict[str, lusid.ModelProperty]
        """

        self._properties = properties

    @property
    def version(self):
        """Gets the version of this DiaryEntry.  # noqa: E501


        :return: The version of this DiaryEntry.  # noqa: E501
        :rtype: lusid.Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DiaryEntry.


        :param version: The version of this DiaryEntry.  # noqa: E501
        :type version: lusid.Version
        """

        self._version = version

    @property
    def links(self):
        """Gets the links of this DiaryEntry.  # noqa: E501


        :return: The links of this DiaryEntry.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this DiaryEntry.


        :param links: The links of this DiaryEntry.  # noqa: E501
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
        if not isinstance(other, DiaryEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DiaryEntry):
            return True

        return self.to_dict() != other.to_dict()
