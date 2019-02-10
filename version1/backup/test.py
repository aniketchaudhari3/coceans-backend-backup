from collector import *
jq = input("Enter title:  ")
jl = input("Enter location:  ")
jp = input("Enter page:  ")

a = get_job_dataset(jq,jl,jp)
print("Total jobs : ",total_job_count)
print("------------------------------")
print(a)
