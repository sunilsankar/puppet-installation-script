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
def get_package_manager(os=False):

    if os:
        dist = os;
    else:
        dist = platform.dist()[0].lower()
    print "Distribution is : ", dist
    return{
        'ubuntu': '1', 
        'debian': '1',
        'centos': '2',
        'redhat': '2',
        'fedora': '2',
        'suse'  : '3',
    }.get(dist,0)


def install_puppet(pkg, master_ip, domain, hostname='node', port='8140', agent='agent'):
## For debian
    if (pkg == '1' and agent == 'master'):
        print "Detected OS as Ubuntu and going to install puppet master"
        ubuntu.configure_puppet_master(master_ip,domain,port,agent)
    elif (pkg == '1' and agent == 'agent'):
        print "Detected OS as Ubuntu and going to install puppet agent"
        ubuntu.configure_puppet_agent(master_ip,domain,hostname,port,agent)
## For RedHat
    elif (pkg == '2' and agent == 'master'):
        print "Detected OS as Redhat and going to install puppet master"
        redhat.configure_puppet_master(master_ip,domain,port,agent)
    elif (pkg == '2' and agent == 'agent'):
        print "Detected OS as RedHat and going to install puppet agent"
        redhat.configure_puppet_agent(master_ip,domain,hostname,port,agent)
    elif (pkg > 2):
        print "Curently this only supports for debian and RedHat base operating systems only."
        exit(0)
    else:
        print "Error detecting the operating system : " + str(pkg) + " or detecting agent : " + str(agent)
        exit(1)
