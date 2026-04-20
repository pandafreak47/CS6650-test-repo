from task_001 import do_POST
def do_POST(request):
    if request.method == 'POST':
        data = request.get_json()
        if not all(key in data for key in ['name', 'email', 'password']):
            raise InvalidInputError('All input fields are required.')
        return {'message': 'Your account has been created successfully.', 'token': create_token(data)}
    else:
        return 'POST request not allowed.'

if __name__ == '__main__':
    app.run(debug=True)