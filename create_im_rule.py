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
base, basedir = var2.split("=")
print (basedir.rstrip())
include, includefiles = var3.split("=")
print (includefiles.rstrip())
exclude, excludefiles = var4.split("=")
print (excludefiles.rstrip())

# Setup
if not sys.warnoptions:
    warnings.simplefilter("ignore")
configuration = deepsecurity.Configuration()
configuration.host = 'https://ec2-35-171-228-214.compute-1.amazonaws.com:4119/api'

# Authentication
configuration.api_key['api-secret-key'] = '6:ff9K3EtTWAh4qYUh2amGWNohOP6Pt2P+/PAg1hvKfsk='

# Initialization
# Set Any Required Values
api_instance = deepsecurity.IntegrityMonitoringRulesApi(deepsecurity.ApiClient(configuration))
api_version = 'v1'
integrity_monitoring_rule = deepsecurity.IntegrityMonitoringRule()
integrity_monitoring_rule.name=rulename.rstrip()
integrity_monitoring_rule.file_base_directory=basedir.rstrip()
integrity_monitoring_rule.file_included_values=includefiles.rstrip()
integrity_monitoring_rule.file_excluded_values=excludefiles.rstrip()
integrity_monitoring_rule.template="file"

try:
    api_response = api_instance.create_integrity_monitoring_rule(api_version, integrity_monitoring_rule=integrity_monitoring_rule)
    pprint(api_response)
except ApiException as e:
    print("An exception occurred when calling IntegrityMonitoringRulesApi.create_integrity_monitoring_rule: %s\n" % e)


