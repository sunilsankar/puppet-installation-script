#!/usr/bin/env python

try:
    import sys
    import system 

except Exception as e :
    print "Error : ", e


def get_confirmation(master_ip, domain, hostname):
    
    print "====================================================================="
    print ""
    print "Puppet Masters IP address : ", master_ip
    print "Domain of the deployment  : ", domain
    print "FQDN of this node         :  " + hostname + "." + domain
    print ""
    print "Please check your input and confirm by pressing [Enter] to continue."
    print "or press [Ctrl] + [c] to stop the installationan exit."
    print "====================================================================="
    try:
        print raw_input()
    except KeyboardInterrupt as e:
        print "Pressed [Ctrl] + [c]."
        print "Script will now exit ..."
        sys.exit(0) 


def get_user_input():
    
    print "To install,"
    print "1.) Puppet Master."
    print "2.) Puppet Agent."
    agent = raw_input("Select only 1 or 2 : ").strip()

    if agent == "1":
        print ""
        print "You select option 1 to install puppet master."
        print ""
        master_ip = raw_input("Give the IP address of puppet master : ")
        if not master_ip:
            sys.exit(1)
        domain =  raw_input("Give the domain of the deployment [apps.wso2.com] : ")
        if not domain:
            domain="apps.wso2.com"
        return agent,master_ip,domain,"puppetmaster"
    elif agent == "2":
        print ""
        print "You select option 2 to install puppet agent."
        print ""
        master_ip = raw_input("Give the IP address of puppet master : ")
        if not master_ip:
            sys.exit(1)
        domain =  raw_input("Give the domain of the deployment [apps.wso2.com] : ")
        if not domain:
            domain="apps.wso2.com"
        hostname = raw_input("Give the hostname of the node [node1] : ")
        if not hostname:
            hostname="node1"
        return agent.strip(),master_ip.strip(),domain.strip(),hostname.strip()
    else:
        print "The option you select is incorrect."
        get_user_input()





if system.check_user():
    print "This is a puppet installation script."
    print ""
    agent, master_ip, domain, hostname = get_user_input()
    get_confirmation(master_ip, domain, hostname)
    pkg = system.get_package_manager()
    if not pkg:
        print "Unidentified package manager."
        exit(1)
    else:
        system.install_puppet(pkg, master_ip=master_ip, domain=domain, hostname=hostname, agent=agent)
        pass
else:
    print "Need root access."	
    print "Run the script as \'root\' or with \'sudo\' permissions. "
