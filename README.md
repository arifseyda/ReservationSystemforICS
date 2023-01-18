# ReservationSystemforICS

Users first make reservations through the site to use ICS products.Reservation users get remote access to industrial control system by using ssl vpn feature in firewall.
The website is developed with Django Framework. Every configuration in firewall and user creation in active directory is enhanced with python netmiko and rpyc library.

A registered person would like to be able to use the water or electricity infrastructure at Sakarya University National Test Bed Center remotely. You can see the date and the free time of that date as in the image below.

![3](https://user-images.githubusercontent.com/47140243/213259059-509be669-060f-4420-9c09-7276628f3586.PNG)

For example, in order to use the electrical systems between 19.01.2023 and 12.00-15.00, a reservation is made as in the image below.

![4](https://user-images.githubusercontent.com/47140243/213259914-aa3ac7bd-2872-4708-96ea-119cbc3b53af.PNG)

After making a reservation to the electrical system, it is seen in the image below that the 12.00-15.00 interval is full in our calendar. Rules have been added to ensure that no other person can book on this date and this time.

![5](https://user-images.githubusercontent.com/47140243/213260604-4354c372-76d2-424c-ac89-ac57b3b3f5c2.PNG)

Active Directory user is created by using this username, password, date and time information. The rules have been written that this user can only use the Test Bed Center remotely on the date and time he made the reservation. It is developed with the Python rpyc library.

LDAP users are added to Fortinet Firewall. Every rule required for remote connection with SSL VPN has been developed in Python. Python netmiko library is used, which provides ssh connection to Fortinet Firewall.
