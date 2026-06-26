# Publisher

## What is a Publisher?

A **Publisher** is a ROS2 node that sends data to a topic.

It does **not** know who receives the data.

Its only responsibility is:

```
Create Message
      |
Publish Message
      |
    Topic
```

---

## Creating a Publisher

```python
self.cmd_vel_pub_ = self.create_publisher(
    Twist,
    "/turtle1/cmd_vel",
    10
)
```

---

## Understanding the Parameters

```python
self.create_publisher(
    Twist,
    "/turtle1/cmd_vel",
    10
)
```

### 1. `Twist`

The **message type**.

It defines what kind of data will be sent.

Example:

- `Twist`
- `Pose`
- `String`
- `Image`

---

### 2. `/turtle1/cmd_vel`

Topic name.

Every subscriber listening to this topic will receive the published message.

---

### 3. `10`

Queue size.

If subscribers cannot receive messages fast enough, ROS2 temporarily stores them.

Queue size tells ROS2 how many messages can be stored before older ones are discarded.

---

## Publishing a Message

Example:

```python
msg = Twist()

msg.linear.x = 2.0
msg.angular.z = 1.0

self.cmd_vel_pub_.publish(msg)
```

The publisher creates a message and publishes it.

---

## Remember

A publisher is also a ROS2 node.

If you import another ROS2 package, add it inside `package.xml` under dependencies:

```xml
<depend>another_package_name</depend>
```

Here  this another package is just a ros2 package that is imported in the file using import. For example: rclpy, geometry_msgs, etc.

