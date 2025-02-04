# import yaml
# import pyeapi


# file = open('vlans.yml', 'r')
# vlan_dict = yaml.safe_load(file)

# pyeapi.load_config('eapi.conf')

# connect = pyeapi.connect_to('leaf1')
# vlan_api = connect.api('vlans')
# vlan_api.create('10')
# vlan_api.set_name('DMZ')
# ssh 

# """
# import yaml
# import pyeapi


# file = open('vlans.yml', 'r')

# pyeapi.load_config('eapi.conf')
# vlan_dict = yaml.safe_load(file)

# for switch in vlan_dict['switches']:
#     print(f"Connecting to {switch}")
#     connect = pyeapi.connect_to(switch)
#     vlan_api = connect.api('vlans')
#     for vlan in vlan_dict['vlans']:
#         vlan_id = vlan['id']
#         vlan_name = vlan['name']
#         print(f"Adding VLAN {vlan_id} to {switch}")
#         vlan_api.create(vlan_id)
#         vlan_api.set_name(vlan_id, vlan_name)

# """

import pyeapi
conn = pyeapi.connect(
    host='192.168.0.21',  # Change this to your leaf1 IP
    username='arista',
    password='aristaqi7h',
    transport='https'
)

print(conn)  # This should print an `HttpsEapiConnection` object

node = pyeapi.client.Node(conn)
print(node.run_commands(['show version']))  # Check if commands work
