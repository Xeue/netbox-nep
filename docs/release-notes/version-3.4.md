# NetBox v3.4

!!! warning "PostgreSQL 11 Required"
    NetBox v3.4 requires PostgreSQL 11 or later.

### Breaking Changes

* Device and virtual machine names are no longer case-sensitive. Attempting to create e.g. "device1" and "DEVICE1" will raise a validation error.
* The `asn` field has been removed from the provider model. Please replicate any provider ASN assignments to the ASN model introduced in NetBox v3.1 prior to upgrading.
* The `noc_contact`, `admin_contact`, and `portal_url` fields have been removed from the provider model. Please replicate any data remaining in these fields to the contact model introduced in NetBox v3.1 prior to upgrading.
* The `content_type` field on the CustomLink and ExportTemplate models have been renamed to `content_types` and now supports the assignment of multiple content types.
* The `cf` property on an object with custom fields now returns deserialized values. For example, a custom field referencing an object will return the object instance rather than its numeric ID. To access the raw serialized values, use `custom_field_data` instead.

### New Features

#### New Global Search ([#10560](https://github.com/netbox-community/netbox/issues/10560))

NetBox's global search functionality has been completely overhauled and replaced by a new cache-based lookup.

### JSON/YAML Bulk Imports ([#4347](https://github.com/netbox-community/netbox/issues/4347))

NetBox's bulk import feature, which was previously limited to CSV-formatted data for most objects, has been extended to support the import of objects from JSON and/or YAML data as well.

#### CSV-Based Bulk Updates ([#7961](https://github.com/netbox-community/netbox/issues/7961))

NetBox's CSV-based bulk import functionality has been extended to support also modifying existing objects. When an `id` column is present in the import form, it will be used to infer the object to be modified, rather than a new object being created. All fields (columns) are optional when modifying existing objects.

#### Top-Level Plugin Navigation Menus ([#9071](https://github.com/netbox-community/netbox/issues/9071))

A new `PluginMenu` class has been introduced, which enables a plugin to inject a top-level menu in NetBox's navigation menu. This menu can have one or more groups of menu items, just like core items. Backward compatibility with the existing `menu_items` has been maintained.

### Enhancements

* [#7376](https://github.com/netbox-community/netbox/issues/7376) - Enable the assignment of tags during CSV import
* [#8245](https://github.com/netbox-community/netbox/issues/8245) - Enable GraphQL filtering of related objects
* [#8274](https://github.com/netbox-community/netbox/issues/8274) - Enable associating a custom link with multiple object types
* [#8485](https://github.com/netbox-community/netbox/issues/8485) - Enable journaling for all organizational models
* [#8853](https://github.com/netbox-community/netbox/issues/8853) - Introduce the `ALLOW_TOKEN_RETRIEVAL` config parameter to restrict the display of API tokens
* [#9249](https://github.com/netbox-community/netbox/issues/9249) - Device and virtual machine names are no longer case-sensitive
* [#9478](https://github.com/netbox-community/netbox/issues/9478) - Add `link_peers` field to GraphQL types for cabled objects
* [#9654](https://github.com/netbox-community/netbox/issues/9654) - Add `weight` field to racks, device types, and module types
* [#9817](https://github.com/netbox-community/netbox/issues/9817) - Add `assigned_object` field to GraphQL type for IP addresses and L2VPN terminations
* [#9832](https://github.com/netbox-community/netbox/issues/9832) - Add `mounting_depth` field to rack model
* [#9892](https://github.com/netbox-community/netbox/issues/9892) - Add optional `name` field for FHRP groups
* [#10052](https://github.com/netbox-community/netbox/issues/10052) - The `cf` attribute now returns deserialized custom field data
* [#10348](https://github.com/netbox-community/netbox/issues/10348) - Add decimal custom field type
* [#10556](https://github.com/netbox-community/netbox/issues/10556) - Include a `display` field in all GraphQL object types
* [#10595](https://github.com/netbox-community/netbox/issues/10595) - Add GraphQL relationships for additional generic foreign key fields
* [#10698](https://github.com/netbox-community/netbox/issues/10698) - Omit app label from content type in table columns
* [#10710](https://github.com/netbox-community/netbox/issues/10710) - Add `status` field to WirelessLAN
* [#10761](https://github.com/netbox-community/netbox/issues/10761) - Enable associating an export template with multiple object types
* [#10781](https://github.com/netbox-community/netbox/issues/10781) - Add support for Python v3.11

### Plugins API

* [#8927](https://github.com/netbox-community/netbox/issues/8927) - Enable inclusion of plugin models in global search via `SearchIndex`
* [#9071](https://github.com/netbox-community/netbox/issues/9071) - Introduce `PluginMenu` for top-level plugin navigation menus
* [#9072](https://github.com/netbox-community/netbox/issues/9072) - Enable registration of tabbed plugin views for core NetBox models
* [#9880](https://github.com/netbox-community/netbox/issues/9880) - Introduce `django_apps` plugin configuration parameter
* [#9887](https://github.com/netbox-community/netbox/issues/9887) - Inspect `docs_url` property to determine link to model documentation
* [#10314](https://github.com/netbox-community/netbox/issues/10314) - Move `clone()` method from NetBoxModel to CloningMixin
* [#10543](https://github.com/netbox-community/netbox/issues/10543) - Introduce `get_plugin_config()` utility function
* [#10739](https://github.com/netbox-community/netbox/issues/10739) - Introduce `get_queryset()` method on generic views

### Other Changes

* [#9045](https://github.com/netbox-community/netbox/issues/9045) - Remove legacy ASN field from provider model
* [#9046](https://github.com/netbox-community/netbox/issues/9046) - Remove legacy contact fields from provider model
* [#10358](https://github.com/netbox-community/netbox/issues/10358) - Raise minimum required PostgreSQL version from 10 to 11
* [#10697](https://github.com/netbox-community/netbox/issues/10697) - Move application registry into core app
* [#10699](https://github.com/netbox-community/netbox/issues/10699) - Remove custom `import_object()` function
* [#10816](https://github.com/netbox-community/netbox/issues/10816) - Pass the current request when instantiating a FilterSet within UI views
* [#10820](https://github.com/netbox-community/netbox/issues/10820) - Switch timezone library from pytz to zoneinfo
* [#10821](https://github.com/netbox-community/netbox/issues/10821) - Enable data localization

### REST API Changes

* circuits.provider
    * Removed the `asn`, `noc_contact`, `admin_contact`, and `portal_url` fields
    * Added a `description` field
* dcim.Cable
    * Added `description` and `comments` fields
* dcim.Device
    * Added a `description` field
* dcim.DeviceType
    * Added a `description` field
    * Added optional `weight` and `weight_unit` fields
* dcim.Module
    * Added a `description` field
* dcim.ModuleType
    * Added a `description` field
    * Added optional `weight` and `weight_unit` fields
* dcim.PowerFeed
    * Added a `description` field
* dcim.PowerPanel
    * Added `description` and `comments` fields
* dcim.Rack
    * Added a `description` field
    * Added optional `weight` and `weight_unit` fields
* dcim.RackReservation
    * Added a `comments` field
* dcim.VirtualChassis
    * Added `description` and `comments` fields
* extras.CustomLink
    * Renamed `content_type` field to `content_types`
* extras.ExportTemplate
    * Renamed `content_type` field to `content_types`
* ipam.Aggregate
    * Added a `comments` field
* ipam.ASN
    * Added a `comments` field
* ipam.FHRPGroup
    * Added a `comments` field
    * Added optional `name` field
* ipam.IPAddress
    * Added a `comments` field
* ipam.IPRange
    * Added a `comments` field
* ipam.L2VPN
    * Added a `comments` field
* ipam.Prefix
    * Added a `comments` field
* ipam.RouteTarget
    * Added a `comments` field
* ipam.Service
    * Added a `comments` field
* ipam.ServiceTemplate
    * Added a `comments` field
* ipam.VLAN
    * Added a `comments` field
* ipam.VRF
    * Added a `comments` field
* tenancy.Contact
    * Added a `description` field
* virtualization.Cluster
    * Added a `description` field
* virtualization.VirtualMachine
    * Added a `description` field
* wireless.WirelessLAN
    * Added a required `status` choice field
    * Added a `comments` field
* wireless.WirelessLink
    * Added a `comments` field

### GraphQL API Changes

* All object types now include a `display` field
* All cabled object types now include a `link_peers` field
* Add a `contacts` relationship for all relevant models
* dcim.Cable
    * Add A/B terminations fields
* dcim.CableTermination
    * Add `termination` field
* dcim.InventoryItem
    * Add `component` field
* dcim.InventoryItemTemplate
    * Add `component` field
* dcim.Rack
    * Add `mounting_depth` field
* ipam.FHRPGroupAssignment
    * Add `interface` field
* ipam.IPAddress
    * Add `assigned_object` field
* ipam.L2VPNTermination
    * Add `assigned_object` field
* ipam.VLANGroupType
    * Add `scope` field