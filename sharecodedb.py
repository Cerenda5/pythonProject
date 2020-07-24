#!/usr/bin/env python3

from flask import Flask, request, render_template, \
                  redirect


from model_sqlite import createTables, \
                         createCode, \
                         getCode, \
                         getAllCode, \
                         updateCode, \
                         createUser, \
                         getUser

app = Flask(__name__)
createTables()

@app.route('/')
def index():
    return render_template('index.html', data = getAllCode())

@app.route('/create')
def create():
    uid = createCode()
    return redirect("{}edit/{}".format(request.host_url,uid))
    
@app.route('/edit/<string:uid>/')
def edit(uid):
    row = getCode(uid)
    if row is None:
        return render_template('error.html',uid=uid)
    d = dict( uid=uid, code=row[0], lang=row[1],
              url="{}view/{}".format(request.host_url,uid))
    return render_template('edit.html', **d) 

@app.route('/publish',methods=['POST'])
def publish():
    code = request.form['code']
    uid  = request.form['uid']
    lang = request.form['lang']
    updateCode(uid,code,lang)
    return redirect("{}{}/{}".format(request.host_url,
                                     request.form['submit'],
                                     uid))

@app.route('/view/<string:uid>/')
def view(uid):
    row = getCode(uid)
    if row is None:
        return render_template('error.html',uid=uid)
    d = dict( uid=uid, code=row[0], lang=row[1],
              url="{}view/{}".format(request.host_url,uid))
    return render_template('view.html', **d)

@app.route('/admin/')
def admin():
    pass

if __name__ == '__main__':
    app.run(debug=True)

