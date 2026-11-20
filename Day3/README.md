Day 3 -- Backend Server, Async & API Design
Learning Goal
Understand how a backend server receives and processes requests, how
asynchronous work is handled, and how to design APIs that are clear,
reliable, and secure.
1. What Is a Server?
A server is a computer or software program that receives requests
from clients, processes them, and sends responses.

For example, when you log in to an application, the app sends your login
details to the backend server. The server checks the details and sends
back a response.
Basic request--response flow
Client (Browser / App)
        |
        | Request
        v
  Backend Server
        |
        | Read or update data
        v
     Database
        |
        | Result
        v
  Backend Server
        |
        | Response
        v
Client (Browser / App)
Key point: The client makes a request; the server processes it and
returns a response.
2. Blocking vs Non-Blocking Execution
Blocking
In blocking execution, the program waits for an operation to finish
before continuing with the next operation.

Example: You order food and wait at the counter until it is ready
before doing anything else.
Task 1: [------]
Task 2:          [------]
Task 3:                   [------]
Non-blocking
In non-blocking execution, the program can continue doing other work
while an operation is waiting to finish.

Example: You order food, receive a token, and do something else
while your food is being prepared.
Start Task 1 ---- waiting for result
Start Task 2 ---- complete
Start Task 3 ---- complete
Task 1 result --- complete later
Key point: Blocking waits before continuing; non-blocking allows
other work to progress while waiting.
3. Synchronous vs Asynchronous Concepts
Synchronous (Sync)
Synchronous code generally runs one step after another. The next step
waits for the current step to finish.
Task A  --->  Task B  --->  Task C
Asynchronous (Async)
Asynchronous code can start an operation and continue with other work
while waiting for that operation to finish. The result is handled later.
Start Task A
     |
Start async Task B ---- waiting
     |
Continue Task C
     |
Task B result arrives
Example: A program starts downloading a file and can continue
handling other work while the download is in progress.

Key point: Sync describes an ordered, wait-for-completion flow.
Async allows work to continue while an operation is pending.
Blocking/non-blocking and sync/async are related concepts, but they
are not exactly the same. Synchronous code is often blocking, while
asynchronous code is commonly used to avoid blocking during I/O
operations.

4. Event Loop Basics
The event loop is part of JavaScript's runtime. It coordinates
asynchronous callbacks so JavaScript can handle operations such as
timers and network or file I/O without waiting for each one on the main
call stack.

In simple terms:
1. Synchronous code runs on the call stack.
2. An asynchronous operation is started.
3. When its result is ready, its callback or promise continuation is
   queued.
4. The event loop coordinates when queued work can run after the call
   stack is clear.
Simplified event loop diagram
       JavaScript Code
              |
              v
          Call Stack
              |
              v
     Start async operation
              |
              v
   Runtime / I/O operation
              |
       Result is ready
              |
              v
      Callback / Promise
            Queue
              |
              v
          Event Loop
              |
     Stack is available?
              |
              v
       Run queued work
Key point: The event loop helps JavaScript coordinate asynchronous
work; it does not mean every task runs at the same time.
5. Routing and Middleware
Routing
Routing decides which backend function should handle an incoming
request, based on its URL and HTTP method.

Examples:

  Method   Route        Purpose
  GET      /users     Get users
GET      /users/1   Get a specific user
POST     /users     Create a user
PUT      /users/1   Update a user
DELETE   /users/1   Delete a user
Middleware
Middleware is code that runs during the request--response process,
usually before the final route handler. It can inspect or modify the
request, send a response, or pass control to the next step.

Common uses include: - Logging requests - Checking authentication -
Validating input - Handling errors
Request flow
Client Request
      |
      v
  Middleware
      |
      v
    Router
      |
      v
 Route Handler
      |
      v
   Database
      |
      v
   Response
Key point: Routing chooses the handler; middleware performs shared
checks or tasks along the way.
6. Input Validation
Input validation means checking incoming data to make sure it has
the expected format and values before the backend uses it.

Example registration request:
{
  "name": "John",
  "email": "john@example.com",
  "age": 22
}
The backend should check: - Is the name present and within the allowed
length? - Is the email in an acceptable format? - Is the age a valid
number and within the allowed range? - Are required fields missing? -
Are values within the application's allowed limits?

If the data is invalid, the server should return a clear error, such as
400 Bad Request.

Why is validation important? - Prevents invalid or unexpected
data. - Helps protect the application from malicious input. - Keeps
stored data consistent. - Makes API errors easier to understand.

Key point: Never rely only on frontend validation. Validate data on
the backend because clients can send modified requests.
7. API Design Best Practices
An API (Application Programming Interface) lets different software
components communicate. A well-designed API is predictable, consistent,
secure, and easy to maintain.
Use clear routes and HTTP methods
  Method   Example endpoint   Purpose
  GET      /users           Retrieve users
GET      /users/1         Retrieve one user
POST     /users           Create a user
PUT      /users/1         Replace/update a user
PATCH    /users/1         Partially update a user
DELETE   /users/1         Delete a user
Common HTTP status codes
  Code   Meaning
  200    OK -- request succeeded
201    Created -- resource created
204    No Content -- succeeded with no response body
400    Bad Request -- invalid request
401    Unauthorized -- authentication is missing or invalid
403    Forbidden -- user is not allowed to perform the action
404    Not Found -- resource does not exist
500    Internal Server Error -- unexpected server error
Good API design practices
1. Use meaningful and consistent endpoint names.
2. Choose the correct HTTP method.
3. Return appropriate status codes.
4. Validate all incoming data.
5. Use a consistent response and error format.
6. Authenticate users and authorize access where needed.
7. Avoid exposing passwords, tokens, or other sensitive information.
8. Document endpoints, request formats, and responses.
Key point: A good API should be easy to understand, consistent, and
safe to use.
8. Authentication Basics -- JWT Concepts
Authentication is the process of verifying a user's identity.

JWT stands for JSON Web Token. It is a compact token format
often used to carry claims between a client and a server.
Basic JWT login flow
1. User sends login details
             |
             v
2. Backend verifies credentials
             |
             v
3. Backend creates and signs JWT
             |
             v
4. Client receives and stores token safely
             |
             v
5. Client sends token with later requests
             |
             v
6. Backend verifies token and checks access
             |
             v
       Request allowed or rejected
Three parts of a JWT
A JWT has three parts separated by dots:
Header.Payload.Signature
- Header: Describes the token type and signing algorithm.
- Payload: Contains claims, such as a user identifier and token
  expiry time.
- Signature: Allows the server to verify that the token has not
  been changed and was signed with the expected key.
Important security points
- A JWT payload is encoded, not encrypted by default. Do not put
  passwords or secrets in it.
- Use HTTPS when sending tokens.
- Set an appropriate expiration time.
- Verify the signature and relevant claims on the backend.
- Do not trust a role or permission just because it appears in
  client-controlled data; enforce authorization on the server.
Key point: A JWT can help a server verify a user's authenticated
identity, but the backend must still check what that user is allowed to
do.
9. Quick Revision
  Topic                               Simple meaning
  Server                              Receives, processes, and responds
to client requests

  Blocking                            Waits for an operation before
continuing

  Non-blocking                        Allows other work to progress while
an operation is pending

  Synchronous                         Runs steps in an ordered flow; a
step waits for the previous step

  Asynchronous                        Allows a program to continue while
an operation is pending

  Event loop                          Coordinates queued asynchronous
work in JavaScript

  Routing                             Selects a handler for a request

  Middleware                          Runs shared logic during the
request--response flow

  Input validation                    Checks whether incoming data is
acceptable

  API design                          Defines clear and consistent ways
for software to communicate

  Authentication                      Verifies who a user is
JWT                                 A signed token format that carries
claims
10. Practice Questions
Use these questions to check your understanding:
1. What is a server, and how does it communicate with a client?
2. What is the difference between blocking and non-blocking execution?
3. What is the difference between synchronous and asynchronous code?
4. What does the JavaScript event loop do?
5. What is routing in a backend application?
6. What is middleware? Give two examples of its uses.
7. Why should input validation happen on the backend?
8. What are the common HTTP methods used in REST APIs?
9. What is the difference between HTTP status codes 401 and 403?
10. What are the three parts of a JWT?
Day 3 -- Final Understanding
A backend server receives requests from clients and sends responses. It
uses routing to select the correct handler and middleware to perform
shared tasks such as logging, authentication, and validation.
Asynchronous execution and the JavaScript event loop help the server
handle waiting operations efficiently. Good API design makes
communication consistent, while authentication mechanisms such as JWT
help verify users.

Main takeaway: Understand the complete request flow:
Client
  |
  v
HTTP Request
  |
  v
Middleware (checks)
  |
  v
Route Handler
  |
  v
Validation + Business Logic
  |
  v
Database (if needed)
  |
  v
HTTP Response
  |
  v
Client