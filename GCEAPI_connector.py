# Created by Andrei Lomakin
# Teoglobal Solutions
# https://teo-global.com/
# Insert this code into your business logic

from google.cloud import compute_v1

# Instantiate a client object
client = compute_v1.InstancesClient.from_service_account_json('/path/to/your/credentials.json')

# Get a list of instances in a zone
zone = 'us-central1-a'
project = 'your-project-id'
instances = client.list(project=project, zone=zone)

# Start an instance
instance_name = 'your-instance-name'
instance = client.get(project=project, zone=zone, instance=instance_name)
if instance.status == 'TERMINATED':
    client.start(project=project, zone=zone, instance=instance_name)
