import urllib2
import boto
reponse = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
html = reponse.read()
print(html)
html1,html2 = html.split(':')

print(html1)
print(html2)
print(boto.Version)



