import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
import urllib2

# Get the keys from a specific url and then use them to connect to AWS Service

response = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')

html=response.read()

result = html.split(':')

access_key_id = result[0]
secret_access_key = result[1]

#print (access_key_id,secret_access_key)
# Set up a connection to the AWS service.
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

Student_number = 'C13469208'



my_queue = conn.get_queue(Student_number+sys.argv[1])
rp = my_queue.get_messages()
mes = rp[0]
print mes.get_body()
