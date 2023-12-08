resource "aws_s3_bucket" "beanstalk_deploys" {
  bucket = "tukro-deploys"
}

resource "aws_s3_object" "docker" {
  depends_on = [
    aws_s3_bucket.beanstalk_deploys
  ]
  bucket = "tukro-deploys"
  key    = "deploy.zip"
  source = "deploy.zip"
  etag = filemd5("deploy.zip")
}