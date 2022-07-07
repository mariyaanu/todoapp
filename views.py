#authentication
#login
#view for listing all todos
#view for fecting a specific todoapp
#list all todos created by authenticated user
#view for updating a specific todos
#view deleting a specific todoapp
#logout
#
from todoapp.models import users,todos

username="anu"
password="Password@123"





def authenticate(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user_data=[user for user in users if user["username"]==username and user["password"]==password]
    return user_data

session={} #details of loged user


def loginin_reqried(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            raise Exception("u must login")
    return wrapper

@loginin_reqried
def logged_user():
    username=session.get("user")
    user_id=[user for user in users if user["username"]==username][0]
    return user_id


class LoginView:

    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authenticate(username=username,password=password)
        if user:
            print("sucess")
            session["user"]=username
        else:
            print("faill")

@loginin_reqried
def logout(*args,**kwargs):
    session.pop("user")


class TodoListView:
    @loginin_reqried
    def get(self,*args,**kwargs):
        return todos

tv=TodoListView()
try:
    all_todos=tv.get()
except Exception as e:
    print(e)

class MyTodoView:
    @loginin_reqried
    def get(self,*args,**kwargs):
        username=session.get("user")
        userId=[user ["id"] for user in users if user["username"]==username][0]
        my_task=[todo for todo in todos if todo["userId"]==userId]
        return my_task

class TodoDetailView:
    @loginin_reqried
    def get(self,*args,**kwargs):
        todoId=kwargs.get("todoId")
        qs=[t for t in todos if t.get("todoId")==todoId]
        return qs
    def put(self,id=None,*args,**kwargs):

        todo=[todo for todo  in todos if todo.get("id")==id][0]
        userId=kwargs.get("userId")
        task_name=kwargs.get("task_name")
        completed=kwargs.get("completed")
        todo["userId"]=userId
        todo["task_name"]=task_name
        todo["completed"]=completed
        print(todo)

    def delete(self,*args,**kwargs):
        todoId=kwargs.get("todoId")
        data=[todo for todo in todos if todo["todoId"]==todoId]
        if data:
            todo=data[0]
            todos.remove(todo)
            print("todo removed")
            print(len(todos))


lv=LoginView()
lv.post(username="anu",password="Password@123")
print(session)

# logout()
# print(session)


tv=TodoListView()
all_todos=tv.get()
for tv in all_todos:
    print(tv)


todo=MyTodoView()
print(todo.get())

details=TodoDetailView()
print(details.get(todoId=7))



details.put(todoId=7,userId=4,task_name="mobilerecharge",completed=True)

details.delete(todoId=5)


# logout()
# print(session)
#













