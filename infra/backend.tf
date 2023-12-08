terraform {
  backend "s3" {
    bucket = "tukro-tr-backend"
    key    = "tr-state"
    region = "us-east-2"
  }
}