# Closed Loop System

A closed loop system is created by combining a **Publisher** and a **Subscriber** inside the same node.

The subscriber receives the robot's current state.

The publisher sends the next command based on that state.

---

## How it Works

```text
              Topic
          (/turtle1/pose)

          Pose Publisher
                |
                |
          Controller Node
      (Subscriber + Publisher)
                |
                |
              Topic
        (/turtle1/cmd_vel)

         Turtle Subscriber
```

---

## Step-by-Step Flow

### Step 1

The robot continuously publishes its current position.

```text
Publisher ------> /turtle1/pose
```

---

### Step 2

The controller node subscribes to this topic.

It always knows the latest position of the robot.

---

### Step 3

The controller compares:

```
Current Position
        VS
Desired Position
```

---

### Step 4

The controller calculates what the robot should do next.

Example:

```
Move Forward
Turn Left
etc.
```

---

### Step 5

The controller publishes a new velocity command.

```text
Publisher
    │
    ▼
/turtle1/cmd_vel
```

---

### Step 6

The robot receives the command and moves.

Its position changes...

which again gets published...

which again gets received...

and the cycle continues.

---

## Complete Loop

```text
Robot Position
      |
      |
 Pose Publisher
      |
      |
 Pose Topic
      |
      |
Controller Node
(Subscriber + Logic + Publisher)
      |
      |
Velocity Topic
      |
      |
    Robot  <---------- Feedback
```

---

## Why is it called "Closed Loop"?

Because the output is continuously fed back to the controller.

The controller never works blindly.

It always knows the robot's latest state before sending the next command.

---

## Note:

A closed loop controller is usually **one node** that contains:

* A Subscriber (to receive feedback)
* Some logic (decision making)
* A Publisher (to send commands)
