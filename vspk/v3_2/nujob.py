# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUMetadatasFetcher

from bambou import NURESTObject


class NUJob(NURESTObject):
    """ Represents a Job in the VSD

        Notes:
            Represents JOB entity. The job API accepts a command and parameters and executes the job and returns the results. Jobs API are typically used for long running tasks.
    """

    __rest_name__ = "job"
    __resource_name__ = "jobs"

    
    ## Constants
    
    CONST_ASSOC_ENTITY_TYPE_INGRESS_ADV_FWD_ENTRY = "INGRESS_ADV_FWD_ENTRY"
    
    CONST_ASSOC_ENTITY_TYPE_MIRROR_DESTINATION = "MIRROR_DESTINATION"
    
    CONST_ASSOC_ENTITY_TYPE_SERVICE_VRF_SEQUENCENO = "SERVICE_VRF_SEQUENCENO"
    
    CONST_ASSOC_ENTITY_TYPE_EGRESS_QOS_MR = "EGRESS_QOS_MR"
    
    CONST_ASSOC_ENTITY_TYPE_VLAN = "VLAN"
    
    CONST_ASSOC_ENTITY_TYPE_NETWORK_MACRO_GROUP = "NETWORK_MACRO_GROUP"
    
    CONST_ASSOC_ENTITY_TYPE_GROUPKEY_ENCRYPTION_PROFILE = "GROUPKEY_ENCRYPTION_PROFILE"
    
    CONST_COMMAND_RETRIEVE_ACTIVE_NSGS = "RETRIEVE_ACTIVE_NSGS"
    
    CONST_ASSOC_ENTITY_TYPE_GATEWAY_SECURITY_REQUEST = "GATEWAY_SECURITY_REQUEST"
    
    CONST_ASSOC_ENTITY_TYPE_CERTIFICATE = "CERTIFICATE"
    
    CONST_ASSOC_ENTITY_TYPE_ENDPOINT = "ENDPOINT"
    
    CONST_ASSOC_ENTITY_TYPE_NSREDUNDANT_GW_GRP = "NSREDUNDANT_GW_GRP"
    
    CONST_ASSOC_ENTITY_TYPE_ADDRESS_RANGE_STATE = "ADDRESS_RANGE_STATE"
    
    CONST_ASSOC_ENTITY_TYPE_POLICY_GROUP = "POLICY_GROUP"
    
    CONST_ASSOC_ENTITY_TYPE_RATE_LIMITER = "RATE_LIMITER"
    
    CONST_ASSOC_ENTITY_TYPE_GATEWAY_VPORT_CONFIG = "GATEWAY_VPORT_CONFIG"
    
    CONST_ASSOC_ENTITY_TYPE_ZONE = "ZONE"
    
    CONST_ASSOC_ENTITY_TYPE_NSGATEWAY_TEMPLATE = "NSGATEWAY_TEMPLATE"
    
    CONST_ASSOC_ENTITY_TYPE_RD_SEQUENCENO = "RD_SEQUENCENO"
    
    CONST_ASSOC_ENTITY_TYPE_APPD_FLOW_FORWARDING_POLICY = "APPD_FLOW_FORWARDING_POLICY"
    
    CONST_ASSOC_ENTITY_TYPE_PORT_TEMPLATE = "PORT_TEMPLATE"
    
    CONST_ASSOC_ENTITY_TYPE_KEYSERVER_MEMBER = "KEYSERVER_MEMBER"
    
    CONST_ASSOC_ENTITY_TYPE_BOOTSTRAP_ACTIVATION = "BOOTSTRAP_ACTIVATION"
    
    CONST_COMMAND_EXPORT = "EXPORT"
    
    CONST_ASSOC_ENTITY_TYPE_ENTERPRISE_PERMISSION = "ENTERPRISE_PERMISSION"
    
    CONST_ASSOC_ENTITY_TYPE_MONITORING_PORT = "MONITORING_PORT"
    
    CONST_COMMAND_BATCH_GATEWAY_SECURED_DATAS = "BATCH_GATEWAY_SECURED_DATAS"
    
    CONST_ASSOC_ENTITY_TYPE_NSGATEWAY = "NSGATEWAY"
    
    CONST_ASSOC_ENTITY_TYPE_SUBNET_ENTRY = "SUBNET_ENTRY"
    
    CONST_ASSOC_ENTITY_TYPE_PORT_MR = "PORT_MR"
    
    CONST_COMMAND_FORCE_KEYSERVER_VSD_RESYNC = "FORCE_KEYSERVER_VSD_RESYNC"
    
    CONST_ASSOC_ENTITY_TYPE_GEO_VM_REQ = "GEO_VM_REQ"
    
    CONST_ASSOC_ENTITY_TYPE_GEO_VM_RES = "GEO_VM_RES"
    
    CONST_ASSOC_ENTITY_TYPE_GATEWAY_SECURITY_PROFILE_REQUEST = "GATEWAY_SECURITY_PROFILE_REQUEST"
    
    CONST_ASSOC_ENTITY_TYPE_LOCATION = "LOCATION"
    
    CONST_COMMAND_CERTIFICATE_NSG_REVOKE = "CERTIFICATE_NSG_REVOKE"
    
    CONST_ASSOC_ENTITY_TYPE_GATEWAY_SERVICE_CONFIG_RESP = "GATEWAY_SERVICE_CONFIG_RESP"
    
    CONST_ASSOC_ENTITY_TYPE_INGRESS_ACL = "INGRESS_ACL"
    
    CONST_ASSOC_ENTITY_TYPE_INGRESS_EXT_SERVICE = "INGRESS_EXT_SERVICE"
    
    CONST_COMMAND_APPLY_POLICY_CHANGES = "APPLY_POLICY_CHANGES"
    
    CONST_COMMAND_NSG_REGISTRATION_INFO = "NSG_REGISTRATION_INFO"
    
    CONST_ASSOC_ENTITY_TYPE_ENTERPRISE_NETWORK = "ENTERPRISE_NETWORK"
    
    CONST_ASSOC_ENTITY_TYPE_DC_CONFIG = "DC_CONFIG"
    
    CONST_ASSOC_ENTITY_TYPE_NETWORK_ELEMENT = "NETWORK_ELEMENT"
    
    CONST_ASSOC_ENTITY_TYPE_VPORTTAG = "VPORTTAG"
    
    CONST_ASSOC_ENTITY_TYPE_ADDRESS_RANGE = "ADDRESS_RANGE"
    
    CONST_ASSOC_ENTITY_TYPE_ENTERPRISE_PROFILE = "ENTERPRISE_PROFILE"
    
    CONST_ASSOC_ENTITY_TYPE_VMWARE_VCENTER = "VMWARE_VCENTER"
    
    CONST_ASSOC_ENTITY_TYPE_NEXT_HOP_RESP = "NEXT_HOP_RESP"
    
    CONST_ASSOC_ENTITY_TYPE_VIRTUAL_MACHINE_REPORT = "VIRTUAL_MACHINE_REPORT"
    
    CONST_ASSOC_ENTITY_TYPE_INGRESS_ADV_FWD = "INGRESS_ADV_FWD"
    
    CONST_ASSOC_ENTITY_TYPE_SUBNET_MAC_ENTRY = "SUBNET_MAC_ENTRY"
    
    CONST_ASSOC_ENTITY_TYPE_APPD_TIER = "APPD_TIER"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ASSOC_ENTITY_TYPE_INFRASTRUCTURE_PORT_PROFILE = "INFRASTRUCTURE_PORT_PROFILE"
    
    CONST_ASSOC_ENTITY_TYPE_PORT = "PORT"
    
    CONST_ASSOC_ENTITY_TYPE_KEYSERVER_MONITOR_SEED = "KEYSERVER_MONITOR_SEED"
    
    CONST_ASSOC_ENTITY_TYPE_SUBNET_TEMPLATE = "SUBNET_TEMPLATE"
    
    CONST_ASSOC_ENTITY_TYPE_GATEWAY_SECURITY_RESPONSE = "GATEWAY_SECURITY_RESPONSE"
    
    CONST_ASSOC_ENTITY_TYPE_DHCP_ALLOC_MESSAGE = "DHCP_ALLOC_MESSAGE"
    
    CONST_ASSOC_ENTITY_TYPE_EGRESS_ACL_ENTRY = "EGRESS_ACL_ENTRY"
    
    CONST_ASSOC_ENTITY_TYPE_VPORT_TAG_BASE = "VPORT_TAG_BASE"
    
    CONST_ASSOC_ENTITY_TYPE_INGRESS_EXT_SERVICE_ENTRY = "INGRESS_EXT_SERVICE_ENTRY"
    
    CONST_ASSOC_ENTITY_TYPE_SITE_RES = "SITE_RES"
    
    CONST_ASSOC_ENTITY_TYPE_ALARM = "ALARM"
    
    CONST_ASSOC_ENTITY_TYPE_DHCP_OPTION = "DHCP_OPTION"
    
    CONST_ASSOC_ENTITY_TYPE_PATCONFIG_CONFIG_RESP = "PATCONFIG_CONFIG_RESP"
    
    CONST_ASSOC_ENTITY_TYPE_VMWARE_VCENTER_HYPERVISOR = "VMWARE_VCENTER_HYPERVISOR"
    
    CONST_ASSOC_ENTITY_TYPE_VMWARE_VCENTER_CLUSTER = "VMWARE_VCENTER_CLUSTER"
    
    CONST_ASSOC_ENTITY_TYPE_GROUP = "GROUP"
    
    CONST_COMMAND_NOTIFY_NSG_REGISTRATION = "NOTIFY_NSG_REGISTRATION"
    
    CONST_ASSOC_ENTITY_TYPE_INGRESS_EXT_SERVICE_TEMPLATE = "INGRESS_EXT_SERVICE_TEMPLATE"
    
    CONST_ASSOC_ENTITY_TYPE_HOSTINTERFACE = "HOSTINTERFACE"
    
    CONST_COMMAND_NSG_NOTIFICATION_TEST = "NSG_NOTIFICATION_TEST"
    
    CONST_ASSOC_ENTITY_TYPE_APPD_FLOW = "APPD_FLOW"
    
    CONST_ASSOC_ENTITY_TYPE_VPORT_MEDIATION_REQUEST = "VPORT_MEDIATION_REQUEST"
    
    CONST_ASSOC_ENTITY_TYPE_INGRESS_ADV_FWD_TEMPLATE_ENTRY = "INGRESS_ADV_FWD_TEMPLATE_ENTRY"
    
    CONST_COMMAND_FORCE_KEYSERVER_UPDATE = "FORCE_KEYSERVER_UPDATE"
    
    CONST_ASSOC_ENTITY_TYPE_VSP = "VSP"
    
    CONST_ASSOC_ENTITY_TYPE_GATEWAY_CONFIG_RESP = "GATEWAY_CONFIG_RESP"
    
    CONST_ASSOC_ENTITY_TYPE_GATEWAY_SERVICE_CONFIG = "GATEWAY_SERVICE_CONFIG"
    
    CONST_ASSOC_ENTITY_TYPE_STATIC_ROUTE_RESP = "STATIC_ROUTE_RESP"
    
    CONST_ASSOC_ENTITY_TYPE_APPLICATION = "APPLICATION"
    
    CONST_ASSOC_ENTITY_TYPE_VMWARE_VCENTER_EAM_CONFIG = "VMWARE_VCENTER_EAM_CONFIG"
    
    CONST_ASSOC_ENTITY_TYPE_NSG_NOTIFICATION = "NSG_NOTIFICATION"
    
    CONST_ASSOC_ENTITY_TYPE_EXPORTIMPORT = "EXPORTIMPORT"
    
    CONST_ASSOC_ENTITY_TYPE_VSC = "VSC"
    
    CONST_ASSOC_ENTITY_TYPE_UPLINK_RD = "UPLINK_RD"
    
    CONST_ASSOC_ENTITY_TYPE_VSD = "VSD"
    
    CONST_ASSOC_ENTITY_TYPE_BOOTSTRAP = "BOOTSTRAP"
    
    CONST_ASSOC_ENTITY_TYPE_GATEWAY = "GATEWAY"
    
    CONST_ASSOC_ENTITY_TYPE_VMWARE_VCENTER_VRS_CONFIG = "VMWARE_VCENTER_VRS_CONFIG"
    
    CONST_ASSOC_ENTITY_TYPE_VM_INTERFACE = "VM_INTERFACE"
    
    CONST_ASSOC_ENTITY_TYPE_INFRASTRUCTURE_VSC_PROFILE = "INFRASTRUCTURE_VSC_PROFILE"
    
    CONST_ASSOC_ENTITY_TYPE_BACK_HAUL_SERVICE_RESP = "BACK_HAUL_SERVICE_RESP"
    
    CONST_ASSOC_ENTITY_TYPE_LDAP_CONFIG = "LDAP_CONFIG"
    
    CONST_ASSOC_ENTITY_TYPE_VLAN_TEMPLATE = "VLAN_TEMPLATE"
    
    CONST_ASSOC_ENTITY_TYPE_VPORTTAGTEMPLATE = "VPORTTAGTEMPLATE"
    
    CONST_ASSOC_ENTITY_TYPE_ENTERPRISE_SECURITY = "ENTERPRISE_SECURITY"
    
    CONST_ASSOC_ENTITY_TYPE_FLOATINGIP = "FLOATINGIP"
    
    CONST_ASSOC_ENTITY_TYPE_IKEV2_ENCRYPTION_PROFILE = "IKEV2_ENCRYPTION_PROFILE"
    
    CONST_COMMAND_GATEWAY_AUDIT = "GATEWAY_AUDIT"
    
    CONST_COMMAND_NOTIFY_NSG_REGISTRATION_TEST = "NOTIFY_NSG_REGISTRATION_TEST"
    
    CONST_ASSOC_ENTITY_TYPE_DSCP_FORWARDING_CLASS_TABLE = "DSCP_FORWARDING_CLASS_TABLE"
    
    CONST_ASSOC_ENTITY_TYPE_ENTITY_METADATA_BINDING = "ENTITY_METADATA_BINDING"
    
    CONST_ASSOC_ENTITY_TYPE_KEYSERVER_NOTIFICATION = "KEYSERVER_NOTIFICATION"
    
    CONST_ASSOC_ENTITY_TYPE_CUSTOMER_VRF_SEQUENCENO = "CUSTOMER_VRF_SEQUENCENO"
    
    CONST_ASSOC_ENTITY_TYPE_VPORT_MIRROR = "VPORT_MIRROR"
    
    CONST_COMMAND_CLEAR_IPSEC_DATA = "CLEAR_IPSEC_DATA"
    
    CONST_STATUS_FAILED = "FAILED"
    
    CONST_ASSOC_ENTITY_TYPE_HSC = "HSC"
    
    CONST_ASSOC_ENTITY_TYPE_SUBNET = "SUBNET"
    
    CONST_ASSOC_ENTITY_TYPE_DOMAIN_CONFIG = "DOMAIN_CONFIG"
    
    CONST_ASSOC_ENTITY_TYPE_VSG_REDUNDANT_PORT = "VSG_REDUNDANT_PORT"
    
    CONST_ASSOC_ENTITY_TYPE_MULTI_NIC_VPORT = "MULTI_NIC_VPORT"
    
    CONST_COMMAND_KEYSERVER_NOTIFICATION_TEST = "KEYSERVER_NOTIFICATION_TEST"
    
    CONST_ASSOC_ENTITY_TYPE_DOMAIN_TEMPLATE = "DOMAIN_TEMPLATE"
    
    CONST_ASSOC_ENTITY_TYPE_POLICY_GROUP_TEMPLATE = "POLICY_GROUP_TEMPLATE"
    
    CONST_ASSOC_ENTITY_TYPE_INGRESS_ACL_TEMPLATE_ENTRY = "INGRESS_ACL_TEMPLATE_ENTRY"
    
    CONST_ASSOC_ENTITY_TYPE_SITE_REQ = "SITE_REQ"
    
    CONST_ASSOC_ENTITY_TYPE_RESYNC = "RESYNC"
    
    CONST_ASSOC_ENTITY_TYPE_KEYSERVER_MONITOR_SEK = "KEYSERVER_MONITOR_SEK"
    
    CONST_ASSOC_ENTITY_TYPE_VPORT_GATEWAY_RESPONSE = "VPORT_GATEWAY_RESPONSE"
    
    CONST_ASSOC_ENTITY_TYPE_STATISTICS = "STATISTICS"
    
    CONST_ASSOC_ENTITY_TYPE_VSD_COMPONENT = "VSD_COMPONENT"
    
    CONST_STATUS_SUCCESS = "SUCCESS"
    
    CONST_ASSOC_ENTITY_TYPE_NS_REDUNDANT_PORT = "NS_REDUNDANT_PORT"
    
    CONST_ASSOC_ENTITY_TYPE_L2DOMAIN = "L2DOMAIN"
    
    CONST_ASSOC_ENTITY_TYPE_L2DOMAIN_TEMPLATE = "L2DOMAIN_TEMPLATE"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_ASSOC_ENTITY_TYPE_STATS_TCA = "STATS_TCA"
    
    CONST_ASSOC_ENTITY_TYPE_INFRASTRUCTURE_CONFIG = "INFRASTRUCTURE_CONFIG"
    
    CONST_ASSOC_ENTITY_TYPE_EGRESS_QOS_QUEUE_MR = "EGRESS_QOS_QUEUE_MR"
    
    CONST_ASSOC_ENTITY_TYPE_RTRD_ENTITY = "RTRD_ENTITY"
    
    CONST_ASSOC_ENTITY_TYPE_INGRESS_ACL_TEMPLATE = "INGRESS_ACL_TEMPLATE"
    
    CONST_ASSOC_ENTITY_TYPE_APPD_APPLICATION = "APPD_APPLICATION"
    
    CONST_ASSOC_ENTITY_TYPE_VIRTUAL_MACHINE = "VIRTUAL_MACHINE"
    
    CONST_ASSOC_ENTITY_TYPE_DSCP_FORWARDING_CLASS_MAPPING = "DSCP_FORWARDING_CLASS_MAPPING"
    
    CONST_ASSOC_ENTITY_TYPE_STATS_POLICY = "STATS_POLICY"
    
    CONST_ASSOC_ENTITY_TYPE_STATSSERVER = "STATSSERVER"
    
    CONST_ASSOC_ENTITY_TYPE_APPD_EXTERNAL_APP_SERVICE = "APPD_EXTERNAL_APP_SERVICE"
    
    CONST_ASSOC_ENTITY_TYPE_QOS_PRIMITIVE = "QOS_PRIMITIVE"
    
    CONST_ASSOC_ENTITY_TYPE_DOMAIN = "DOMAIN"
    
    CONST_ASSOC_ENTITY_TYPE_RTRD_SEQUENCENO = "RTRD_SEQUENCENO"
    
    CONST_ASSOC_ENTITY_TYPE_IP_BINDING = "IP_BINDING"
    
    CONST_ASSOC_ENTITY_TYPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_ASSOC_ENTITY_TYPE_ENTERPRISE_SECURED_DATA = "ENTERPRISE_SECURED_DATA"
    
    CONST_ASSOC_ENTITY_TYPE_STATS_COLLECTOR = "STATS_COLLECTOR"
    
    CONST_ASSOC_ENTITY_TYPE_MC_CHANNEL_MAP = "MC_CHANNEL_MAP"
    
    CONST_ASSOC_ENTITY_TYPE_VPN_CONNECT = "VPN_CONNECT"
    
    CONST_ASSOC_ENTITY_TYPE_ENTERPRISE_CONFIG_RESP = "ENTERPRISE_CONFIG_RESP"
    
    CONST_ASSOC_ENTITY_TYPE_EVENT_LOG = "EVENT_LOG"
    
    CONST_ASSOC_ENTITY_TYPE_GATEWAY_TEMPLATE = "GATEWAY_TEMPLATE"
    
    CONST_ASSOC_ENTITY_TYPE_WAN_SERVICE = "WAN_SERVICE"
    
    CONST_ASSOC_ENTITY_TYPE_FLOATINGIP_ACL_ENTRY = "FLOATINGIP_ACL_ENTRY"
    
    CONST_ASSOC_ENTITY_TYPE_SYSTEM_CONFIG_RESP = "SYSTEM_CONFIG_RESP"
    
    CONST_COMMAND_VCENTER_RECONNECT = "VCENTER_RECONNECT"
    
    CONST_ASSOC_ENTITY_TYPE_PUBLIC_NETWORK = "PUBLIC_NETWORK"
    
    CONST_ASSOC_ENTITY_TYPE_MC_RANGE = "MC_RANGE"
    
    CONST_ASSOC_ENTITY_TYPE_APPD_SERVICE = "APPD_SERVICE"
    
    CONST_COMMAND_NOTIFY_NSG_REGISTRATION_ACK = "NOTIFY_NSG_REGISTRATION_ACK"
    
    CONST_ASSOC_ENTITY_TYPE_MC_LIST = "MC_LIST"
    
    CONST_ASSOC_ENTITY_TYPE_EGRESS_ACL_TEMPLATE = "EGRESS_ACL_TEMPLATE"
    
    CONST_ASSOC_ENTITY_TYPE_BGPPEER = "BGPPEER"
    
    CONST_ASSOC_ENTITY_TYPE_SHAPING_POLICY = "SHAPING_POLICY"
    
    CONST_ASSOC_ENTITY_TYPE_DISKSTATS = "DISKSTATS"
    
    CONST_ASSOC_ENTITY_TYPE_BRIDGEINTERFACE = "BRIDGEINTERFACE"
    
    CONST_COMMAND_RELOAD_GEO_REDUNDANT_INFO = "RELOAD_GEO_REDUNDANT_INFO"
    
    CONST_ASSOC_ENTITY_TYPE_VRS = "VRS"
    
    CONST_ASSOC_ENTITY_TYPE_NSPORT = "NSPORT"
    
    CONST_ASSOC_ENTITY_TYPE_POLICING_POLICY = "POLICING_POLICY"
    
    CONST_COMMAND_FORCE_KEYSERVER_UPDATE_ACK = "FORCE_KEYSERVER_UPDATE_ACK"
    
    CONST_ASSOC_ENTITY_TYPE_DOMAIN_FLOATING_IP_ACL_TEMPLATE = "DOMAIN_FLOATING_IP_ACL_TEMPLATE"
    
    CONST_ASSOC_ENTITY_TYPE_ESI_SEQUENCENO = "ESI_SEQUENCENO"
    
    CONST_ASSOC_ENTITY_TYPE_APPD_FLOW_SECURITY_POLICY = "APPD_FLOW_SECURITY_POLICY"
    
    CONST_ASSOC_ENTITY_TYPE_VMWARE_VCENTER_VRS_BASE_CONFIG = "VMWARE_VCENTER_VRS_BASE_CONFIG"
    
    CONST_ASSOC_ENTITY_TYPE_VPORT = "VPORT"
    
    CONST_ASSOC_ENTITY_TYPE_GATEWAY_SECURITY = "GATEWAY_SECURITY"
    
    CONST_ASSOC_ENTITY_TYPE_VM_DESCRIPTION = "VM_DESCRIPTION"
    
    CONST_ASSOC_ENTITY_TYPE_USER = "USER"
    
    CONST_ASSOC_ENTITY_TYPE_KEYSERVER_MONITOR = "KEYSERVER_MONITOR"
    
    CONST_ASSOC_ENTITY_TYPE_SHARED_RESOURCE = "SHARED_RESOURCE"
    
    CONST_ASSOC_ENTITY_TYPE_NSGATEWAY_CONFIG = "NSGATEWAY_CONFIG"
    
    CONST_ASSOC_ENTITY_TYPE_DOMAIN_FLOATING_IP_ACL_TEMPLATE_ENTRY = "DOMAIN_FLOATING_IP_ACL_TEMPLATE_ENTRY"
    
    CONST_ASSOC_ENTITY_TYPE_NETWORK_POLICY_GROUP = "NETWORK_POLICY_GROUP"
    
    CONST_ASSOC_ENTITY_TYPE_VNID_SEQUENCENO = "VNID_SEQUENCENO"
    
    CONST_ASSOC_ENTITY_TYPE_GATEWAY_SECURITY_PROFILE_RESPONSE = "GATEWAY_SECURITY_PROFILE_RESPONSE"
    
    CONST_ASSOC_ENTITY_TYPE_EVPN_BGP_COMMUNITY_TAG_SEQ_NO = "EVPN_BGP_COMMUNITY_TAG_SEQ_NO"
    
    CONST_COMMAND_VCENTER_RELOAD = "VCENTER_RELOAD"
    
    CONST_ASSOC_ENTITY_TYPE_IKEV2_GATEWAY = "IKEV2_GATEWAY"
    
    CONST_ASSOC_ENTITY_TYPE_FLOATING_IP_ACL_TEMPLATE = "FLOATING_IP_ACL_TEMPLATE"
    
    CONST_ASSOC_ENTITY_TYPE_UNSUPPORTED = "UNSUPPORTED"
    
    CONST_ASSOC_ENTITY_TYPE_FLOATINGIP_ACL = "FLOATINGIP_ACL"
    
    CONST_ASSOC_ENTITY_TYPE_SERVICES_GATEWAY_RESPONSE = "SERVICES_GATEWAY_RESPONSE"
    
    CONST_ASSOC_ENTITY_TYPE_EVPN_BGP_COMMUNITY_TAG_ENTRY = "EVPN_BGP_COMMUNITY_TAG_ENTRY"
    
    CONST_ASSOC_ENTITY_TYPE_CHILD_ENTITY_POLICY_CHANGE = "CHILD_ENTITY_POLICY_CHANGE"
    
    CONST_ASSOC_ENTITY_TYPE_DOMAIN_CONFIG_RESP = "DOMAIN_CONFIG_RESP"
    
    CONST_ASSOC_ENTITY_TYPE_GATEWAY_SECURED_DATA = "GATEWAY_SECURED_DATA"
    
    CONST_ASSOC_ENTITY_TYPE_POLICY_DECISION = "POLICY_DECISION"
    
    CONST_ASSOC_ENTITY_TYPE_PERMITTED_ACTION = "PERMITTED_ACTION"
    
    CONST_ASSOC_ENTITY_TYPE_SITE = "SITE"
    
    CONST_COMMAND_BEGIN_POLICY_CHANGES = "BEGIN_POLICY_CHANGES"
    
    CONST_ASSOC_ENTITY_TYPE_LICENSE = "LICENSE"
    
    CONST_ASSOC_ENTITY_TYPE_PERMISSION = "PERMISSION"
    
    CONST_ASSOC_ENTITY_TYPE_NATMAPENTRY = "NATMAPENTRY"
    
    CONST_ASSOC_ENTITY_TYPE_EXTERNAL_SERVICE = "EXTERNAL_SERVICE"
    
    CONST_ASSOC_ENTITY_TYPE_METADATA = "METADATA"
    
    CONST_ASSOC_ENTITY_TYPE_REDUNDANT_GW_GRP = "REDUNDANT_GW_GRP"
    
    CONST_ASSOC_ENTITY_TYPE_AUTO_DISC_GATEWAY = "AUTO_DISC_GATEWAY"
    
    CONST_ASSOC_ENTITY_TYPE_INFRASTRUCTURE_GATEWAY_PROFILE = "INFRASTRUCTURE_GATEWAY_PROFILE"
    
    CONST_ASSOC_ENTITY_TYPE_VPRN_LABEL_SEQUENCENO = "VPRN_LABEL_SEQUENCENO"
    
    CONST_COMMAND_RELOAD_NSG_CONFIG = "RELOAD_NSG_CONFIG"
    
    CONST_ASSOC_ENTITY_TYPE_STATIC_ROUTE = "STATIC_ROUTE"
    
    CONST_ASSOC_ENTITY_TYPE_METADATA_TAG = "METADATA_TAG"
    
    CONST_ASSOC_ENTITY_TYPE_EGRESS_QOS_PRIMITIVE = "EGRESS_QOS_PRIMITIVE"
    
    CONST_ASSOC_ENTITY_TYPE_CLOUD_MGMT_SYSTEM = "CLOUD_MGMT_SYSTEM"
    
    CONST_ASSOC_ENTITY_TYPE_EGRESS_ACL = "EGRESS_ACL"
    
    CONST_ASSOC_ENTITY_TYPE_INGRESS_EXT_SERVICE_TEMPLATE_ENTRY = "INGRESS_EXT_SERVICE_TEMPLATE_ENTRY"
    
    CONST_COMMAND_BATCH_CRUD_REQUEST = "BATCH_CRUD_REQUEST"
    
    CONST_ASSOC_ENTITY_TYPE_SYSTEM_CONFIG_REQ = "SYSTEM_CONFIG_REQ"
    
    CONST_ASSOC_ENTITY_TYPE_ACLENTRY_LOCATION = "ACLENTRY_LOCATION"
    
    CONST_ASSOC_ENTITY_TYPE_VMWARE_VCENTER_DATACENTER = "VMWARE_VCENTER_DATACENTER"
    
    CONST_ASSOC_ENTITY_TYPE_NSPORT_STATIC_CONFIG = "NSPORT_STATIC_CONFIG"
    
    CONST_ASSOC_ENTITY_TYPE_FLOATING_IP_ACL_TEMPLATE_ENTRY = "FLOATING_IP_ACL_TEMPLATE_ENTRY"
    
    CONST_ASSOC_ENTITY_TYPE_NETWORK_LAYOUT = "NETWORK_LAYOUT"
    
    CONST_ASSOC_ENTITY_TYPE_PATNATPOOL = "PATNATPOOL"
    
    CONST_ASSOC_ENTITY_TYPE_SUBNET_POOL_ENTRY = "SUBNET_POOL_ENTRY"
    
    CONST_ASSOC_ENTITY_TYPE_NODE_EXECUTION_ERROR = "NODE_EXECUTION_ERROR"
    
    CONST_ASSOC_ENTITY_TYPE_ZONE_TEMPLATE = "ZONE_TEMPLATE"
    
    CONST_ASSOC_ENTITY_TYPE_JOB = "JOB"
    
    CONST_ASSOC_ENTITY_TYPE_VMWARE_RELOAD_CONFIG = "VMWARE_RELOAD_CONFIG"
    
    CONST_ASSOC_ENTITY_TYPE_HEALTH_REQ = "HEALTH_REQ"
    
    CONST_STATUS_RUNNING = "RUNNING"
    
    CONST_ASSOC_ENTITY_TYPE_SYSTEM_MONITORING = "SYSTEM_MONITORING"
    
    CONST_ASSOC_ENTITY_TYPE_NSPORT_TEMPLATE = "NSPORT_TEMPLATE"
    
    CONST_COMMAND_IMPORT = "IMPORT"
    
    CONST_ASSOC_ENTITY_TYPE_GATEWAY_CONFIG = "GATEWAY_CONFIG"
    
    CONST_ASSOC_ENTITY_TYPE_LIBVIRT_INTERFACE = "LIBVIRT_INTERFACE"
    
    CONST_ASSOC_ENTITY_TYPE_DHCP_CONFIG_RESP = "DHCP_CONFIG_RESP"
    
    CONST_ASSOC_ENTITY_TYPE_GATEWAY_VPORT_CONFIG_RESP = "GATEWAY_VPORT_CONFIG_RESP"
    
    CONST_ASSOC_ENTITY_TYPE_VIRTUAL_IP = "VIRTUAL_IP"
    
    CONST_COMMAND_CERTIFICATE_NSG_RENEW = "CERTIFICATE_NSG_RENEW"
    
    CONST_COMMAND_DISCARD_POLICY_CHANGES = "DISCARD_POLICY_CHANGES"
    
    CONST_ASSOC_ENTITY_TYPE_INGRESS_ACL_ENTRY = "INGRESS_ACL_ENTRY"
    
    CONST_COMMAND_RELOAD = "RELOAD"
    
    CONST_ASSOC_ENTITY_TYPE_SYSTEM_CONFIG = "SYSTEM_CONFIG"
    
    CONST_ASSOC_ENTITY_TYPE_ENTERPRISE_CONFIG = "ENTERPRISE_CONFIG"
    
    CONST_ASSOC_ENTITY_TYPE_L2DOMAIN_SHARED = "L2DOMAIN_SHARED"
    
    CONST_ASSOC_ENTITY_TYPE_INGRESS_ADV_FWD_TEMPLATE = "INGRESS_ADV_FWD_TEMPLATE"
    
    CONST_ASSOC_ENTITY_TYPE_SERVICE_GATEWAY_RESPONSE = "SERVICE_GATEWAY_RESPONSE"
    
    CONST_ASSOC_ENTITY_TYPE_EGRESS_ACL_TEMPLATE_ENTRY = "EGRESS_ACL_TEMPLATE_ENTRY"
    
    CONST_ASSOC_ENTITY_TYPE_KEYSERVER_MONITOR_ENCRYPTED_SEED = "KEYSERVER_MONITOR_ENCRYPTED_SEED"
    
    CONST_ASSOC_ENTITY_TYPE_VMWARE_VRS_ADDRESS_RANGE = "VMWARE_VRS_ADDRESS_RANGE"
    
    CONST_ASSOC_ENTITY_TYPE_GEO_VM_EVENT = "GEO_VM_EVENT"
    
    

    def __init__(self, **kwargs):
        """ Initializes a Job instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> job = NUJob(id=u'xxxx-xxx-xxx-xxx', name=u'Job')
                >>> job = NUJob(data=my_dict)
        """

        super(NUJob, self).__init__()

        # Read/Write Attributes
        
        self._assoc_entity_type = None
        self._command = None
        self._entity_scope = None
        self._external_id = None
        self._last_updated_by = None
        self._parameters = None
        self._progress = None
        self._result = None
        self._status = None
        
        self.expose_attribute(local_name="assoc_entity_type", remote_name="assocEntityType", attribute_type=str, is_required=False, is_unique=False, choices=[u'ACLENTRY_LOCATION', u'ADDRESS_RANGE', u'ADDRESS_RANGE_STATE', u'ALARM', u'APPD_APPLICATION', u'APPD_EXTERNAL_APP_SERVICE', u'APPD_FLOW', u'APPD_FLOW_FORWARDING_POLICY', u'APPD_FLOW_SECURITY_POLICY', u'APPD_SERVICE', u'APPD_TIER', u'APPLICATION', u'AUTO_DISC_GATEWAY', u'BACK_HAUL_SERVICE_RESP', u'BGPPEER', u'BOOTSTRAP', u'BOOTSTRAP_ACTIVATION', u'BRIDGEINTERFACE', u'CERTIFICATE', u'CHILD_ENTITY_POLICY_CHANGE', u'CLOUD_MGMT_SYSTEM', u'CUSTOMER_VRF_SEQUENCENO', u'DC_CONFIG', u'DHCP_ALLOC_MESSAGE', u'DHCP_CONFIG_RESP', u'DHCP_OPTION', u'DISKSTATS', u'DOMAIN', u'DOMAIN_CONFIG', u'DOMAIN_CONFIG_RESP', u'DOMAIN_FLOATING_IP_ACL_TEMPLATE', u'DOMAIN_FLOATING_IP_ACL_TEMPLATE_ENTRY', u'DOMAIN_TEMPLATE', u'DSCP_FORWARDING_CLASS_MAPPING', u'DSCP_FORWARDING_CLASS_TABLE', u'EGRESS_ACL', u'EGRESS_ACL_ENTRY', u'EGRESS_ACL_TEMPLATE', u'EGRESS_ACL_TEMPLATE_ENTRY', u'EGRESS_QOS_MR', u'EGRESS_QOS_PRIMITIVE', u'EGRESS_QOS_QUEUE_MR', u'ENDPOINT', u'ENTERPRISE', u'ENTERPRISE_CONFIG', u'ENTERPRISE_CONFIG_RESP', u'ENTERPRISE_NETWORK', u'ENTERPRISE_PERMISSION', u'ENTERPRISE_PROFILE', u'ENTERPRISE_SECURED_DATA', u'ENTERPRISE_SECURITY', u'ENTITY_METADATA_BINDING', u'ESI_SEQUENCENO', u'EVENT_LOG', u'EVPN_BGP_COMMUNITY_TAG_ENTRY', u'EVPN_BGP_COMMUNITY_TAG_SEQ_NO', u'EXPORTIMPORT', u'EXTERNAL_SERVICE', u'FLOATING_IP_ACL_TEMPLATE', u'FLOATING_IP_ACL_TEMPLATE_ENTRY', u'FLOATINGIP', u'FLOATINGIP_ACL', u'FLOATINGIP_ACL_ENTRY', u'GATEWAY', u'GATEWAY_CONFIG', u'GATEWAY_CONFIG_RESP', u'GATEWAY_SECURED_DATA', u'GATEWAY_SECURITY', u'GATEWAY_SECURITY_PROFILE_REQUEST', u'GATEWAY_SECURITY_PROFILE_RESPONSE', u'GATEWAY_SECURITY_REQUEST', u'GATEWAY_SECURITY_RESPONSE', u'GATEWAY_SERVICE_CONFIG', u'GATEWAY_SERVICE_CONFIG_RESP', u'GATEWAY_TEMPLATE', u'GATEWAY_VPORT_CONFIG', u'GATEWAY_VPORT_CONFIG_RESP', u'GEO_VM_EVENT', u'GEO_VM_REQ', u'GEO_VM_RES', u'GROUP', u'GROUPKEY_ENCRYPTION_PROFILE', u'HEALTH_REQ', u'HOSTINTERFACE', u'HSC', u'IKEV2_ENCRYPTION_PROFILE', u'IKEV2_GATEWAY', u'INFRASTRUCTURE_CONFIG', u'INFRASTRUCTURE_GATEWAY_PROFILE', u'INFRASTRUCTURE_PORT_PROFILE', u'INFRASTRUCTURE_VSC_PROFILE', u'INGRESS_ACL', u'INGRESS_ACL_ENTRY', u'INGRESS_ACL_TEMPLATE', u'INGRESS_ACL_TEMPLATE_ENTRY', u'INGRESS_ADV_FWD', u'INGRESS_ADV_FWD_ENTRY', u'INGRESS_ADV_FWD_TEMPLATE', u'INGRESS_ADV_FWD_TEMPLATE_ENTRY', u'INGRESS_EXT_SERVICE', u'INGRESS_EXT_SERVICE_ENTRY', u'INGRESS_EXT_SERVICE_TEMPLATE', u'INGRESS_EXT_SERVICE_TEMPLATE_ENTRY', u'IP_BINDING', u'JOB', u'KEYSERVER_MEMBER', u'KEYSERVER_MONITOR', u'KEYSERVER_MONITOR_ENCRYPTED_SEED', u'KEYSERVER_MONITOR_SEED', u'KEYSERVER_MONITOR_SEK', u'KEYSERVER_NOTIFICATION', u'L2DOMAIN', u'L2DOMAIN_SHARED', u'L2DOMAIN_TEMPLATE', u'LDAP_CONFIG', u'LIBVIRT_INTERFACE', u'LICENSE', u'LOCATION', u'MC_CHANNEL_MAP', u'MC_LIST', u'MC_RANGE', u'METADATA', u'METADATA_TAG', u'MIRROR_DESTINATION', u'MONITORING_PORT', u'MULTI_NIC_VPORT', u'NATMAPENTRY', u'NETWORK_ELEMENT', u'NETWORK_LAYOUT', u'NETWORK_MACRO_GROUP', u'NETWORK_POLICY_GROUP', u'NEXT_HOP_RESP', u'NODE_EXECUTION_ERROR', u'NS_REDUNDANT_PORT', u'NSG_NOTIFICATION', u'NSGATEWAY', u'NSGATEWAY_CONFIG', u'NSGATEWAY_TEMPLATE', u'NSPORT', u'NSPORT_STATIC_CONFIG', u'NSPORT_TEMPLATE', u'NSREDUNDANT_GW_GRP', u'PATCONFIG_CONFIG_RESP', u'PATNATPOOL', u'PERMISSION', u'PERMITTED_ACTION', u'POLICING_POLICY', u'POLICY_DECISION', u'POLICY_GROUP', u'POLICY_GROUP_TEMPLATE', u'PORT', u'PORT_MR', u'PORT_TEMPLATE', u'PUBLIC_NETWORK', u'QOS_PRIMITIVE', u'RATE_LIMITER', u'RD_SEQUENCENO', u'REDUNDANT_GW_GRP', u'RESYNC', u'RTRD_ENTITY', u'RTRD_SEQUENCENO', u'SERVICE_GATEWAY_RESPONSE', u'SERVICE_VRF_SEQUENCENO', u'SERVICES_GATEWAY_RESPONSE', u'SHAPING_POLICY', u'SHARED_RESOURCE', u'SITE', u'SITE_REQ', u'SITE_RES', u'STATIC_ROUTE', u'STATIC_ROUTE_RESP', u'STATISTICS', u'STATS_COLLECTOR', u'STATS_POLICY', u'STATS_TCA', u'STATSSERVER', u'SUBNET', u'SUBNET_ENTRY', u'SUBNET_MAC_ENTRY', u'SUBNET_POOL_ENTRY', u'SUBNET_TEMPLATE', u'SYSTEM_CONFIG', u'SYSTEM_CONFIG_REQ', u'SYSTEM_CONFIG_RESP', u'SYSTEM_MONITORING', u'UNSUPPORTED', u'UPLINK_RD', u'USER', u'VIRTUAL_IP', u'VIRTUAL_MACHINE', u'VIRTUAL_MACHINE_REPORT', u'VLAN', u'VLAN_TEMPLATE', u'VM_DESCRIPTION', u'VM_INTERFACE', u'VMWARE_RELOAD_CONFIG', u'VMWARE_VCENTER', u'VMWARE_VCENTER_CLUSTER', u'VMWARE_VCENTER_DATACENTER', u'VMWARE_VCENTER_EAM_CONFIG', u'VMWARE_VCENTER_HYPERVISOR', u'VMWARE_VCENTER_VRS_BASE_CONFIG', u'VMWARE_VCENTER_VRS_CONFIG', u'VMWARE_VRS_ADDRESS_RANGE', u'VNID_SEQUENCENO', u'VPN_CONNECT', u'VPORT', u'VPORT_GATEWAY_RESPONSE', u'VPORT_MEDIATION_REQUEST', u'VPORT_MIRROR', u'VPORT_TAG_BASE', u'VPORTTAG', u'VPORTTAGTEMPLATE', u'VPRN_LABEL_SEQUENCENO', u'VRS', u'VSC', u'VSD', u'VSD_COMPONENT', u'VSG_REDUNDANT_PORT', u'VSP', u'WAN_SERVICE', u'ZONE', u'ZONE_TEMPLATE'])
        self.expose_attribute(local_name="command", remote_name="command", attribute_type=str, is_required=True, is_unique=False, choices=[u'APPLY_POLICY_CHANGES', u'BATCH_CRUD_REQUEST', u'BATCH_GATEWAY_SECURED_DATAS', u'BEGIN_POLICY_CHANGES', u'CERTIFICATE_NSG_RENEW', u'CERTIFICATE_NSG_REVOKE', u'CLEAR_IPSEC_DATA', u'DISCARD_POLICY_CHANGES', u'EXPORT', u'FORCE_KEYSERVER_UPDATE', u'FORCE_KEYSERVER_UPDATE_ACK', u'FORCE_KEYSERVER_VSD_RESYNC', u'GATEWAY_AUDIT', u'IMPORT', u'KEYSERVER_NOTIFICATION_TEST', u'NOTIFY_NSG_REGISTRATION', u'NOTIFY_NSG_REGISTRATION_ACK', u'NOTIFY_NSG_REGISTRATION_TEST', u'NSG_NOTIFICATION_TEST', u'NSG_REGISTRATION_INFO', u'RELOAD', u'RELOAD_GEO_REDUNDANT_INFO', u'RELOAD_NSG_CONFIG', u'RETRIEVE_ACTIVE_NSGS', u'VCENTER_RECONNECT', u'VCENTER_RELOAD'])
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="parameters", remote_name="parameters", attribute_type=dict, is_required=False, is_unique=False)
        self.expose_attribute(local_name="progress", remote_name="progress", attribute_type=float, is_required=False, is_unique=False)
        self.expose_attribute(local_name="result", remote_name="result", attribute_type=dict, is_required=False, is_unique=False)
        self.expose_attribute(local_name="status", remote_name="status", attribute_type=str, is_required=False, is_unique=False, choices=[u'FAILED', u'RUNNING', u'SUCCESS'])
        

        # Fetchers
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def assoc_entity_type(self):
        """ Get assoc_entity_type value.

            Notes:
                Entity with which this job is associated Refer to API section for supported types.

                
                This attribute is named `assocEntityType` in VSD API.
                
        """
        return self._assoc_entity_type

    @assoc_entity_type.setter
    def assoc_entity_type(self, value):
        """ Set assoc_entity_type value.

            Notes:
                Entity with which this job is associated Refer to API section for supported types.

                
                This attribute is named `assocEntityType` in VSD API.
                
        """
        self._assoc_entity_type = value

    
    @property
    def command(self):
        """ Get command value.

            Notes:
                Name of the command.

                
        """
        return self._command

    @command.setter
    def command(self, value):
        """ Set command value.

            Notes:
                Name of the command.

                
        """
        self._command = value

    
    @property
    def entity_scope(self):
        """ Get entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        return self._entity_scope

    @entity_scope.setter
    def entity_scope(self, value):
        """ Set entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        self._entity_scope = value

    
    @property
    def external_id(self):
        """ Get external_id value.

            Notes:
                External object ID. Used for integration with third party systems

                
                This attribute is named `externalID` in VSD API.
                
        """
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        """ Set external_id value.

            Notes:
                External object ID. Used for integration with third party systems

                
                This attribute is named `externalID` in VSD API.
                
        """
        self._external_id = value

    
    @property
    def last_updated_by(self):
        """ Get last_updated_by value.

            Notes:
                ID of the user who last updated the object.

                
                This attribute is named `lastUpdatedBy` in VSD API.
                
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, value):
        """ Set last_updated_by value.

            Notes:
                ID of the user who last updated the object.

                
                This attribute is named `lastUpdatedBy` in VSD API.
                
        """
        self._last_updated_by = value

    
    @property
    def parameters(self):
        """ Get parameters value.

            Notes:
                Additional arguments required for the specific command. Differs based on types of command.

                
        """
        return self._parameters

    @parameters.setter
    def parameters(self, value):
        """ Set parameters value.

            Notes:
                Additional arguments required for the specific command. Differs based on types of command.

                
        """
        self._parameters = value

    
    @property
    def progress(self):
        """ Get progress value.

            Notes:
                Indicates the progress of the job as a faction. eg : 0.5 means 50% done.

                
        """
        return self._progress

    @progress.setter
    def progress(self, value):
        """ Set progress value.

            Notes:
                Indicates the progress of the job as a faction. eg : 0.5 means 50% done.

                
        """
        self._progress = value

    
    @property
    def result(self):
        """ Get result value.

            Notes:
                Results from the execution of the job

                
        """
        return self._result

    @result.setter
    def result(self, value):
        """ Set result value.

            Notes:
                Results from the execution of the job

                
        """
        self._result = value

    
    @property
    def status(self):
        """ Get status value.

            Notes:
                Current status of the job. Possible values are RUNNING, FAILED, SUCCESS, .

                
        """
        return self._status

    @status.setter
    def status(self, value):
        """ Set status value.

            Notes:
                Current status of the job. Possible values are RUNNING, FAILED, SUCCESS, .

                
        """
        self._status = value

    

    