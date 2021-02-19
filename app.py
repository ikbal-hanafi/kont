import base64, subprocess as s
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/exec', methods=['POST'])
def exec_():
  form = request.form
  if "code" in form and "py_v" in form:
    print(code)
    code = base64.b64encode(form["code"].encode("utf-8")).decode()
    py_v = form["py_v"]
    
    try:
      return s.check_output(['python%s' % py_v, '-c', 'exec(__import__("base64").b64decode("%s".encode()).decode())' % code, '2>', '/dev/null'])
    except Exception, e:
      return str(e)

  return abort(404)