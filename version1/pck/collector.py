from indeed_test3 import *
import time


# query = input("Enter job title: ")
# location = input("Enter job location: ")
# page_offset = input("Enter page no: ")

#indeed_dataset
total_job_count = 0
job_dataset = []



def get_job_dataset(c_query, c_location, c_page_offset):
    global total_job_count,job_dataset
    start = time.time()
    job_dataset.clear()
    total_job_count = 0
    #indeed.com collector
    indeed_j_count, indeed_job_dataset  = scrape_indeed(c_query, c_location, c_page_offset)
    job_dataset.append(indeed_job_dataset)
    total_job_count = total_job_count + int(indeed_j_count)

    end = time.time()
    print(end - start)

    return job_dataset

