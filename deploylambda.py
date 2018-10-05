import boto3
import botocore.exceptions

awslambda = boto3.client('lambda',region_name='us-west-2')
iam_client = boto3.client('iam')

fn_name = "hello"
fn_role = 'arn:aws:iam::617272699181:role/awsoverflow-dev-us-west-2-lambdaRole'




with open('hello.zip', 'rb') as f:
  zipped_code = f.read()

	#role = iam_client.get_role(RoleName='awsoverflow-dev-us-west-2-lambdaRole')

response = awslambda.create_function(
  FunctionName=fn_name,
  Runtime='python3.6',
  Role=fn_role,
  Handler="{0}.lambda_handler".format(fn_name),
  Code=dict(ZipFile=zipped_code),
  Timeout=300
  )
print response
