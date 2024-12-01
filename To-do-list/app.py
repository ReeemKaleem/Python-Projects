#class -to do list
##create tasks, view tasks, update status of tasks ,delete tasks 
## storing all our to-dos in json file 
##good using colors and ascii art .. and using inquirer to avoid manual typing 
#exit options so that when 

#fulture enhancements 
#add more features to make it complex and different from others


import json 
from datetime import datetime
from termcolor import colored
import pyfiglet
import inquirer

#creating a class 
class ToDoList:
    file_path = 'data.json' #class variable 
    #constructor 
    def __init__(self, name ,desc ,datestart=None,status=False):
        self.name=name 
        self.desc=desc
        self.datestart= datestart if datestart else str(datetime.now().date())
        self.status = status
    ##dunder methods in python  also called magic method 
    def __str__(self):#print __repr__()
        #we can customise how we want to see the output 
        status_str ='Completed' if self.status else 'pending'
        return (f"ToDo:{self.name}\n"
                f"Description:{self.desc}\n"
                f"Start Date:{self.datestart}\n"
                f"Status:{status_str}\n"
                )


    #read_data,add task, deletetask, updatestatus
    ## addding task:create an object 
    #since we're data in json ,reading data, deleting tasks from datafile,update 
    #obj1 ,obj2,view tasks
    @staticmethod
    #doent depend upon the objects created 
    def readdata():
        try:
            with open(ToDoList.file_path,"r") as file:
                #json.load json->object 
                #json.dump object -> json
                return json.load(file)
        except Exception as e:
            return []
        
    @staticmethod
    def loadtasks():
        """
        [
        {name1 : to-do1,description :a,shdgygys,datetime:30th november,status :pending}
        {name2 : to-do1,description :a,shdgygys,datetime:30th november,status :pending}
        {name3 : to-do1,description :a,shdgygys,datetime:30th november,status :pending}
        ]
        [**] ->used for unpacking the dictionary/iterable
        def 
        """
        data=ToDoList.readdata()
        return [ToDoList(**task) for task in data]
        #create object

    def addtask(self):
        data = ToDoList.readdata()
        data.append(self.__dict__)#{name :todo, desc :defk,datestart:30-11-2024}
        try :
            with open(ToDoList.file_path,"w") as file:
                json.dump(data,file,indent=2)
        except Exception as e:
            print(e)

    #reading , adding tasks 
    @staticmethod
    def deletetask(index):
        data=ToDoList._read_data()
        try:
            data.pop(index-1)
            with open(ToDoList.file_path,"w") as file:
                json.dump(data,file,indent=2)
        except IndexError:
            print(f"Error :no task at index{index}")
        except Exception as e:
            print(e)

    #changing status 
    @staticmethod 
    def updatestatus(index,new_status):
        data=ToDoList._read_data()
        try:
            data[index-1]['status'] = new_status
            with open(data,"w") as file:
                json.dump(data,file,indent=2)
        except IndexError:
            print(f"Eroor :no task at index{index}")
        except Exception as e :
            print(e)

def main():
    while True :
        print(colored(pyfiglet.figlet_format("To-Do List"),"cyan"))
        menu =[
            inquirer.List(
                'choice',
                message="what do you want to do?",
                choices=[
                    "Add Task",
                    "View Task",
                    "Delete Task",
                    "Exit"
                ]
            )
        ]
        choice = inquirer.prompt(menu)['choice']

        if choice == "Add Task":
            name=input(colored("enter the task name","green"))
            desc=input(colored("enter task description","green"))
            task =ToDoList(name,desc)
            task.addtask()
            print(colored("task added successfully","yellow"))

        if choice == "View Task":
            tasks =ToDoList.loadtasks()
            for index, task in enumerate(tasks, start=1):
                '''
                task 1
                -----------
                '''
                print(colored(f"\n Task {index}:\n{'-'*20}\n{-*20},blue"))
        elif choice == "Delete Task":
            index=int(input(colored("enter the task index to be deleted","red")))
            ToDoList.deletetask(index)
        elif choice=="Update Status":
            index=int(input(colored("enter the task to update"),"red"))
            status =inquirer.prompt([inquirer.List('status',message="do you want to enter task enter new status",choices=['true',false])])
            ['status']=="true"
            ToDoList.updatestatus(index,status)
            print(colored("Task update dsuccessfully","green"))

        elif choice =="Exit" :
            print(colored("exiting the program","red"))

#run this code only when told to 
#orelse when we import the file it will run inorder to overcome this the code below is used
if __name__ == '__main__':
    main()

        

            
