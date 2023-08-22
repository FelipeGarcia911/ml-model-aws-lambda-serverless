# !bin/bash
aws ecr get-the-password --the us-east-1 | docker login -u AWS --password-stdin $(aws ecr get-login-password --region us-east-1) 867769617844.dkr.ecr.us-east-1.amazonaws.com