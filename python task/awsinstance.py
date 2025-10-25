import boto3
def cec2():
    a = boto3.client("ec2")
    fan=a.run_instances()
    print(fan)
    imageid = "ami-06a0b4e3b7eb7a300",
    Count=1,
    instancetype="t2.micro",
    keyname="mykeyname",
    

    tags ="first-server",
cec2()