Day 3 – Backend Server, Async & API Design
Today's goal is to understand how a backend server works, how it handles multiple requests, and how we design secure and efficient APIs.
1. What is a Server?
A server is a computer or software that receives requests from clients, processes them, and sends back responses.

Example: When you log in to Instagram, your app sends a request to the backend server, and the server verifies your login details.
  Client (Browser/App)
          |
          | Request
          ▼
     Backend Server
          |
          ▼
       Database
          |
          ▼
     Backend Server
          |
          | Response
          ▼
     Client (Browser/App)


2. Blocking vs Non-Blocking Execution
Blocking: The program waits for one task to finish before moving to the next task.

Non-blocking: The program can continue executing other tasks while waiting for a task to complete.

Example:
- Blocking: You order food and wait at the counter until it is ready.
- Non-blocking: You order food, receive a token, and do other work while waiting.
Blocking:
Task 1 ─────── Task 2 ─────── Task 3

Non-Blocking:
Task 1 ─────── Waiting
Task 2 ─────── Task 3


3. Sync vs Async Concepts
Synchronous (Sync): Tasks execute one after another. The next task waits for the previous task to finish.

Asynchronous (Async): A task can start and wait for a result without stopping other work from progressing.

Example:
- Sync: Download a file and wait until it finishes before doing anything else.
- Async: Start downloading a file and continue browsing while it downloads.
Sync:
Task A → Task B → Task C

Async:
Task A → Start Task B
       → Continue Task C
       → Task B completes later


4. Event Loop Basics
The Event Loop is a mechanism used by JavaScript to manage asynchronous operations without blocking the main thread.

It checks whether the call stack is free and executes callbacks waiting in the task queues.

Example: When your backend fetches data from a database, the event loop allows other operations to continue while waiting for the database response.








dev.to


Simple flow:
Call Stack
    |
    ▼
Async Operation
    |
    ▼
Waiting for Result
    |
    ▼
Callback / Promise Queue
    |
    ▼
Event Loop
    |
    ▼
Call Stack executes callback


5. Routing and Middleware
Routing: Routing decides which function should handle a particular API request.

Example:
- /users → Get users
- /login → Login user
- /products → Get products
Middleware: Middleware is a function that runs between receiving a request and sending a response.

It can check authentication, validate data, log requests, and handle errors.
Client Request
      |
      ▼
  Middleware
      |
      ▼
    Router
      |
      ▼
 Controller
      |
      ▼
   Database
      |
      ▼
   Response


6. Input Validation
Input validation means checking whether the data received from the user is correct and safe before processing it.

Example:

A registration API expects:
{
  "name": "John",
  "email": "john@gmail.com",
  "age": 22
}


Backend checks:
- Is the name provided?
- Is the email in a valid format?
- Is the age a valid number?
- Are required fields missing?
If the input is invalid, the backend returns an appropriate error.

Why important? It prevents invalid data, reduces security risks, and maintains data quality.
7. API Design Best Practices
An API (Application Programming Interface) allows two applications to communicate with each other.

Good API design makes APIs easy to understand, secure, and maintain.

Important practices:
1. Use meaningful endpoint names.
2. Use correct HTTP methods.
3. Return proper status codes.
4. Validate user input.
5. Handle errors properly.
6. Protect sensitive information.
7. Use authentication and authorization.
Example:
Method	Endpoint	Purpose
GET	/users	Get all users
GET	/users/1	Get one user
POST	/users	Create user
PUT	/users/1	Update user
DELETE	/users/1	Delete user

Common HTTP status codes:
Code	Meaning
200	Success
201	Created
400	Bad Request
401	Unauthorized
403	Forbidden
404	Not Found
500	Internal Server Error

8. Authentication Basics (JWT Concepts)
Authentication means verifying who the user is.

JWT stands for JSON Web Token. It is a token commonly used to securely communicate authentication claims between a client and server.

Example login process:








scaler.com


1. User Login
      |
      ▼
2. Backend Verifies Credentials
      |
      ▼
3. Backend Generates JWT
      |
      ▼
4. Client Stores Token Securely
      |
      ▼
5. Client Sends Token with API Request
      |
      ▼
6. Backend Verifies Token
      |
      ▼
7. Access Granted / Rejected


A JWT generally contains three parts:
Header.Payload.Signature


- Header: Token type and signing algorithm.
- Payload: Claims such as user ID and expiration time.
- Signature: Helps verify that the token has not been modified.
Important: JWT payloads are encoded, not encrypted by default. Never store passwords or sensitive secrets inside them.

9. Quick Revision – Day 3
Topic	Simple meaning
Server	Receives and processes client requests
Blocking	Waits until a task finishes
Non-blocking	Continues other work while waiting
Sync	Executes tasks in sequence
Async	Handles waiting operations without blocking progress
Event Loop	Coordinates asynchronous JavaScript execution
Routing	Decides which API handles a request
Middleware	Executes checks between request and response
Input Validation	Checks whether incoming data is correct
API Design	Creates clear and consistent APIs
JWT	Token used to carry authentication claims