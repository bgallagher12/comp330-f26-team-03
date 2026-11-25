"""Run the local Campus Connect terminal application."""

import argparse
import logging
import sqlite3

from src import reviewer_service, student_service
from src.cli import read_secret, run
from src.database import init_db


def confirmed_password(role):
    password = read_secret(f"New {role} password: ")
    if password != read_secret(f"Confirm {role} password: "):
        raise ValueError("Passwords do not match.")
    return password


def student_sign_in():
    print("Student sign-in")
    email = input("Email (or type /register): ").strip()
    if email.lower() == "/register":
        email = input("Email: ")
        student_id = input("Student ID: ")
        student_service.create_account(email, student_id, confirmed_password("student"))
        print("Student account created. Sign in with your email and password.")
        email = input("Email: ")

    return student_service.authenticate(email, read_secret("Password: "))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--reviewer", action="store_true", help="Sign in as a reviewer")
    modes.add_argument("--add-reviewer", metavar="USERNAME", help="Create a local reviewer account")
    modes.add_argument(
        "--add-student", nargs=2, metavar=("EMAIL", "STUDENT_ID"),
        help="Provision a student account, including for an ID with existing requests",
    )
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    try:
        init_db()
        if args.add_reviewer is not None:
            reviewer_service.create_account(args.add_reviewer, confirmed_password("reviewer"))
            print("Reviewer account created.")
            return 0

        if args.add_student is not None:
            student_service.create_account(
                *args.add_student, confirmed_password("student"), allow_existing_requests=True,
            )
            print("Student account created.")
            return 0

        if args.reviewer:
            username = input("Reviewer username: ")
            password = read_secret("Reviewer password: ")
            if not reviewer_service.authenticate(username, password):
                print("Invalid reviewer username or password.")
                logging.warning("reviewer_sign_in_denied")
                return 1
            logging.info("reviewer_sign_in_succeeded")
            run(reviewer=True)
        else:
            student_id = student_sign_in()
            if student_id is None:
                print("Invalid student email or password.")
                logging.warning("student_sign_in_denied")
                return 1
            logging.info("student_sign_in_succeeded")
            run(student_id=student_id)
    except ValueError as error:
        print(error)
        return 1
    except (sqlite3.Error, OSError) as error:
        logging.error("storage_failure error_type=%s", type(error).__name__)
        return 1
    except (EOFError, KeyboardInterrupt):
        logging.info("terminal_session_ended: interactive input was interrupted")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
