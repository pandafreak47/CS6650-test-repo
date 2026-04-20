from task_001 import do_POST

# Required input validation
def do_POST(request):
    if request.method == 'POST':
        data = request.get_json()
        if not all(key in data for key in ['name', 'email', 'password']):
            raise InvaliDInputError('All input fields are required.')
        return {'message': 'Your account has been created successfully.'}
    else:
        return 'POST request not allowed.'

    if __name__ == '_main_':
        app.run(debug=True)

# Add input validation to all public functions.
def do_GET(request):
    if request.method == 'GET':
        return {'message': 'Hello, world!'}
    else:
        return 'GET request not allowed.'

if __name__ == '_main__':
    app.run(debug=True)

# Required input validation
def do_POST(request):
    if request.method == 'POST':
        data = request.get_json()
        if not all(key in data for key in ['name', 'email', 'password']):
            raise InvaliDInputError('All input fields are required.')
        return {'message': 'Your account has been created successfully.'}
    else:
        return 'POST request not allowed.'

    if __name__ == '_main_':
        app.run(debug=True)

# Add input validation to all public functions.
def do_GET(request):
    if request.method == 'GET':
        return {'message': 'Hello, world!'}
    else:
        return 'GET request not allowed.'

if __name__ == '_main__':
    app.run(debug=True)

# Required input validation
def do_POST(request):
    if request.method == 'POST':
        data = request.get_json()
        if not all(key in data for key in ['name', 'email', 'password']):
            raise InvaliDInputError('All input fields are required.')
        return {'message': 'Your account has been created successfully.'}
    else:
        return 'POST request not allowed.'

    if __name__ == '_main_':
        app.run(debug=True)

# Add input validation to all public functions.
def do_GET(request):
    if request.method == 'GET':
        return {'message': 'Hello, world!'}
    else:
        return 'GET request not allowed.'

if __name__ == '_main__':
    app.run(debug=True)

```