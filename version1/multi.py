#multithreading requests
import requests
import time
import threading
import random
def req1():
    url = ["https://www.indeed.co.in/viewjob?jk=30360000f6a80209&tk=1d230eet99mgl800&from=serp&vjs=3&advn=1843736485120977&adid=261703868&sjdu=0ZFwD5rbjMRcHz87Kzx_g8vtnJAGSOaP8RyL3yj9HeeQS1STkN1gCy_-HtMsk6ywKuwRRIAi-F1DtnErdv_tQ0SSJTk-p3fvJ8JnKAg2kyxaZ5ETrWSD9TYvaIPtYcdi-7N1KMx_7cybvr1lkty4GXHLhNNHsUSbYmWE2GXOrm8",
    "https://www.indeed.co.in/viewjob?jk=2ad7810002aeee26&tk=1d230ef869mgl800&from=serp&vjs=3&advn=1843736485120977&adid=261704293&sjdu=0ZFwD5rbjMRcHz87Kzx_g8vtnJAGSOaP8RyL3yj9HeeQS1STkN1gCy_-HtMsk6ywKuwRRIAi-F1DtnErdv_tQ0SSJTk-p3fvJ8JnKAg2kyxaZ5ETrWSD9TYvaIPtYcdicdkMwyH1KrV4qtL0_HMFjXHLhNNHsUSbYmWE2GXOrm8",
    "https://www.indeed.co.in/viewjob?jk=66d0ffeda5163775&from=serp&vjs=3"]
    res = requests.get(url[random.randint(0,2)])
    

def req2():
    url = [
        "https://www.dice.com/jobs/detail/SAP-Software-Engineer-Moody%27s-Corporation-New-York-NY-10001/RTL107782/13909BR",
        "https://www.dice.com/jobs/detail/Software-Engineer-IBG%2C-LLC-New-York-NY-10001/10340106/1824",
        "https://www.dice.com/jobs/detail/Java-Software-Engineer-JPMorgan-Chase-%26-Co.-Brooklyn-NY-11202/10125746/180107044"
    ]
    res = requests.get(url[random.randint(0,2)])
    

def req3():
    url = [
        "https://www.idealist.org/en/nonprofit/11a57fbe3ef94e328d0209831bd4f00d-american-civil-liberties-union-new-york",
        "https://www.idealist.org/en/social-enterprise-job/b43db666f6964693a16b4b142fa23602-field-engineer-data-acquisition-group-carbon-lighthouse-new-york",
        "https://www.idealist.org/en/nonprofit-job/29ca01ca6a544084b334bd28498b8163-associate-director-of-development-adl-new-york-regional-office-anti-defamation-league-new-york"
    ]
    res = requests.get(url[random.randint(0,2)])


t1 = threading.Thread(target=req1) 
t2 = threading.Thread(target=req2) 
t3 = threading.Thread(target=req3) 

#calc time

start = time.time()


t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end = time.time()

total = end - start
print(str(total))
