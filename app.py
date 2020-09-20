from packages.packages import *

if __name__ == '__main__':
    # socketio.run(app, host='0.0.0.0', port=5000)
    socketio.run(app)
    # app.run(debug = True)
    # app.run(host='192.168.43.209', port="5000")
    # app.run(debug=True, ssl_context = ('cert.pem', 'key.pem'), host='192.168.43.209', port=5000)