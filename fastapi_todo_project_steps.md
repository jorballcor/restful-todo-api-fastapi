
# 📝 Project Guide: FastAPI Todo REST API

This guide outlines the key steps and concepts involved in building a basic Todo API using **FastAPI**, focusing on understanding the *why* behind each step.

---

## 🔧 Step 1: Set Up the Project Environment

**Why**: Isolate dependencies and create a clean workspace.

- Create a project folder: `todo_app`
- Initialize a Python virtual environment
- Install FastAPI and Uvicorn (the server)

---

## 🚦 Step 2: Create a Basic FastAPI App

**Why**: Define the entry point of your application and configure your first route.

- Create `main.py` and initialize FastAPI
- Add a base route (GET `/`) to confirm it's working
- Start the server with `uvicorn main:app --reload`

---

## 🗃️ Step 3: Design Your Data Model

**Why**: Define what a "Todo" means—structure the data you're handling.

- Define fields like `id`, `title`, `description`, `completed`
- Use Pydantic to create a Todo schema
- Enforce data validation automatically

---

## 🔄 Step 4: Implement CRUD Operations

**Why**: Provide full interaction with the Todo list using standard HTTP verbs.

| Action        | Method | URL             |
|---------------|--------|------------------|
| Create Todo   | POST   | `/todos`         |
| Read Todos    | GET    | `/todos`         |
| Read by ID    | GET    | `/todos/{id}`    |
| Update Todo   | PUT    | `/todos/{id}`    |
| Delete Todo   | DELETE | `/todos/{id}`    |

---

## 📦 Step 5: Use In-Memory Storage

**Why**: Start simple without a database to focus on logic and endpoints.

- Use a Python list or dictionary to store todos
- Generate and manage unique IDs manually

---

## 🔍 Step 6: Test the API

**Why**: Validate that the API behaves correctly and returns the right responses.

- Use Postman or curl to:
  - Create new todos
  - Fetch todos
  - Update existing todos
  - Delete todos
- Observe HTTP status codes and JSON responses

---

## 📄 Step 7: Explore Auto-Generated Docs

**Why**: FastAPI provides Swagger UI for interactive documentation.

- Access the docs at `http://127.0.0.1:8000/docs`
- Try out each endpoint directly from the browser

---

## ✅ Learning Goals

After completing this project, you should be able to:

- Explain what a RESTful API is
- Understand CRUD operations and HTTP methods
- Handle request bodies and URL parameters
- Return appropriate status codes and responses
- Test endpoints using tools like Postman or curl

---

Use this guide as a checklist to reinforce your understanding as you build!
