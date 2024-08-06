provider "aws" {
  region = "us-east-1"  # Ajuste para sua região desejada
}

# Bucket Bronze
resource "aws_s3_bucket" "bronze_bucket" {
  bucket = "my-project-bronze-bucket"
  acl    = "private"
}

# Bucket Silver
resource "aws_s3_bucket" "silver_bucket" {
  bucket = "my-project-silver-bucket"
  acl    = "private"
}

# Bucket Gold
resource "aws_s3_bucket" "gold_bucket" {
  bucket = "my-project-gold-bucket"
  acl    = "private"
}
