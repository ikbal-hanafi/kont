import base64, os, uuid, time
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/kontol', methods=['POST'])
def kontol():
  form = request.form
  if 'code' in form and 'py_v' in form:
    py_v = form['py_v']
    if py_v in ['3','2']:
      fname1 = f'.kontol{uuid.uuid4()}{time.time()}'
      fname2 = f'.memek{uuid.uuid4()}{time.time()}'
      with open(fname1, 'w') as f:
        f.write(form['code'])
      os.system(f'python{py_v} {fname1} 2> /dev/null > {fname2}')
      try:
        with open(fname2, 'r') as f:
          result = f.read()
        os.remove(fname1)
        os.remove(fname2)
        return result
      except Exception as e:
        return str(e)

  return abort(404)