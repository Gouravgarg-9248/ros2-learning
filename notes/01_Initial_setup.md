# Initial Setup

### Install Colcon Extensions

Install "python3-colcon-common-extensions"

```bash
sudo apt update
sudo apt install python3-colcon-common-extensions
```

### Source ROS2 Automatically

Add the following in `~/.bashrc` file at the end. 

```bash
source /opt/ros/humble/setup.bash
```

> This sources ros2 in every new terminal.

### Enable Colcon Auto-completion

Add the following in `~/.bashrc` file at the end. 

```bash
source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
```

> This sources colcon autocompletion for arguments.

### How to add 

Open `~/.bashrc` file:

```bash
nano ~/.bashrc
```

Add the lines at the end.
Then press `ctrl+o` to save, then `Enter` , then `ctrl+x` to exit.

OR

```bash
gedit ~/.bashrc
```
Simply add the lines at the end and save the file.


> Then run:
```bash
source ~/.bashrc
```
This sources the `~/.bashrc` file.

> Or simply open a new terminal.


> All these steps are to be done only one time.


