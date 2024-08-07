resource "aws_s3_bucket" "bronze_bucket" {
  bucket = "${var.bucket_prefix}bronze-bucket"

  tags = {
    Layer = "Bronze"
  }
}

resource "aws_s3_bucket" "silver_bucket" {
  bucket = "${var.bucket_prefix}silver-bucket"

  tags = {
    Layer = "Silver"
  }
}

resource "aws_s3_bucket" "gold_bucket" {
  bucket = "${var.bucket_prefix}gold-bucket"

  tags = {
    Layer = "Gold"
  }
}
