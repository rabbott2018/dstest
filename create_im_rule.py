from __future__ import print_function
import sys, warnings
import deepsecurity
from deepsecurity.rest import ApiException
from pprint import pprint
from deepsecurity.models import integrity_monitoring_rule
from time import sleep

f = open("imrule.txt","r")
lines = f.readlines()
print (lines)
print (len(lines))
f.close()
for n, val in enumerate(lines):
   globals()["var%d"%n] = val

host,hostname = var0.split("=")
print (hostname.rstrip())
imrule, rulename = var1.split("=")
print (rulename.rstrip())
include, includedir = var2.split("=")
print (includedir.rstrip())
exclude, excludedir = var3.split("=")
print (excludedir.rstrip())

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
integrity_monitoring_rule = deepsecurity.IntegrityMonitoringRule()
integrity_monitoring_rule.name=rulename.rstrip()
integrity_monitoring_rule.file_base_directory=includedir.rstrip()
integrity_monitoring_rule.file_excluded_values=excludedir.rstrip()
integrity_monitoring_rule.template="file"

try:
    api_response = api_instance.create_integrity_monitoring_rule(api_version, integrity_monitoring_rule=integrity_monitoring_rule)
    pprint(api_response)
except ApiException as e:
    print("An exception occurred when calling IntegrityMonitoringRulesApi.create_integrity_monitoring_rule: %s\n" % e)


