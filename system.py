#!/usr/bin/env python

try:
    import platform
    import os
    import ubuntu

except Exception as e :
    print "Error : ", e


# Check user.
def check_user():
    if os.getuid(): 
        return 0
    else:
        return 1

# Detect OS.
def get_package_manager():

    dist = platform.dist()[0].lower()
    print "Distribution is : ", dist
    return{
        'ubuntu': 1, 
        'centos': 2,
    }.get(dist,0)


def install_puppet(pkg, master_ip, domain, hostname='node', port='8140', agent="2"):
    if (pkg == 1 and agent == '1'):
        print "Detected OS as Ubuntu and going to install puppet master"
        ubuntu.apt_update()
        ubuntu.apt_install_master()
        ubuntu.configure_puppet_master(master_ip,domain,port,agent)
    elif (pkg == 1 and agent == '2'):
        print "Detected OS as Ubuntu and going to install puppet agent"
        ubuntu.apt_update()
        ubuntu.apt_install_agent()
        ubuntu.configure_puppet_agent(master_ip,domain,hostname,port,agent)
