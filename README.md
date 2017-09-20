mpharrigan.github.io
====================

[http://mpharrigan.com](http://mpharrigan.com)

My personal website hosted using Github pages with Jekyll

Building
--------

Make sure these are installed:

 - Node.js
 - Ruby
 - Python
 
Then get dependencies

    gem install bundler
    bundle install
    npm install
    
and run a little script to compile the css and
copy things over to the `assets/` directory

    python build.py

Host a dev version of the site with

    ./jekyll.sh
    
which just does

    bundle exec jekyll serve --incremental
