from local import hello

"""
Use imported method to respond.
"""
def hello_world(request):
    return hello.say_hello()
