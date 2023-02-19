import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-todos',
  templateUrl: './todos.component.html',
  styleUrls: ['./todos.component.css'],
})
export class TodosComponent implements OnInit {
  todo:string  = '';
  todos:Array<TodoItem> = [];

  constructor() {}
  ngOnInit() {}

  addTodo() {
    if(this.todo.length==0){return;}else{
    const newTodo =new TodoItem(this.todo,'active');
    this.todos.push(newTodo);
    this.todo = '';
  }
  }
  markAsComplete(todo: { status: string; }) {
    todo.status = 'completed';
  }

  undo(todo: { status: string; }) {
    todo.status = 'active';
  }
  delete(item:TodoItem) {
    const index = this.todos.indexOf(item);
    if (index > -1) {
      this.todos= this.todos.slice(0, index).concat(this.todos.slice(index + 1));

    }
   console.log(this.todos.length)
  }

}
export class TodoItem{
  name: string;
  status:string;
  constructor(name:string,status:string) {
    this.name=name;
    this.status=status;
  }
}
