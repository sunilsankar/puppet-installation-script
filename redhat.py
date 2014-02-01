#!/usr/bin/env python

try:
    import platform
    import os
    from subprocess import STDOUT, check_call
    import puppet_master_conf as pmc
    import puppet_agent_conf as pac

except Exception as e :
    print "Error : ", e

def set_repo():
    try:
        check_call(["wget", "https://yum.puppetlabs.com/el/6/products/x86_64/puppetlabs-release-6-7.noarch.rpm"])
        print "Download the puppetlabs rpm."
        check_call(["rpm", "-ivh", "puppetlabs-release-6-7.noarch.rpm"])
        print "Install the puppetlabs repo."
    except Exception as set_repo_e:
        print "Error while installing puppetlabs repository."
        print "More details : " , set_repo_e


def yum_update():
    try:
        print "Updating repo list. Please wait ..."
        check_call(['yum', 'list'], stdout=open(os.devnull, 'wb'))
        print "Update yum repository."
    except Exception as yum_update_e:
        print "Error while updating the repository."
        print "More details : " , yum_update_e
    

def yum_install_master():
    try:
        check_call(['yum', 'install', 'puppet-server' ,'-y'], stderr=STDOUT) 
        print "Installed puppet master/server via yum"
    except Exception as master_install_e:
        print "Error while installing puppet master/server via yum."
        print "More details : " , master_install_e

def yum_install_agent():
    try:
        check_call(['yum', 'install', 'puppet', '-y'], stderr=STDOUT)
        print "Installed puppet agent via yum"
    except Exception as agent_install_e:
        print "Error while installing puppet agent via yum."
        print "More details : " , agent_install_e


def restart_master():
    try:
        print "Restarting puppet master ... "
        check_call(['service', 'puppetmaster', 'restart'], stderr=STDOUT)
    except Exception as master_restart_e:
        print "Error while restarting puppet master."
        print "More details : " , master_restart_e

def restart_agent():
    try:
        print "Restarting puppet agent ... "
        check_call(['service', 'puppet', 'restart'], stderr=STDOUT)
    except Exception as agent_restart_e:
        print "Error while restarting puppet agent."
        print "More details : " , agent_restart_e


def configure_puppet_master(master_ip,domain,port,agent):
    pmc.set_host_name(domain=domain, hostname='puppetmaster')
    pmc.add_etc_hosts(domain=domain, master_ip=master_ip)
    set_repo()
    yum_update()
    yum_install_master()
    pmc.config_puppetmaster_default(port=port, daemon_opts="--ssl_client_header=HTTP_X_SSL_SUBJECT")
    pmc.config_puppet_conf(domain=domain)
    #pmc.config_fileserver_conf(domain=domain)
    #pmc.config_auth_conf(domain=domain)
    pmc.config_autosign_conf(domain=domain)
    restart_master()

def configure_puppet_agent(master_ip,domain,hostname,port,agent='agent'):
    pac.set_host_name(domain=domain,hostname=hostname)
    pac.add_etc_hosts(master_ip=master_ip,domain=domain,hostname=hostname)
    set_repo()
    yum_update()
    yum_install_agent()
    pac.config_puppetagent_default()
    pac.config_puppet_conf(domain=domain)
    restart_agent()
