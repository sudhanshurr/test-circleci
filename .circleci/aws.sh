mkdir ~/.aws/
	touch ~/.aws/config
	touch ~/.aws/credentials

	echo "[default]" >> ~/.aws/config
	echo "region = us-west-2" >> ~/.aws/config
	echo "output = json" >> ~/.aws/config

	echo "[default]" >> ~/.aws/credentials
	echo "aws_secret_access_key = " $AWS_SECRET_ACCESS_KEY >> ~/.aws/credentials
echo "aws_access_key_id = " $AWS_ACCESS_KEY_ID >> ~/.aws/credentials
