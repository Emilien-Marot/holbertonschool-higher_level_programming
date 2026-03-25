def generate_invitations(template: str, attendees):
    if len(template) == 0:
        return
    if len(attendees) == 0:
        return
    for i in range(0, len(attendees)):
        attendee = attendees[i]
        with open(f'output_{i + 1}.txt', 'w') as file:
            string = template.format(
                name=attendee.get('name', "N/A"),
                event_title=attendee.get('event_title', "N/A"),
                event_date=attendee.get('event_date', "N/A"),
                event_location=attendee.get('event_location', "N/A"))
            file.write(string)
