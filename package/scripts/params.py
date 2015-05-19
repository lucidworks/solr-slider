#!/usr/bin/env python
from resource_management import *

# server configurations
config = Script.get_config()

app_root = config['configurations']['global']['app_root']
java64_home = config['hostLevelParams']['java_home']
app_user = config['configurations']['global']['app_user']
port = config['configurations']['global']['listen_port']
zk_host = config['configurations']['global']['zk_host']
zk_timeout = config['configurations']['global']['zk_timeout']
gc_tune = config['configurations']['global']['gc_tune']
xmx_val = config['configurations']['global']['xmx_val']
xms_val = config['configurations']['global']['xms_val']
if not xms_val:
    xms_val = xmx_val
pid_file = config['configurations']['global']['pid_file']
server_module = config['configurations']['global']['server_module']
stop_port = int(port)-1000
stop_key = config['configurations']['global']['stop_key']
solr_opts = config['configurations']['global']['solr_opts']
solr_host = config['configurations']['global']['solr_host']