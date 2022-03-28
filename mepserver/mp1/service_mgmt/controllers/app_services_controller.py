import sys

import cherrypy

sys.path.append("../../")
from mp1.models import *


class ApplicationServicesController:
    @json_out(cls=NestedEncoder)
    def applications_services_get(self, appInstanceId: str, **kwargs):
        """
        This method retrieves information about a list of mecService resources. This method is typically used in "service availability query" procedure

        Required params
        :param appInstanceId: Represents a MEC application instance. Note that the appInstanceId is allocated by the MEC platform manager.
        :type appInstanceId: String

        Query Params - kwargs
        :param ser_instance_id: A MEC application instance may use multiple ser_instance_ids as an input parameter to query the availability of a list of MEC service instances. Either "ser_instance_id" or "ser_name" or "ser_category_id" or none of them shall be present.
        :type ser_instance_id: List[String]
        :param ser_name: A MEC application instance may use multiple ser_names as an input parameter to query the availability of a list of MEC service instances. Either "ser_instance_id" or "ser_name" or "ser_category_id" or none of them shall be present.
        :type ser_name: List[String]
        :param ser_category_id: A MEC application instance may use ser_category_id as an input parameter to query the availability of a list of MEC service instances in a serCategory. Either "ser_instance_id" or "ser_name" or "ser_category_id" or none of them shall be present.
        :type ser_category_id: String
        :param consumed_local_only: Indicate whether the service can only be consumed by the MEC applications located in the same locality (as defined by scopeOfLocality) as this service instance.
        :type consumed_local_only: boolean
        :param is_local: Indicate whether the service is located in the same locality (as defined by scopeOfLocality) as the consuming MEC application.
        :type is_local: boolean
        :param scope_of_locality: A MEC application instance may use scope_of_locality as an input parameter to query the availability of a list of MEC service instances with a certain scope of locality.
        :type scope_of_locality: String

        :note: ser_name, ser_category_id, ser_instance_id are mutually-exclusive only one should be used


        :return: ProblemDetails or ServiceInfo
        HTTP STATUS CODE: 200, 400, 403, 404, 414
        """

        # TODO VALIDATE PARAMETERS (i.e mutually exclusive) AND CREATE QUERY
        data = json.loads(
            '{"livenessInterval":5,"_links":{"self":{"href":"http://www.google.com"},"liveness":{"href":"http://www.google.com"}},"serCategory":{"href":"http://www.google.com","id":"string","name":"string","version":"string"},"version":"string","state":"ACTIVE","transportInfo":{"id":"string","endpoint":{"uris":["http://www.google.com"]},"name":"string","description":"string","type":"REST_HTTP","protocol":"string","version":"string","security":{"oAuth2Info":{"grantTypes":["OAUTH2_AUTHORIZATION_CODE","OAUTH2_RESOURCE_OWNER"],"tokenEndpoint":"string"}},"implSpecificInfo":{}},"serializer":"JSON","scopeOfLocality":"MEC_SYSTEM","consumedLocalOnly":true,"isLocal":true}'
        )
        serviceInfo = ServiceInfo.from_json(data)
        return serviceInfo

    @cherrypy.tools.json_in()
    @json_out(cls=NestedEncoder)
    def applications_services_post(self, appInstanceId: str):
        """
        This method is used to create a mecService resource. This method is typically used in "service availability update and new service registration" procedure

        :param appInstanceId: Represents a MEC application instance. Note that the appInstanceId is allocated by the MEC platform manager.
        :type appInstanceId: String

        :return: ServiceInfo or ProblemDetails
        HTTP STATUS CODE: 201, 400, 403, 404
        """
        data = cherrypy.request.json
        serviceInfo = ServiceInfo.from_json(data)
        return serviceInfo

    @json_out(cls=NestedEncoder)
    def applicaton_services_get_with_service_id(
        self, appInstanceId: str, serviceId: str
    ):
        """
        This method retrieves information about a mecService resource. This method is typically used in "service availability query" procedure

        :param appInstanceId: Represents a MEC application instance. Note that the appInstanceId is allocated by the MEC platform manager.
        :type appInstanceId: String
        :param serviceId: Represents a MEC service instance.
        :type serviceId: String

        :return: ServiceInfo or ProblemDetails
        HTTP STATUS CODE: 200, 400, 403, 404
        """
        # TODO VALIDATE PARAMETERS (i.e mutually exclusive) AND CREATE QUERY
        data = json.loads(
            '{"serInstanceId":"string","livenessInterval":5,"_links":{"self":{"href":"http://www.google.com"},"liveness":{"href":"http://www.google.com"}},"version":"string","state":"ACTIVE","transportInfo":{"id":"string","endpoint":{"uris":["http://www.google.com"]},"name":"string","description":"string","type":"REST_HTTP","protocol":"string","version":"string","security":{"oAuth2Info":{"grantTypes":["OAUTH2_AUTHORIZATION_CODE","OAUTH2_RESOURCE_OWNER"],"tokenEndpoint":"string"}},"implSpecificInfo":{}},"serializer":"JSON","scopeOfLocality":"MEC_SYSTEM","consumedLocalOnly":true,"isLocal":true}'
        )
        serviceInfo = ServiceInfo.from_json(data)
        return serviceInfo

    @cherrypy.tools.json_in()
    @json_out(cls=NestedEncoder)
    def application_services_put(self, appInstanceId: str, serviceId: str):
        """
                This method updates the information about a mecService resource

                :param appInstanceId: Represents a MEC application instance. Note that the appInstanceId is allocated by the MEC platform manager.
                :type appInstanceId: String
                :param serviceId: Represents a MEC service instance.
                :type serviceId: String
        2
                :request body: New ServiceInfo with updated "state" is included as entity body of the request


                :return: ServiceInfo or ProblemDetails
                HTTP STATUS CODE: 200, 400, 403, 404, 412
        """
        # TODO PUT ONLY NEEDS TO RECEIVE ONE UPDATABLE CRITERIA
        data = cherrypy.request.json
        serviceInfo = ServiceInfo.from_json(data)
        return serviceInfo

    @json_out(cls=NestedEncoder)
    def application_services_delete(self, appInstanceId: str, serviceId: str):
        """
        This method deletes a mecService resource. This method is typically used in the service deregistration procedure.

        :param appInstanceId: Represents a MEC application instance. Note that the appInstanceId is allocated by the MEC platform manager.
        :type appInstanceId: String
        :param serviceId: Represents a MEC service instance.
        :type serviceId: String


        :return: No Content or ProblemDetails
        HTTP STATUS CODE: 204, 403, 404,
        """
        cherrypy.response.status = 204
        return
