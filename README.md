puppet-installation-script
==========================

This script will install puppet master and puppet agents in an interactive way.

### Usage options:

#### Interactive mode installation

- Run script in interactive mode :

    ```
    sudo python puppet_install.py
    ```

#### Install using argument passing mode : 

- Install puppet agent : 

    ``` 
    sudo python puppet_install.py --agent master \
        --domain apps.wso2.com --master-ip 10.1.1.1 --os ubuntu
    ```

- Install puppet agent : 

    ```
    sudo python puppet_install.py --agent agent \
        --domain apps.wso2.com --master-ip 10.1.1.1 --hostname node01 --os ubuntu
    ```
