from psutil import net_if_addrs

trop_dinfos = net_if_addrs()
wifi = trop_dinfos['Wi-Fi'].pop(1)
address_wifi = wifi.address
mask_wifi = wifi.netmask

binary_address = ''
for byte in mask_wifi.split("."):
    binary_byte = bin(int(byte))
    binary_address += binary_byte

cidr = binary_address.count("1")

print(address_wifi)
print(f"{mask_wifi}/{cidr}")
print(2**(32-cidr))

