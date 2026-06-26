# Nodes

## What is a Node?

A **Node** is the smallest executable unit in ROS2.

Each node is responsible for performing **one specific task**.

Examples:

* Reading data from a sensor
* Controlling a robot
* Publishing camera images
* Receiving velocity commands
* Planning a path

Instead of writing one large program, ROS2 encourages dividing the application into multiple independent nodes.

---

## Creating a Node

Navigate to your package:

```bash
cd workspace_name
cd src
cd package_name
cd package_name
```

> Both the package and the folder inside it, have the same name.

Create a new node:

```bash
touch node_name.py
chmod +x node_name.py
```

Open the workspace in VS Code:

```bash
cd ../..
code .
```

---

## Registering the Node

To execute a node using ROS2 commands, it must be registered inside `setup.py`.

Locate the following section:

```python
entry_points={
    "console_scripts": [
    ],
},
```

Add your node:

```python
entry_points={
    "console_scripts": [
        "test_node = package_name.node_name:main",
    ],
},
```

### Understanding the Syntax

```python
test_node = package_name.node_name:main
```

| Part           | Meaning                              |
| -------------- | ------------------------------------ |
| `test_node`    | Executable name used with `ros2 run` |
| `package_name` | Name of your ROS2 package            |
| `node_name`    | Python file name (without `.py`)     |
| `main`         | Function that ROS2 executes          |

---

## Build the Workspace

After registering the node:

```bash
cd ~/workspace_name

colcon build
```

Source the workspace:

```bash
source ~/.bashrc
```

---

## Running the Node

```bash
ros2 run package_name test_node
```

ROS2 executes the `main()` function of the node.

---

## Updating the Node

Suppose you modify your node:

```python
self.get_logger().info("Hello from ROS2")
```

to

```python
self.get_logger().info("ROS2")
```

The changes may not appear immediately.

<br>Build the workspace using:

```bash
colcon build --symlink-install
```

Then source the workspace again:

```bash
source ~/.bashrc
```

Now run the node:

```bash
ros2 run package_name test_node
```

---

## Why `--symlink-install`?

Normally, `colcon build` copies your Python files into the `install` folder.

If you later modify the source code, ROS2 still executes the old copied version.

Using:

```bash
colcon build --symlink-install
```

creates symbolic links instead of copying the files.

Now, whenever you edit the source code, ROS2 automatically uses the latest version without needing to rebuild every time.

> Usually, `--symlink-install` only needs to be used once for a workspace. After that, simply editing the Python files is enough. If changes are not reflected, source the workspace again or rebuild if necessary.

---

## Node Lifecycle

```text
   Create Node
        |
Register in setup.py
        |
 Build Workspace
        |
 Source Workspace
        |
     Run Node
```

---

## Remember

* Every publisher is a node.
* Every subscriber is a node.
* Every service server/client is a node.
* A ROS2 application usually consists of multiple nodes working together.
