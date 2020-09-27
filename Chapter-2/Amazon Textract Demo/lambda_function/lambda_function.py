import boto3
import time
from trp import Document
textract_client=boto3.client('textract')

def lambda_handler(event, context): 
    print("- - - Amazon Textract Demo - - -") 
    # read the bucket name from the event 
    name_of_the_bucket=event['Records'][0]['s3']['bucket']['name'] 
    # read the object from the event 
    name_of_the_doc=event['Records'][0]['s3']['object']['key']
    print(name_of_the_bucket)
    print(name_of_the_doc)
    # Starts the asynchronous analysis of an input document for relationships between detected items such as key-value pairs, tables, and selection elements.
    # API ref : https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/textract.html#Textract.Client.start_document_analysis
    # textract_response = textract_client.start_document_text_detection(DocumentLocation={'S3Object': {'Bucket': name_of_the_bucket,'Name': name_of_the_doc}})
    response = textract_client.analyze_document(Document={'S3Object': {'Bucket': name_of_the_bucket,'Name': name_of_the_doc}},FeatureTypes=["TABLES","FORMS"])
    print(str(response))
    doc=Document(response)
    for page in doc.pages:
        # Print tables
        for table in page.tables:
            for r, row in enumerate(table.rows):
                for c, cell in enumerate(row.cells):
                    print("Table[{}][{}] = {}".format(r, c, cell.text))
    for page in doc.pages:
        # Print fields
        print("Fields:")
        for field in page.form.fields:
            print("Key: {}, Value: {}".format(field.key, field.value))
            
def isJobComplete(jobId):
    #Details at: https://docs.aws.amazon.com/textract/latest/dg/api-async.html
    time.sleep(5)
    response = textract_client.get_document_text_detection(JobId=jobId)
    status = response["JobStatus"]
    print("Job status: {}".format(status))
    while(status == "IN_PROGRESS"):
        time.sleep(5)
        response = textract_client.get_document_text_detection(JobId=jobId)
        status = response["JobStatus"]
        print("Job status: {}".format(status))
        return status
        
# Reference : https://github.com/aws-samples/amazon-textract-code-samples/tree/master/python