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

class ProfileManifest(object):
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
        'editable': 'bool',
        'data': 'str',
        'edit': 'list[ProfileEdit]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'editable': 'editable',
        'data': 'data',
        'edit': 'edit'
    }

    def __init__(self, name=None, description=None, editable=None, data=None, edit=None):  # noqa: E501
        """ProfileManifest - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._editable = None
        self._data = None
        self._edit = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if editable is not None:
            self.editable = editable
        if data is not None:
            self.data = data
        if edit is not None:
            self.edit = edit

    @property
    def name(self):
        """Gets the name of this ProfileManifest.  # noqa: E501

        The profile name.  # noqa: E501

        :return: The name of this ProfileManifest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProfileManifest.

        The profile name.  # noqa: E501

        :param name: The name of this ProfileManifest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ProfileManifest.  # noqa: E501

        The profile description.  # noqa: E501

        :return: The description of this ProfileManifest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProfileManifest.

        The profile description.  # noqa: E501

        :param description: The description of this ProfileManifest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def editable(self):
        """Gets the editable of this ProfileManifest.  # noqa: E501

        Whether the profile is editable by licensed users.  # noqa: E501

        :return: The editable of this ProfileManifest.  # noqa: E501
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """Sets the editable of this ProfileManifest.

        Whether the profile is editable by licensed users.  # noqa: E501

        :param editable: The editable of this ProfileManifest.  # noqa: E501
        :type: bool
        """

        self._editable = editable

    @property
    def data(self):
        """Gets the data of this ProfileManifest.  # noqa: E501

        Profile JSON in string format.  # noqa: E501

        :return: The data of this ProfileManifest.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ProfileManifest.

        Profile JSON in string format.  # noqa: E501

        :param data: The data of this ProfileManifest.  # noqa: E501
        :type: str
        """

        self._data = data

    @property
    def edit(self):
        """Gets the edit of this ProfileManifest.  # noqa: E501

        The profile's editable field configuration.  # noqa: E501

        :return: The edit of this ProfileManifest.  # noqa: E501
        :rtype: list[ProfileEdit]
        """
        return self._edit

    @edit.setter
    def edit(self, edit):
        """Sets the edit of this ProfileManifest.

        The profile's editable field configuration.  # noqa: E501

        :param edit: The edit of this ProfileManifest.  # noqa: E501
        :type: list[ProfileEdit]
        """

        self._edit = edit

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
        if issubclass(ProfileManifest, dict):
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
        if not isinstance(other, ProfileManifest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
