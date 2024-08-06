provider "aws" {
  region = "us-east-1"
}

# Bucket Bronze
resource "aws_s3_bucket" "bronze_bucket" {
  bucket = "bees-breweries-tf-bronze-bucket"

  tags = {
    Name  = "Bees Breweries"
    Layer = "Bronze"
  }
}

# Bucket Silver
resource "aws_s3_bucket" "silver_bucket" {
  bucket = "bees-breweries-tf-silver-bucket"

  tags = {
    Name  = "Bees Breweries"
    Layer = "Bronze"
  }
}

# Bucket Gold
resource "aws_s3_bucket" "gold_bucket" {
  bucket = "bees-breweries-tf-gold-bucket"

  tags = {
    Name  = "Bees Breweries"
    Layer = "Bronze"
  }
}
