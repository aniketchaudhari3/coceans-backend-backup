from flask import *
from collector import *
from os import system as sys
app = Flask(__name__)

@app.route('/')
def index():   
    return 'careeroceans web api'

@app.route('/file')
def file():
   return sys('cat ../indeed_test3.py')

@app.route('/api', methods=['GET'])
def api():
    job_query = request.args.get('q')
    job_location = request.args.get('l')
    job_page = request.args.get('page')
    print("job query: ",job_query)
    print("job location: ",job_location)
    print("job page: ",job_page)

    return jsonify(get_job_dataset(job_query, job_location,job_page)[0])
app.run(host='0.0.0.0',port='80')
