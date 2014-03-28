from bottle import route, run

@route('/object/<id:int>')
def callback(id):
    assert isinstance(id, int)
		
run(host='localhost', port=8000, debug=True)	
