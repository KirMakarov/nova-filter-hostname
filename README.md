# nova-filter-hostname
Nova filter hostname

For using the filter, you need to modify `/etc/nova/nova.conf` to include your new filter. You need to add the new filter to both available_filters and to enabled_filters.
You can look example example-nova.conf or block here
```
[filter_scheduler]
available_filters = nova.scheduler.filters.all_filters
available_filters = nova_filter_example.RandomFilter
track_instance_changes = False
enabled_filters = ComputeFilter,RandomFilter
```
