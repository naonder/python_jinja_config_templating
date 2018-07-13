#!/usr/bin/env python3
# Templating for core switches

import jinja2
import yaml
import templating_ospf_base
import templating_bgp_base
import templating_eigrp_base

while True:
    eigrp_routing_selection = input('\r\nWill you be using EIGRP:' '\r\n1 - yes' '\r\n2 - no' '\r\nInput selection: ')
    if eigrp_routing_selection == '2':
        break
    else:
        templating_eigrp_base.eigrp()
        break

while True:
    ospf_routing_selection = input('\r\nWill you be using OSPF:' '\r\n1 - yes' '\r\n2 - no' '\r\nInput selection: ')
    if ospf_routing_selection == '2':
        break
    else:
        templating_ospf_base.ospf()
        break

while True:
    bgp_routing_selection = input('\r\nWill you be using BGP:' '\r\n1 - yes' '\r\n2 - no' '\r\nInput selection: ')
    if bgp_routing_selection == '2':
        break
    else:
        templating_bgp_base.bgp()
        break

file_name = input('Input a file name to use: ')

config_file = \
    open('C:/path/to/templating_base/configs/'
         '{}.txt'.format(file_name), 'w')

config_template = 'templating_core_template.j2'
config_vars = \
    'C:/path/to/templating_base/yaml_variables/' \
    'templating_core_variables.yaml'

# Load yaml data and jinja2 template. From that write to the config file which will be pushed to a device
config_data = yaml.load(open(config_vars))
env = jinja2.Environment(loader=jinja2.FileSystemLoader
(['C:/path/to/templating_base/jinja_templates',
 'C:/path/to/templating_base/configs']),
                         trim_blocks=True,
                         lstrip_blocks=True)
template = env.get_template(config_template)
config_file.write(template.render(config_data))
print(config_data)
config_file.close()
