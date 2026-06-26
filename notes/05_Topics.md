# Topics

## What is a Topic?

A **Topic** is a communication channel between ROS2 nodes.

- Publishers **send** messages to a topic.
- Subscribers **receive** messages from that topic.

Neither the publisher nor the subscriber knows about each other. They only know the topic name.

---

## Topic Communication

```text
             Topic (/turtle1/pose)
Publisher --------------------------> Subscriber
```

Multiple publishers and multiple subscribers can use the same topic.

---

## Important Points

- Topics provide **one-way communication**.
- Communication is **asynchronous**.
- Publisher and Subscriber do **not** need to know each other.
- ROS2 automatically creates a topic when a publisher/subscriber starts using it.

---

## Useful Commands

List all topics:

```bash
ros2 topic list
```

<br>Get information about a topic:

```bash
ros2 topic info /topic_name
```

<br>See the data being published:

```bash
ros2 topic echo /topic_name
```

<br>Know the message type:

```bash
ros2 topic type /topic_name
```

---

## Example

Topic:

```
/turtle1/cmd_vel
```

Publisher:

```
Keyboard Controller
```

Subscriber:

```
Turtlesim Node
```

The keyboard node publishes velocity commands.

The turtlesim node subscribes to the same topic and moves the turtle.