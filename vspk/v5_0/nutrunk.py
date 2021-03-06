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



from .fetchers import NUVPortsFetcher

from bambou import NURESTObject


class NUTrunk(NURESTObject):
    """ Represents a Trunk in the VSD

        Notes:
            Trunk is an object that is an aggregator of sub-vports corresponding to segmentation-ids (vlans) in a trunk
    """

    __rest_name__ = "trunk"
    __resource_name__ = "trunks"

    

    def __init__(self, **kwargs):
        """ Initializes a Trunk instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> trunk = NUTrunk(id=u'xxxx-xxx-xxx-xxx', name=u'Trunk')
                >>> trunk = NUTrunk(data=my_dict)
        """

        super(NUTrunk, self).__init__()

        # Read/Write Attributes
        
        self._name = None
        self._associated_vport_id = None
        
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="associated_vport_id", remote_name="associatedVPortID", attribute_type=str, is_required=True, is_unique=False)
        

        # Fetchers
        
        
        self.vports = NUVPortsFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def name(self):
        """ Get name value.

            Notes:
                The name of the trunk

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                The name of the trunk

                
        """
        self._name = value

    
    @property
    def associated_vport_id(self):
        """ Get associated_vport_id value.

            Notes:
                the uuid of the parent vport (the trunkRole of the parent vport must be PARENT_PORT)

                
                This attribute is named `associatedVPortID` in VSD API.
                
        """
        return self._associated_vport_id

    @associated_vport_id.setter
    def associated_vport_id(self, value):
        """ Set associated_vport_id value.

            Notes:
                the uuid of the parent vport (the trunkRole of the parent vport must be PARENT_PORT)

                
                This attribute is named `associatedVPortID` in VSD API.
                
        """
        self._associated_vport_id = value

    

    