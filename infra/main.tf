terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = var.aws_region
}

resource "aws_db_instance" "tukro-db" {
  allocated_storage    = 5
  db_name              = "tukro"
  engine               = "postgres"
  engine_version       = "15.3"
  instance_class       = "db.t3.micro"
  username             = var.db_username
  password             = var.db_password
  skip_final_snapshot  = true
}

resource "aws_elastic_beanstalk_application" "tukro_app" {
  name        = "tukro-app"
  description = "Tukro Application"
}

resource "aws_elastic_beanstalk_environment" "tukro_app_env" {
  name                = "tukro-app-env"
  application         = aws_elastic_beanstalk_application.tukro_app.name
  solution_stack_name = "64bit Amazon Linux 2023 v4.1.0 running Docker"

  setting {
    namespace = "aws:autoscaling:launchconfiguration"
    name      = "InstanceType"
    value     = "t2.micro"
  }

  setting {
    namespace = "aws:autoscaling:launchconfiguration"
    name      = "IamInstanceProfile"
    value     = aws_iam_instance_profile.beanstalk_ec2_profile.name
  }

  setting {
    namespace = "aws:autoscaling:launchconfiguration"
    name      = "EC2KeyName"
    value     = var.key_pair_name
  }

  setting {
    namespace = "aws:elasticbeanstalk:application:environment"
    name      = "DB_USER"
    value     = var.db_username
  }

  setting {
    namespace = "aws:elasticbeanstalk:application:environment"
    name      = "DB_PASSWORD"
    value     = var.db_password
  }

  setting {
    namespace = "aws:elasticbeanstalk:application:environment"
    name      = "DB_NAME"
    value     = aws_db_instance.tukro-db.db_name
  }
  
  setting {
    namespace = "aws:elasticbeanstalk:application:environment"
    name      = "DB_HOST"
    value     = aws_db_instance.tukro-db.address
  }
  
  setting {
    namespace = "aws:elasticbeanstalk:application:environment"
    name      = "DB_PORT"
    value     = aws_db_instance.tukro-db.port
  }

  setting {
    namespace = "aws:elasticbeanstalk:application:environment"
    name = "APP_SECRET"
    value = var.app_secret
  }

  setting {
    namespace = "aws:elasticbeanstalk:application:environment"
    name = "JWT_SECRET"
    value = var.jwt_secret
  }

  setting {
    namespace = "aws:elasticbeanstalk:application:environment"
    name = "DJANGO_SETTINGS_MODULE"
    value = var.django_settings_module
  }
}

resource "aws_elastic_beanstalk_application_version" "default" {
  depends_on = [
    aws_elastic_beanstalk_environment.tukro_app_env,
    aws_elastic_beanstalk_application.tukro_app,
    aws_s3_object.docker
  ]
  name        = "tukro-version"
  application = aws_elastic_beanstalk_application.tukro_app.name
  bucket      = aws_s3_bucket.beanstalk_deploys.id
  key         = aws_s3_object.docker.id
}