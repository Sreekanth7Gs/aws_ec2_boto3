import boto3
import time
import sys

def perform_action(ec2, instance_ids, action):
    try:
        if action.lower() == 'start':
            ec2.start_instances(InstanceIds=instance_ids)
            print("Waiting for a few seconds...")
            time.sleep(5)
            print(f"the instance {instance_id} is started..")
        elif action.lower() == 'stop':
            ec2.stop_instances(InstanceIds=instance_ids)
            print("Waiting for a few seconds...")
            time.sleep(5)
            print(f"the instance {instance_id} is stopped... ")
        else:
            print("Invalid action. Please enter 'start' or 'stop'.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    region = sys.argv[3] if len(sys.argv) > 3 else 'us-east-1'
    ec2 = boto3.client('ec2', region_name=region)

    instance_id = sys.argv[1] if len(sys.argv) > 1 else input("Enter instance_id (press enter for all instances): ")
    action = sys.argv[2] if len(sys.argv) > 2 else input("Enter 'start' or 'stop' (press enter to choose later): ")

    if not instance_id:
        instances = ec2.describe_instances()['Reservations']
        instance_ids = [instance['InstanceId'] for reservation in instances for instance in reservation['Instances']]

        if instance_ids:
            perform_action(ec2, instance_ids, action)
        else:
            print("No instances to start or stop.")
    else:
        perform_action(ec2, [instance_id], action)
