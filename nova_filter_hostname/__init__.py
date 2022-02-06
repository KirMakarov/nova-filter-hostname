from nova.objects.request_spec import RequestSpec
from nova.scheduler.filters import BaseHostFilter
from nova.scheduler.host_manager import HostState
from oslo_log import log as logging

LOG = logging.getLogger(__name__)

BASE_HOST_NAME = "hostname"


class HostnameFilter(BaseHostFilter):
    """A simple filter that checks each host on the suffix named."""

    def host_passes(self, host_state: HostState, spec_obj: RequestSpec) -> bool:
        if BASE_HOST_NAME in host_state.nodename:
            LOG.debug(f'Allowing VM on host: {host_state.host}')
            return True
        LOG.debug(f'Not allowing VM on host: {host_state.host}')
        return False
