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

#print (result[0])
#print (result[1])

access_key_id = result[0]
secret_access_key = result[1]

#print (access_key_id,secret_access_key)
# Set up a connection to the AWS service.
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

Student_number = 'C13469208'
#conn.delete_queue(sys.argv[1])
queue_name = Student_number+sys.argv[1]
# Get a list of the queues that exists and then print the list out
rp = conn.get_queue(queue_name)
print "message being added"               
rp.set_message_class(Message)		
mes = Message()
mes.set_body(sys.argv[2])
rp.write(mes)
