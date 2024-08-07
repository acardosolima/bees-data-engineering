output "bronze_bucket_name" {
  description = "Bronze S3 bucket name"
  value       = aws_s3_bucket.bronze_bucket
}

output "silver_bucket_name" {
  description = "Silver S3 bucket name"
  value       = aws_s3_bucket.silver_bucket
}

output "gold_bucket_name" {
  description = "Gold S3 bucket name"
  value       = aws_s3_bucket.gold_bucket
}