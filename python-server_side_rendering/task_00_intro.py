#!/usr/bin/env python3

from tempfile import template


def generate_invitations(template, attendees):
    """
    Generates personalized invitations for
    a list of attendees based on a given template.

    Args:
        template (str): The invitation template
        containing placeholders for attendee names.
        attendees (list): A list of attendee names
        to personalize the invitations.
    Returns:
        list: A list of personalized invitations for each attendee.
    """

    if not isinstance(template, str):
        print("Template must be a string.")
        return
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not isinstance(attendees, list):
        print("Attendees must be a list.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Attendees must be a list of dictionaries.")
        return

    for index, attendee in enumerate(attendees, start=1):
        copy_template = template

        keys = ["name", "event_title", "event_date", "event_location"]

        for key in keys:
            value = attendee.get(key)

            if value is None:
                value = "N/A"

            placeholder = f"{{{key}}}"
            copy_template = copy_template.replace(placeholder, str(value))

        with open(f"output_{index}.txt", "w") as file:
            file.write(copy_template)
