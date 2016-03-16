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



from .fetchers import NUAddressRangesFetcher


from .fetchers import NUDHCPOptionsFetcher


from .fetchers import NUEventLogsFetcher


from .fetchers import NUGlobalMetadatasFetcher


from .fetchers import NUIPReservationsFetcher


from .fetchers import NUMetadatasFetcher


from .fetchers import NUQOSsFetcher


from .fetchers import NUVMResyncsFetcher


from .fetchers import NUStatisticsFetcher


from .fetchers import NUStatisticsPoliciesFetcher


from .fetchers import NUTCAsFetcher


from .fetchers import NUVirtualIPsFetcher


from .fetchers import NUVMsFetcher


from .fetchers import NUVMInterfacesFetcher


from .fetchers import NUVPortsFetcher

from bambou import NURESTObject


class NUSubnet(NURESTObject):
    """ Represents a Subnet in the VSD

        Notes:
            This is the definition of a subnet associated with a zone.
    """

    __rest_name__ = "subnet"
    __resource_name__ = "subnets"

    
    ## Constants
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_APPD_FLOW_FORWARDING_POLICY = "APPD_FLOW_FORWARDING_POLICY"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_MIRROR_DESTINATION = "MIRROR_DESTINATION"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_KEYSERVER_MEMBER = "KEYSERVER_MEMBER"
    
    CONST_PAT_ENABLED_INHERITED = "INHERITED"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_GATEWAY_SERVICE_CONFIG = "GATEWAY_SERVICE_CONFIG"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VSD_COMPONENT = "VSD_COMPONENT"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_INGRESS_ACL = "INGRESS_ACL"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_EVPN_BGP_COMMUNITY_TAG_SEQ_NO = "EVPN_BGP_COMMUNITY_TAG_SEQ_NO"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_SYSTEM_CONFIG_RESP = "SYSTEM_CONFIG_RESP"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_INFRASTRUCTURE_PORT_PROFILE = "INFRASTRUCTURE_PORT_PROFILE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_APPLICATION = "APPLICATION"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_ENTERPRISE_CONFIG = "ENTERPRISE_CONFIG"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VIRTUAL_MACHINE = "VIRTUAL_MACHINE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_EGRESS_QOS_PRIMITIVE = "EGRESS_QOS_PRIMITIVE"
    
    CONST_UNDERLAY_ENABLED_ENABLED = "ENABLED"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_SYSTEM_MONITORING = "SYSTEM_MONITORING"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_POLICY_GROUP = "POLICY_GROUP"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_DC_CONFIG = "DC_CONFIG"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_NSPORT_STATIC_CONFIG = "NSPORT_STATIC_CONFIG"
    
    CONST_UNDERLAY_ENABLED_INHERITED = "INHERITED"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_ENTERPRISE_PROFILE = "ENTERPRISE_PROFILE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_FLOATING_IP_ACL_TEMPLATE_ENTRY = "FLOATING_IP_ACL_TEMPLATE_ENTRY"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_GATEWAY_SECURITY_PROFILE_RESPONSE = "GATEWAY_SECURITY_PROFILE_RESPONSE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VMWARE_VCENTER_CLUSTER = "VMWARE_VCENTER_CLUSTER"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_CERTIFICATE = "CERTIFICATE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_NETWORK_POLICY_GROUP = "NETWORK_POLICY_GROUP"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_STATS_COLLECTOR = "STATS_COLLECTOR"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_ENTERPRISE_NETWORK = "ENTERPRISE_NETWORK"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VPORT_GATEWAY_RESPONSE = "VPORT_GATEWAY_RESPONSE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_GATEWAY_SECURED_DATA = "GATEWAY_SECURED_DATA"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_INGRESS_ACL_TEMPLATE_ENTRY = "INGRESS_ACL_TEMPLATE_ENTRY"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_ACLENTRY_LOCATION = "ACLENTRY_LOCATION"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_RTRD_ENTITY = "RTRD_ENTITY"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_ZONE = "ZONE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_DSCP_FORWARDING_CLASS_MAPPING = "DSCP_FORWARDING_CLASS_MAPPING"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VPORT_MIRROR = "VPORT_MIRROR"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_DOMAIN_FLOATING_IP_ACL_TEMPLATE = "DOMAIN_FLOATING_IP_ACL_TEMPLATE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_MC_CHANNEL_MAP = "MC_CHANNEL_MAP"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_ENTERPRISE_SECURED_DATA = "ENTERPRISE_SECURED_DATA"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_PORT_TEMPLATE = "PORT_TEMPLATE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_FLOATINGIP_ACL = "FLOATINGIP_ACL"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_BRIDGEINTERFACE = "BRIDGEINTERFACE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_POLICING_POLICY = "POLICING_POLICY"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_GATEWAY_SECURITY_RESPONSE = "GATEWAY_SECURITY_RESPONSE"
    
    CONST_PAT_ENABLED_ENABLED = "ENABLED"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_SERVICE_VRF_SEQUENCENO = "SERVICE_VRF_SEQUENCENO"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_INGRESS_ADV_FWD_TEMPLATE = "INGRESS_ADV_FWD_TEMPLATE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_GROUP = "GROUP"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_KEYSERVER_MONITOR = "KEYSERVER_MONITOR"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_NSGATEWAY_TEMPLATE = "NSGATEWAY_TEMPLATE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_GATEWAY_CONFIG_RESP = "GATEWAY_CONFIG_RESP"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_MC_RANGE = "MC_RANGE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_NETWORK_LAYOUT = "NETWORK_LAYOUT"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_BACK_HAUL_SERVICE_RESP = "BACK_HAUL_SERVICE_RESP"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_GATEWAY_SECURITY_PROFILE_REQUEST = "GATEWAY_SECURITY_PROFILE_REQUEST"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_SUBNET_POOL_ENTRY = "SUBNET_POOL_ENTRY"
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VM_DESCRIPTION = "VM_DESCRIPTION"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_APPD_TIER = "APPD_TIER"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VM_INTERFACE = "VM_INTERFACE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_EGRESS_QOS_QUEUE_MR = "EGRESS_QOS_QUEUE_MR"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VLAN = "VLAN"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_ADDRESS_RANGE = "ADDRESS_RANGE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_EGRESS_ACL_TEMPLATE = "EGRESS_ACL_TEMPLATE"
    
    CONST_UNDERLAY_ENABLED_DISABLED = "DISABLED"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_EGRESS_QOS_MR = "EGRESS_QOS_MR"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_GEO_VM_RES = "GEO_VM_RES"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_DISKSTATS = "DISKSTATS"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VSP = "VSP"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_NEXT_HOP_RESP = "NEXT_HOP_RESP"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_DOMAIN = "DOMAIN"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_GATEWAY_TEMPLATE = "GATEWAY_TEMPLATE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_INGRESS_ADV_FWD = "INGRESS_ADV_FWD"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VMWARE_VCENTER_HYPERVISOR = "VMWARE_VCENTER_HYPERVISOR"
    
    CONST_IP_TYPE_IPV6 = "IPV6"
    
    CONST_IP_TYPE_IPV4 = "IPV4"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VSC = "VSC"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VMWARE_VCENTER = "VMWARE_VCENTER"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_GATEWAY_SECURITY = "GATEWAY_SECURITY"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_SYSTEM_CONFIG_REQ = "SYSTEM_CONFIG_REQ"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_MULTI_NIC_VPORT = "MULTI_NIC_VPORT"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VMWARE_VRS_ADDRESS_RANGE = "VMWARE_VRS_ADDRESS_RANGE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VSG_REDUNDANT_PORT = "VSG_REDUNDANT_PORT"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_INFRASTRUCTURE_CONFIG = "INFRASTRUCTURE_CONFIG"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_LIBVIRT_INTERFACE = "LIBVIRT_INTERFACE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_ENTITY_METADATA_BINDING = "ENTITY_METADATA_BINDING"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_REDUNDANT_GW_GRP = "REDUNDANT_GW_GRP"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_L2DOMAIN_TEMPLATE = "L2DOMAIN_TEMPLATE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_METADATA = "METADATA"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_POLICY_GROUP_TEMPLATE = "POLICY_GROUP_TEMPLATE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_DOMAIN_CONFIG_RESP = "DOMAIN_CONFIG_RESP"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VMWARE_VCENTER_VRS_BASE_CONFIG = "VMWARE_VCENTER_VRS_BASE_CONFIG"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_INGRESS_EXT_SERVICE_TEMPLATE_ENTRY = "INGRESS_EXT_SERVICE_TEMPLATE_ENTRY"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_CUSTOMER_VRF_SEQUENCENO = "CUSTOMER_VRF_SEQUENCENO"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_BGPPEER = "BGPPEER"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_RTRD_SEQUENCENO = "RTRD_SEQUENCENO"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_IP_BINDING = "IP_BINDING"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_HSC = "HSC"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VPORT = "VPORT"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_APPD_SERVICE = "APPD_SERVICE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VIRTUAL_MACHINE_REPORT = "VIRTUAL_MACHINE_REPORT"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_RATE_LIMITER = "RATE_LIMITER"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_APPD_EXTERNAL_APP_SERVICE = "APPD_EXTERNAL_APP_SERVICE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_INGRESS_ACL_TEMPLATE = "INGRESS_ACL_TEMPLATE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_SITE_RES = "SITE_RES"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_KEYSERVER_NOTIFICATION = "KEYSERVER_NOTIFICATION"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_DOMAIN_FLOATING_IP_ACL_TEMPLATE_ENTRY = "DOMAIN_FLOATING_IP_ACL_TEMPLATE_ENTRY"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_ENTERPRISE_CONFIG_RESP = "ENTERPRISE_CONFIG_RESP"
    
    CONST_MULTICAST_DISABLED = "DISABLED"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_EVPN_BGP_COMMUNITY_TAG_ENTRY = "EVPN_BGP_COMMUNITY_TAG_ENTRY"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_FLOATING_IP_ACL_TEMPLATE = "FLOATING_IP_ACL_TEMPLATE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_AUTO_DISC_GATEWAY = "AUTO_DISC_GATEWAY"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_PUBLIC_NETWORK = "PUBLIC_NETWORK"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_LDAP_CONFIG = "LDAP_CONFIG"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_EXPORTIMPORT = "EXPORTIMPORT"
    
    CONST_ENCRYPTION_ENABLED = "ENABLED"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_INGRESS_ADV_FWD_TEMPLATE_ENTRY = "INGRESS_ADV_FWD_TEMPLATE_ENTRY"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VMWARE_VCENTER_VRS_CONFIG = "VMWARE_VCENTER_VRS_CONFIG"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_SUBNET_TEMPLATE = "SUBNET_TEMPLATE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_INFRASTRUCTURE_VSC_PROFILE = "INFRASTRUCTURE_VSC_PROFILE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VMWARE_VCENTER_DATACENTER = "VMWARE_VCENTER_DATACENTER"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_NSPORT_TEMPLATE = "NSPORT_TEMPLATE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_GEO_VM_REQ = "GEO_VM_REQ"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_UPLINK_RD = "UPLINK_RD"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_NSG_NOTIFICATION = "NSG_NOTIFICATION"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_DHCP_OPTION = "DHCP_OPTION"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_INGRESS_EXT_SERVICE_TEMPLATE = "INGRESS_EXT_SERVICE_TEMPLATE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VPRN_LABEL_SEQUENCENO = "VPRN_LABEL_SEQUENCENO"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VPORT_MEDIATION_REQUEST = "VPORT_MEDIATION_REQUEST"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_NSGATEWAY = "NSGATEWAY"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_DHCP_ALLOC_MESSAGE = "DHCP_ALLOC_MESSAGE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_SUBNET_ENTRY = "SUBNET_ENTRY"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_DSCP_FORWARDING_CLASS_TABLE = "DSCP_FORWARDING_CLASS_TABLE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_KEYSERVER_MONITOR_SEK = "KEYSERVER_MONITOR_SEK"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_USER = "USER"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_EVENT_LOG = "EVENT_LOG"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_NETWORK_MACRO_GROUP = "NETWORK_MACRO_GROUP"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_EXTERNAL_SERVICE = "EXTERNAL_SERVICE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VMWARE_VCENTER_EAM_CONFIG = "VMWARE_VCENTER_EAM_CONFIG"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_ZONE_TEMPLATE = "ZONE_TEMPLATE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_SYSTEM_CONFIG = "SYSTEM_CONFIG"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_STATIC_ROUTE_RESP = "STATIC_ROUTE_RESP"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_HEALTH_REQ = "HEALTH_REQ"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_SITE_REQ = "SITE_REQ"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_IKEV2_GATEWAY = "IKEV2_GATEWAY"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_EGRESS_ACL_ENTRY = "EGRESS_ACL_ENTRY"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_LICENSE = "LICENSE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_SHARED_RESOURCE = "SHARED_RESOURCE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VRS = "VRS"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_FLOATINGIP_ACL_ENTRY = "FLOATINGIP_ACL_ENTRY"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_MC_LIST = "MC_LIST"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_GATEWAY_SECURITY_REQUEST = "GATEWAY_SECURITY_REQUEST"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_NSPORT = "NSPORT"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_FLOATINGIP = "FLOATINGIP"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_INGRESS_ADV_FWD_ENTRY = "INGRESS_ADV_FWD_ENTRY"
    
    CONST_MULTICAST_INHERITED = "INHERITED"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VSD = "VSD"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_DOMAIN_TEMPLATE = "DOMAIN_TEMPLATE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_APPD_APPLICATION = "APPD_APPLICATION"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_L2DOMAIN_SHARED = "L2DOMAIN_SHARED"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_MONITORING_PORT = "MONITORING_PORT"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_GEO_VM_EVENT = "GEO_VM_EVENT"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_INGRESS_EXT_SERVICE_ENTRY = "INGRESS_EXT_SERVICE_ENTRY"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_CLOUD_MGMT_SYSTEM = "CLOUD_MGMT_SYSTEM"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_PATNATPOOL = "PATNATPOOL"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_GATEWAY_VPORT_CONFIG = "GATEWAY_VPORT_CONFIG"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_NS_REDUNDANT_PORT = "NS_REDUNDANT_PORT"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_STATSSERVER = "STATSSERVER"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_NODE_EXECUTION_ERROR = "NODE_EXECUTION_ERROR"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_INFRASTRUCTURE_GATEWAY_PROFILE = "INFRASTRUCTURE_GATEWAY_PROFILE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_SUBNET = "SUBNET"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_ENTERPRISE_PERMISSION = "ENTERPRISE_PERMISSION"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_HOSTINTERFACE = "HOSTINTERFACE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_KEYSERVER_MONITOR_SEED = "KEYSERVER_MONITOR_SEED"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_PORT = "PORT"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_EGRESS_ACL = "EGRESS_ACL"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_BOOTSTRAP = "BOOTSTRAP"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_SERVICE_GATEWAY_RESPONSE = "SERVICE_GATEWAY_RESPONSE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_NSREDUNDANT_GW_GRP = "NSREDUNDANT_GW_GRP"
    
    CONST_ENCRYPTION_INHERITED = "INHERITED"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VPORTTAG = "VPORTTAG"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_SHAPING_POLICY = "SHAPING_POLICY"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_RD_SEQUENCENO = "RD_SEQUENCENO"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_GROUPKEY_ENCRYPTION_PROFILE = "GROUPKEY_ENCRYPTION_PROFILE"
    
    CONST_PAT_ENABLED_DISABLED = "DISABLED"
    
    CONST_ENCRYPTION_DISABLED = "DISABLED"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_SUBNET_MAC_ENTRY = "SUBNET_MAC_ENTRY"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_DHCP_CONFIG_RESP = "DHCP_CONFIG_RESP"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VIRTUAL_IP = "VIRTUAL_IP"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_L2DOMAIN = "L2DOMAIN"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_APPD_FLOW_SECURITY_POLICY = "APPD_FLOW_SECURITY_POLICY"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_JOB = "JOB"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_GATEWAY_SERVICE_CONFIG_RESP = "GATEWAY_SERVICE_CONFIG_RESP"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_CHILD_ENTITY_POLICY_CHANGE = "CHILD_ENTITY_POLICY_CHANGE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_SITE = "SITE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_IKEV2_ENCRYPTION_PROFILE = "IKEV2_ENCRYPTION_PROFILE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_ADDRESS_RANGE_STATE = "ADDRESS_RANGE_STATE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_NETWORK_ELEMENT = "NETWORK_ELEMENT"
    
    CONST_MAINTENANCE_MODE_DISABLED = "DISABLED"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_PERMITTED_ACTION = "PERMITTED_ACTION"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_GATEWAY_CONFIG = "GATEWAY_CONFIG"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_STATS_POLICY = "STATS_POLICY"
    
    CONST_MAINTENANCE_MODE_ENABLED_INHERITED = "ENABLED_INHERITED"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_SERVICES_GATEWAY_RESPONSE = "SERVICES_GATEWAY_RESPONSE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_INGRESS_ACL_ENTRY = "INGRESS_ACL_ENTRY"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_BOOTSTRAP_ACTIVATION = "BOOTSTRAP_ACTIVATION"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_STATS_TCA = "STATS_TCA"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_APPD_FLOW = "APPD_FLOW"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VPORT_TAG_BASE = "VPORT_TAG_BASE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_WAN_SERVICE = "WAN_SERVICE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_ALARM = "ALARM"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_NSGATEWAY_CONFIG = "NSGATEWAY_CONFIG"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_PERMISSION = "PERMISSION"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VMWARE_RELOAD_CONFIG = "VMWARE_RELOAD_CONFIG"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_GATEWAY_VPORT_CONFIG_RESP = "GATEWAY_VPORT_CONFIG_RESP"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_NATMAPENTRY = "NATMAPENTRY"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_INGRESS_EXT_SERVICE = "INGRESS_EXT_SERVICE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_RESYNC = "RESYNC"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_DOMAIN_CONFIG = "DOMAIN_CONFIG"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_ENDPOINT = "ENDPOINT"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VPN_CONNECT = "VPN_CONNECT"
    
    CONST_MULTICAST_ENABLED = "ENABLED"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_LOCATION = "LOCATION"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_PORT_MR = "PORT_MR"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_EGRESS_ACL_TEMPLATE_ENTRY = "EGRESS_ACL_TEMPLATE_ENTRY"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_KEYSERVER_MONITOR_ENCRYPTED_SEED = "KEYSERVER_MONITOR_ENCRYPTED_SEED"
    
    CONST_MAINTENANCE_MODE_ENABLED = "ENABLED"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_STATISTICS = "STATISTICS"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_GATEWAY = "GATEWAY"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_PATCONFIG_CONFIG_RESP = "PATCONFIG_CONFIG_RESP"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VNID_SEQUENCENO = "VNID_SEQUENCENO"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_ENTERPRISE_SECURITY = "ENTERPRISE_SECURITY"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_ESI_SEQUENCENO = "ESI_SEQUENCENO"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VLAN_TEMPLATE = "VLAN_TEMPLATE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_METADATA_TAG = "METADATA_TAG"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_UNSUPPORTED = "UNSUPPORTED"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_QOS_PRIMITIVE = "QOS_PRIMITIVE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_POLICY_DECISION = "POLICY_DECISION"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_VPORTTAGTEMPLATE = "VPORTTAGTEMPLATE"
    
    CONST_ASSOCIATED_APPLICATION_OBJECT_TYPE_STATIC_ROUTE = "STATIC_ROUTE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a Subnet instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> subnet = NUSubnet(id=u'xxxx-xxx-xxx-xxx', name=u'Subnet')
                >>> subnet = NUSubnet(data=my_dict)
        """

        super(NUSubnet, self).__init__()

        # Read/Write Attributes
        
        self._ip_type = None
        self._pat_enabled = None
        self._address = None
        self._associated_application_id = None
        self._associated_application_object_id = None
        self._associated_application_object_type = None
        self._associated_multicast_channel_map_id = None
        self._associated_shared_network_resource_id = None
        self._description = None
        self._encryption = None
        self._entity_scope = None
        self._external_id = None
        self._gateway = None
        self._gateway_mac_address = None
        self._last_updated_by = None
        self._maintenance_mode = None
        self._multicast = None
        self._name = None
        self._netmask = None
        self._policy_group_id = None
        self._proxy_arp = None
        self._public = None
        self._route_distinguisher = None
        self._route_target = None
        self._service_id = None
        self._split_subnet = None
        self._template_id = None
        self._underlay_enabled = None
        self._vn_id = None
        
        self.expose_attribute(local_name="ip_type", remote_name="IPType", attribute_type=str, is_required=False, is_unique=False, choices=[u'IPV4', u'IPV6'])
        self.expose_attribute(local_name="pat_enabled", remote_name="PATEnabled", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name="address", remote_name="address", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_application_id", remote_name="associatedApplicationID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_application_object_id", remote_name="associatedApplicationObjectID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_application_object_type", remote_name="associatedApplicationObjectType", attribute_type=str, is_required=False, is_unique=False, choices=[u'ACLENTRY_LOCATION', u'ADDRESS_RANGE', u'ADDRESS_RANGE_STATE', u'ALARM', u'APPD_APPLICATION', u'APPD_EXTERNAL_APP_SERVICE', u'APPD_FLOW', u'APPD_FLOW_FORWARDING_POLICY', u'APPD_FLOW_SECURITY_POLICY', u'APPD_SERVICE', u'APPD_TIER', u'APPLICATION', u'AUTO_DISC_GATEWAY', u'BACK_HAUL_SERVICE_RESP', u'BGPPEER', u'BOOTSTRAP', u'BOOTSTRAP_ACTIVATION', u'BRIDGEINTERFACE', u'CERTIFICATE', u'CHILD_ENTITY_POLICY_CHANGE', u'CLOUD_MGMT_SYSTEM', u'CUSTOMER_VRF_SEQUENCENO', u'DC_CONFIG', u'DHCP_ALLOC_MESSAGE', u'DHCP_CONFIG_RESP', u'DHCP_OPTION', u'DISKSTATS', u'DOMAIN', u'DOMAIN_CONFIG', u'DOMAIN_CONFIG_RESP', u'DOMAIN_FLOATING_IP_ACL_TEMPLATE', u'DOMAIN_FLOATING_IP_ACL_TEMPLATE_ENTRY', u'DOMAIN_TEMPLATE', u'DSCP_FORWARDING_CLASS_MAPPING', u'DSCP_FORWARDING_CLASS_TABLE', u'EGRESS_ACL', u'EGRESS_ACL_ENTRY', u'EGRESS_ACL_TEMPLATE', u'EGRESS_ACL_TEMPLATE_ENTRY', u'EGRESS_QOS_MR', u'EGRESS_QOS_PRIMITIVE', u'EGRESS_QOS_QUEUE_MR', u'ENDPOINT', u'ENTERPRISE', u'ENTERPRISE_CONFIG', u'ENTERPRISE_CONFIG_RESP', u'ENTERPRISE_NETWORK', u'ENTERPRISE_PERMISSION', u'ENTERPRISE_PROFILE', u'ENTERPRISE_SECURED_DATA', u'ENTERPRISE_SECURITY', u'ENTITY_METADATA_BINDING', u'ESI_SEQUENCENO', u'EVENT_LOG', u'EVPN_BGP_COMMUNITY_TAG_ENTRY', u'EVPN_BGP_COMMUNITY_TAG_SEQ_NO', u'EXPORTIMPORT', u'EXTERNAL_SERVICE', u'FLOATING_IP_ACL_TEMPLATE', u'FLOATING_IP_ACL_TEMPLATE_ENTRY', u'FLOATINGIP', u'FLOATINGIP_ACL', u'FLOATINGIP_ACL_ENTRY', u'GATEWAY', u'GATEWAY_CONFIG', u'GATEWAY_CONFIG_RESP', u'GATEWAY_SECURED_DATA', u'GATEWAY_SECURITY', u'GATEWAY_SECURITY_PROFILE_REQUEST', u'GATEWAY_SECURITY_PROFILE_RESPONSE', u'GATEWAY_SECURITY_REQUEST', u'GATEWAY_SECURITY_RESPONSE', u'GATEWAY_SERVICE_CONFIG', u'GATEWAY_SERVICE_CONFIG_RESP', u'GATEWAY_TEMPLATE', u'GATEWAY_VPORT_CONFIG', u'GATEWAY_VPORT_CONFIG_RESP', u'GEO_VM_EVENT', u'GEO_VM_REQ', u'GEO_VM_RES', u'GROUP', u'GROUPKEY_ENCRYPTION_PROFILE', u'HEALTH_REQ', u'HOSTINTERFACE', u'HSC', u'IKEV2_ENCRYPTION_PROFILE', u'IKEV2_GATEWAY', u'INFRASTRUCTURE_CONFIG', u'INFRASTRUCTURE_GATEWAY_PROFILE', u'INFRASTRUCTURE_PORT_PROFILE', u'INFRASTRUCTURE_VSC_PROFILE', u'INGRESS_ACL', u'INGRESS_ACL_ENTRY', u'INGRESS_ACL_TEMPLATE', u'INGRESS_ACL_TEMPLATE_ENTRY', u'INGRESS_ADV_FWD', u'INGRESS_ADV_FWD_ENTRY', u'INGRESS_ADV_FWD_TEMPLATE', u'INGRESS_ADV_FWD_TEMPLATE_ENTRY', u'INGRESS_EXT_SERVICE', u'INGRESS_EXT_SERVICE_ENTRY', u'INGRESS_EXT_SERVICE_TEMPLATE', u'INGRESS_EXT_SERVICE_TEMPLATE_ENTRY', u'IP_BINDING', u'JOB', u'KEYSERVER_MEMBER', u'KEYSERVER_MONITOR', u'KEYSERVER_MONITOR_ENCRYPTED_SEED', u'KEYSERVER_MONITOR_SEED', u'KEYSERVER_MONITOR_SEK', u'KEYSERVER_NOTIFICATION', u'L2DOMAIN', u'L2DOMAIN_SHARED', u'L2DOMAIN_TEMPLATE', u'LDAP_CONFIG', u'LIBVIRT_INTERFACE', u'LICENSE', u'LOCATION', u'MC_CHANNEL_MAP', u'MC_LIST', u'MC_RANGE', u'METADATA', u'METADATA_TAG', u'MIRROR_DESTINATION', u'MONITORING_PORT', u'MULTI_NIC_VPORT', u'NATMAPENTRY', u'NETWORK_ELEMENT', u'NETWORK_LAYOUT', u'NETWORK_MACRO_GROUP', u'NETWORK_POLICY_GROUP', u'NEXT_HOP_RESP', u'NODE_EXECUTION_ERROR', u'NS_REDUNDANT_PORT', u'NSG_NOTIFICATION', u'NSGATEWAY', u'NSGATEWAY_CONFIG', u'NSGATEWAY_TEMPLATE', u'NSPORT', u'NSPORT_STATIC_CONFIG', u'NSPORT_TEMPLATE', u'NSREDUNDANT_GW_GRP', u'PATCONFIG_CONFIG_RESP', u'PATNATPOOL', u'PERMISSION', u'PERMITTED_ACTION', u'POLICING_POLICY', u'POLICY_DECISION', u'POLICY_GROUP', u'POLICY_GROUP_TEMPLATE', u'PORT', u'PORT_MR', u'PORT_TEMPLATE', u'PUBLIC_NETWORK', u'QOS_PRIMITIVE', u'RATE_LIMITER', u'RD_SEQUENCENO', u'REDUNDANT_GW_GRP', u'RESYNC', u'RTRD_ENTITY', u'RTRD_SEQUENCENO', u'SERVICE_GATEWAY_RESPONSE', u'SERVICE_VRF_SEQUENCENO', u'SERVICES_GATEWAY_RESPONSE', u'SHAPING_POLICY', u'SHARED_RESOURCE', u'SITE', u'SITE_REQ', u'SITE_RES', u'STATIC_ROUTE', u'STATIC_ROUTE_RESP', u'STATISTICS', u'STATS_COLLECTOR', u'STATS_POLICY', u'STATS_TCA', u'STATSSERVER', u'SUBNET', u'SUBNET_ENTRY', u'SUBNET_MAC_ENTRY', u'SUBNET_POOL_ENTRY', u'SUBNET_TEMPLATE', u'SYSTEM_CONFIG', u'SYSTEM_CONFIG_REQ', u'SYSTEM_CONFIG_RESP', u'SYSTEM_MONITORING', u'UNSUPPORTED', u'UPLINK_RD', u'USER', u'VIRTUAL_IP', u'VIRTUAL_MACHINE', u'VIRTUAL_MACHINE_REPORT', u'VLAN', u'VLAN_TEMPLATE', u'VM_DESCRIPTION', u'VM_INTERFACE', u'VMWARE_RELOAD_CONFIG', u'VMWARE_VCENTER', u'VMWARE_VCENTER_CLUSTER', u'VMWARE_VCENTER_DATACENTER', u'VMWARE_VCENTER_EAM_CONFIG', u'VMWARE_VCENTER_HYPERVISOR', u'VMWARE_VCENTER_VRS_BASE_CONFIG', u'VMWARE_VCENTER_VRS_CONFIG', u'VMWARE_VRS_ADDRESS_RANGE', u'VNID_SEQUENCENO', u'VPN_CONNECT', u'VPORT', u'VPORT_GATEWAY_RESPONSE', u'VPORT_MEDIATION_REQUEST', u'VPORT_MIRROR', u'VPORT_TAG_BASE', u'VPORTTAG', u'VPORTTAGTEMPLATE', u'VPRN_LABEL_SEQUENCENO', u'VRS', u'VSC', u'VSD', u'VSD_COMPONENT', u'VSG_REDUNDANT_PORT', u'VSP', u'WAN_SERVICE', u'ZONE', u'ZONE_TEMPLATE'])
        self.expose_attribute(local_name="associated_multicast_channel_map_id", remote_name="associatedMulticastChannelMapID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="associated_shared_network_resource_id", remote_name="associatedSharedNetworkResourceID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="encryption", remote_name="encryption", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        self.expose_attribute(local_name="gateway", remote_name="gateway", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway_mac_address", remote_name="gatewayMACAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="maintenance_mode", remote_name="maintenanceMode", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'ENABLED_INHERITED'])
        self.expose_attribute(local_name="multicast", remote_name="multicast", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="netmask", remote_name="netmask", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="policy_group_id", remote_name="policyGroupID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="proxy_arp", remote_name="proxyARP", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="public", remote_name="public", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="route_distinguisher", remote_name="routeDistinguisher", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="route_target", remote_name="routeTarget", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="service_id", remote_name="serviceID", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="split_subnet", remote_name="splitSubnet", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="template_id", remote_name="templateID", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="underlay_enabled", remote_name="underlayEnabled", attribute_type=str, is_required=False, is_unique=False, choices=[u'DISABLED', u'ENABLED', u'INHERITED'])
        self.expose_attribute(local_name="vn_id", remote_name="vnId", attribute_type=int, is_required=False, is_unique=False)
        

        # Fetchers
        
        
        self.address_ranges = NUAddressRangesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.dhcp_options = NUDHCPOptionsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.event_logs = NUEventLogsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.ip_reservations = NUIPReservationsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.qoss = NUQOSsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vm_resyncs = NUVMResyncsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.statistics = NUStatisticsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.statistics_policies = NUStatisticsPoliciesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.tcas = NUTCAsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.virtual_ips = NUVirtualIPsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vms = NUVMsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vm_interfaces = NUVMInterfacesFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.vports = NUVPortsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def ip_type(self):
        """ Get ip_type value.

            Notes:
                IPv4 or IPv6

                
                This attribute is named `IPType` in VSD API.
                
        """
        return self._ip_type

    @ip_type.setter
    def ip_type(self, value):
        """ Set ip_type value.

            Notes:
                IPv4 or IPv6

                
                This attribute is named `IPType` in VSD API.
                
        """
        self._ip_type = value

    
    @property
    def pat_enabled(self):
        """ Get pat_enabled value.

            Notes:
                None

                
                This attribute is named `PATEnabled` in VSD API.
                
        """
        return self._pat_enabled

    @pat_enabled.setter
    def pat_enabled(self, value):
        """ Set pat_enabled value.

            Notes:
                None

                
                This attribute is named `PATEnabled` in VSD API.
                
        """
        self._pat_enabled = value

    
    @property
    def address(self):
        """ Get address value.

            Notes:
                IP address of the subnet defined. In case of zone, this is an optional field for and allows users to allocate an IP address range to a zone. The VSD will auto-assign IP addresses to subnets from this range if a specific IP address is not defined for the subnet

                
        """
        return self._address

    @address.setter
    def address(self, value):
        """ Set address value.

            Notes:
                IP address of the subnet defined. In case of zone, this is an optional field for and allows users to allocate an IP address range to a zone. The VSD will auto-assign IP addresses to subnets from this range if a specific IP address is not defined for the subnet

                
        """
        self._address = value

    
    @property
    def associated_application_id(self):
        """ Get associated_application_id value.

            Notes:
                The associated application ID.

                
                This attribute is named `associatedApplicationID` in VSD API.
                
        """
        return self._associated_application_id

    @associated_application_id.setter
    def associated_application_id(self, value):
        """ Set associated_application_id value.

            Notes:
                The associated application ID.

                
                This attribute is named `associatedApplicationID` in VSD API.
                
        """
        self._associated_application_id = value

    
    @property
    def associated_application_object_id(self):
        """ Get associated_application_object_id value.

            Notes:
                The associated application object ID.

                
                This attribute is named `associatedApplicationObjectID` in VSD API.
                
        """
        return self._associated_application_object_id

    @associated_application_object_id.setter
    def associated_application_object_id(self, value):
        """ Set associated_application_object_id value.

            Notes:
                The associated application object ID.

                
                This attribute is named `associatedApplicationObjectID` in VSD API.
                
        """
        self._associated_application_object_id = value

    
    @property
    def associated_application_object_type(self):
        """ Get associated_application_object_type value.

            Notes:
                The associated application object type. Refer to API section for supported types.

                
                This attribute is named `associatedApplicationObjectType` in VSD API.
                
        """
        return self._associated_application_object_type

    @associated_application_object_type.setter
    def associated_application_object_type(self, value):
        """ Set associated_application_object_type value.

            Notes:
                The associated application object type. Refer to API section for supported types.

                
                This attribute is named `associatedApplicationObjectType` in VSD API.
                
        """
        self._associated_application_object_type = value

    
    @property
    def associated_multicast_channel_map_id(self):
        """ Get associated_multicast_channel_map_id value.

            Notes:
                The ID of the Multi Cast Channel Map  this Subnet/Subnet Template is associated with. This has to be set when enableMultiCast is set to ENABLED

                
                This attribute is named `associatedMulticastChannelMapID` in VSD API.
                
        """
        return self._associated_multicast_channel_map_id

    @associated_multicast_channel_map_id.setter
    def associated_multicast_channel_map_id(self, value):
        """ Set associated_multicast_channel_map_id value.

            Notes:
                The ID of the Multi Cast Channel Map  this Subnet/Subnet Template is associated with. This has to be set when enableMultiCast is set to ENABLED

                
                This attribute is named `associatedMulticastChannelMapID` in VSD API.
                
        """
        self._associated_multicast_channel_map_id = value

    
    @property
    def associated_shared_network_resource_id(self):
        """ Get associated_shared_network_resource_id value.

            Notes:
                The ID of public subnet that is associated with this subnet

                
                This attribute is named `associatedSharedNetworkResourceID` in VSD API.
                
        """
        return self._associated_shared_network_resource_id

    @associated_shared_network_resource_id.setter
    def associated_shared_network_resource_id(self, value):
        """ Set associated_shared_network_resource_id value.

            Notes:
                The ID of public subnet that is associated with this subnet

                
                This attribute is named `associatedSharedNetworkResourceID` in VSD API.
                
        """
        self._associated_shared_network_resource_id = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                A description field provided by the user that identifies the subnet

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                A description field provided by the user that identifies the subnet

                
        """
        self._description = value

    
    @property
    def encryption(self):
        """ Get encryption value.

            Notes:
                Determines whether or not IPSEC is enabled.

                
        """
        return self._encryption

    @encryption.setter
    def encryption(self, value):
        """ Set encryption value.

            Notes:
                Determines whether or not IPSEC is enabled.

                
        """
        self._encryption = value

    
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
    def gateway(self):
        """ Get gateway value.

            Notes:
                The IP address of the gateway of this subnet

                
        """
        return self._gateway

    @gateway.setter
    def gateway(self, value):
        """ Set gateway value.

            Notes:
                The IP address of the gateway of this subnet

                
        """
        self._gateway = value

    
    @property
    def gateway_mac_address(self):
        """ Get gateway_mac_address value.

            Notes:
                None

                
                This attribute is named `gatewayMACAddress` in VSD API.
                
        """
        return self._gateway_mac_address

    @gateway_mac_address.setter
    def gateway_mac_address(self, value):
        """ Set gateway_mac_address value.

            Notes:
                None

                
                This attribute is named `gatewayMACAddress` in VSD API.
                
        """
        self._gateway_mac_address = value

    
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
    def maintenance_mode(self):
        """ Get maintenance_mode value.

            Notes:
                maintenanceMode is an enum that indicates if the SubNetwork is accepting VM activation requests.

                
                This attribute is named `maintenanceMode` in VSD API.
                
        """
        return self._maintenance_mode

    @maintenance_mode.setter
    def maintenance_mode(self, value):
        """ Set maintenance_mode value.

            Notes:
                maintenanceMode is an enum that indicates if the SubNetwork is accepting VM activation requests.

                
                This attribute is named `maintenanceMode` in VSD API.
                
        """
        self._maintenance_mode = value

    
    @property
    def multicast(self):
        """ Get multicast value.

            Notes:
                multicast is enum that indicates multicast policy on Subnet/Subnet Template.

                
        """
        return self._multicast

    @multicast.setter
    def multicast(self, value):
        """ Set multicast value.

            Notes:
                multicast is enum that indicates multicast policy on Subnet/Subnet Template.

                
        """
        self._multicast = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of the current entity(Zone or zone template or subnet etc..) Valid characters are alphabets, numbers, space and hyphen( - ).

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of the current entity(Zone or zone template or subnet etc..) Valid characters are alphabets, numbers, space and hyphen( - ).

                
        """
        self._name = value

    
    @property
    def netmask(self):
        """ Get netmask value.

            Notes:
                Netmask of the subnet defined

                
        """
        return self._netmask

    @netmask.setter
    def netmask(self, value):
        """ Set netmask value.

            Notes:
                Netmask of the subnet defined

                
        """
        self._netmask = value

    
    @property
    def policy_group_id(self):
        """ Get policy_group_id value.

            Notes:
                PG ID for the subnet. This is unique per domain and will be in the range 1-4095

                
                This attribute is named `policyGroupID` in VSD API.
                
        """
        return self._policy_group_id

    @policy_group_id.setter
    def policy_group_id(self, value):
        """ Set policy_group_id value.

            Notes:
                PG ID for the subnet. This is unique per domain and will be in the range 1-4095

                
                This attribute is named `policyGroupID` in VSD API.
                
        """
        self._policy_group_id = value

    
    @property
    def proxy_arp(self):
        """ Get proxy_arp value.

            Notes:
                 when set VRS will act as  ARP Proxy

                
                This attribute is named `proxyARP` in VSD API.
                
        """
        return self._proxy_arp

    @proxy_arp.setter
    def proxy_arp(self, value):
        """ Set proxy_arp value.

            Notes:
                 when set VRS will act as  ARP Proxy

                
                This attribute is named `proxyARP` in VSD API.
                
        """
        self._proxy_arp = value

    
    @property
    def public(self):
        """ Get public value.

            Notes:
                when set to true means public subnet under a public zone

                
        """
        return self._public

    @public.setter
    def public(self, value):
        """ Set public value.

            Notes:
                when set to true means public subnet under a public zone

                
        """
        self._public = value

    
    @property
    def route_distinguisher(self):
        """ Get route_distinguisher value.

            Notes:
                The Route Distinguisher value assigned by VSD for this subnet that is used by the BGP-EVPN protocol in VSC

                
                This attribute is named `routeDistinguisher` in VSD API.
                
        """
        return self._route_distinguisher

    @route_distinguisher.setter
    def route_distinguisher(self, value):
        """ Set route_distinguisher value.

            Notes:
                The Route Distinguisher value assigned by VSD for this subnet that is used by the BGP-EVPN protocol in VSC

                
                This attribute is named `routeDistinguisher` in VSD API.
                
        """
        self._route_distinguisher = value

    
    @property
    def route_target(self):
        """ Get route_target value.

            Notes:
                The Route Target value assigned by VSD for this subnet that is used by the BGP-EVPN protocol in VSC

                
                This attribute is named `routeTarget` in VSD API.
                
        """
        return self._route_target

    @route_target.setter
    def route_target(self, value):
        """ Set route_target value.

            Notes:
                The Route Target value assigned by VSD for this subnet that is used by the BGP-EVPN protocol in VSC

                
                This attribute is named `routeTarget` in VSD API.
                
        """
        self._route_target = value

    
    @property
    def service_id(self):
        """ Get service_id value.

            Notes:
                The service ID used by the VSCs to identify this subnet

                
                This attribute is named `serviceID` in VSD API.
                
        """
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        """ Set service_id value.

            Notes:
                The service ID used by the VSCs to identify this subnet

                
                This attribute is named `serviceID` in VSD API.
                
        """
        self._service_id = value

    
    @property
    def split_subnet(self):
        """ Get split_subnet value.

            Notes:
                Need to add correct description

                
                This attribute is named `splitSubnet` in VSD API.
                
        """
        return self._split_subnet

    @split_subnet.setter
    def split_subnet(self, value):
        """ Set split_subnet value.

            Notes:
                Need to add correct description

                
                This attribute is named `splitSubnet` in VSD API.
                
        """
        self._split_subnet = value

    
    @property
    def template_id(self):
        """ Get template_id value.

            Notes:
                The ID of the subnet template that this subnet object was derived from

                
                This attribute is named `templateID` in VSD API.
                
        """
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        """ Set template_id value.

            Notes:
                The ID of the subnet template that this subnet object was derived from

                
                This attribute is named `templateID` in VSD API.
                
        """
        self._template_id = value

    
    @property
    def underlay_enabled(self):
        """ Get underlay_enabled value.

            Notes:
                Indicates whether UNDERLAY is enabled for the subnets in this domain

                
                This attribute is named `underlayEnabled` in VSD API.
                
        """
        return self._underlay_enabled

    @underlay_enabled.setter
    def underlay_enabled(self, value):
        """ Set underlay_enabled value.

            Notes:
                Indicates whether UNDERLAY is enabled for the subnets in this domain

                
                This attribute is named `underlayEnabled` in VSD API.
                
        """
        self._underlay_enabled = value

    
    @property
    def vn_id(self):
        """ Get vn_id value.

            Notes:
                Current Network's  globally unique  VXLAN network identifier generated by VSD

                
                This attribute is named `vnId` in VSD API.
                
        """
        return self._vn_id

    @vn_id.setter
    def vn_id(self, value):
        """ Set vn_id value.

            Notes:
                Current Network's  globally unique  VXLAN network identifier generated by VSD

                
                This attribute is named `vnId` in VSD API.
                
        """
        self._vn_id = value

    

    
    ## Custom methods
    def is_template(self):
        """ Verify that the object is a template
    
            Returns:
                (bool): True if the object is a template
        """
        return False
    
    def is_from_template(self):
        """ Verify if the object has been instantiated from a template
    
            Note:
                The object has to be fetched. Otherwise, it does not
                have information from its parent
    
            Returns:
                (bool): True if the object is a template
        """
        return self.template_id
    