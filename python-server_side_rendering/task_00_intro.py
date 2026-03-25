import os


def generate_invitations(template: str, attendees):
    if len(template) == 0:
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return
    if not isinstance(template, str) or not isinstance(attendees, list):
        print("test")
        return
    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("test")
            return
    id_max = 1
    while os.path.exists(f"output_{id_max}.txt"):
        id_max += 1
    for id in range(0, len(attendees)):
        attendee = attendees[id]
        with open(f'output_{id_max + id}.txt', 'w') as file:
            string = template.format(
                name=attendee.get('name', "N/A"),
                event_title=attendee.get('event_title', "N/A"),
                event_date=attendee.get('event_date', "N/A"),
                event_location=attendee.get('event_location', "N/A"))
            file.write(string)
