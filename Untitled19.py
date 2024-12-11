#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import time
from concurrent.futures import ThreadPoolExecutor

# File paths
students_csv_path = "students.csv"  # Ensure this file exists and has valid content
marks_csv_path = "marks.csv"  # Ensure this file exists and has valid content

# Function to load students data
def load_students():
    try:
        students_df = pd.read_csv(students_csv_path)
        return students_df
    except Exception as e:
        print(f"Error loading students data: {e}")
        return None

# Function to load marks data
def load_marks():
    try:
        marks_df = pd.read_csv(marks_csv_path)
        return marks_df
    except Exception as e:
        print(f"Error loading marks data: {e}")
        return None

# Serial execution
def serial_execution():
    start_time = time.time()
    students = load_students()
    marks = load_marks()
    end_time = time.time()
    return students, marks, end_time - start_time

# Parallel execution
def parallel_execution():
    start_time = time.time()
    with ThreadPoolExecutor() as executor:
        future_students = executor.submit(load_students)
        future_marks = executor.submit(load_marks)
        students = future_students.result()
        marks = future_marks.result()
    end_time = time.time()
    return students, marks, end_time - start_time

# Run and measure execution times
students_serial, marks_serial, serial_time = serial_execution()
students_parallel, marks_parallel, parallel_time = parallel_execution()

# Print results
print("Serial Execution Time:", serial_time)
print("Parallel Execution Time:", parallel_time)

# Uncomment these lines to verify the loaded data
# if students_serial is not None:
#     print(students_serial.head())
# if marks_serial is not None:
#     print(marks_serial.head())
# if students_parallel is not None:
#     print(students_parallel.head())
# if marks_parallel is not None:
#     print(marks_parallel.head())


# In[ ]:




