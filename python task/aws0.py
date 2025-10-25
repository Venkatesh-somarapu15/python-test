import boto3
def create_user(username):
    a = boto3.client("iam")
    response = a.create_user(UserName=username)
    print(response)
create_user("Gangi")
