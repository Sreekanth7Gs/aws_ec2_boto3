#Create a python script to start and stop the EC2 instance. 
# Hardcode the instance id in the script. The script should be triggered from your local.
import boto3

def start_ec2(instance_id):
    try:
        ec2 = boto3.client('ec2')
        ec2.start_instances(InstanceIds=[instance_id])
        print(f"Instance {instance_id} started successfully.")
    except Exception as e:
        print(f"Error starting instance {instance_id}: {e}")

def stop_ec2(instance_id):
    try:
        ec2 = boto3.client('ec2')
        ec2.stop_instances(InstanceIds=[instance_id])
        print(f"Instance {instance_id} stopped successfully.")
    except Exception as e:
        print(f"Error stopping instance {instance_id}: {e}")

def main():
    instance_id = 'i-0ecbcfbdc38f5ed95'  
    start_ec2(instance_id)
    
    print("Waiting for a few seconds...")
    import time
    time.sleep(5)

    stop_ec2(instance_id)

if __name__ == "__main__":
    main()
