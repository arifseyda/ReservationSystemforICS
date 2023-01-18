from netmiko import ConnectHandler
import veritabanı

fortinet = {
    "host": "SAUTYM_ENERGYIT",
    "device_type": "fortinet",
    "ip": "192.168.1.99",
    "username": "ozcelik",
    "password": "Smntc15*s"

}

net_connect = ConnectHandler(**fortinet)


def create_ldap_user():
    user_array = []
    for i in veritabanı.array_resrvasyon:
        if i[6] == 0 and i[7] == 0:
            user_array.append(i[1])

    user_array = list(dict.fromkeys((user_array)))

    for i in range(0,len(user_array)):
        config_commands = ["config user local",
                           "edit '{}'".format(user_array[i]),
                           "set type ldap",
                           'set ldap-server SiberLab',
                           "end"]
        output = net_connect.send_config_set(config_commands)
        print(output)


def create_user_group():
    user_array = []
    for i in veritabanı.array_resrvasyon:
        if i[6] == 0 and i[7] == 0:
            user_array.append(i[1])

    user_array = list(dict.fromkeys((user_array)))

    elemanlar = ""
    for i in range(0, len(user_array)):
        elemanlar += user_array[i]
        if i != len(user_array) - 1:
            elemanlar += " "


    config_commands = ["config user group",
                        "edit ssl_vpn_group",
                        "set group-type firewall",
                        "set member {}".format(elemanlar),
                        "end"]
    output = net_connect.send_config_set(config_commands)
    print(output)


def create_addresses():
    #ip adressleri atama yapıcalak şuan önemi yok diye hepsi aynı ip
    user_array = []
    for i in veritabanı.array_resrvasyon:
        if i[6] == 0 and i[7] == 0:
            user_array.append(i[1])

    user_array = list(dict.fromkeys((user_array)))

    sayi = 201
    for i in range(0,len(user_array)):
        config_commands = ["config firewall address",
                           "edit SSLVPN_Tunnel_{}".format(user_array[i]),
                           "set type ipmask",
                           "set subnet 10.212.134.{}/32".format(sayi),
                           "end"]
        sayi = sayi + 1
        output = net_connect.send_config_set(config_commands)
        print(output)


def create_sslvpn_portal():
    user_array = []
    for i in veritabanı.array_resrvasyon:
        if i[6] == 0 and i[7] == 0:
            user_array.append(i[1])

    user_array = list(dict.fromkeys((user_array)))

    for i in range(0, len(user_array)):
        config_commands = ["config vpn ssl web portal",
                           "edit SSLVPN_Portal_{}".format(user_array[i]),
                           "set tunnel-mode enable",
                           "set web-mode enable",
                           "set ip-pools SSLVPN_Tunnel_{}".format(user_array[i]),
                           "end"]
        output = net_connect.send_config_set(config_commands)
        print(output)


def create_ssl_vpn_Settings():
    ssl_vpn_tunnel = "SSLVPN_TUNNEL_ADDR1 "
    sayi = 8
    user_array = []
    for i in veritabanı.array_resrvasyon:
        if i[6] == 0 and i[7] == 0:
            user_array.append(i[1])

    user_array = list(dict.fromkeys((user_array)))

    for i in range(0, len(user_array)):
        ssl_vpn_tunnel += "SSLVPN_Tunnel_{}".format(user_array[i])
        if i != len(user_array) - 1:
            ssl_vpn_tunnel += " "


    for i in range(0, len(user_array)):
        config_commands = ["config vpn ssl settings",
                           "set tunnel-ip-pools {}".format(ssl_vpn_tunnel),
                           "config authentication-rule",
                           "edit {}".format(sayi),
                           "set groups ssl_vpn_group",
                           "set portal SSLVPN_Portal_{}".format(user_array[i]),
                           "next",
                           "end",
                           "end"]
        sayi = sayi + 1
        output = net_connect.send_config_set(config_commands)
        print(output)

def create_ip4_policy():
    user_array = []
    sayi = 143
    for i in veritabanı.array_resrvasyon:
        if i[6] == 0 and i[7] == 0:
            user_array.append(i[1])

    user_array = list(dict.fromkeys((user_array)))

    for i in range(0, len(user_array)):
        config_commands = ["config firewall policy",
                           "edit {}".format(sayi),
                           "set name SSLVPN_Policy_{}".format(user_array[i]),
                           "set srcintf ssl.root",
                           "set dstintf port10",
                           "set srcaddr SSLVPN_Tunnel_{}".format(user_array[i]),
                           "set dstaddr MANAGEMET_NETWORK",
                           "set action accept",
                           "set schedule always",
                           "set service ALL",
                           "set logtraffic all",
                           "set group ssl_vpn_group",
                           "next",
                           "end"]

        sayi = sayi + 1
        output = net_connect.send_config_set(config_commands)
        print(output)


if __name__ == '__main__':

    #create_ldap_user()
    #create_user_group()
    #create_addresses()
    #create_sslvpn_portal()
    #create_ssl_vpn_Settings()
    create_ip4_policy()
