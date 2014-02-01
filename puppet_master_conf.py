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
def add_etc_hosts(master_ip, domain, file_path='/etc/hosts'):

    try: 
        config = open(file_path,'w')
        config.write("# Added by the puppet installation script.\n")
        config.write("127.0.0.1 localhost\n")
        config.write(master_ip + " puppetmaster." + domain +" \n")
        config.close()
        print "Configured the /etc/hosts."
    except Exception as hosts_e:
        print "Error while configuring /etc/hosts."
        print "More details : " , hosts_e 


# Configure 'puppetmaster-default'
def config_puppetmaster_default(file_path='/etc/default/puppetmaster', daemon_opts="", servertype='webrick', masters='1', port='8140'):

    try: 
        config = open(file_path,'w')
        config.write("# Added by the puppet installation script.\n")
        config.write("START=yes\n")
        config.write("DAEMON_OPTS=\"" + daemon_opts + "\"\n")
        config.write("SERVERTYPE=" + servertype + "\n")
        config.write("PUPPETMASTERS=" + masters + "\n")
        config.write("PORT=" + port + "\n")
        config.close()
        print "Configured the puppet master default settings."
    except Exception as master_config_e:
        print "Error while configuring puppet master defaults."
        print "More details : " , master_config_e


# Configure 'puppet.conf'
def config_puppet_conf(domain, file_path='/etc/puppet/puppet.conf'):

    try:
        setserver = '2i server=puppetmaster.' + domain
        check_call(["sed", "-i", setserver, file_path ]) 
        print "Configured the puppet.conf settings."
    except Exception as agent_config_e:
        print "Error while configuring puppet.conf."
        print "More details : " , agent_config_e

def config_autosign_conf(domain,path='/etc/puppet/autosign.conf'):
    
    try:
        config = open(path,'w')
        config.write('*.' + domain + '\n')
        print "Configured the autosign.conf settings."
        config.close()
    except Exception as autosign_config_e:
        print "Error while  configuring autosign.conf"
        print "More details : " , autosign_config_e


