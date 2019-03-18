# coding: utf-8

"""
    Trend Micro Deep Security API

    Get protected, stay secured, and keep informed with Trend Micro Deep Security's new RESTful API. Access system data and manage security configurations to automate your security workflows and integrate Deep Security into your CI/CD pipeline.  # noqa: E501

    OpenAPI spec version: 11.3.184
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UpdateRights(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'can_import_software': 'bool',
        'can_delete_software': 'bool',
        'can_edit_software_properties': 'bool',
        'can_import_rule_updates': 'bool',
        'can_delete_rule_updates': 'bool',
        'can_view_rule_updates': 'bool'
    }

    attribute_map = {
        'can_import_software': 'canImportSoftware',
        'can_delete_software': 'canDeleteSoftware',
        'can_edit_software_properties': 'canEditSoftwareProperties',
        'can_import_rule_updates': 'canImportRuleUpdates',
        'can_delete_rule_updates': 'canDeleteRuleUpdates',
        'can_view_rule_updates': 'canViewRuleUpdates'
    }

    def __init__(self, can_import_software=None, can_delete_software=None, can_edit_software_properties=None, can_import_rule_updates=None, can_delete_rule_updates=None, can_view_rule_updates=None):  # noqa: E501
        """UpdateRights - a model defined in Swagger"""  # noqa: E501

        self._can_import_software = None
        self._can_delete_software = None
        self._can_edit_software_properties = None
        self._can_import_rule_updates = None
        self._can_delete_rule_updates = None
        self._can_view_rule_updates = None
        self.discriminator = None

        if can_import_software is not None:
            self.can_import_software = can_import_software
        if can_delete_software is not None:
            self.can_delete_software = can_delete_software
        if can_edit_software_properties is not None:
            self.can_edit_software_properties = can_edit_software_properties
        if can_import_rule_updates is not None:
            self.can_import_rule_updates = can_import_rule_updates
        if can_delete_rule_updates is not None:
            self.can_delete_rule_updates = can_delete_rule_updates
        if can_view_rule_updates is not None:
            self.can_view_rule_updates = can_view_rule_updates

    @property
    def can_import_software(self):
        """Gets the can_import_software of this UpdateRights.  # noqa: E501

        Right to import software.  # noqa: E501

        :return: The can_import_software of this UpdateRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_import_software

    @can_import_software.setter
    def can_import_software(self, can_import_software):
        """Sets the can_import_software of this UpdateRights.

        Right to import software.  # noqa: E501

        :param can_import_software: The can_import_software of this UpdateRights.  # noqa: E501
        :type: bool
        """

        self._can_import_software = can_import_software

    @property
    def can_delete_software(self):
        """Gets the can_delete_software of this UpdateRights.  # noqa: E501

        Right to delete software.  # noqa: E501

        :return: The can_delete_software of this UpdateRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_delete_software

    @can_delete_software.setter
    def can_delete_software(self, can_delete_software):
        """Sets the can_delete_software of this UpdateRights.

        Right to delete software.  # noqa: E501

        :param can_delete_software: The can_delete_software of this UpdateRights.  # noqa: E501
        :type: bool
        """

        self._can_delete_software = can_delete_software

    @property
    def can_edit_software_properties(self):
        """Gets the can_edit_software_properties of this UpdateRights.  # noqa: E501

        Right to edit software properties.  # noqa: E501

        :return: The can_edit_software_properties of this UpdateRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_edit_software_properties

    @can_edit_software_properties.setter
    def can_edit_software_properties(self, can_edit_software_properties):
        """Sets the can_edit_software_properties of this UpdateRights.

        Right to edit software properties.  # noqa: E501

        :param can_edit_software_properties: The can_edit_software_properties of this UpdateRights.  # noqa: E501
        :type: bool
        """

        self._can_edit_software_properties = can_edit_software_properties

    @property
    def can_import_rule_updates(self):
        """Gets the can_import_rule_updates of this UpdateRights.  # noqa: E501

        Right to import and apply rule updates.  # noqa: E501

        :return: The can_import_rule_updates of this UpdateRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_import_rule_updates

    @can_import_rule_updates.setter
    def can_import_rule_updates(self, can_import_rule_updates):
        """Sets the can_import_rule_updates of this UpdateRights.

        Right to import and apply rule updates.  # noqa: E501

        :param can_import_rule_updates: The can_import_rule_updates of this UpdateRights.  # noqa: E501
        :type: bool
        """

        self._can_import_rule_updates = can_import_rule_updates

    @property
    def can_delete_rule_updates(self):
        """Gets the can_delete_rule_updates of this UpdateRights.  # noqa: E501

        Right to delete rule updates.  # noqa: E501

        :return: The can_delete_rule_updates of this UpdateRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_delete_rule_updates

    @can_delete_rule_updates.setter
    def can_delete_rule_updates(self, can_delete_rule_updates):
        """Sets the can_delete_rule_updates of this UpdateRights.

        Right to delete rule updates.  # noqa: E501

        :param can_delete_rule_updates: The can_delete_rule_updates of this UpdateRights.  # noqa: E501
        :type: bool
        """

        self._can_delete_rule_updates = can_delete_rule_updates

    @property
    def can_view_rule_updates(self):
        """Gets the can_view_rule_updates of this UpdateRights.  # noqa: E501

        Right to view rule updates.  # noqa: E501

        :return: The can_view_rule_updates of this UpdateRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_view_rule_updates

    @can_view_rule_updates.setter
    def can_view_rule_updates(self, can_view_rule_updates):
        """Sets the can_view_rule_updates of this UpdateRights.

        Right to view rule updates.  # noqa: E501

        :param can_view_rule_updates: The can_view_rule_updates of this UpdateRights.  # noqa: E501
        :type: bool
        """

        self._can_view_rule_updates = can_view_rule_updates

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(UpdateRights, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateRights):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
