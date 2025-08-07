# EasyNetBox

A simple client for NetBox supporting sync and async access patterns.

## Installation

```bash
pip install easynetbox
```

## Usage

`easynetbox` provides both synchronous and asynchronous clients for interacting with NetBox APIs.

### Basic Setup

```python
import easynetbox

# Synchronous client
nb = easynetbox.SyncClient("https://netbox.example.com", "your-api-token")

# Asynchronous client
async with easynetbox.AsyncClient("https://netbox.example.com", "your-api-token") as nb:
    # your async code here
    pass
```

### Accessing Resources

Resources are accessed via NetBox apps (dcim, ipam, tenancy, etc.) and then by resource type:

```python
# Access resources via app.resource pattern
devices = nb.dcim.devices
sites = nb.dcim.sites
tenants = nb.tenancy.tenants
```

### Listing Resources

```python
# List all devices
async for device in nb.dcim.devices.list():
    print(device.name)

# List with filters
async for device in nb.dcim.devices.list(site_id=1, role="server"):
    print(device.name, device.serial)
```

### Getting Single Resources

```python
# Get first matching resource
site = await nb.dcim.sites.first(slug="datacenter1")
tenant = await nb.tenancy.tenants.first(name="Company A")

# Get resource by ID
device = await nb.dcim.devices.fetch(123)
```

### Creating Resources

```python
# Create a new site
site_data = {
    "name": "New Datacenter",
    "slug": "new-dc",
    "status": "active"
}
new_site = await nb.dcim.sites.create(site_data)
```

### Updating Resources

```python
# Update a resource
updated_device = await nb.dcim.devices.patch(device_id, {"status": "offline"})

# Replace a resource entirely
replaced_device = await nb.dcim.devices.replace(device_id, complete_device_data)
```

### Complete Example

```python
import asyncio
import easynetbox

async def main():
    netbox_url = "https://netbox.example.com"
    netbox_token = "your-api-token-here"
    
    async with easynetbox.AsyncClient(netbox_url, netbox_token) as nb:
        # Find a tenant
        tenant = await nb.tenancy.tenants.first(slug="company-a")
        
        # Find a site
        site = await nb.dcim.sites.first(slug="datacenter1")
        
        # Find a device role
        role = await nb.dcim.device_roles.first(slug="server")
        
        # List devices matching criteria
        async for device in nb.dcim.devices.list(
            tenant_id=tenant.id,
            site_id=site.id,
            role_id=role.id,
        ):
            print(f"{device.name}: {device.serial} ({device.status.value})")

if __name__ == "__main__":
    asyncio.run(main())
```

### Synchronous Usage

The same patterns work with the synchronous client:

```python
import easynetbox

nb = easynetbox.SyncClient("https://netbox.example.com", "your-api-token")

# List devices synchronously
for device in nb.dcim.devices.list(site_id=1):
    print(device.name)

# Get single resource
site = nb.dcim.sites.first(slug="datacenter1")
```

## Development

```bash
pip install -e ".[dev]"
```