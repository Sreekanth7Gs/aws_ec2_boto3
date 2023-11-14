import boto3
def start_instances(instance_id):
 ec2 = boto3.client('ec2',region_name = 'us-east-1')
 try:
     ec2.start_instances(InstanceIds = [instance_id])
     print(f"instance {instance_id} is starting...")
     waiter = ec2.get_waiter("instance is running")
     waiter.wait(InstanceIds = [instance_id]) 
     print(f" Instance {instance_id} is now running")
 except Exception as e:
     print(f"Error: {e}")
if __name__ == "__main__":
    instance_id_to_start = 'i-0e13829aa840a8c17'
    start_instances(instance_id_to_start)    