import boto3 
ec2 = boto3.client('ec2')
try:
    instance_id = input("Enter instance_id (press enter for all instances): ")
    if not instance_id:
        ec2_action = input("Enter 'start' to start all instances or 'stop' to stop all instances: ")
        instances = ec2.describe_instances()['Reservations']
        instance_ids = [instance['InstanceId'] for reservation in instances for instance in reservation['Instances']]

        if instance_ids:
            ec2_action = input("Enter 'start' to start the instances (or) 'stop' to stop the instances: ")
            if ec2_action.lower() == 'start':
                ec2.start_instances(InstanceIds=instance_ids)
                print("Waiting for a few seconds...")
                import time
                time.sleep(5)
            elif ec2_action.lower() == 'stop':
                ec2.stop_instances(InstanceIds=instance_ids)
                print("Waiting for a few seconds...")
                import time
                time.sleep(5)
            else:
                print("Invalid Input... Please enter start/stop for the instances.")
        else:
            print("No instances found.")
    else:
        ec2_action = input("Enter 'start' to start the instance (or) 'stop' to stop the instance: ")
        if ec2_action.lower() == 'start':
            ec2.start_instances(InstanceIds=[instance_id])
            print("Waiting for a few seconds...")
            import time
            time.sleep(5)
        elif ec2_action.lower() == 'stop':
            ec2.stop_instances(InstanceIds=[instance_id])
            print("Waiting for a few seconds...")
            import time
            time.sleep(5)
        else:
            print("Invalid Input... Please enter 'start' or 'stop'.")
except Exception as e:
    print(f"Error: {e}")

if __name__ == "__main__":
    pass
