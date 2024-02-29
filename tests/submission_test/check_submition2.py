import filecmp

"""
Author: Ilan Simchon
Date: 16/01/2024

This script clones a Git repository, checks out a specified commit, compiles Java code, and runs the compiled class.
"""

import os
import subprocess
import shutil


def clone_and_rename(repo_url, commit_number, student_ids):
    """
    Clone a Git repository, checkout a specified commit, compile Java code, and run the compiled class.

    Parameters:
    - repo_url (str): The URL of the Git repository.
    - commit_number (str): The commit hash or branch name to checkout.
    - student_ids (list): List of student IDs associated with the repository.

    Returns:
    None
    """
    # Extract repository name from the URL
    repo_name = repo_url.split("/")[-1].rstrip(".git")

    # Clone the repository
    subprocess.run(["git", "clone", "-n", repo_url, os.path.join(os.getcwd(), repo_name)])

    # Change to the repository directory
    repo_dir = os.path.join(os.getcwd(), repo_name)
    os.chdir(repo_dir)

    # Checkout the specified commit
    subprocess.run(["git", "checkout", commit_number])

    student_output = "student_output.txt"
    student_output_file = open(student_output,'w+')
    # Compile the Java code
    try:
        try:
            compile_command = ['python3', 'main.py']
            subprocess.run(compile_command,stdout=student_output_file, check=True)
        except Exception:
            compile_command = ['python', 'main.py']
            subprocess.run(compile_command,stdout=student_output_file, check=True)

        # Compare the student's output to the correct output
        if filecmp.cmp(student_output, 'output.txt', shallow=False):
            print("Output is correct. You passed the test successfully!")
            print(f"Success!! Code compiled and executed for student IDs {', '.join(student_ids)}.")
        else:
            print("Output is incorrect. You are required to fix your code")


    except subprocess.CalledProcessError:
        print(f"Error: There is a problem in your code, go fix your code and try again.")


if __name__ == "__main__":
    # Get the script's directory
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Iterate through each text file with a .txt extension
    for filename in os.listdir(script_dir):
        if filename.endswith(".txt") and filename != 'output.txt':
            file_path = os.path.join(script_dir, filename)

            try:
                with open(file_path, "r") as file:
                    lines = file.read().splitlines()

                    # Extract information from the text file
                    repo_url = lines[0]
                    commit_number = lines[1]
                    student_ids = lines[2].split()

            except FileNotFoundError:
                print("Error: There is a problem in your submission. go fix it and try again")

            # Call the function to clone and rename
            clone_and_rename(repo_url, commit_number, student_ids)
