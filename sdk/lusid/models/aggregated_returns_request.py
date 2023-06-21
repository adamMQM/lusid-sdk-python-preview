# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.273
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


class AggregatedReturnsRequest(object):
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
        'metrics': 'list[PerformanceReturnsMetric]',
        'return_ids': 'list[ResourceId]',
        'recipe_id': 'ResourceId',
        'composite_method': 'str',
        'period': 'str',
        'output_frequency': 'str',
        'alternative_inception_date': 'str',
        'holiday_calendars': 'list[str]'
    }

    attribute_map = {
        'metrics': 'metrics',
        'return_ids': 'returnIds',
        'recipe_id': 'recipeId',
        'composite_method': 'compositeMethod',
        'period': 'period',
        'output_frequency': 'outputFrequency',
        'alternative_inception_date': 'alternativeInceptionDate',
        'holiday_calendars': 'holidayCalendars'
    }

    required_map = {
        'metrics': 'required',
        'return_ids': 'optional',
        'recipe_id': 'optional',
        'composite_method': 'optional',
        'period': 'optional',
        'output_frequency': 'optional',
        'alternative_inception_date': 'optional',
        'holiday_calendars': 'optional'
    }

    def __init__(self, metrics=None, return_ids=None, recipe_id=None, composite_method=None, period=None, output_frequency=None, alternative_inception_date=None, holiday_calendars=None, local_vars_configuration=None):  # noqa: E501
        """AggregatedReturnsRequest - a model defined in OpenAPI"
        
        :param metrics:  A list of metrics to calculate in the AggregatedReturns. (required)
        :type metrics: list[lusid.PerformanceReturnsMetric]
        :param return_ids:  The Scope and code of the returns.
        :type return_ids: list[lusid.ResourceId]
        :param recipe_id: 
        :type recipe_id: lusid.ResourceId
        :param composite_method:  The method used to calculate the Portfolio performance: Equal/Asset.
        :type composite_method: str
        :param period:  The type of the returns used to calculate the aggregation result: Daily/Monthly.
        :type period: str
        :param output_frequency:  The type of calculated output: Daily/Weekly/Monthly/Quarterly/Half-Yearly/Yearly.
        :type output_frequency: str
        :param alternative_inception_date:  Optional - either a date, or the key for a portfolio property containing a date. If provided, the given date will override the inception date for this request.
        :type alternative_inception_date: str
        :param holiday_calendars:  The holiday calendar(s) that should be used in determining the date schedule. Holiday calendar(s) are supplied by their codes, for example, 'CoppClark'. Note that when the calendars are not available (e.g. when the user has insufficient permissions), a recipe setting will be used to determine whether the whole batch should then fail or whether the calendar not being available should simply be ignored.
        :type holiday_calendars: list[str]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._metrics = None
        self._return_ids = None
        self._recipe_id = None
        self._composite_method = None
        self._period = None
        self._output_frequency = None
        self._alternative_inception_date = None
        self._holiday_calendars = None
        self.discriminator = None

        self.metrics = metrics
        self.return_ids = return_ids
        if recipe_id is not None:
            self.recipe_id = recipe_id
        self.composite_method = composite_method
        self.period = period
        self.output_frequency = output_frequency
        self.alternative_inception_date = alternative_inception_date
        self.holiday_calendars = holiday_calendars

    @property
    def metrics(self):
        """Gets the metrics of this AggregatedReturnsRequest.  # noqa: E501

        A list of metrics to calculate in the AggregatedReturns.  # noqa: E501

        :return: The metrics of this AggregatedReturnsRequest.  # noqa: E501
        :rtype: list[lusid.PerformanceReturnsMetric]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this AggregatedReturnsRequest.

        A list of metrics to calculate in the AggregatedReturns.  # noqa: E501

        :param metrics: The metrics of this AggregatedReturnsRequest.  # noqa: E501
        :type metrics: list[lusid.PerformanceReturnsMetric]
        """
        if self.local_vars_configuration.client_side_validation and metrics is None:  # noqa: E501
            raise ValueError("Invalid value for `metrics`, must not be `None`")  # noqa: E501

        self._metrics = metrics

    @property
    def return_ids(self):
        """Gets the return_ids of this AggregatedReturnsRequest.  # noqa: E501

        The Scope and code of the returns.  # noqa: E501

        :return: The return_ids of this AggregatedReturnsRequest.  # noqa: E501
        :rtype: list[lusid.ResourceId]
        """
        return self._return_ids

    @return_ids.setter
    def return_ids(self, return_ids):
        """Sets the return_ids of this AggregatedReturnsRequest.

        The Scope and code of the returns.  # noqa: E501

        :param return_ids: The return_ids of this AggregatedReturnsRequest.  # noqa: E501
        :type return_ids: list[lusid.ResourceId]
        """

        self._return_ids = return_ids

    @property
    def recipe_id(self):
        """Gets the recipe_id of this AggregatedReturnsRequest.  # noqa: E501


        :return: The recipe_id of this AggregatedReturnsRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._recipe_id

    @recipe_id.setter
    def recipe_id(self, recipe_id):
        """Sets the recipe_id of this AggregatedReturnsRequest.


        :param recipe_id: The recipe_id of this AggregatedReturnsRequest.  # noqa: E501
        :type recipe_id: lusid.ResourceId
        """

        self._recipe_id = recipe_id

    @property
    def composite_method(self):
        """Gets the composite_method of this AggregatedReturnsRequest.  # noqa: E501

        The method used to calculate the Portfolio performance: Equal/Asset.  # noqa: E501

        :return: The composite_method of this AggregatedReturnsRequest.  # noqa: E501
        :rtype: str
        """
        return self._composite_method

    @composite_method.setter
    def composite_method(self, composite_method):
        """Sets the composite_method of this AggregatedReturnsRequest.

        The method used to calculate the Portfolio performance: Equal/Asset.  # noqa: E501

        :param composite_method: The composite_method of this AggregatedReturnsRequest.  # noqa: E501
        :type composite_method: str
        """

        self._composite_method = composite_method

    @property
    def period(self):
        """Gets the period of this AggregatedReturnsRequest.  # noqa: E501

        The type of the returns used to calculate the aggregation result: Daily/Monthly.  # noqa: E501

        :return: The period of this AggregatedReturnsRequest.  # noqa: E501
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this AggregatedReturnsRequest.

        The type of the returns used to calculate the aggregation result: Daily/Monthly.  # noqa: E501

        :param period: The period of this AggregatedReturnsRequest.  # noqa: E501
        :type period: str
        """

        self._period = period

    @property
    def output_frequency(self):
        """Gets the output_frequency of this AggregatedReturnsRequest.  # noqa: E501

        The type of calculated output: Daily/Weekly/Monthly/Quarterly/Half-Yearly/Yearly.  # noqa: E501

        :return: The output_frequency of this AggregatedReturnsRequest.  # noqa: E501
        :rtype: str
        """
        return self._output_frequency

    @output_frequency.setter
    def output_frequency(self, output_frequency):
        """Sets the output_frequency of this AggregatedReturnsRequest.

        The type of calculated output: Daily/Weekly/Monthly/Quarterly/Half-Yearly/Yearly.  # noqa: E501

        :param output_frequency: The output_frequency of this AggregatedReturnsRequest.  # noqa: E501
        :type output_frequency: str
        """

        self._output_frequency = output_frequency

    @property
    def alternative_inception_date(self):
        """Gets the alternative_inception_date of this AggregatedReturnsRequest.  # noqa: E501

        Optional - either a date, or the key for a portfolio property containing a date. If provided, the given date will override the inception date for this request.  # noqa: E501

        :return: The alternative_inception_date of this AggregatedReturnsRequest.  # noqa: E501
        :rtype: str
        """
        return self._alternative_inception_date

    @alternative_inception_date.setter
    def alternative_inception_date(self, alternative_inception_date):
        """Sets the alternative_inception_date of this AggregatedReturnsRequest.

        Optional - either a date, or the key for a portfolio property containing a date. If provided, the given date will override the inception date for this request.  # noqa: E501

        :param alternative_inception_date: The alternative_inception_date of this AggregatedReturnsRequest.  # noqa: E501
        :type alternative_inception_date: str
        """

        self._alternative_inception_date = alternative_inception_date

    @property
    def holiday_calendars(self):
        """Gets the holiday_calendars of this AggregatedReturnsRequest.  # noqa: E501

        The holiday calendar(s) that should be used in determining the date schedule. Holiday calendar(s) are supplied by their codes, for example, 'CoppClark'. Note that when the calendars are not available (e.g. when the user has insufficient permissions), a recipe setting will be used to determine whether the whole batch should then fail or whether the calendar not being available should simply be ignored.  # noqa: E501

        :return: The holiday_calendars of this AggregatedReturnsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._holiday_calendars

    @holiday_calendars.setter
    def holiday_calendars(self, holiday_calendars):
        """Sets the holiday_calendars of this AggregatedReturnsRequest.

        The holiday calendar(s) that should be used in determining the date schedule. Holiday calendar(s) are supplied by their codes, for example, 'CoppClark'. Note that when the calendars are not available (e.g. when the user has insufficient permissions), a recipe setting will be used to determine whether the whole batch should then fail or whether the calendar not being available should simply be ignored.  # noqa: E501

        :param holiday_calendars: The holiday_calendars of this AggregatedReturnsRequest.  # noqa: E501
        :type holiday_calendars: list[str]
        """

        self._holiday_calendars = holiday_calendars

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
        if not isinstance(other, AggregatedReturnsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AggregatedReturnsRequest):
            return True

        return self.to_dict() != other.to_dict()
