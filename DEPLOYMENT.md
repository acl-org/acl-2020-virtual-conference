Deploy to AWS with authentication.
Adjusted based on [this tutorial](https://douglasduhaime.com/posts/s3-lambda-auth.html).

* [S3](https://aws.amazon.com/s3/)
* [CloudFront](https://aws.amazon.com/cloudfront/)

#### Upload static files to AWS S3

1. Create a AWS S3 bucket (e.g., `acl2020virtual`).
    * https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html
    * Block all public access.
    * Do NOT use Static website hosting as in the original tutorial.
1. `make freeze` and upload `build/` folder to the S3 bucket.

#### Distribute S3 site with CloudFront

#### Create IAM Credentials

#### Create the Authentication Layer with AWS Lambda

