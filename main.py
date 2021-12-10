from flask import Flask, request, send_from_directory, render_template, send_file
from io import BytesIO
import backend.input_handle as ih
import backend.draw as draw


def serve_pil_image(img):
  """
  Allows to save PIL image object to a
  virtual file in memory and then return
  it as a HTTP response
  """

  img_io = BytesIO()
  img.save(img_io, 'PNG', quality=70)
  img_io.seek(0)
  return send_file(img_io, mimetype='image/png')


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

#--------------------App-functionality---------------------------------------#
@app.route('/get_output', methods=['post'])
def get_output():

    inpt = request.form.get('user-input')
    width = int(request.form.get('im-width'))

    tree = ih.get_tree(inpt)
    draw_obj = draw.DrawTree(width, width, tree)
    im = draw_obj.get_image()

    return serve_pil_image(im)



app.run()
