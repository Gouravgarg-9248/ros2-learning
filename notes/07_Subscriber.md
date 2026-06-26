# Subscriber

## What is a Subscriber?

A **Subscriber** is a ROS2 node that listens to a topic.

Whenever a new message arrives, ROS2 automatically calls a callback function.

```
     Topic
       |
   Subscriber
       |
Callback Function
```

---

## Creating a Subscriber

```python
self.pose_subscriber_ = self.create_subscription(
    Pose,
    "/turtle1/pose",
    self.pose_callback,
    10
)
```

---

## Understanding the Parameters

```python
self.create_subscription(
    Pose,
    "/turtle1/pose",
    self.pose_callback,
    10
)
```

### 1. `Pose`

Message type.

Must match the publisher's message type.

---

### 2. `/turtle1/pose`

Topic name.

Subscriber listens only to this topic.

---

### 3. `self.pose_callback`

Whenever a new message arrives,

ROS2 automatically executes this function.

Example:

```python
def pose_callback(self, msg):
    self.get_logger().info(str(msg))
```

The received message is available through `msg`.

---

### 4. `10`

Queue size.

Works exactly like the publisher queue.

---

## Flow

```
   Publisher
       |
     Topic
       |
   Subscriber
       |
Callback Function
```

---

## Remember

- A subscriber never asks for data.
- It simply waits.
- Whenever data is published, the callback function runs automatically.
- If another ROS2 package is imported in the code, add it inside `package.xml`.
