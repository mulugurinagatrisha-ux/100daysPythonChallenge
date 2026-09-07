# Global variable
message = "Hello from Global Scope"

def show_scope():
    print("Global Variable:", globals()["message"])
    message = "Hello from Local Scope"
    print("Local Variable:", message)
show_scope()
print("Global Variable Outside Function:", message)