'''
This module provides functions to create folders to organize my courses.
It is filled with for in range and while loops as well as using lists in for loops.
I currently teach Geometry and Consumer Mathematics to high school students.
'''
# import main modules and libraries
import math
import statistics
import pathlib

# import other needed modules and libraries
import Shellenberger_utils as utils # used for byline
import time

#printing byline
print(f'Byline: {utils.byline}')

# define all functions

def create_folder(folder_name: str) -> None:
    ''' 
    Creates folder
    :param folder_name: name of folder to be created, example: "test"
    returns: None
    '''
    pathlib.Path(folder_name).mkdir(exist_ok=True)

def create_folder_from_range(folder_name: str, start: int, end: int) -> None:
    '''
    Creates folders from a range of years and stores them in a parent folder.
    :param folder_name: name of folder to be created, example: "test"
    :param start: first year to be created, example: 2000
    :param end: last year to be created, example: 2024
    returns: None
    '''
    folder_name = lowercase_and_remove_spaces(folder_name)
    create_folder(folder_name)
    
    for year in range(start, end + 1):
        year_folder = pathlib.Path(folder_name).joinpath(str(year))
        create_folder(year_folder)

def create_courses_from_list(folder_name: list, folder_list: list) -> None:
    '''
    Creates folders from a list of course names ans stores them in a parent folder.
    :param folder_name: name of folder to be created, example: "test"
    :param folder_list: list of course names, example: ['Geometry', 'Consumer Math']
    returns: None
    '''
    folder_name = lowercase_and_remove_spaces(folder_name)
    create_folder(folder_name)
    
    for course in folder_list:
        course = lowercase_and_remove_spaces(course)
        course_folder = pathlib.Path(folder_name).joinpath(course)
        create_folder(course_folder)

def create_prefixed_folders(folder_name: str, folder_list: list, prefix: str) -> None:
    '''
    Creates folders from a specified prefix + a list of course names ans stores them in a parent folder.
    :param folder_name: name of folder to be created, example: "test"
    :param folder_list: list of course names, example: ['Geometry', 'Consumer Math']
    returns: None
    '''
    folder_name = lowercase_and_remove_spaces(folder_name)
    create_folder(folder_name)
    
    for block in folder_list:
        block = lowercase_and_remove_spaces(block)
        prefix_blocks_folder = pathlib.Path(folder_name).joinpath(prefix + block)
        create_folder(prefix_blocks_folder)


def create_folders_periodically(duration_sec: int, folder_name: str, number_of_folders: int, starting_number: int) -> None:
    '''
    Creates folders from a range of student numbers ans stores them in a parent folder in a time-delay.
    :param duration_secs: duration in seconds
    :param folder_name: name of folder to be created, example: "test"
    :param number_of_folders: number of folders to be created: example: 10
    :param starting_number: first number to start with, example: 20
    returns: None
    '''
    folder_name = lowercase_and_remove_spaces(folder_name)
    create_folder(folder_name)
    student_number = starting_number # Switching starting number ot student number
    
    while number_of_folders > 0:
        time.sleep(duration_sec)
        student_folder = pathlib.Path(folder_name).joinpath(str(student_number))
        create_folder(student_folder)
        number_of_folders -= 1
        student_number += 1

def lowercase_and_remove_spaces(folder_name: str) -> str:
    '''
    Converts a string to lowercase and removes spaces from it.
    :param company: string to be modified, example: "Apple Inc."
    returns: string
    '''
    folder_name = folder_name.replace(' ', '') # removes spaces from string
    folder_name = folder_name.lower() # converts string to lowercase
    return folder_name

# define main function
def main():
    '''
    Main function
    Calls function to create folders from various variables.
    '''
    courses_i_teach = ['Geometry', 'Consumer Math'] # list of companies that I have worked with over the years
    create_courses_from_list(folder_name= 'Courses', folder_list= courses_i_teach)
    
    create_folder_from_range(folder_name= 'Usd 231', start= 2021, end= 2023)
    
    blocks_i_teach = ['B1', 'B3', 'B5', 'W2', 'W3', 'W5']
    create_prefixed_folders(folder_name = "Blocks",folder_list = blocks_i_teach, prefix = 'data-')
    
    create_folders_periodically(duration_sec= 2, folder_name= "Student Number", number_of_folders= 5, starting_number= 1000)
    


# All clear module
if __name__ == '__main__':
  main()
