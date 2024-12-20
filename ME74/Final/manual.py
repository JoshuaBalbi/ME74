import airtable as airtable

def movewindow():
    status = airtable.req_info()
    if status == "Opened":
        airtable.post_info("Closed")
        return "Closed"
    elif status == "Closed":
        airtable.post_info("Opened")
        return "Opened"