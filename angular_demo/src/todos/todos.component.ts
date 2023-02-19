import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-todos',
  templateUrl: './todos.component.html',
  styleUrls: ['./todos.component.css'],
})
export class TodosComponent implements OnInit {
  todo:string  = '';

  todos:any = [];

  constructor() {}

  ngOnInit() {}

  addTodo() {
    if(this.todo.length==0){return;}else{
    const newTodo = { todo: this.todo, status: 'active' };
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
}
