import base64, subprocess as s
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/exec', methods=['POST'])
def exec_():
  form = request.form
  if "code" in form and "py_v" in form:
    code = base64.b64encode(form["code"].encode("utf-8")).decode()
    py_v = form["py_v"]
    result = s.getoutput(f'python{py_v} -c \'exec(__import__("base64").b64decode("{code}".encode()).decode())\' 2> /dev/null')

    with open('file.txt', 'a') as f:
      f.write(f'{py_v}{repr(result)}\n\n')

    return result

  return abort(404)