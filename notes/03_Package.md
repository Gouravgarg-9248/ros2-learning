# Creating a Package

## Creating a Package

Navigate to the workspace source directory:

```bash
cd
cd workspace_name
cd src
```

Create a Python package:

```bash
ros2 pkg create robotName_Function-Of-Package --build-type ament_python --dependencies rclpy
```

### Notes

- `robotName_Function-Of-Package` is the package name.
    - Example: `my_robot_controller`
- Do **not** use spaces in package names.
- Use `ament_python` for Python packages.
- Use `ament_cmake` for C++ packages.
- `colcon` is the build tool which uses ament a build system.
- Dependencies are the other packages or functionalities that we are going to need to use in this custom package we are creating.
    - Example: `rclpy` is the ROS2 Python client library.


<br>Open the workspace in VS Code:

```bash
code .
```

> Use `code .` while inside the `src` directory.

The package will be created, and inside it you'll find another folder with the same name. This is where your ROS2 nodes will be created.


<br>Build the workspace:

> First go to "workspace_name" folder by using `cd ..` or `cd ~/workspace_name`
```bash
cd ..
colcon build
ls
```

Verify the installation if needed:

```bash
cd install
ls
```