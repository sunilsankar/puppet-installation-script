#!/usr/bin/env python

try:
    import sys
    import system 

except Exception as e :
    print "Error : ", e


def get_user_input():
    
    print "To install,"
    print "1.) Puppet Master."
    print "2.) Puppet Agent."
    agent = raw_input("Select only 1 or 2 : ")

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
        return agent,master_ip,domain,hostname
    else:
        print "The option you select is incorrect."
        get_user_input()





if system.check_user():
    print "This is a puppet installation script."
    print ""
    agent, master_ip, domain, hostname = get_user_input()
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
