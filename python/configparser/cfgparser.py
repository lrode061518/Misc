#!/usr/bin/env python
import os

try:
    import configparser as cfgparser
    from io import StringIO as strio
except ImportError:
    import ConfigParser as cfgparser
    import StringIO as strio

CONF_PATH = 'test.conf'

# override default value if TPS provision.conf exists
if os.path.exists(CONF_PATH):
    try:
        with open(CONF_PATH) as provision:
            cfg = strio.StringIO()
            cfg.write('[dummy_section]\n') # create dummy section, it's necessary for configparser.
            cfg.write(provision.read().replace('%', '%%'))
            cfg.seek(0, os.SEEK_SET)

            cfgp = cfgparser.ConfigParser()
            cfgp.readfp(cfg)

            r = dict(cfgp.items('dummy_section'))
            value1 = r['v1']
            value2 = r['v2']

            print(r)

    except Exception as e:
        print("failed to read '{}'".format(CONF_PATH))
        print(e)
