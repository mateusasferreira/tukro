ws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 466706364244.dkr.ecr.us-east-2.amazonaws.com

docker build --tag=466706364244.dkr.ecr.us-east-2.amazonaws.com/tukro_repo:1.0.0 .

docker push 466706364244.dkr.ecr.us-east-2.amazonaws.com/tukro_repo:1.0.0