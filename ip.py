import netifaces as ni
ip = ni.ifaddresses('enp2s0')[ni.AF_INET][0]['addr']
print(ip)  # should print "192.168.100.37"
