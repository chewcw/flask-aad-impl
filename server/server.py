import os
from dotenv import load_dotenv
from flask import Flask
from pathlib import Path
from flask_azure_oauth import FlaskAzureOauth

# environment file
load_dotenv()

# application
app = Flask(__name__)
# for hot reloading
app.debug = True
# configuration
app.config['AZURE_OAUTH_TENANCY'] = os.environ['AZURE_OAUTH_TENANCY']
app.config['AZURE_OAUTH_APPLICATION_ID'] = os.environ['AZURE_OAUTH_APPLICATION_ID']
app.config['AZURE_OAUTH_CLIENT_APPLICATION_IDS'] = os.environ['AZURE_OAUTH_CLIENT_ID']

auth = FlaskAzureOauth()
auth.init_app(app=app)

@app.route('/api/unprotected')
def unprotected():
    return 'this is public route without protection'

@app.route('/api/protected')
@auth()
def protected():
    return 'hahahaah, this is protected route without scope specified'

@app.route('/api/all')
@auth('All.Information')
def test():
	return 'hahahahah, this is protected route with scope `all` specified'

if __name__ == '__main__':
	app.run(port=8000)