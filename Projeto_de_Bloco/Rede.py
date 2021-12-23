import psutil

dic_interfaces = psutil.net_if_addrs()
print(dic_interfaces['Ethernet'][0].address)