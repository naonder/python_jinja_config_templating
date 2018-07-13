#!/usr/bin/env python3
# Templating for BGP
# To be imported into core or router base script

import jinja2
import yaml


def bgp():
    config_file = \
        open('C:/path/to/templating_base/configs/'
             'templating_bgp_config.txt', 'w')

    config_template = 'templating_bgp_template.j2'
    config_vars = \
        'C:/path/to/templating_base/yaml_variables/' \
        'templating_bgp_variables.yaml'

    # Load yaml data and jinja2 template. From that write to the config file which will be pushed to a device
    config_data = yaml.load(open(config_vars))
    env = jinja2.Environment(loader=jinja2.FileSystemLoader
    ('C:/path/to/templating_base/jinja_templates'),
                             trim_blocks=True,
                             lstrip_blocks=True)
    template = env.get_template(config_template)
    config_file.write(template.render(config_data))
    print(config_data)
    config_file.close()


if __name__ == '__main__':
    bgp()
