import boto3

def lambda_handler(event, context): 
    language_name = {'en':'English', 'fr':'French', 'de':'German', 'es':'Espanol'}
    print("========lambda_handler for Amazon Comprehend=======") 
    # read the bucket name from the event 
    name_of_the_bucket=event['Records'][0]['s3']['bucket']['name'] 
    # read the object from the event 
    name_of_the_file=event['Records'][0]['s3']['object']['key'] 
    extracted_text = extract_text_from_image(name_of_the_file,name_of_the_bucket)
    print("Text Extracted from Image:  "+str(extracted_text))
    language_detected = detect_language_from_text(extracted_text) 
    print("I believe the Sign Board is written in :  "+language_name[language_detected]) 

def extract_text_from_image(img_file, bucket):
    try:
        # Create Amazon Rekognition Client to read the Image File and Extract the texts, if any
        rekog_client = boto3.client('rekognition')
        text_list = []
        response_rekog = rekog_client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':img_file}})
        for text_detection in response_rekog['TextDetections']:
            text_list.append(text_detection['DetectedText'])
        return text_list
    except Exception as ex:
        print(ex)
        print("Error processing text file {} from bucket {}. ".format(img_file,bucket))
        raise ex

def detect_language_from_text(text_list):
    try:
        # Create Amazon Comprehend Client to read the text from the previous step to detect the language
        comprehend_client = boto3.client('comprehend')
        key_val_dict={}
        new_list_min_20_chars=[]
        #Take the Documents which have more than 20 characters.
        for text in text_list:
            if len(text)>=20:
                new_list_min_20_chars.append(text)
        print(new_list_min_20_chars)
        response_comprehend = comprehend_client.batch_detect_dominant_language(TextList=new_list_min_20_chars)
        print(response_comprehend)
        for result_set in response_comprehend['ResultList']:
            for language in result_set['Languages']:
                lang = language['LanguageCode']
                if lang not in key_val_dict.keys():
                    key_val_dict[lang]=1
                else:
                    key_val_dict[lang] = key_val_dict[lang]+1
        print("Unsorted Dictionary: "+str(key_val_dict))
        # Sort in descending order by values
        sorted_dict = sorted(key_val_dict.items(),key=lambda x: x[1], reverse=True) 
        print("Sorted Dictionary: "+str(sorted_dict))
        return sorted_dict[0][0]
    except Exception as ex:
        print(ex)
        print("Error in detecting the language from the text.")
        raise ex

    