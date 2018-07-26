from prototype import create_app


def test_config():
	assert(not create_app().testing)
	assert create_app({'TESTING':True}).testing

def hello(client):
	response = client.get('/hello')
	assert response.data == 'Hello, World!'
