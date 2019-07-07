# Billing Alerts Stack

![Billing Alerts Diagram](https://static.cloudsumu.com/billingalerts/diagram.png)

Uses SNS, Lambda, and CloudWatch to send billing alerts via:
- Email
- Text
- Discord
- Slack

Easy to launch and configure!

## Launching Stack

### Option 1: Launch via Link

Make sure you are logged into the AWS Console and have permissions then click:

[![Launch in AWS Console](https://static.cloudsumu.com/billingalerts/launch_button.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/template?stackName=BillingAlerts&templateURL=https://sumu-billingalerts.s3.amazonaws.com/production/cloudformation/top.yaml)

Fill out the parameters and launch!

### Option 2: Manually input template into AWS Console

1.  Download top template or copy URL for later.

    *Development S3 URL:* [https://sumu-billingalerts.s3.amazonaws.com/develop/cloudformation/top.yaml](https://sumu-billingalerts.s3.amazonaws.com/production/cloudformation/top.yaml)

    *Production S3 URL:* [https://sumu-billingalerts.s3.amazonaws.com/production/cloudformation/top.yaml](https://sumu-billingalerts.s3.amazonaws.com/production/cloudformation/top.yaml)

2. Go to [CloudFormation on the AWS Console](https://console.aws.amazon.com/cloudformation/home)
3. Click the "Create stack" button
4. Under "Prepare template" make sure that "Template is ready" is selected, it should be the default.

    Then under "Template Source" either paste in the template URL or upload the downloaded template.

    Then click "Next"

5.  Fill out stack parameters then launch!