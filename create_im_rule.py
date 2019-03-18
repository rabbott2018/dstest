from __future__ import print_function
import sys, warnings
import deepsecurity
from deepsecurity.rest import ApiException
from pprint import pprint
from deepsecurity.models import integrity_monitoring_rule
from time import sleep

#f = open("imrule.txt","r")
#lines = f.readlines()
# print lines
#print len(lines)
#f.close()
#for n, val in enumerate(lines):
#   globals()["var%d"%n] = val

#host,hostname = var0.split("=")
#print hostname.rstrip()
#imrule, rulename = var1.split("=")
#print rulename.rstrip()
#include, includedir = var2.split("=")
#print includedir.rstrip()
#exclude, excludedir = var3.split("=")
#print excludedir.rstrip()

# Setup
if not sys.warnoptions:
    warnings.simplefilter("ignore")
configuration = deepsecurity.Configuration()
configuration.host = 'https://rickadsquic-dsmelb-17fdwfok283md-1362197788.us-east-1.elb.amazonaws.com/api'

# Authentication
configuration.api_key['api-secret-key'] = '3:JrbkU4dZBTxHaMJZBi80Tqksprv24+7nXDLwIEUlSmU='

# Initialization
# Set Any Required Values
api_instance = deepsecurity.IntegrityMonitoringRulesApi(deepsecurity.ApiClient(configuration))
api_version = 'v1'

try:
    api_response = api_instance.list_integrity_monitoring_rules(api_version)
    attrs = api_response._integrity_monitoring_rules
    ids = [len(attrs)]
    for x in attrs:
        print((getattr(x,"name")),(getattr(x,"id")))
        #pprint(getattr(x,"id"))
        #ids.append(getattr(x,"id"))
        #sleep(1)
    
    #print(len(attrs))
    #print(len(ids))
    #for y in ids:
    #    print(y)
    #    sleep(0.5)
    #i=29
    #pprint(getattr(attrs,attrs[i]))
    #pprint(len(attrs))
    
    #pprint(api_response)
    #integrity_monitoring_rule_id = 1;
    #api_response = api_instance.describe_integrity_monitoring_rule(integrity_monitoring_rule_id, api_version)
    #pprint(getattr(api_response, "id"))
    #pprint(api_response)
except ApiException as e:
    print("An exception occurred when calling IntegrityMonitoringRulesApi.list_integrity_monitoring_rules: %s\n" % e)
