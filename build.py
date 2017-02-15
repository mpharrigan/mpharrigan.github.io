from subprocess import run
import shutil
import re

run(['scss', '--load-path', 'node_modules/bootstrap/scss', 'scss/mph.scss', 'assets/style.css'])
run(['node_modules/.bin/postcss', '--use', 'autoprefixer', '--replace', 'assets/style.css'])

with open('node_modules/pygments-css/default.css') as inf, open('assets/pygments.css', 'w') as outf:
    outf.write(re.sub(r'codehilite', r'highlight', inf.read()))

shutil.copy2('node_modules/bootstrap/dist/js/bootstrap.min.js', 'assets/bootstrap.min.js')
shutil.copy2('node_modules/jquery/dist/jquery.min.js', 'assets/jquery.min.js')
