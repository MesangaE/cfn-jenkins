
import json
import boto3

def lambda_handler(event, context):
 print(event) #whatever triggers the lambda function
 print("High CPU Utilization")
 subject = 'Attention Please!'
 client = boto3.client("ses")
 body = """
             <br>
              this mail comes from lambda even scheduling!
              CPU utilization is very high!
              please look into it.
         """
 message = body
 response = client.send_email(source ["yourmail@gmail.com"], Destination ["theirsa@gmail.com"], Message = message) 
 print("The mail is sent successefully")