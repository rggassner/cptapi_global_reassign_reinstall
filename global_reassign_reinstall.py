#!/usr/bin/python3
# -*- coding: utf-8 -*-
import OpenSSL
from cptapi import Cptapi
from my_config import *
domain_name='Global'
domain=Cptapi(user,password,url,domain_name,api_wait_time=api_wait_time,read_only=False,page_size=page_size,publish_wait_time=publish_wait_time)
try:
    domain.publish()
    domain.reassign_all()
    domain.reinstall_all_policies()
    domain.logout()
except OpenSSL.SSL.SysCallError as e:
    logging.error(e)
    logging.error("SSL connection error.")
    logout()
except requests.exceptions.SSLError as e:
    logging.error(e)
    logout()
except requests.exceptions.ConnectionError as e:
    logging.error(e)
    logging.error("Connection error.")
except ValueError as err:
    print(err.args)
