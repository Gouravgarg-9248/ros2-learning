# Services (Client - Server)

Topics continuously send data.

Sometimes we don't want continuous communication.

Sometimes we only want to ask a question once and receive one answer.

For this, ROS2 provides **Services**.

---

## Communication

```text
           Request
Client ---------------> Service <----------- Server
```

The client sends a request through a service.

The server processes it and sends back a response.

After that, communication ends.

---

## Roles

### Client

* Sends a request.
* Waits for the response.

Example:

```
Please spawn a new turtle.
```

---

### Service

A service defines:

* What request can be sent.
* What response will be returned.

It is like a communication contract between the client and server.

---

### Server

* Waits for incoming requests.
* Processes them.
* Sends the response.

Example:

```
Turtle created successfully.
```

---

## Complete Flow

```text
         Request            Process Request           Response
Client ----------> Server ------------------> Server ----------> Client
```

---

## Topics vs Services

### Topics

```text
Publisher ----------> Topic ----------> Subscriber
```

* Continuous communication
* No reply
* Best for sensor data and robot states

---

### Services

```text
Client -------> Server
Client <------- Server
```

* One request
* One response
* Communication ends

---

## ROS2 Commands

List all services:

```bash
ros2 service list
```

Service information:

```bash
ros2 service info /service_name
```

Service type:

```bash
ros2 service type /service_name
```

Call a service:

```bash
ros2 service call /service_name service_type "{data}"
```

Example:

```bash
ros2 service call /clear std_srvs/srv/Empty "{}"
```

---

## Note:

Topic says:

> "Keep sending me data."

Service says:

> "Do this once and tell me the result."

Choose Topics when communication is continuous.

Choose Services when a reply is required.
