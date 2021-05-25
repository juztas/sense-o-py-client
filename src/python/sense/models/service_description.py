# coding: utf-8

"""
    SENSE-O Northbound Intent API

    StackV SENSE-O Northbound REST API Documentation  # noqa: E501

    OpenAPI spec version: 2.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ServiceDescription(object):
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
        'uuid': 'str',
        'bandwidth': 'Bandwidth',
        'terminals': 'list[Terminal]',
        'status': 'str'
    }

    attribute_map = {
        'name': 'name',
        'uuid': 'uuid',
        'bandwidth': 'bandwidth',
        'terminals': 'terminals',
        'status': 'status'
    }

    def __init__(self, name=None, uuid=None, bandwidth=None, terminals=None, status=None):  # noqa: E501
        """ServiceDescription - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._uuid = None
        self._bandwidth = None
        self._terminals = None
        self._status = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if uuid is not None:
            self.uuid = uuid
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if terminals is not None:
            self.terminals = terminals
        if status is not None:
            self.status = status

    @property
    def name(self):
        """Gets the name of this ServiceDescription.  # noqa: E501


        :return: The name of this ServiceDescription.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ServiceDescription.


        :param name: The name of this ServiceDescription.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def uuid(self):
        """Gets the uuid of this ServiceDescription.  # noqa: E501


        :return: The uuid of this ServiceDescription.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this ServiceDescription.


        :param uuid: The uuid of this ServiceDescription.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def bandwidth(self):
        """Gets the bandwidth of this ServiceDescription.  # noqa: E501


        :return: The bandwidth of this ServiceDescription.  # noqa: E501
        :rtype: Bandwidth
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this ServiceDescription.


        :param bandwidth: The bandwidth of this ServiceDescription.  # noqa: E501
        :type: Bandwidth
        """

        self._bandwidth = bandwidth

    @property
    def terminals(self):
        """Gets the terminals of this ServiceDescription.  # noqa: E501


        :return: The terminals of this ServiceDescription.  # noqa: E501
        :rtype: list[Terminal]
        """
        return self._terminals

    @terminals.setter
    def terminals(self, terminals):
        """Sets the terminals of this ServiceDescription.


        :param terminals: The terminals of this ServiceDescription.  # noqa: E501
        :type: list[Terminal]
        """

        self._terminals = terminals

    @property
    def status(self):
        """Gets the status of this ServiceDescription.  # noqa: E501


        :return: The status of this ServiceDescription.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ServiceDescription.


        :param status: The status of this ServiceDescription.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(ServiceDescription, dict):
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
        if not isinstance(other, ServiceDescription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
