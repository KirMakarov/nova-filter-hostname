import pytest

from nova_filter_hostname import HostnameFilter


@pytest.mark.parametrize('host_name, expected', [
    ('foo-hostname_bar', True),
    ('42', False)
])
def test_hostname_filter(mocker, host_name_filter, expected):
    mocker.patch('nova_filter_hostname.oslo_log')
    mocker.patch('nova_filter_hostname.nova')
    mock_host_state = mocker.Mock(nodename=host_name_filter)
    mock_spec_obj = mocker.Mock()

    host_name_filter = HostnameFilter()
    assert host_name_filter.host_passes(mock_host_state, mock_spec_obj) == expected
