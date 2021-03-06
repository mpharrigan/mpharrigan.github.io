from subprocess import run as _run, PIPE
import sys
import shutil
import re
import os

if sys.platform == 'win32':
    def run(args):
        cp = _run(args, shell=True, stderr=PIPE, stdout=PIPE)
        if cp.returncode:
            print(cp.stdout)
            raise RuntimeError(cp.stderr)
else:
    run = _run

run(['scss',
     '--load-path', 'node_modules/bootstrap/scss',
     '--sourcemap=none',
     '--style', 'compressed',
     'scss/mph.scss', 'assets/style.css'])
run([os.path.join('node_modules','.bin', 'postcss'), '--use', 'autoprefixer', '--replace', 'assets/style.css'])

with open('node_modules/pygments-css/default.css') as inf, open('assets/pygments.css', 'w') as outf:
    outf.write(re.sub(r'codehilite', r'highlight', inf.read()))

shutil.copy2('node_modules/bootstrap/dist/js/bootstrap.min.js', 'assets/bootstrap.min.js')
shutil.copy2('node_modules/jquery/dist/jquery.min.js', 'assets/jquery.min.js')
shutil.copy2('node_modules/popper.js/dist/umd/popper.js', 'assets/popper.js')
