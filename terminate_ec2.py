import boto3
def terminate_instance(instance_id):
    try:
        ec2 = boto3.client('ec2', region_name = 'us-east-1')
        ec2.terminate_instances(InstanceIds = instance_id)
        print(f"instance {instance_id} is terminating.... ")
        waiter = ec2.get.waiter("instance is terminating")
        waiter.wait(InstanceIds=[instance_id])
    except Exception as e:
        print(f"instance {instance_id} is terminated..")
if __name__ == "__main__":
   instance_ter = input("Enter instance to be terminate: ")
   terminate_instance(instance_ter)