from flask import Flask, render_template


app = Flask('simple app')


@app.route('/home', methods=['GET'])
def hello():
    return 'hello'


@app.route('/get_name/<name>', methods=['GET'])
def get_name(name):
    return name


@app.route('/<user>/<project>/get_gallery', methods=['GET'])
def get_gallery(user, project):
    if user == 'bob':
        if project == 'cats':
            return 'rof: siami, dom: black, gon: egyption'
    return 'not found', 404


@app.route('/<user>/<project>/get_credits', methods=['GET'])
def get_credits(user, project):
    if user == 'bob' and project == 'store':
        return '{} credits'.format(50)
    return 'not found', 404


@app.route('/simple_html', methods=['GET'])
def simple_html():
    return '''
    <div>
      <h1>Big</h1>
      <h3>med</h3>
      <h6>s</h6>
    </div>
    '''


@app.route('/temp/<name>', methods=['GET'])
def temp(name):
    return render_template('template.html', name=name)


app.run()
