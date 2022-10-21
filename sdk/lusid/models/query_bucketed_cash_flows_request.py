# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4884
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


class QueryBucketedCashFlowsRequest(object):
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
        'as_at': 'datetime',
        'window_start': 'datetime',
        'window_end': 'datetime',
        'portfolio_entity_ids': 'list[PortfolioEntityId]',
        'effective_at': 'datetime',
        'recipe_id': 'ResourceId',
        'rounding_method': 'str',
        'bucketing_dates': 'list[datetime]',
        'bucketing_tenors': 'list[str]',
        'report_currency': 'str',
        'group_by': 'list[str]',
        'addresses': 'list[str]',
        'equip_with_subtotals': 'bool'
    }

    attribute_map = {
        'as_at': 'asAt',
        'window_start': 'windowStart',
        'window_end': 'windowEnd',
        'portfolio_entity_ids': 'portfolioEntityIds',
        'effective_at': 'effectiveAt',
        'recipe_id': 'recipeId',
        'rounding_method': 'roundingMethod',
        'bucketing_dates': 'bucketingDates',
        'bucketing_tenors': 'bucketingTenors',
        'report_currency': 'reportCurrency',
        'group_by': 'groupBy',
        'addresses': 'addresses',
        'equip_with_subtotals': 'equipWithSubtotals'
    }

    required_map = {
        'as_at': 'optional',
        'window_start': 'required',
        'window_end': 'required',
        'portfolio_entity_ids': 'required',
        'effective_at': 'required',
        'recipe_id': 'required',
        'rounding_method': 'required',
        'bucketing_dates': 'optional',
        'bucketing_tenors': 'optional',
        'report_currency': 'required',
        'group_by': 'optional',
        'addresses': 'optional',
        'equip_with_subtotals': 'optional'
    }

    def __init__(self, as_at=None, window_start=None, window_end=None, portfolio_entity_ids=None, effective_at=None, recipe_id=None, rounding_method=None, bucketing_dates=None, bucketing_tenors=None, report_currency=None, group_by=None, addresses=None, equip_with_subtotals=None, local_vars_configuration=None):  # noqa: E501
        """QueryBucketedCashFlowsRequest - a model defined in OpenAPI"
        
        :param as_at:  The time of the system at which to query for bucketed cashflows.
        :type as_at: datetime
        :param window_start:  The start date of the window. (required)
        :type window_start: datetime
        :param window_end:  The end date of the window. (required)
        :type window_end: datetime
        :param portfolio_entity_ids:  The set of portfolios and portfolio groups to which the instrument events must belong. (required)
        :type portfolio_entity_ids: list[lusid.PortfolioEntityId]
        :param effective_at:  The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows (required)
        :type effective_at: datetime
        :param recipe_id:  (required)
        :type recipe_id: lusid.ResourceId
        :param rounding_method:  When bucketing, there is not a unique way to allocate the bucket points. RoundingMethod Supported string (enumeration) values are: [RoundDown, RoundUp]. (required)
        :type rounding_method: str
        :param bucketing_dates:  A list of dates to perform cashflow bucketing upon. If this is provided, the list of tenors for bucketing should be empty.
        :type bucketing_dates: list[datetime]
        :param bucketing_tenors:  A list of tenors to perform cashflow bucketing upon. If this is provided, the list of dates for bucketing should be empty.
        :type bucketing_tenors: list[str]
        :param report_currency:  Three letter ISO currency string indicating what currency to report in for ReportCurrency denominated queries. (required)
        :type report_currency: str
        :param group_by:  The set of address keys to use to group the bucketed cash flows.
        :type group_by: list[str]
        :param addresses:  The set of items that the user wishes to see in the results. If empty, will be defaulted to standard ones.
        :type addresses: list[str]
        :param equip_with_subtotals:  Flag directing the Valuation call to populate the results with subtotals of aggregates.
        :type equip_with_subtotals: bool

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._as_at = None
        self._window_start = None
        self._window_end = None
        self._portfolio_entity_ids = None
        self._effective_at = None
        self._recipe_id = None
        self._rounding_method = None
        self._bucketing_dates = None
        self._bucketing_tenors = None
        self._report_currency = None
        self._group_by = None
        self._addresses = None
        self._equip_with_subtotals = None
        self.discriminator = None

        self.as_at = as_at
        self.window_start = window_start
        self.window_end = window_end
        self.portfolio_entity_ids = portfolio_entity_ids
        self.effective_at = effective_at
        self.recipe_id = recipe_id
        self.rounding_method = rounding_method
        self.bucketing_dates = bucketing_dates
        self.bucketing_tenors = bucketing_tenors
        self.report_currency = report_currency
        self.group_by = group_by
        self.addresses = addresses
        if equip_with_subtotals is not None:
            self.equip_with_subtotals = equip_with_subtotals

    @property
    def as_at(self):
        """Gets the as_at of this QueryBucketedCashFlowsRequest.  # noqa: E501

        The time of the system at which to query for bucketed cashflows.  # noqa: E501

        :return: The as_at of this QueryBucketedCashFlowsRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at

    @as_at.setter
    def as_at(self, as_at):
        """Sets the as_at of this QueryBucketedCashFlowsRequest.

        The time of the system at which to query for bucketed cashflows.  # noqa: E501

        :param as_at: The as_at of this QueryBucketedCashFlowsRequest.  # noqa: E501
        :type as_at: datetime
        """

        self._as_at = as_at

    @property
    def window_start(self):
        """Gets the window_start of this QueryBucketedCashFlowsRequest.  # noqa: E501

        The start date of the window.  # noqa: E501

        :return: The window_start of this QueryBucketedCashFlowsRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._window_start

    @window_start.setter
    def window_start(self, window_start):
        """Sets the window_start of this QueryBucketedCashFlowsRequest.

        The start date of the window.  # noqa: E501

        :param window_start: The window_start of this QueryBucketedCashFlowsRequest.  # noqa: E501
        :type window_start: datetime
        """
        if self.local_vars_configuration.client_side_validation and window_start is None:  # noqa: E501
            raise ValueError("Invalid value for `window_start`, must not be `None`")  # noqa: E501

        self._window_start = window_start

    @property
    def window_end(self):
        """Gets the window_end of this QueryBucketedCashFlowsRequest.  # noqa: E501

        The end date of the window.  # noqa: E501

        :return: The window_end of this QueryBucketedCashFlowsRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._window_end

    @window_end.setter
    def window_end(self, window_end):
        """Sets the window_end of this QueryBucketedCashFlowsRequest.

        The end date of the window.  # noqa: E501

        :param window_end: The window_end of this QueryBucketedCashFlowsRequest.  # noqa: E501
        :type window_end: datetime
        """
        if self.local_vars_configuration.client_side_validation and window_end is None:  # noqa: E501
            raise ValueError("Invalid value for `window_end`, must not be `None`")  # noqa: E501

        self._window_end = window_end

    @property
    def portfolio_entity_ids(self):
        """Gets the portfolio_entity_ids of this QueryBucketedCashFlowsRequest.  # noqa: E501

        The set of portfolios and portfolio groups to which the instrument events must belong.  # noqa: E501

        :return: The portfolio_entity_ids of this QueryBucketedCashFlowsRequest.  # noqa: E501
        :rtype: list[lusid.PortfolioEntityId]
        """
        return self._portfolio_entity_ids

    @portfolio_entity_ids.setter
    def portfolio_entity_ids(self, portfolio_entity_ids):
        """Sets the portfolio_entity_ids of this QueryBucketedCashFlowsRequest.

        The set of portfolios and portfolio groups to which the instrument events must belong.  # noqa: E501

        :param portfolio_entity_ids: The portfolio_entity_ids of this QueryBucketedCashFlowsRequest.  # noqa: E501
        :type portfolio_entity_ids: list[lusid.PortfolioEntityId]
        """
        if self.local_vars_configuration.client_side_validation and portfolio_entity_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `portfolio_entity_ids`, must not be `None`")  # noqa: E501

        self._portfolio_entity_ids = portfolio_entity_ids

    @property
    def effective_at(self):
        """Gets the effective_at of this QueryBucketedCashFlowsRequest.  # noqa: E501

        The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows  # noqa: E501

        :return: The effective_at of this QueryBucketedCashFlowsRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_at

    @effective_at.setter
    def effective_at(self, effective_at):
        """Sets the effective_at of this QueryBucketedCashFlowsRequest.

        The valuation (pricing) effective datetime or cut label (inclusive) at which to evaluate the cashflows  # noqa: E501

        :param effective_at: The effective_at of this QueryBucketedCashFlowsRequest.  # noqa: E501
        :type effective_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and effective_at is None:  # noqa: E501
            raise ValueError("Invalid value for `effective_at`, must not be `None`")  # noqa: E501

        self._effective_at = effective_at

    @property
    def recipe_id(self):
        """Gets the recipe_id of this QueryBucketedCashFlowsRequest.  # noqa: E501


        :return: The recipe_id of this QueryBucketedCashFlowsRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._recipe_id

    @recipe_id.setter
    def recipe_id(self, recipe_id):
        """Sets the recipe_id of this QueryBucketedCashFlowsRequest.


        :param recipe_id: The recipe_id of this QueryBucketedCashFlowsRequest.  # noqa: E501
        :type recipe_id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and recipe_id is None:  # noqa: E501
            raise ValueError("Invalid value for `recipe_id`, must not be `None`")  # noqa: E501

        self._recipe_id = recipe_id

    @property
    def rounding_method(self):
        """Gets the rounding_method of this QueryBucketedCashFlowsRequest.  # noqa: E501

        When bucketing, there is not a unique way to allocate the bucket points. RoundingMethod Supported string (enumeration) values are: [RoundDown, RoundUp].  # noqa: E501

        :return: The rounding_method of this QueryBucketedCashFlowsRequest.  # noqa: E501
        :rtype: str
        """
        return self._rounding_method

    @rounding_method.setter
    def rounding_method(self, rounding_method):
        """Sets the rounding_method of this QueryBucketedCashFlowsRequest.

        When bucketing, there is not a unique way to allocate the bucket points. RoundingMethod Supported string (enumeration) values are: [RoundDown, RoundUp].  # noqa: E501

        :param rounding_method: The rounding_method of this QueryBucketedCashFlowsRequest.  # noqa: E501
        :type rounding_method: str
        """
        if self.local_vars_configuration.client_side_validation and rounding_method is None:  # noqa: E501
            raise ValueError("Invalid value for `rounding_method`, must not be `None`")  # noqa: E501

        self._rounding_method = rounding_method

    @property
    def bucketing_dates(self):
        """Gets the bucketing_dates of this QueryBucketedCashFlowsRequest.  # noqa: E501

        A list of dates to perform cashflow bucketing upon. If this is provided, the list of tenors for bucketing should be empty.  # noqa: E501

        :return: The bucketing_dates of this QueryBucketedCashFlowsRequest.  # noqa: E501
        :rtype: list[datetime]
        """
        return self._bucketing_dates

    @bucketing_dates.setter
    def bucketing_dates(self, bucketing_dates):
        """Sets the bucketing_dates of this QueryBucketedCashFlowsRequest.

        A list of dates to perform cashflow bucketing upon. If this is provided, the list of tenors for bucketing should be empty.  # noqa: E501

        :param bucketing_dates: The bucketing_dates of this QueryBucketedCashFlowsRequest.  # noqa: E501
        :type bucketing_dates: list[datetime]
        """

        self._bucketing_dates = bucketing_dates

    @property
    def bucketing_tenors(self):
        """Gets the bucketing_tenors of this QueryBucketedCashFlowsRequest.  # noqa: E501

        A list of tenors to perform cashflow bucketing upon. If this is provided, the list of dates for bucketing should be empty.  # noqa: E501

        :return: The bucketing_tenors of this QueryBucketedCashFlowsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._bucketing_tenors

    @bucketing_tenors.setter
    def bucketing_tenors(self, bucketing_tenors):
        """Sets the bucketing_tenors of this QueryBucketedCashFlowsRequest.

        A list of tenors to perform cashflow bucketing upon. If this is provided, the list of dates for bucketing should be empty.  # noqa: E501

        :param bucketing_tenors: The bucketing_tenors of this QueryBucketedCashFlowsRequest.  # noqa: E501
        :type bucketing_tenors: list[str]
        """

        self._bucketing_tenors = bucketing_tenors

    @property
    def report_currency(self):
        """Gets the report_currency of this QueryBucketedCashFlowsRequest.  # noqa: E501

        Three letter ISO currency string indicating what currency to report in for ReportCurrency denominated queries.  # noqa: E501

        :return: The report_currency of this QueryBucketedCashFlowsRequest.  # noqa: E501
        :rtype: str
        """
        return self._report_currency

    @report_currency.setter
    def report_currency(self, report_currency):
        """Sets the report_currency of this QueryBucketedCashFlowsRequest.

        Three letter ISO currency string indicating what currency to report in for ReportCurrency denominated queries.  # noqa: E501

        :param report_currency: The report_currency of this QueryBucketedCashFlowsRequest.  # noqa: E501
        :type report_currency: str
        """
        if self.local_vars_configuration.client_side_validation and report_currency is None:  # noqa: E501
            raise ValueError("Invalid value for `report_currency`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                report_currency is not None and len(report_currency) > 3):
            raise ValueError("Invalid value for `report_currency`, length must be less than or equal to `3`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                report_currency is not None and len(report_currency) < 0):
            raise ValueError("Invalid value for `report_currency`, length must be greater than or equal to `0`")  # noqa: E501

        self._report_currency = report_currency

    @property
    def group_by(self):
        """Gets the group_by of this QueryBucketedCashFlowsRequest.  # noqa: E501

        The set of address keys to use to group the bucketed cash flows.  # noqa: E501

        :return: The group_by of this QueryBucketedCashFlowsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """Sets the group_by of this QueryBucketedCashFlowsRequest.

        The set of address keys to use to group the bucketed cash flows.  # noqa: E501

        :param group_by: The group_by of this QueryBucketedCashFlowsRequest.  # noqa: E501
        :type group_by: list[str]
        """

        self._group_by = group_by

    @property
    def addresses(self):
        """Gets the addresses of this QueryBucketedCashFlowsRequest.  # noqa: E501

        The set of items that the user wishes to see in the results. If empty, will be defaulted to standard ones.  # noqa: E501

        :return: The addresses of this QueryBucketedCashFlowsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this QueryBucketedCashFlowsRequest.

        The set of items that the user wishes to see in the results. If empty, will be defaulted to standard ones.  # noqa: E501

        :param addresses: The addresses of this QueryBucketedCashFlowsRequest.  # noqa: E501
        :type addresses: list[str]
        """

        self._addresses = addresses

    @property
    def equip_with_subtotals(self):
        """Gets the equip_with_subtotals of this QueryBucketedCashFlowsRequest.  # noqa: E501

        Flag directing the Valuation call to populate the results with subtotals of aggregates.  # noqa: E501

        :return: The equip_with_subtotals of this QueryBucketedCashFlowsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._equip_with_subtotals

    @equip_with_subtotals.setter
    def equip_with_subtotals(self, equip_with_subtotals):
        """Sets the equip_with_subtotals of this QueryBucketedCashFlowsRequest.

        Flag directing the Valuation call to populate the results with subtotals of aggregates.  # noqa: E501

        :param equip_with_subtotals: The equip_with_subtotals of this QueryBucketedCashFlowsRequest.  # noqa: E501
        :type equip_with_subtotals: bool
        """

        self._equip_with_subtotals = equip_with_subtotals

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
        if not isinstance(other, QueryBucketedCashFlowsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QueryBucketedCashFlowsRequest):
            return True

        return self.to_dict() != other.to_dict()
