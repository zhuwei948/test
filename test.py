import ipaddress

# 定义要排除的网段
exclude_nets = [ipaddress.ip_network('100.99.0.0/16'), ipaddress.ip_network('100.95.0.0/16')]

# 遍历IPv4地址空间
for network in ipaddress.IPv4Network('0.0.0.0/0').subnets():
    # 排除要排除的网段
    if network not in exclude_nets:
        print(network)