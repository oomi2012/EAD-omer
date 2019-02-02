#!/bin/sh
#This is script to catch the metadata for AWS-instance 
echo "The meta data for this AWS-EC as following:"
echo "MAC is "
curl http://169.254.169.254/latest/meta-data/mac;
echo ""
echo "IPV4 is "
curl http://169.254.169.254/latest/meta-data/public-ipv4;
echo ""
echo "Host name is "
curl http://169.254.169.254/latest/meta-data/public-hostname
echo ""
