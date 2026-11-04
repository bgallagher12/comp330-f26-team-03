from src.mock_backend import (
    submit_request,
    get_request_status,
    list_pending_requests,
    get_request_for_review,
    resolve_request,
)

categories = [
    "Tutoring",
    "Technology",
    "Campus Club",
    "Equipment Checkout",
    "Advising Intake Request",
    "Approval Request",
    "Student Organization",
]


def display_request(request):
    print(f"Request ID: {request['request_id']}")
    print(f"Student: {request['student_name']}")
    print(f"Title: {request['title']}")
    print(f"Description: {request['description']}")
    print(f"Category: {request['category']}")
    print(f"Status: {request['status']}")

    if request["resolution"]:
        print(f"Resolution: {request['resolution']}")
    else:
        print("Resolution: Not Yet Resolved")


def menu():
    print("1. Submit a Request ")
    print("2. View Request Status")
    print("3. Review Pending Requests")
    print("4. Resolve Request")
    print("5. Exit")


def choose_category():
    print("Choose a category")
    for i in range(len(categories)):
        print(f"{i + 1}. {categories[i]}")

    category_choice = int(input("Enter your category option: ")) - 1

    if category_choice < 1 or category_choice > len(categories):
        print("Choose a category from the list")
        return None

    return categories[category_choice - 1]

    return categories[category_choice - 1]


def submit_request_menu():
    student_name = input("Enter your name: ")
    student_id = input("Enter your student ID: ")
    student_email = input("Enter your student email: ")
    title = input("Enter the request title: ")
    description = input("Enter the request description: ")

    category = choose_category()
    if category is None:
        return

    details = {
        "student_name": student_name,
        "student_id": student_id,
        "student_email": student_email,
        "title": title,
        "description": description,
        "category": category,
    }

    request = submit_request(details)
    print("Request Submitted")


def get_request_id():
    try:
        return int(input("Enter the request ID: ").strip())
    except ValueError:
        print("Request ID must be a whole number")
        return None


def view_request_status():
    request_id = get_request_id()

    request = get_request_status(request_id)

    if request_id is None:
        return

    if not request:
        print("Request Not Found")
        return

    status = request["status"]
    print(f"Request ID: {request_id}")
    print(f"Status: {status}")


def review_pending_requests():
    pending = list_pending_requests()

    if not pending:
        print("There are no pending requests")
        return
    for p in pending:
        print("Pending Request")
        display_request(p)


def resolve_requests():
    request_id = get_request_id()

    if request_id is None:
        return
    request = get_request_for_review(request_id)
    if not request:
        print("Request ID not found")
        return
    print("Request To Resolve: ")
    display_request(request)

    resolution = input("Enter Resolution for this request: ").strip()

    if not resolution:
        print("Resolution cannot be empty")
        return

    updated = resolve_request(request_id, resolution)
    print("Request is resolved")

    if updated:
        display_request(updated)


def run():
    menu()

    running = True
    choice = input("Choose an option: ").strip()
    while running:
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
                running = False
            case _:
                print("Invalid Choice was entered. Please choose an option from 1-5.")

