"""Terminal interface for student and reviewer workflows."""

import getpass
import logging
import warnings

from src import student_service
from src.reviewer_service import (
    list_submitted_requests as list_pending_requests,
    get_request as get_request_for_review,
    save_resolution as resolve_request,
)
categories = ["Technology", "Tutoring", "Facilities", "Other"]
logger = logging.getLogger(__name__)


def read_secret(prompt):
    """Require hidden input for account passwords."""
    with warnings.catch_warnings():
        warnings.simplefilter("error", getpass.GetPassWarning)
        try:
            return getpass.getpass(prompt)
        except getpass.GetPassWarning:
            raise EOFError("Secret input requires an interactive terminal.") from None


def display_request(request):
    """
    Displays the main details of one request
    """
    print(f"Request ID: {request['request_id']}")
    print(f"Student: {request['student_name']}")
    print(f"Title: {request['title']}")
    print(f"Description: {request['description']}")
    print(f"Category: {request['category']}")
    print(f"Status: {request['status']}")

    # Shows the resolution if one has been entered
    if request["resolution"]:
        print(f"Resolution: {request['resolution']}")
    else:
        print("Resolution: Not Yet Resolved")


def menu(reviewer):
    """
    Displays the menu options
    """
    if reviewer:
        print("3. Review Pending Requests")
        print("4. Resolve Request")
        print("5. Exit")
    else:
        print("1. Submit a Request")
        print("2. My Requests")
        print("3. Exit")


def choose_category():
    """
    Asks the user to choose a categroy for their request
    """
    print("Categories:")
    for number, category in enumerate(categories, start=1):
        print(f"{number}. {category}")
    try:
        # Asks the user for the category choice
        category_choice = int(input("Enter your category option: "))
    except ValueError:
        print("Enter a number from 1 to 4.")
        return None
    # Ensures the number matches one of the categories listed
    if category_choice < 1 or category_choice > len(categories):
        print("Choose a category from the list.")
        return None

    return categories[category_choice - 1]


def submit_request_menu(student_id):
    """
    Collects the request details and sends it to the backend
    """
    student_name = input("Enter your name: ")
    student_email = input("Enter your student email: ")
    title = input("Enter the request title: ")
    description = input("Enter the request description: ")

    # Asks the user to select one of the categories
    category = choose_category()
    if category is None:
        return

    # Creates a dictionary expected by submit_reques()
    details = {
        "student_name": student_name,
        "student_id": student_id,
        "student_email": student_email,
        "title": title,
        "description": description,
        "category": category,
    }

    # Saves the request and displays the request returned by the backend
    student_service.submit_request(details)
    print("Request Submitted")
    logger.info("request_submitted")


def get_request_id():
    """
    Asks for the request ID and returns it as an integer

    """
    try:
        request_id = int(input("Enter the request ID: ").strip())
        if not 1 <= request_id <= 2**63 - 1:
            raise ValueError
        return request_id
    except ValueError:
        print("Request ID must be a positive SQLite integer.")
        return None


def view_my_requests(student_id):
    """List the signed-in student's requests and open one by its menu number."""
    print("My Requests")
    requests = student_service.list_requests(student_id)
    if not requests:
        print("You have no requests yet.")
        return

    for number, request in enumerate(requests, start=1):
        badge = ""
        if request["status"] == "resolved" and request["response_seen_at"] is None:
            badge = " [Update available]"
        print(f"{number}. {request['title']}    {request['status'].capitalize()}{badge}")

    choice = input("Choose a request (Enter to go back): ").strip()
    if not choice:
        return
    try:
        number = int(choice)
        if not 1 <= number <= len(requests):
            raise ValueError
    except ValueError:
        print("Choose a request number from this list.")
        return

    request_id = requests[number - 1]["request_id"]
    request = student_service.get_request(student_id, request_id)
    print(request["title"])
    print(f"Status: {request['status'].capitalize()}")
    if request["status"] == "resolved":
        print(f"Professor's response: {request['resolution']}", flush=True)
        student_service.mark_response_seen(student_id, request_id)
        logger.info("student_response_opened")


def review_pending_requests():
    """
    Displays requests that are waiting to be resolved
    """
    pending = list_pending_requests()

    if not pending:
        print("There are no pending requests")
        return
    for p in pending:
        print("Pending Request")
        display_request(p)

def resolve_requests():
    """Show a request and let the reviewer resolve it."""
    request_id = get_request_id()
    if request_id is None:
        return

    request = get_request_for_review(request_id)
    print("Request To Resolve")
    display_request(request)

    resolution = input("Enter the resolution for this request: ").strip()
    if not resolution:
        print("You cannot leave the resolution empty")
        return

    updated = resolve_request(request_id, resolution)
    logger.info("request_resolved")
    print("Request is resolved")
    display_request(updated)

def run(*, reviewer=False, student_id=None):
    """Run one workflow until the operator exits."""
    if not reviewer and not student_id:
        raise ValueError("Student sign-in is required.")

    while True:
        menu(reviewer)
        choice = input("Choose an option: ").strip()
        try:
            match choice:
                case "1" if not reviewer:
                    submit_request_menu(student_id)
                case "2" if not reviewer:
                    view_my_requests(student_id)
                case "3" if reviewer:
                    review_pending_requests()
                case "4" if reviewer:
                    resolve_requests()
                case "3" if not reviewer:
                    print("You are Exiting the App")
                    return
                case "5" if reviewer:
                    print("You are Exiting the App")
                    return
                case _:
                    print("Choose an option from this menu.")
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    from src.main import main

    raise SystemExit(main())
