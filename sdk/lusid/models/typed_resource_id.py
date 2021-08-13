# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3389
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class TypedResourceId(object):
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
        'id_type_scope': 'str',
        'id_type_code': 'str',
        'code': 'str'
    }

    attribute_map = {
        'id_type_scope': 'idTypeScope',
        'id_type_code': 'idTypeCode',
        'code': 'code'
    }

    required_map = {
        'id_type_scope': 'required',
        'id_type_code': 'required',
        'code': 'required'
    }

    def __init__(self, id_type_scope=None, id_type_code=None, code=None):  # noqa: E501
        """
        TypedResourceId - a model defined in OpenAPI

        :param id_type_scope:  The scope of the identifier's (property) definition. (required)
        :type id_type_scope: str
        :param id_type_code:  The code of identifier's (property) definition. This describes what the identifier represents.  For a Person this might be a username, nationalInsuranceNumber or similar.  For a Legal Entity, this might be a registeredCompanyNumber or LEI. (required)
        :type id_type_code: str
        :param code:  The value of the user-defined identifier in respect of the entity. (required)
        :type code: str

        """  # noqa: E501

        self._id_type_scope = None
        self._id_type_code = None
        self._code = None
        self.discriminator = None

        self.id_type_scope = id_type_scope
        self.id_type_code = id_type_code
        self.code = code

    @property
    def id_type_scope(self):
        """Gets the id_type_scope of this TypedResourceId.  # noqa: E501

        The scope of the identifier's (property) definition.  # noqa: E501

        :return: The id_type_scope of this TypedResourceId.  # noqa: E501
        :rtype: str
        """
        return self._id_type_scope

    @id_type_scope.setter
    def id_type_scope(self, id_type_scope):
        """Sets the id_type_scope of this TypedResourceId.

        The scope of the identifier's (property) definition.  # noqa: E501

        :param id_type_scope: The id_type_scope of this TypedResourceId.  # noqa: E501
        :type: str
        """
        if id_type_scope is None:
            raise ValueError("Invalid value for `id_type_scope`, must not be `None`")  # noqa: E501
        if id_type_scope is not None and len(id_type_scope) > 64:
            raise ValueError("Invalid value for `id_type_scope`, length must be less than or equal to `64`")  # noqa: E501
        if id_type_scope is not None and len(id_type_scope) < 1:
            raise ValueError("Invalid value for `id_type_scope`, length must be greater than or equal to `1`")  # noqa: E501
        if (id_type_scope is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', id_type_scope)):  # noqa: E501
            raise ValueError(r"Invalid value for `id_type_scope`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._id_type_scope = id_type_scope

    @property
    def id_type_code(self):
        """Gets the id_type_code of this TypedResourceId.  # noqa: E501

        The code of identifier's (property) definition. This describes what the identifier represents.  For a Person this might be a username, nationalInsuranceNumber or similar.  For a Legal Entity, this might be a registeredCompanyNumber or LEI.  # noqa: E501

        :return: The id_type_code of this TypedResourceId.  # noqa: E501
        :rtype: str
        """
        return self._id_type_code

    @id_type_code.setter
    def id_type_code(self, id_type_code):
        """Sets the id_type_code of this TypedResourceId.

        The code of identifier's (property) definition. This describes what the identifier represents.  For a Person this might be a username, nationalInsuranceNumber or similar.  For a Legal Entity, this might be a registeredCompanyNumber or LEI.  # noqa: E501

        :param id_type_code: The id_type_code of this TypedResourceId.  # noqa: E501
        :type: str
        """
        if id_type_code is None:
            raise ValueError("Invalid value for `id_type_code`, must not be `None`")  # noqa: E501
        if id_type_code is not None and len(id_type_code) > 64:
            raise ValueError("Invalid value for `id_type_code`, length must be less than or equal to `64`")  # noqa: E501
        if id_type_code is not None and len(id_type_code) < 1:
            raise ValueError("Invalid value for `id_type_code`, length must be greater than or equal to `1`")  # noqa: E501
        if (id_type_code is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', id_type_code)):  # noqa: E501
            raise ValueError(r"Invalid value for `id_type_code`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._id_type_code = id_type_code

    @property
    def code(self):
        """Gets the code of this TypedResourceId.  # noqa: E501

        The value of the user-defined identifier in respect of the entity.  # noqa: E501

        :return: The code of this TypedResourceId.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this TypedResourceId.

        The value of the user-defined identifier in respect of the entity.  # noqa: E501

        :param code: The code of this TypedResourceId.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        if code is not None and len(code) > 64:
            raise ValueError("Invalid value for `code`, length must be less than or equal to `64`")  # noqa: E501
        if code is not None and len(code) < 1:
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `1`")  # noqa: E501
        if (code is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', code)):  # noqa: E501
            raise ValueError(r"Invalid value for `code`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._code = code

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
        if not isinstance(other, TypedResourceId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
