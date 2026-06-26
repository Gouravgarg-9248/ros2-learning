# Creating a Workspace


```bash
cd
ls

mkdir workspace_name
cd workspace_name

mkdir src
ls

colcon build

ls
cd install
ls

cd
source ~/workspace_name/install/setup.bash
```

Add the following line to the end of `~/.bashrc`:

```bash
source ~/workspace_name/install/setup.bash
```
> This is to source the custom ros2 workspace in every new terminal.

Then run:

```bash
source ~/.bashrc
```

> Or simply open a new terminal.
