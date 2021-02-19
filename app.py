import base64, subprocess as s
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/exec', methods=['POST'])
def exec_():
  form = request.form
  if "code" in form and "py_v" in form:
    code = repr(repr(base64.b64encode(form["code"].encode("utf-8")).decode()))
    py_v = form["py_v"]

    return s.check_output("python%s -c 'import base64; exec(base64.b64decode({%s.encode()).decode())' 2> /dev/null " % (py_v, code))

  return abort(404)