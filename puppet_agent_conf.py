#!/usr/bin/env python

from subprocess import STDOUT, check_call
import re

# Set the hostname. 
def set_host_name(domain,hostname):
    # set hostname
    fqdn = hostname + "." + domain
    hostname_file = open("/etc/hostname","w")
    hostname_file.write(fqdn + "\n")
    hostname_file.close()
    try:
        check_call(['hostname', fqdn ], stderr=STDOUT) 
    except Exception as hostnamec_e:
        print "Error while setting the hostname via command : ", fqdn
        print "More details : " , hostnamec_e
    print("Add hostname : " + fqdn)


# add entries to /etc/hosts
def add_etc_hosts(master_ip, domain, hostname, file_path='/etc/hosts'):

    try: 
        config = open(file_path,'w')
        config.write("# Added by the puppet installation script.\n")
        config.write("127.0.0.1 localhost\n")
        config.write("127.0.0.1 " + hostname + "." + domain + " \n")
        config.write(master_ip + " puppetmaster." + domain +" \n")
        config.close()
        print "Configured the /etc/hosts."
    except Exception as hosts_e:
        print "Error while configuring /etc/hosts."
        print "More details : " , hosts_e 


# Configure 'puppetagent-default'
def config_puppetagent_default(file_path='/etc/default/puppet', start='yes'):

    try: 
        config = open(file_path,'w')
        config.write("# Added by the puppet installation script.\n")
        config.write("START=" + start + "\n")
        config.close()
        print "Configured the puppet agent default settings."
    except Exception as agent_config_e:
        print "Error while configuring puppet agent defaults."
        print "More details : " , agent_config_e


# Configure 'puppet.conf'
def config_puppet_conf(domain, file_path='/etc/puppet/puppet.conf'):

    try:
        setserver = '2i server=puppetmaster.' + domain
        check_call(["sed", "-i", setserver, file_path ]) 
        print "Configured the puppet.conf settings."
    except Exception as agent_config_e:
        print "Error while configuring puppet.conf."
        print "More details : " , agent_config_e

