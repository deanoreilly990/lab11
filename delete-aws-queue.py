import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
import urllib2
import boto
reponse = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
html = reponse.read()
print(html)
html1,html2 = html.split(':')


# Get the keys from a specific url and then use them to connect to AWS Service
access_key_id = html1
secret_access_key = html2

# Set up a connection to the AWS service.
conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

#delete a queue
readin=sys.argv[1]

rs = conn.get_all_queues()
for q in rs:
	if q.id == readin :
		conn.delete_queue(q)
		print("deleted")
