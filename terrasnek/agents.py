"""
Module for Terraform Cloud API Endpoint: Agent Pools and Agents.
"""

from .endpoint import TFCEndpoint
from._constants import Entitlements

class TFCAgents(TFCEndpoint):
    """
    `Agents API Docs \
        <https://www.terraform.io/docs/cloud/api/agents.html>`_
    """

    def __init__(self, instance_url, org_name, headers, well_known_paths, verify, log_level):
        super().__init__(instance_url, org_name, headers, well_known_paths, verify, log_level)
        self._agent_pools_api_v2_base_url = f"{self._api_v2_base_url}/agent-pools"
        self._agents_api_v2_base_url = f"{self._api_v2_base_url}/agents"
        self._org_api_v2_base_url = f"{self._api_v2_base_url}/organizations"

    def _required_entitlements(self):
        return [Entitlements.AGENTS]

    def create_pool(self, payload):
        """
        ``POST /organizations/:organization_name/agent-pool``

        `Agents Create Pool API Doc Reference \
            <https://www.terraform.io/docs/cloud/api/agents.html#create-an-agent-pool>`_
        """
        url = f"{self._org_api_v2_base_url}/{self._org_name}/agent-pools"
        return self._create(url, payload)

    def list_pools(self):
        """
        ``GET /organizations/:organization_name/agent-pools``

        `Agents List Pools API Doc Reference \
            <https://www.terraform.io/docs/cloud/api/agents.html#list-agent-pools>`_
        """
        url = f"{self._org_api_v2_base_url}/{self._org_name}/agent-pools"
        return self._list(url)

    def list(self, agent_pool_id, filters=None):
        """
        ``GET /agent-pools/:agent_pool_id/agents``

        `Agents List API Doc Reference \
            <https://www.terraform.io/docs/cloud/api/agents.html#list-agents>`_

        Query Parameter(s) (`details \
            <https://www.terraform.io/docs/cloud/api/agents.html#query-parameters>`_):
            - ``filter[last-ping-since]`` (Optional)

        Example filter(s):

        .. code-block:: python

            filters = [
                {
                    "keys": ["last-ping-since"],
                    "value": "foo"
                }
            ]
        """
        url = f"{self._agent_pools_api_v2_base_url}/{agent_pool_id}/agents"
        return self._list(url, filters=filters)

    def show_pool(self, agent_pool_id):
        """
        ``GET /agent-pools/:id``

        `Agents Show Pool API Doc Reference \
            <https://www.terraform.io/docs/cloud/api/agents.html#show-an-agent-pool>`_
        """
        url = f"{self._agent_pools_api_v2_base_url}/{agent_pool_id}"
        return self._show(url)

    def show(self, agent_id):
        """
        ``GET /agents/:id``

        `Agents Show API Doc Reference \
            <https://www.terraform.io/docs/cloud/api/agents.html#show-an-agent>`_
        """
        url = f"{self._agents_api_v2_base_url}/{agent_id}"
        return self._show(url)
