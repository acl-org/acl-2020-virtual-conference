Deploy to AWS with authentication.
Adjusted based on [this tutorial](https://douglasduhaime.com/posts/s3-lambda-auth.html).
Official document: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/SecurityAndPrivateContent.html

* [S3](https://aws.amazon.com/s3/)
* [CloudFront](https://aws.amazon.com/cloudfront/)

#### Upload static files to AWS S3

1. Create a AWS S3 bucket (e.g., `acl2020virtual`).
    * [Official Document](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)
    * Block all public access.
    * Do NOT enable "Static Website Hosting". 
1. `make freeze` and upload `build/` folder to the S3 bucket.

#### Distribute S3 site with CloudFront
1. Create distribution
    * Restrict Bucket Access: Yes
    * Redirect HTTP to HTTPS
    * Default Root Object: index.html

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html

https://aws.amazon.com/blogs/networking-and-content-delivery/authorizationedge-how-to-use-lambdaedge-and-json-web-tokens-to-enhance-web-application-security/
    

#### Create IAM Credentials

#### Create the Authentication Layer with AWS Lambda

