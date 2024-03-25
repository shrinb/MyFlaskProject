from flask import Flask, jsonify, render_template
app = Flask(__name__)
#Step-1: Load the hn_logs TSV file as hn_logs list 
tsv_path='/Users/shrin/Downloads/Python/hn_logs.tsv'
hn_logs=[]
with open(tsv_path, 'r') as tsv_file:
    for line in tsv_file:
        timestamp, query = line.strip().split('\t')    #Given: Each line contains a timestamp and a query separated by a tab.
        hn_logs.append((timestamp, query))
#Step-2: Welcome page or Home page
@app.route('/')     
def Welcome():
    return render_template('Welcome.html')
#Step-3: Page to display the Distinct Query Count json object
@app.route('/1/queries/count/<date_prefix>', methods=['GET']) 
def get_distinct_query_count(date_prefix): 
    distinct_query = set()        #set() : to obtain distinct queries
    for timestamp, query in hn_logs:
        if timestamp.startswith(date_prefix):  #check if it's a part of given time range
            distinct_query.add(query)
    return jsonify({'Count Of Distinct Queries ': len(distinct_query)})

if __name__ == '__main__':
    app.run(debug=True)