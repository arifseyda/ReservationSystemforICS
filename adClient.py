import rpyc
import datetime
import veritabanı


ad_server_ip = "192.168.100.46"
ad_bot_port = 19961
domain_controller = "DC=siberlab, DC=local"
users_ou = 'OU=Siberlab, {}'.format(domain_controller)


def send_command(command):
    try:
        connection = rpyc.connect('192.168.100.46', 19961)
        connection.root.run_command(command)
    except Exception as Err:
        print('Error in send command', str(Err))


def create_user(username, employee_id, display_name,  active=False):
    """
    Create New user in AD
    :param username:
    :param employee_id:
    :param display_name:
    :param active:
    :return:
    """
    if active:
        disabled = 'no'
    else:
        disabled = 'yes'

    description = "Rezervasyon Sistemindeki veritabanı yardımıyla oluşturulmuştur  {}".format(datetime.datetime.now())
    default_password = 'DefaultP@55w0rD'

    dn = '"CN={},{}"'.format(username, users_ou)

    command = 'dsadd user ' \
              '{} ' \
              '-samid "{}" ' \
              '-upn "{}" ' \
              '-display "{}" ' \
              '-empid "{}" ' \
              '-desc "{}" ' \
              '-disabled {} ' \
              '-pwd {} ' \
              '-pwdneverexpires yes ' \
              '-mustchpwd yes ' \
              '-acctexpires never ' \
              ''.format(
                dn,
                username,
                username,
                display_name,
                employee_id,
                description,
                disabled,
                default_password,
                )
    send_command(command)
    print(command)

def manage_user(username, mode):
    """
    This function can manage active directory users
    :param username:
    :param mode:
    :return:
    """
    dn = 'CN={},{}'.format(username, users_ou)
    cmd = ''
    if mode == 'disable':
        cmd = 'dsmod user {} -disabled yes'.format(dn)
    elif mode == 'enable':
        cmd = 'dsmod user {} -disabled no'.format(dn)
    elif mode == 'delete':
        cmd = 'dsrm -noprompt "cn={},{}"'.format(username, users_ou)
    send_command(cmd)
    print(cmd)

def user_password_change(username, new_password):
    """
    This function can change active directory password
    :param new_password:
    :param username:
    :return:
    """
    dn = 'CN={},{}'.format(username, users_ou)
    cmd = 'dsmod user "{}" -pwd {}'.format(dn, new_password)
    send_command(cmd)
    print(cmd)

def manage_logon_hours(username, passwd, day, start_time, end_time):
    cmd = 'net user "{}" "{}" /time:"{}","{}"-"{}"'.format(username,passwd,day,start_time,end_time)
    send_command(cmd)
    print(cmd)

def disable_logon_hours(username,passwd):
    cmd = 'net user "{}" "{}" /time:'.format(username, passwd)
    send_command(cmd)
    print(cmd)

for i in veritabanı.array_resrvasyon:
    if i[6] == 0 and i[7] == 0:
        create_user('{}'.format(i[1] + "_power"), 'siberlab','{}'.format(i[2]),active=True)
        user_password_change('{}'.format(i[1] + "_power"), '{}'.format(i[8]))
        manage_logon_hours('{}'.format(i[1] + "_power"), '{}'.format(i[8]), '{}'.format(i[9]), '{}'.format(i[4]), '{}'.format(i[5]))
        if i[10] < veritabanı.tarih:
            disable_logon_hours('{}'.format(i[1] + "_power"), '{}'.format(i[8]))
    if i[6] == 1 and i[7] == 0:
        create_user('{}'.format(i[1] + "_water"), 'siberlab','{}'.format(i[2]),active=True)
        user_password_change('{}'.format(i[1] + "_water"), '{}'.format(i[8]))
        manage_logon_hours('{}'.format(i[1] + "_water"), '{}'.format(i[8]), '{}'.format(i[9]), '{}'.format(i[4]), '{}'.format(i[5]))
        if i[10] < veritabanı.tarih:
            disable_logon_hours('{}'.format(i[1] + "_water"), '{}'.format(i[8]))


    #manage_user("{}".format(i[1]), mode='delete')

