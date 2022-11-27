import boto3


s3 = boto3.resource('s3')

def lambda_handler(event, context):
    bucketlist = []
    bucket = s3.Bucket('prueba-bucket-aws-cli')
    
    for objeto_bucket in bucket.objects.all():
        bucketlist.append(objeto_bucket.key)
      
    return {
        "statusCode": 200,
        "body": bucketlist
    }
    

