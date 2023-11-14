import boto3

ec2 = boto3.client('ec2')

def stop_instance(instance_id):
    try:
        ec2.stop_instances(InstanceIds=[instance_id])

        print(f"Stopping the instance {instance_id}...")
    
        waiter = ec2.get_waiter('instance_stopped')
        waiter.wait(InstanceIds=[instance_id])

        print(f"Instance {instance_id} is now stopped.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    instance_id_to_stop = 'i-0e13829aa840a8c17'
    stop_instance(instance_id_to_stop)
