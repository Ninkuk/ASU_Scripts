from spontit import SpontitResource


def get_spontit_resource():
    lines = open("username_and_key.txt").read().splitlines()
    resource = SpontitResource(lines[0], lines[1])
    return resource


# if push_to_followers is None, it will send it to everybody
# making the parameter specific_followers default value None does not work and sends nothing.
def send_notification(notification_title, notification_text, content, specific_followers=[]):
    resource = get_spontit_resource()

    if not specific_followers:
        response = resource.push(content, notification_text, notification_title, push_to_followers=None)
    else:
        response = resource.push(content, notification_text, notification_title, push_to_followers=specific_followers)
