class Task:
    id = 1
    
    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.id = Task.id 
        self.status = "NOT FINISHED"
        
        Task.id += 1
        
        
    def mark_finished(self):
        self.status = "FINISHED"
    
    
    def is_finished(self):
        if self.status != "FINISHED":
            return False
        else:
            return True
    
    
    def __str__(self):
        return f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.status}'
    
    
class OrderBook(Task):
    def __init__(self):
        self.tasks = []

    
    def add_order(self, description, programmer, workload):
        task = Task(description, programmer, workload)
        self.tasks.append(task)

    
    def all_orders(self):
        return self.tasks

    
    def programmers(self):
        programmers_set = {task.programmer for task in self.tasks}
        return list(programmers_set)
    
    
    def mark_finished(self, id: int):
        for task in self.tasks:
            if task.id == id:
                task.mark_finished()
                return
        
        raise ValueError(f"No task found with ID: {id}")
    
    
    def finished_orders(self):
        return [task for task in self.tasks if task.is_finished()]
    
    
    def unfinished_orders(self):
        return [task for task in self.tasks if not task.is_finished()]
    
    
    def status_of_programmer(self, programmer: str):
        programmer_tasks = [task for task in self.tasks if task.programmer == programmer]
        
        if not programmer_tasks:
            raise ValueError(f"No tasks found for programmer: {programmer}")
        
        finished_count = 0
        unfinished_count = 0
        finished_workload = 0
        unfinished_workload = 0

        for task in programmer_tasks:
            if task.is_finished():
                finished_count += 1
                finished_workload += task.workload
            else:
                unfinished_count += 1
                unfinished_workload += task.workload
        
        return (finished_count, unfinished_count, finished_workload, unfinished_workload)

class Application:
    def __init__(self):
        self.order_book = OrderBook()
        
        
    def print_commands(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")
    
    
    def add_order(self):
        description = input("description: ")
        name_workload = input("programmer and workload estimate: ")
        programmer = name_workload.split(" ")[0]
        try:
            workload = int(name_workload.split(" ")[-1])
            self.order_book.add_order(description, programmer, workload)
            print("added!\n")
        except ValueError:
            print("erroneous input\n")
        
    
    def print_finished(self):
        tasks = self.order_book.finished_orders()
        if not tasks:
            print("no finished tasks\n")
        for task in tasks:
            print(task)
        print()
    
    
    def print_unfinished(self):
        tasks = self.order_book.unfinished_orders()
        if not tasks:
            print("No unfinished tasks!\n")
        for task in tasks:
            print(task)
        print()
        
        
    def mark_finished(self):
        try:
            id = int(input("id: "))
            self.order_book.mark_finished(id)
            print("marked as finished\n")
            
        except ValueError:
            print("erroneous input\n") 
        
    
    def print_programmers(self):
        programmers = self.order_book.programmers()
        for name in programmers:
            print(name)
        print()
        
        
    def print_status(self):
        try:
            name = input("programmer: ")
            status = self.order_book.status_of_programmer(name)
            print(f'tasks: finished {status[0]} not finished {status[1]}, hours: done {status[2]} scheduled {status[3]}')
            print()
        except KeyError:
            print("erroneous input\n")
    
    
    def run(self):
        while True:
            self.print_commands()
            try:
                command = int(input("command: "))
                if command == 0:
                    break
                elif command == 1:
                    self.add_order()
                elif command == 2:
                    self.print_finished()
                elif command == 3:
                    self.print_unfinished()
                elif command == 4:
                    self.mark_finished()
                elif command == 5:
                    self.print_programmers()
                elif command == 6:
                    self.print_status()
                    
            except ValueError:
                print("erroneous input\n")
        
    
application = Application()
application.run()