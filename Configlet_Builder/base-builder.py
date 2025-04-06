from cvplibrary import CVPGlobalVariables, GlobalVariableNames, Form



# Get this devices Serial


serial = CVPGlobalVariables.getValue( GlobalVariableNames.CVP_SERIAL )
mask = '24'
ServiceRouting = True

#Create the IP address from the serial number


if serial == 'leaf1': # serial number = Device ID in devices tab... 
 IPaddress = '192.168.0.21'
 hostname = 'leaf1'


elif serial == 'leaf2':
 IPaddress = '192.168.0.22'
 hostname = 'leaf2'


elif serial == 'leaf3':
 IPaddress = '192.168.0.23'
 hostname = 'leaf3'


elif serial == 'leaf4':
 IPaddress = '192.168.0.24'
 hostname = 'leaf4'

elif serial == 'spine1':
 IPaddress = '192.168.0.11'
 hostname = 'spine1'

elif serial == 'spine2':
 IPaddress = '192.168.0.12'
 hostname = 'spine2'

elif serial == 'spine3':
 IPaddress = '192.168.0.13'
 hostname = 'spine3'

elif serial == 'spine4':
 IPaddress = '192.168.0.14'
 hostname = 'spine4'

elif serial == 'borderleaf1':
 IPaddress = '192.168.0.25'
 hostname = 'borderleaf1'

elif serial == 'borderleaf2':
 IPaddress = '192.168.0.26'
 hostname = 'borderleaf2'

elif serial == 'host1':
 IPaddress = '192.168.0.51'
 ServiceRouting = False
 hostname = 'host1'


elif serial == 'host2':
 IPaddress = '192.168.0.52'
 ServiceRouting = False
 hostname = 'host2'


# Generate and print config - Ignore the service routing command if not needed
print 'hostname %s' % hostname
print '!'
print 'interface Management 1'
print '  ip address %s/%s' % ( IPaddress, mask )
print '  no lldp transmit'
print '  no lldp receive'
print '!'
if ServiceRouting:
 print 'service routing protocols model multi-agent'
 print '!'
print 'dns domain arista.lab'
print '!'
print 'ip route 0.0.0.0/0 192.168.0.1'
print '!'
print 'ip routing'
print '!'
print 'management api http-commands'
print '  no shutdown'
print '  protocol http'
print '!'