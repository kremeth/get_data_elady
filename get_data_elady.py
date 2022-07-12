import pandas as pd
import glob
import os
import requests
import io
import flask


app = flask.Flask(__name__)

# Get the first 50 items
@app.route('/')
@app.route('/home')
def home():
    return 'waiting'

@app.route('/50')
def fifty():
    # Get the csv
    print(1)
    r = requests.get('https://dropshipping.elady.com/dropshipping/api_item.php?login=drapi4749sb&password=vtx9nE7VnHcP')

    # Turn the content into a pandas dataframe
    data = pd.read_csv(io.StringIO(r.content.decode('utf-8')))
    # Filter out the items that are not BAGS
    data = data[data['category'] == 'BAGS']
    data.reset_index(inplace=True, drop=True)
    return data.iloc[:50, :]

if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()
