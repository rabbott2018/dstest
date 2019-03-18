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


class ApplicationType(object):
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
        'name': 'str',
        'description': 'str',
        'minimum_agent_version': 'str',
        'direction': 'str',
        'protocol': 'str',
        'port_type': 'str',
        'port_multiple': 'list[str]',
        'port_list_id': 'int',
        'recommendations_mode': 'str',
        'id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'minimum_agent_version': 'minimumAgentVersion',
        'direction': 'direction',
        'protocol': 'protocol',
        'port_type': 'portType',
        'port_multiple': 'portMultiple',
        'port_list_id': 'portListID',
        'recommendations_mode': 'recommendationsMode',
        'id': 'ID'
    }

    def __init__(self, name=None, description=None, minimum_agent_version=None, direction=None, protocol=None, port_type=None, port_multiple=None, port_list_id=None, recommendations_mode=None, id=None):  # noqa: E501
        """ApplicationType - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._description = None
        self._minimum_agent_version = None
        self._direction = None
        self._protocol = None
        self._port_type = None
        self._port_multiple = None
        self._port_list_id = None
        self._recommendations_mode = None
        self._id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if minimum_agent_version is not None:
            self.minimum_agent_version = minimum_agent_version
        if direction is not None:
            self.direction = direction
        if protocol is not None:
            self.protocol = protocol
        if port_type is not None:
            self.port_type = port_type
        if port_multiple is not None:
            self.port_multiple = port_multiple
        if port_list_id is not None:
            self.port_list_id = port_list_id
        if recommendations_mode is not None:
            self.recommendations_mode = recommendations_mode
        if id is not None:
            self.id = id

    @property
    def name(self):
        """Gets the name of this ApplicationType.  # noqa: E501

        Display name of the ApplicationType. Searchable as String.  # noqa: E501

        :return: The name of this ApplicationType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApplicationType.

        Display name of the ApplicationType. Searchable as String.  # noqa: E501

        :param name: The name of this ApplicationType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ApplicationType.  # noqa: E501

        Description of the ApplicationType. Searchable as String.  # noqa: E501

        :return: The description of this ApplicationType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApplicationType.

        Description of the ApplicationType. Searchable as String.  # noqa: E501

        :param description: The description of this ApplicationType.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def minimum_agent_version(self):
        """Gets the minimum_agent_version of this ApplicationType.  # noqa: E501

        Version of the Deep Security agent or appliance required to support the ApplicationType. Searchable as String.  # noqa: E501

        :return: The minimum_agent_version of this ApplicationType.  # noqa: E501
        :rtype: str
        """
        return self._minimum_agent_version

    @minimum_agent_version.setter
    def minimum_agent_version(self, minimum_agent_version):
        """Sets the minimum_agent_version of this ApplicationType.

        Version of the Deep Security agent or appliance required to support the ApplicationType. Searchable as String.  # noqa: E501

        :param minimum_agent_version: The minimum_agent_version of this ApplicationType.  # noqa: E501
        :type: str
        """

        self._minimum_agent_version = minimum_agent_version

    @property
    def direction(self):
        """Gets the direction of this ApplicationType.  # noqa: E501

        Direction of the initial communication for the ApplicationType (e.g. 'outgoing' for web browsers). Searchable as Choice.  # noqa: E501

        :return: The direction of this ApplicationType.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this ApplicationType.

        Direction of the initial communication for the ApplicationType (e.g. 'outgoing' for web browsers). Searchable as Choice.  # noqa: E501

        :param direction: The direction of this ApplicationType.  # noqa: E501
        :type: str
        """
        allowed_values = ["incoming", "outgoing"]  # noqa: E501
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def protocol(self):
        """Gets the protocol of this ApplicationType.  # noqa: E501

        Protocol used by the ApplicationType. Searchable as Choice.  # noqa: E501

        :return: The protocol of this ApplicationType.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ApplicationType.

        Protocol used by the ApplicationType. Searchable as Choice.  # noqa: E501

        :param protocol: The protocol of this ApplicationType.  # noqa: E501
        :type: str
        """
        allowed_values = ["icmp", "tcp", "udp", "tcp-udp"]  # noqa: E501
        if protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

    @property
    def port_type(self):
        """Gets the port_type of this ApplicationType.  # noqa: E501

        Port number configuration type. Searchable as Choice.  # noqa: E501

        :return: The port_type of this ApplicationType.  # noqa: E501
        :rtype: str
        """
        return self._port_type

    @port_type.setter
    def port_type(self, port_type):
        """Sets the port_type of this ApplicationType.

        Port number configuration type. Searchable as Choice.  # noqa: E501

        :param port_type: The port_type of this ApplicationType.  # noqa: E501
        :type: str
        """
        allowed_values = ["any", "multiple", "port-list"]  # noqa: E501
        if port_type not in allowed_values:
            raise ValueError(
                "Invalid value for `port_type` ({0}), must be one of {1}"  # noqa: E501
                .format(port_type, allowed_values)
            )

        self._port_type = port_type

    @property
    def port_multiple(self):
        """Gets the port_multiple of this ApplicationType.  # noqa: E501

        If portType is multiple, the list of port numbers the ApplicationType monitors. Searchable as String.  # noqa: E501

        :return: The port_multiple of this ApplicationType.  # noqa: E501
        :rtype: list[str]
        """
        return self._port_multiple

    @port_multiple.setter
    def port_multiple(self, port_multiple):
        """Sets the port_multiple of this ApplicationType.

        If portType is multiple, the list of port numbers the ApplicationType monitors. Searchable as String.  # noqa: E501

        :param port_multiple: The port_multiple of this ApplicationType.  # noqa: E501
        :type: list[str]
        """

        self._port_multiple = port_multiple

    @property
    def port_list_id(self):
        """Gets the port_list_id of this ApplicationType.  # noqa: E501

        If portType is port-list, ID of the PortList containing the port numbers the ApplicationType monitors. Searchable as Numeric.  # noqa: E501

        :return: The port_list_id of this ApplicationType.  # noqa: E501
        :rtype: int
        """
        return self._port_list_id

    @port_list_id.setter
    def port_list_id(self, port_list_id):
        """Sets the port_list_id of this ApplicationType.

        If portType is port-list, ID of the PortList containing the port numbers the ApplicationType monitors. Searchable as Numeric.  # noqa: E501

        :param port_list_id: The port_list_id of this ApplicationType.  # noqa: E501
        :type: int
        """

        self._port_list_id = port_list_id

    @property
    def recommendations_mode(self):
        """Gets the recommendations_mode of this ApplicationType.  # noqa: E501

        Indicates whether recommendation scans consider the ApplicationType. To avoid errors on existing ApplicationTypes, only change the value between enabled (ApplicationType is included in recommendations scan) and ignored (ApplicationType is ignored by recommendations scan). Other values (disabled or ignored) indicate that the ApplicationType is not supported by recommendation scans. Searchable as Choice.  # noqa: E501

        :return: The recommendations_mode of this ApplicationType.  # noqa: E501
        :rtype: str
        """
        return self._recommendations_mode

    @recommendations_mode.setter
    def recommendations_mode(self, recommendations_mode):
        """Sets the recommendations_mode of this ApplicationType.

        Indicates whether recommendation scans consider the ApplicationType. To avoid errors on existing ApplicationTypes, only change the value between enabled (ApplicationType is included in recommendations scan) and ignored (ApplicationType is ignored by recommendations scan). Other values (disabled or ignored) indicate that the ApplicationType is not supported by recommendation scans. Searchable as Choice.  # noqa: E501

        :param recommendations_mode: The recommendations_mode of this ApplicationType.  # noqa: E501
        :type: str
        """
        allowed_values = ["unknown", "enabled", "ignored", "disabled"]  # noqa: E501
        if recommendations_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `recommendations_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(recommendations_mode, allowed_values)
            )

        self._recommendations_mode = recommendations_mode

    @property
    def id(self):
        """Gets the id of this ApplicationType.  # noqa: E501

        ID of the ApplicationType. Searchable as ID.  # noqa: E501

        :return: The id of this ApplicationType.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApplicationType.

        ID of the ApplicationType. Searchable as ID.  # noqa: E501

        :param id: The id of this ApplicationType.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if issubclass(ApplicationType, dict):
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
        if not isinstance(other, ApplicationType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
