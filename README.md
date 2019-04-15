This script is built using Python 3 and Boto3  to connect to AWS.
AWS Credentials involve in the script it self, i used Python 3 due to suporting some library like random 
The chaos2 script fullfill the following: 
1.The script select random instance IDs for disruption 
2. The ‘disruption’ consist of instance termination
3.The script wait for long enough to test if HA works, so i allow the script to sleep or wait long enough for HA to kick in (not exceeding 10 min )
4.The purpose of the script to test the HA features of AWS, and report a status (pass/fail) 
5.The script gives the user the time of how long time it take 
6.The script failed , for instance if the Number of instances were more than 6 ( the system design to accept 6 as min and maximum ), the script will wait for 10 min and the No. of instances will not be able to reach to that amount so it will fail 

The link for Video https://youtu.be/hMJAgT2h3kA  

