from src.student_service import submit_request, get_request_status
from src.reviewer_service import (
    list_submitted_requests as list_pending_requests,
    get_request as get_request_for_review,
    save_resolution as resolve_request,
)
categories = ["Technology", "Tutoring", "Facilities", "Other"]


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


def menu():
    """
    Displays the menu options
    """
    print("1. Submit a Request ")
    print("2. View Request Status")
    print("3. Review Pending Requests")
    print("4. Resolve Request")
    print("5. Exit")


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


def submit_request_menu():
    """
    Collects the request details and sends it to the backend
    """
    student_name = input("Enter your name: ")
    student_id = input("Enter your student ID: ")
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
    request = submit_request(details)
    print("Request Submitted")
    display_request(request)


def get_request_id():
    """
    Asks for the request ID and returns it as an integer

    """
    try:
        return int(input("Enter the request ID: ").strip())
    except ValueError:
        print("Request ID must be a whole number")
        return None


def view_request_status():
    """Find a request and display its status and resolution."""
    request_id = get_request_id()
    if request_id is None:
        return

    request = get_request_status(request_id)
    display_request(request)

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
    print("Request is resolved")
    display_request(updated)

def run():
    """
    Keeps showing the menu until the user chooses Exit
    """
    while True:
        menu()
        choice = input("Choose an option: ").strip()
        try:
            match choice:
                case "1":
                    submit_request_menu()
                case "2":
                    view_request_status()
                case "3":
                    review_pending_requests()
                case "4":
                    resolve_requests()
                case "5":
                    print("You are Exiting the App")
                    break
                case _:
                    print("Invalid Choice. Please choose an option from 1-5.")
        except ValueError as error:
            print(error)

if __name__ == "__main__":
    from src.database import init_db

    init_db()
    run()
