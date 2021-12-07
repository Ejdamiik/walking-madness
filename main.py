from flask import Flask, request, send_from_directory, render_template
from typing import Tuple, Callable


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.static_folder = r'frontend\static'


#---------------------Page-getters-------------------------------------------#

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path: str) -> str:
    """
    HTTP response for other actions
    """

    if (len(path) == 0):

        return send_from_directory('frontend', 'index.html')

    return send_from_directory('frontend', path)

#---------------------Page-getters-------------------------------------------#

app.run()
