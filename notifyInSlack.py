def notifyInSlack(slack_token, slack_channel, environment_name, job_name, error_message):
    """A function to post a message in a slack channel"""
    from slack_sdk import WebClient
    from slack_sdk.errors import SlackApiError
    
    # set up slack client
    client = WebClient(slack_token)
    
    
    # create the message block
    message_block = [
        # header block for error message
        {
            "type":"header",
            "text":{
                "type":"plain_text",
                "text":f"Failure in {environment_name} with {job_name}"
            }
        },
        
        # actual error message
        {
            "type":"section",
            "text":{
                "type":"mrkdwn",
                "text":error_message
            }
        }
    ]
    
    # post message
    response = client,chat_postMessage(
        channel = slack_channel,
        blocks = message_block,
        text = f"Failure in {environment_name} with {job_name}"
    )