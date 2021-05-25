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

class DomainDescription(object):
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
        'uri': 'str',
        'edge_points': 'list[DomainDescriptionEdgePoints]'
    }

    attribute_map = {
        'name': 'name',
        'uri': 'uri',
        'edge_points': 'edge_points'
    }

    def __init__(self, name=None, uri=None, edge_points=None):  # noqa: E501
        """DomainDescription - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._uri = None
        self._edge_points = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if uri is not None:
            self.uri = uri
        if edge_points is not None:
            self.edge_points = edge_points

    @property
    def name(self):
        """Gets the name of this DomainDescription.  # noqa: E501


        :return: The name of this DomainDescription.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DomainDescription.


        :param name: The name of this DomainDescription.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def uri(self):
        """Gets the uri of this DomainDescription.  # noqa: E501


        :return: The uri of this DomainDescription.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this DomainDescription.


        :param uri: The uri of this DomainDescription.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def edge_points(self):
        """Gets the edge_points of this DomainDescription.  # noqa: E501


        :return: The edge_points of this DomainDescription.  # noqa: E501
        :rtype: list[DomainDescriptionEdgePoints]
        """
        return self._edge_points

    @edge_points.setter
    def edge_points(self, edge_points):
        """Sets the edge_points of this DomainDescription.


        :param edge_points: The edge_points of this DomainDescription.  # noqa: E501
        :type: list[DomainDescriptionEdgePoints]
        """

        self._edge_points = edge_points

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
        if issubclass(DomainDescription, dict):
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
        if not isinstance(other, DomainDescription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
