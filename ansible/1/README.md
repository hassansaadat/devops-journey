# Ping pong

## Simple ping servers
```bash
ansible all -i hosts_v1 -m ping
```

group servers
```bash
ansible droplet -i hosts_v2 -m ping
```

use variables
```bash
ansible droplet -i hosts_v3 -m ping
```

## Host key checking
- solution 1: ssh-copy-id for each server
- solution 2: disable it!

Disable host key checking in one of this files:
- /etc/ansible/ansible.cfg
- ~/.ansible.cfg
- ansible.cfg

I've added one more host and removed previous two known hosts! then:
```bash
 ansible droplet -i hosts_v4 -m ping
```

it works!
