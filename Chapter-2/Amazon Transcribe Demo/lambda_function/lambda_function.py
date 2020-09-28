import boto3
import time
client=boto3.client('transcribe')

def lambda_handler(event, context): 
    print("=== Speech-to-Text ===") 
    # read the bucket name from the event 
    session = boto3.session.Session()
    region = session.region_name
    name_of_the_bucket=event['Records'][0]['s3']['bucket']['name'] 
    # read the object from the event 
    name_of_the_file=event['Records'][0]['s3']['object']['key'] 
    
    url = "https://s3-" + region + ".amazonaws.com/" + name_of_the_bucket + "/" + name_of_the_file

    extract_text_from_audio(url,name_of_the_bucket,'Audio-to-Text-')
    
    print("Check your Output Bucket")
    print("Speech to text Completed :   ") 

def extract_text_from_audio(url, bucket, job_name):
    try:
        client.start_transcription_job(TranscriptionJobName=job_name,Media={'MediaFileUri':url},OutputBucketName=bucket,LanguageCode='en-IE')
        status = client.get_transcription_job(TranscriptionJobName=job_name)
        while status['TranscriptionJob']['TranscriptionJobStatus'].upper()!='COMPLETED':
            print('checking status... It is not complete')
            time.sleep(20)
            status = client.get_transcription_job(TranscriptionJobName=job_name)
    except Exception as ex:
        print(ex)
        print("Error processing audio file from bucket {}. ".format(url))
        raise ex
