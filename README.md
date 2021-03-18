# AWS Certified Machine Learning Specialty: MLS-C01 Certification Guide

<a href="https://www.packtpub.com/product/aws-certified-machine-learning-specialty-2020-certification-guide/9781800569003"><img src="https://static.packt-cdn.com/products/9781800569003/cover/smaller" alt="Book Name" height="256px" align="right"></a>

This is the code repository for [AWS Certified Machine Learning Specialty: MLS-C01 Certification Guide](https://github.com/PacktPublishing/AWS-Certified-Machine-Learning-Specialty-MLS-C01-Certification-Guide), published by Packt.

**The definitive guide to passing the MLS-C01 exam on the very first attempt**

## What is this book about?
The AWS Certified Machine Learning Specialty exam tests your competency to perform machine learning (ML) on AWS infrastructure. This book covers the entire exam syllabus using practical examples to help you with your real-world machine learning projects on AWS.
This book covers the following exciting features: 
* Understand all four domains covered in the exam, along with types of questions, exam duration, and scoring
* Become well-versed with machine learning terminologies, methodologies, frameworks, and the different AWS services for machine learning
* Get to grips with data preparation and using AWS services for batch and real-time data processing
* Explore the built-in machine learning algorithms in AWS and build and deploy your own models
* Evaluate machine learning models and tune hyperparameters
* Deploy machine learning models with the AWS infrastructure

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1800569009) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders. For example, Chapter07.

The code will look like the following:
```
import sagemaker
knn = sagemaker.estimator.Estimator((get_image_uri(boto3.Session().region_name, "knn"),
    get_execution_role(),
    train_instance_count=1,
    train_instance_type='ml.m5.2xlarge',
    output_path=output_path,
    sagemaker_session=sagemaker.Session())
knn.set_hyperparameters(**hyperparams)

```

**Following is what you need for this book:**
This AWS book is for professionals and students who want to prepare for and pass the AWS Certified Machine Learning Specialty exam or gain deeper knowledge of machine learning with a special focus on AWS. Beginner-level knowledge of machine learning and AWS services is necessary before getting started with this book.

With the following software and hardware list you can run all code files present in the book (Chapter 1-13).

### Software and Hardware List

| Chapter  | Software required                   | OS required                        |
| -------- | ------------------------------------| -----------------------------------|
| 1-9      | AWS Account                         | Windows, Mac OS X, and Linux (Any) |

We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://static.packt-cdn.com/downloads/9781800569003_ColorImages.pdf).

### Related products <Other books you may enjoy>
* Learn Amazon SageMaker [[Packt]](https://www.packtpub.com/product/learn-amazon-sagemaker/9781800208919) [[Amazon]](https://www.amazon.com/Learn-Amazon-SageMaker-developers-scientists/dp/180020891X)

* Mastering Machine Learning on AWS[[Packt]](https://www.packtpub.com/product/mastering-machine-learning-on-aws/9781789349795) [[Amazon]](https://www.amazon.com/Mastering-Machine-Learning-AWS-TensorFlow/dp/1789349796)

## Get to Know the Author(s)
**Somanath Nanda**
Somanath has 10 years of working experience in IT industry which includes Prod development, Devops, Design and architect products from end to end. He has also worked at AWS as a Big Data Engineer for about 2 years.
 
 **Weslley Moura**
Weslley Moura has 17 years of working experience in Information Technology (last 9 years working on data teams and last 5 years working as a lead data scientist). He has been working in a variety of industries, such as financial, telecommunications, healthcare and logistics. In 2019, he was a nominee for data scientist of the year by The European DatSci & AI Awards.


