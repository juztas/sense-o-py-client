# coding: utf-8
"""
    SENSE-O Northbound Intent API

    StackV SENSE-O Northbound REST API Documentation  # noqa: E501

    OpenAPI spec version: 2.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import
import six
from sense.client.requestwrapper import RequestWrapper


class ProfileApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """
    def __init__(self, req_wrapper=None):
        if req_wrapper is None:
            self.client = RequestWrapper()
        else:
            self.client = req_wrapper
        if 'SI_UUID' in self.client.config:
            self.si_uuid = self.client.config['SI_UUID']
        else:
            self.si_uuid = None

    def profile_list(self, **kwargs):
        """Get skimmed profile data  # noqa: E501

        Retrieves the list of profiles the user is permitted to use without any JSON data.  # noqa: E501
        This method makes a synchronous HTTP request by default.
        :param async_req bool
        :return: list[SlimProfile]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.profile_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.profile_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def profile_get_with_http_info(self, **kwargs):
        """Get skimmed profile data  # noqa: E501

        Retrieves the list of profiles the user is permitted to use without any JSON data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profile_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[SlimProfile]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method profile_get" % key)
            params[key] = val
        del params['kwargs']

        return self.client.request('GET', f'/profile')

    def profile_describe(self, desc, **kwargs):  # noqa: E501
        """Get single profile  # noqa: E501

        Retrieves the specified profile.  # noqa: E501
        This method makes a synchronous HTTP request by default.
        :param async_req bool
        :param str uuid: Profile UUID. (required)
        :return: FullProfile
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.profile_search_get_with_http_info(search,
                                                        **kwargs)  # noqa: E501
        else:
            (data) = self.profile_search_get_with_http_info(
                desc, **kwargs)  # noqa: E501
            return data

    def profile_search_get_with_http_info(self, search, **kwargs):  # noqa: E501
        """Get single profile by name or uuid # noqa: E501

        Retrieves the specified profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profile_search_get_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Profile UUID. (required)
        :return: FullProfile
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search', 'force', 'fetch']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method profile_uuid_get" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('search' not in params or params['search'] is None):
            raise ValueError(
                "Missing the required parameter `uuid` when calling `profile_uuid_get`"
            )  # noqa: E501

        query_params = []
        if 'force' in params:
            query_params.append(('force', params['force']))
        if 'fetch' in params:
            query_params.append(('fetch', params['fetch']))

        return self.client.request('GET', f'/profile/' + search,
                                   query_params=query_params)

    def profile_create(self, body, **kwargs):  # noqa: E501
        """Create a profile  # noqa: E501

        Builds and saves a new profile, using provided starting data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profile_create(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProfileManifest body: Profile creation manifest. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.profile_post_with_http_info(body,
                                                    **kwargs)  # noqa: E501
        else:
            (data) = self.profile_post_with_http_info(body,
                                                      **kwargs)  # noqa: E501
            return data

    def profile_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create a profile  # noqa: E501

        Builds and saves a new profile, using provided starting data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profile_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProfileManifest body: Profile creation manifest. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method profile_post" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or params['body'] is None):
            raise ValueError(
                "Missing the required parameter `body` when calling `profile_post`"
            )  # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.client.request('POST',
                                   f'/profile',
                                   body_params=body_params)

    def profile_delete(self, uuid, **kwargs):  # noqa: E501
        """Delete profile  # noqa: E501

        Deletes the specified profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profile_delete(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Profile UUID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.profile_uuid_delete_with_http_info(
                uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.profile_uuid_delete_with_http_info(
                uuid, **kwargs)  # noqa: E501
            return data

    def profile_uuid_delete_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Delete profile  # noqa: E501

        Deletes the specified profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profile_uuid_delete_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Profile UUID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method profile_uuid_delete" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or params['uuid'] is None):
            raise ValueError(
                "Missing the required parameter `uuid` when calling `profile_uuid_delete`"
            )  # noqa: E501

        return self.client.request('DELETE', f'/profile/{uuid}')

    def profile_add_licenses(self, body, uuid, **kwargs):  # noqa: E501
        """Add new license  # noqa: E501

        Assigns a new license to a user, giving them access to execute the specified profile (and potentially edit as well).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profile_add_licenses(body, uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProfileLicense body: License object. (required)
        :param str uuid: Profile UUID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.profile_uuid_licenses_post_with_http_info(
                body, uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.profile_uuid_licenses_post_with_http_info(
                body, uuid, **kwargs)  # noqa: E501
            return data

    def profile_uuid_licenses_post_with_http_info(self, body, uuid,
                                                  **kwargs):  # noqa: E501
        """Add new license  # noqa: E501

        Assigns a new license to a user, giving them access to execute the specified profile (and potentially edit as well).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profile_uuid_licenses_post_with_http_info(body, uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProfileLicense body: License object. (required)
        :param str uuid: Profile UUID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method profile_uuid_licenses_post" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or params['body'] is None):
            raise ValueError(
                "Missing the required parameter `body` when calling `profile_uuid_licenses_post`"
            )  # noqa: E501
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or params['uuid'] is None):
            raise ValueError(
                "Missing the required parameter `uuid` when calling `profile_uuid_licenses_post`"
            )  # noqa: E501

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']  # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.client.request('POST',
                                   f'/profile/{uuid}/licenses',
                                   body_params=body_params)

    def profile_update_licenses(self, body, uuid, **kwargs):  # noqa: E501
        """Edit existing license  # noqa: E501

        Edits an existing license to a user. Setting the remaining field to 0 will delete the license.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profile_update_licenses(body, uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProfileLicense body: License object. (required)
        :param str uuid: Profile UUID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.profile_uuid_licenses_put_with_http_info(
                body, uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.profile_uuid_licenses_put_with_http_info(
                body, uuid, **kwargs)  # noqa: E501
            return data

    def profile_uuid_licenses_put_with_http_info(self, body, uuid,
                                                 **kwargs):  # noqa: E501
        """Edit existing license  # noqa: E501

        Edits an existing license to a user. Setting the remaining field to 0 will delete the license.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profile_uuid_licenses_put_with_http_info(body, uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProfileLicense body: License object. (required)
        :param str uuid: Profile UUID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method profile_uuid_licenses_put" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or params['body'] is None):
            raise ValueError(
                "Missing the required parameter `body` when calling `profile_uuid_licenses_put`"
            )  # noqa: E501
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or params['uuid'] is None):
            raise ValueError(
                "Missing the required parameter `uuid` when calling `profile_uuid_licenses_put`"
            )  # noqa: E501

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']  # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.client.request('PUT',
                                   f'/profile/{uuid}/licenses',
                                   body_params=body_params)

    def profile_update(self, body, uuid, **kwargs):  # noqa: E501
        """Edit a profile  # noqa: E501

        Submits an updated version of a profile for saving.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profile_uuid_put(body, uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProfileManifest body: Profile creation manifest. (required)
        :param str uuid: Profile UUID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.profile_uuid_put_with_http_info(body, uuid,
                                                        **kwargs)  # noqa: E501
        else:
            (data) = self.profile_uuid_put_with_http_info(
                body, uuid, **kwargs)  # noqa: E501
            return data

    def profile_uuid_put_with_http_info(self, body, uuid,
                                        **kwargs):  # noqa: E501
        """Edit a profile  # noqa: E501

        Submits an updated version of a profile for saving.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profile_uuid_put_with_http_info(body, uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProfileManifest body: Profile creation manifest. (required)
        :param str uuid: Profile UUID. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method profile_uuid_put" % key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or params['body'] is None):
            raise ValueError(
                "Missing the required parameter `body` when calling `profile_uuid_put`"
            )  # noqa: E501
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or params['uuid'] is None):
            raise ValueError(
                "Missing the required parameter `uuid` when calling `profile_uuid_put`"
            )  # noqa: E501

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']  # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']

        return self.client.request('PUT',
                                   f'/profile/{uuid}',
                                   body_params=body_params)

    def profile_get_uses(self, uuid, username, **kwargs):  # noqa: E501
        """Get license usage  # noqa: E501

        Retrieves the remaining number of tickets or slots for allocations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profile_uuid_uses_username_get(uuid, username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Profile UUID. (required)
        :param str username: Username of licensed user. (required)
        :return: float
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.profile_uuid_uses_username_get_with_http_info(
                uuid, username, **kwargs)  # noqa: E501
        else:
            (data) = self.profile_uuid_uses_username_get_with_http_info(
                uuid, username, **kwargs)  # noqa: E501
            return data

    def profile_uuid_uses_username_get_with_http_info(self, uuid, username,
                                                      **kwargs):  # noqa: E501
        """Get license usage  # noqa: E501

        Retrieves the remaining number of tickets or slots for allocations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.profile_uuid_uses_username_get_with_http_info(uuid, username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: Profile UUID. (required)
        :param str username: Username of licensed user. (required)
        :return: float
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'username']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'"
                                " to method profile_uuid_uses_username_get" %
                                key)
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or params['uuid'] is None):
            raise ValueError(
                "Missing the required parameter `uuid` when calling `profile_uuid_uses_username_get`"
            )  # noqa: E501
        # verify the required parameter 'username' is set
        if ('username' not in params or params['username'] is None):
            raise ValueError(
                "Missing the required parameter `username` when calling `profile_uuid_uses_username_get`"
            )  # noqa: E501

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']  # noqa: E501
        if 'username' in params:
            path_params['username'] = params['username']  # noqa: E501

        return self.client.request('GET', f'/profile/{uuid}/uses/{username}')
