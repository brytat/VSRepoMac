import React, { useState } from 'react';
import './App.css';
import Todo from "./components/Todo";

function App() {
  const [newTodo, setNewTodo] = useState(""); 
  const [todos, setTodos] = useState([]);

  const handleNewTodoSubmit = (event) => {
    event.preventDefault();
    console.log(event);

    if (newTodo.length === 0) {
      return;
    }

    const todoItem = {
      text: newTodo,
      complete: false
    };

    setTodos([...todos, todoItem]);
    setNewTodo("");
  };

  const handleDelete = (deletedIndex) => {
    const filteredTodos = todos.filter((_todo, i) => {
      return i !== deletedIndex;
    });

    setTodos(filteredTodos);
  }

  const handleToggleComplete = (index) => {
    const updatedTodos = todos.map((todo, i) => {
      if (index === i) {
        todo.complete = !todo.complete;
        //Extra level to avoid mutating todo directly. This is best practice.
        // const updatedTodo = { ...todo, complete: !todo.complete };
        // return updatedTodo;
      }
      return todo;
    });
    setTodos(updatedTodos);
  }

  return (
    <div style={{textAlign: "center"}}>
      <form
        onSubmit={(event) => {
          handleNewTodoSubmit(event);
        }}
      >
        <input
          onChange={(event) => {
            setNewTodo(event.target.value);
          }}
          type="text"
          value={newTodo}
        />
        <div>
          <button>Add</button>
        </div>
      </form>

      <hr />

      {todos.map((todo, i) => {
        return (
          <Todo
            key={i}
            i={i}
            todo={todo}
            handleToggleComplete={handleToggleComplete}
            handleDelete={handleDelete}
          />
        );
      })}
    </div>
  );
}

export default App;
