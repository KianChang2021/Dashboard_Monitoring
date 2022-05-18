from flask import render_template,Flask

app=Flask(__name__,template_folder='ui')
@app.route('/Main/')
def main():
    return render_template('Main.html')


if __name__ == '__main__':
    # app.debug = True
    # app.run()
    serve(app, host="0.0.0.0", port=8084)
