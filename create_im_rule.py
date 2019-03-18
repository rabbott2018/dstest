Skip to content
 
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 @rabbott2018 Sign out
0
0 0 rabbott2018/dstest
 Code  Issues 0  Pull requests 0  Projects 0  Wiki  Insights  Settings
dstest/create_im_rule.py
 ricka updated create_im_rule.py to apply the rule after it's created
39e4e92  4 minutes ago
88 lines (71 sloc)  3.02 KB
    
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

# Create the new IM rule
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

# Find the host id of the host we want to apply the rule to
# Set Any Required Values
api_instance = deepsecurity.ComputersApi(deepsecurity.ApiClient(configuration))
api_version = 'v1'
overrides = False

try:
    computers = api_instance.list_computers(api_version, overrides=False)
    for computer in computers.computers:
            computer_info = []
            
            if computer.host_name == hostname.rstrip():
                host_id = computer.id
    
except ApiException as e:
    print("An exception occurred when calling ComputersApi.search_computers: %s\n" % e)

# Apply the rule to the host
api_instance = deepsecurity.ComputerIntegrityMonitoringRuleAssignmentsRecommendationsApi(deepsecurity.ApiClient(configuration))
computer_id = host_id
api_version = 'v1'
integrity_monitoring_rule_ids = deepsecurity.RuleIDs()
integrity_monitoring_rule_ids.rule_ids=rule_id
overrides = False

try:
    api_response = api_instance.add_integrity_monitoring_rule_ids_to_computer(computer_id, api_version, integrity_monitoring_rule_ids=integrity_monitoring_rule_ids, overrides=overrides)
    pprint(api_response)
except ApiException as e:
    print("An exception occurred when calling ComputerIntegrityMonitoringRuleAssignmentsRecommendationsApi.add_integrity_monitoring_rule_ids_to_computer: %s\n" % e)

