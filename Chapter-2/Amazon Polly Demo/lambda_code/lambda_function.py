from __future__ import print_function 

import boto3

def lambda_handler(event, context): 
    print("========lambda_handler for polly started=======") 
    # read the bucket name from the event 
    name_of_the_bucket=event['Records'][0]['s3']['bucket']['name'] 
    # read the object from the event 
    name_of_the_file=event['Records'][0]['s3']['object']['key'] 
    store_the_audio_file(name_of_the_file,name_of_the_bucket) 
    print("Audio File Saved Successfully") 
 

def store_the_audio_file(name_of_the_file, bucket): 
    try:
        polly_client = boto3.client('polly')
        s3_client = boto3.client('s3')
        obj = s3_client.get_object(Bucket=bucket, Key=name_of_the_file)
        text_data_from_file = obj['Body'].read().decode('utf-8')
        print("File Content:  "+text_data_from_file)
        #Create an asynchronous synthesis task
        polly_response = polly_client.start_speech_synthesis_task(
            Engine='standard',LanguageCode='en-GB',OutputFormat='mp3',
            OutputS3BucketName=bucket,OutputS3KeyPrefix='output-audio/',
            Text=text_data_from_file,VoiceId='Aditi')
        # Once the task is created, monitor the task through get_speech_synthesis_task till it is completed 
        print(polly_response)
        task_id = polly_response['SynthesisTask']['TaskId']
        task_status = polly_response['SynthesisTask']['TaskStatus']
        while task_status!='completed':
            # get the task status response
            task_status_response = polly_client.get_speech_synthesis_task(TaskId=task_id)
            task_status = task_status_response['SynthesisTask']['TaskStatus']
            print("Task Status is : "+task_status)
    except Exception as ex:
        print(ex)
        print("Error processing text file {} from bucket {}. ".format(name_of_the_file,bucket))
        raise ex