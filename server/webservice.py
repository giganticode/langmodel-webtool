import argparse
from flask import Flask, redirect

PORT = 3000
app = Flask(__name__, static_folder='')

@app.route('/')
def default():
    return redirect("/home", code=302)

@app.route('/home')
def home_page():
    return app.send_static_file('static/index.html')

@app.errorhandler(404) #redirect 404 errors to the client (VueJS)
def page_not_found(e):
    return app.send_static_file('static/index.html')    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', default=False, action='store_false', help='Start the server in debug mode.')
    parser.add_argument('-p', '--port', default=PORT, type=int, action='store', help='Set the port for of the web server.')
    parser.add_argument('-sh', '--serverhost', default='127.0.0.1', type=str, action='store', help='Set the host of the web server.')
    args = parser.parse_args()

    port = args.port
    debug = args.debug
    host = args.serverhost

    print("Starting Web-Tool on host " + host + ", Port " + str(port))
    print("Debug ", debug)

    app.run(use_reloader=debug, port=port, debug=debug, host=host)
