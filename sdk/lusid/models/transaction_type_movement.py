# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4296
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


class TransactionTypeMovement(object):
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
        'movement_types': 'str',
        'side': 'str',
        'direction': 'int',
        'properties': 'dict(str, PerpetualProperty)',
        'mappings': 'list[TransactionTypePropertyMapping]',
        'name': 'str'
    }

    attribute_map = {
        'movement_types': 'movementTypes',
        'side': 'side',
        'direction': 'direction',
        'properties': 'properties',
        'mappings': 'mappings',
        'name': 'name'
    }

    required_map = {
        'movement_types': 'required',
        'side': 'required',
        'direction': 'required',
        'properties': 'optional',
        'mappings': 'optional',
        'name': 'optional'
    }

    def __init__(self, movement_types=None, side=None, direction=None, properties=None, mappings=None, name=None, local_vars_configuration=None):  # noqa: E501
        """TransactionTypeMovement - a model defined in OpenAPI"
        
        :param movement_types:  Movement types determine the impact of the movement on the holdings (required)
        :type movement_types: str
        :param side:  The Side determines which of the fields from our transaction are used to generate the Movement. Side1 means the 'security' side of the transaction, ie the Instrument and Units; Side2 means the 'cash' side, ie the Total Consideration (required)
        :type side: str
        :param direction:   A multiplier to apply to Transaction amounts; the values are -1 to indicate to reverse the signs and 1 to indicate to use the signed values from the Transaction directly. For a typical Transaction with unsigned values, 1 means increase, -1 means decrease (required)
        :type direction: int
        :param properties:  The properties associated with the underlying Movement
        :type properties: dict[str, lusid.PerpetualProperty]
        :param mappings:  This allows you to map a transaction property to a property on the underlying holding
        :type mappings: list[lusid.TransactionTypePropertyMapping]
        :param name:  The movement name (optional)
        :type name: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._movement_types = None
        self._side = None
        self._direction = None
        self._properties = None
        self._mappings = None
        self._name = None
        self.discriminator = None

        self.movement_types = movement_types
        self.side = side
        self.direction = direction
        self.properties = properties
        self.mappings = mappings
        self.name = name

    @property
    def movement_types(self):
        """Gets the movement_types of this TransactionTypeMovement.  # noqa: E501

        Movement types determine the impact of the movement on the holdings  # noqa: E501

        :return: The movement_types of this TransactionTypeMovement.  # noqa: E501
        :rtype: str
        """
        return self._movement_types

    @movement_types.setter
    def movement_types(self, movement_types):
        """Sets the movement_types of this TransactionTypeMovement.

        Movement types determine the impact of the movement on the holdings  # noqa: E501

        :param movement_types: The movement_types of this TransactionTypeMovement.  # noqa: E501
        :type movement_types: str
        """
        if self.local_vars_configuration.client_side_validation and movement_types is None:  # noqa: E501
            raise ValueError("Invalid value for `movement_types`, must not be `None`")  # noqa: E501

        self._movement_types = movement_types

    @property
    def side(self):
        """Gets the side of this TransactionTypeMovement.  # noqa: E501

        The Side determines which of the fields from our transaction are used to generate the Movement. Side1 means the 'security' side of the transaction, ie the Instrument and Units; Side2 means the 'cash' side, ie the Total Consideration  # noqa: E501

        :return: The side of this TransactionTypeMovement.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this TransactionTypeMovement.

        The Side determines which of the fields from our transaction are used to generate the Movement. Side1 means the 'security' side of the transaction, ie the Instrument and Units; Side2 means the 'cash' side, ie the Total Consideration  # noqa: E501

        :param side: The side of this TransactionTypeMovement.  # noqa: E501
        :type side: str
        """
        if self.local_vars_configuration.client_side_validation and side is None:  # noqa: E501
            raise ValueError("Invalid value for `side`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                side is not None and len(side) > 64):
            raise ValueError("Invalid value for `side`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                side is not None and len(side) < 1):
            raise ValueError("Invalid value for `side`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                side is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', side)):  # noqa: E501
            raise ValueError(r"Invalid value for `side`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._side = side

    @property
    def direction(self):
        """Gets the direction of this TransactionTypeMovement.  # noqa: E501

         A multiplier to apply to Transaction amounts; the values are -1 to indicate to reverse the signs and 1 to indicate to use the signed values from the Transaction directly. For a typical Transaction with unsigned values, 1 means increase, -1 means decrease  # noqa: E501

        :return: The direction of this TransactionTypeMovement.  # noqa: E501
        :rtype: int
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this TransactionTypeMovement.

         A multiplier to apply to Transaction amounts; the values are -1 to indicate to reverse the signs and 1 to indicate to use the signed values from the Transaction directly. For a typical Transaction with unsigned values, 1 means increase, -1 means decrease  # noqa: E501

        :param direction: The direction of this TransactionTypeMovement.  # noqa: E501
        :type direction: int
        """
        if self.local_vars_configuration.client_side_validation and direction is None:  # noqa: E501
            raise ValueError("Invalid value for `direction`, must not be `None`")  # noqa: E501

        self._direction = direction

    @property
    def properties(self):
        """Gets the properties of this TransactionTypeMovement.  # noqa: E501

        The properties associated with the underlying Movement  # noqa: E501

        :return: The properties of this TransactionTypeMovement.  # noqa: E501
        :rtype: dict[str, lusid.PerpetualProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this TransactionTypeMovement.

        The properties associated with the underlying Movement  # noqa: E501

        :param properties: The properties of this TransactionTypeMovement.  # noqa: E501
        :type properties: dict[str, lusid.PerpetualProperty]
        """

        self._properties = properties

    @property
    def mappings(self):
        """Gets the mappings of this TransactionTypeMovement.  # noqa: E501

        This allows you to map a transaction property to a property on the underlying holding  # noqa: E501

        :return: The mappings of this TransactionTypeMovement.  # noqa: E501
        :rtype: list[lusid.TransactionTypePropertyMapping]
        """
        return self._mappings

    @mappings.setter
    def mappings(self, mappings):
        """Sets the mappings of this TransactionTypeMovement.

        This allows you to map a transaction property to a property on the underlying holding  # noqa: E501

        :param mappings: The mappings of this TransactionTypeMovement.  # noqa: E501
        :type mappings: list[lusid.TransactionTypePropertyMapping]
        """

        self._mappings = mappings

    @property
    def name(self):
        """Gets the name of this TransactionTypeMovement.  # noqa: E501

        The movement name (optional)  # noqa: E501

        :return: The name of this TransactionTypeMovement.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TransactionTypeMovement.

        The movement name (optional)  # noqa: E501

        :param name: The name of this TransactionTypeMovement.  # noqa: E501
        :type name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 512):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[\s\S]*$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, TransactionTypeMovement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionTypeMovement):
            return True

        return self.to_dict() != other.to_dict()
