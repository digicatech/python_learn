import socket, struct

def ip2long(ip):
    """
    Convert an IP string to long
    """
    packedIP = socket.inet_aton(ip)
    return struct.unpack("!L", packedIP)[0]


ipno = socket.inet_ntoa(struct.pack('!L', 2130706433))
print(ipno)

print(ip2long("212.175.39.254"))