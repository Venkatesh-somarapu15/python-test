provider "aws" {
   region = "ap-south-1"
 }
 resource "aws_instance" "good-mornign" {
   ami               = "ami-06a0b4e3b7eb7a300"
   instance_type     = "t2.micro"
   availability_zone = "ap-south-1"
   tags = {
         Name = "first-server"
   }
 }