import base64, os, uuid, time, hashlib, gzip
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/kontol', methods=['POST'])
def kontol():
  form = request.form
  if 'code' in form and 'py_v' in form:
    py_v = form['py_v']
    if py_v in ['3','2']:
      path_root = '.caches-exec'
      path = f'{path_root}/{hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()}'
      os.makedirs(path, exist_ok=True)
      fname1 = f'{path}/{uuid.uuid4()}{time.time()}'
      fname2 = f'{path}/{uuid.uuid4()}{time.time()}'
      with open(fname1, 'w') as f:
        f.write(f'exec(base64.b64decode(__import__("sys").argv[1].decode()))')
      os.system(f'python{py_v} {fname1} {base64.b64encode(form["code"].encode()).decode()} 2> /dev/null > {fname2}')
      try:
        with open(fname2, 'r') as f:
          result = f.read()
        try: os.remove(path_root)
        except: pass
        finally: return result
      except Exception as e:
        return str(e)

  return abort(404)