#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, render_template
import os, json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

jsons_name = os.listdir("/home/shiyanlou/files")
with open(os.path.join("/home/shiyanlou/files",jsons_name[0]), 'r') as f:
    world = json.loads(f.read())
with open(os.path.join("/home/shiyanlou/files",jsons_name[1]), 'r') as f:
    shiyanlou = json.loads(f.read())
#filename = 'helloworld'
#afile = os.path.join("/home/shiyanlou/files","{}.json".format(filename))
#if os.path.isfile(afile):
#    with open(afile, 'r') as f:
#        file_info = json.loads(f.read())
    
#print(file_info)
#print(os.path.isfile(os.path.join("/home/shiyanlou/files","{}.json".format(filename))))

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

@app.route('/')
def index():
    return render_template('index.html',a = world, b = shiyanlou )

@app.route('/files/<filename>')
def file(filename):
    
    #afile = os.path.join("/home/shiyanlou/files","{}.json".format(filename))
    #if os.path.isfile(afile):
        
     return render_template('file.html',filename = filename,world = world,shiyanlou=shiyanlou)
   




