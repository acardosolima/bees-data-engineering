terraform {
    required_providers {
      aws = {
        source = "hashicorp/aws"
        version = "~> 4.0.0"
      }
    }
}

provider "aws" {
  profile = "terraform"
  region  = "sa-east-1"

  default_tags {
    tags = {
      Project = "Bees Breweries"
    }
  }
}