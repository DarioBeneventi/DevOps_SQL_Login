#Imports the unittest module (gives us acces to the unittest pre-written functions)
import unittest
#Imports our previous script and declare it to the variable script
import ipv4_subnetmasks_prefixes as script


class test_ipaddresses(unittest.TestCase):
    
    #Test if the submask corresponds to the given binary notation
    def test_get_network_bits(self):
        subnetmask = '255.255.255.240'
        bits = '1111 1111 1111 1111 1111 1111 1111 0000'
        self.assertEqual(script.get_network_bits(subnetmask), bits)

    #Test if the subnet mask corresponds to the given prefix
    def test_get_prefix(self):
        subnetmask = '255.255.255.240'
        prefix = '/28'
        self.assertEqual(script.get_net_prefix(subnetmask), prefix)

    #Test if the prefix corresponds to the given submask (other way around then the previous method/function)
    def test_netmask(self):
        subnetmask = '255.255.255.240'
        prefix = '/28'
        self.assertEqual(script.get_netmask(prefix), subnetmask)

    #Test if the total number of ip addresses corresponds to the given prefix
    def test_get_number_ip_addresses(self):
        prefix = '/28'
        addresses = 16
        self.assertEqual(script.get_number_ip_addresses(prefix), addresses)
    
    #Test if the usable addresses (by hosts) correspond to the given prefix
    def test_get_ip_hosts(self):
        prefix = '/28'
        host_addresses = 14
        self.assertEqual(script.get_number_ip_hosts(prefix), host_addresses)

#Execute the unittest
if __name__ == '__main__':
    unittest.main()








