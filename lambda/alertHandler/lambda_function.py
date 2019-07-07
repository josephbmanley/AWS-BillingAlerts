import json, requests, os, boto3


def lambda_handler(event, context):
    if 'Records' in event:
        for record in event['Records']:
            if record['EventSource'] == "aws:sns":
                if "Message" in record['Sns']:
                    message = json.loads(record['Sns']['Message'])
                    if "NewStateValue" in message:
                        print(message)
                        is_important = "HighPriority" in message["AlarmName"] and (message["NewStateValue"] != "OK")
                        send_message(message["NewStateReason"], "AWS Billing Alert", is_important)
                    else:
                        send_message(message, record['Sns']['Subject'])

#-------------------
# Messaging Methods
#-------------------
def send_discord_message(message, name = None, high_priority = False):
    if high_priority:
        send_discord_message("@everyone \n**HIGH PRIORITY:** " + message, name)
        return
    if "discordWebhook" in os.environ and os.environ["discordWebhook"] != "":
        r = requests.post(os.environ['discordWebhook'],
            data={'content': message, 'username': name})
        print("Sent to Discord: " + message)
    else:
        print("Discord webhook not setup. Skipping...")

def send_sns_message(message, name = "Billing Alert", high_priority = False):
    if high_priority:
        send_sns_message(message, "HIGH PRIORITY: " + name)
        return
    if 'snsTopic' in os.environ and os.environ["snsTopic"] != "":
        boto3.client('sns').publish(
            TargetArn=os.environ['snsTopic'],
            Message=json.dumps({'default':message,
                                'sms' : name +"\n---\n" + message}),
            Subject=name,
            MessageStructure='json'
        )
        print("Published to SNS: " + message)
    else:
        print("SNS not setup. Skipping...")

def send_slack_message(message, name = None, high_priority = False):
    if high_priority:
        send_slack_message("<!channel> \n*HIGH PRIORITY:* " + message, name)
        return
    if "slackWebhook" in os.environ and os.environ["slackWebhook"] != "":
        r = requests.post(os.environ['slackWebhook'],
            data=json.dumps({'text': message, 'username' : name}),
            headers={'Content-Type' : 'application/json'})
        print("Sent to Slack: " + message)
    else:
        print("Slack webhook not setup. Skipping...")

#Function sends message to every messaging method
def send_message(message, name = None, high_priority = False):
    send_discord_message(message, name, high_priority)
    send_slack_message(message, name, high_priority)
    send_sns_message(message, name, high_priority)