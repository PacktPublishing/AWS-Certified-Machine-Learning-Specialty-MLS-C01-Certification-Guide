import boto3
language_name = {'en':'English', 'fr':'French', 'de':'German', 'es':'Espanol'}

def lambda_handler(event, context): 
    print("========lambda_handler for Amazon Comprehend=======") 
    # read the bucket name from the event 
    name_of_the_bucket=event['Records'][0]['s3']['bucket']['name'] 
    # read the object from the event 
    name_of_the_file=event['Records'][0]['s3']['object']['key'] 
    extracted_text = extract_text_from_image(name_of_the_file,name_of_the_bucket)
    translated_dict = translate_to(extracted_text,'en') 
    print("=========================")
    print("Translation of the text from the Image :   "+str(translated_dict)) 

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

def translate_to(text_list,target_lang_code):
    try:
        # Create Amazon Comprehend Client to read the text from the previous step to detect the language
        comprehend_client = boto3.client('comprehend')
        translate_client = boto3.client('translate')
        translate_dict={}
        #Take the Documents which have more than 20 characters.
        # API reference : https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.detect_dominant_language
        for text in text_list:
            if len(text)>=20:
                response_comprehend = comprehend_client.detect_dominant_language(Text=text)
                source_language_code = response_comprehend['Languages'][0]['LanguageCode']
                print('Source Language Detected:  '+str(language_name[source_language_code]))
                response_translate = translate_client.translate_text(Text=text,SourceLanguageCode=source_language_code,TargetLanguageCode=target_lang_code)
                output_text = response_translate['TranslatedText']
                translate_dict[text] = output_text
        return translate_dict
    except Exception as ex:
        print(ex)
        print("Error in detecting or translating the language from the text.")
        raise ex
    