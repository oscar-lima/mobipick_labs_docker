# Mobipick Lab docker
Docker (compose) environment for the DFKI MobiPick lab (https://github.com/DFKI-NI/mobipick_labs)

# Dependencies
Install docker (or mobi) and docker compose, install [nvidia-docker2](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/nvidia-docker.html) if you have an nvidia graphics card.

# Usage
If you just want to run the simulation without planning and without rviz `mobipick.bash`. It will download all required container and start the mobipick-gazebo environment for the tables demo (see `command:` in `docker compose.yml`).

To run custom ROS commands just prefix them with `./cmd.bash`. This starts a new docker container with your command connected to the ROScore of the mobipick-container instance.

## Example Run

### Option 1: run each command separately
Instead of starting all docker container and run one terminator for logging you can also start everything in single commands:

1. open a first terminal and run `./mobipick.bash` to start the Gazebo robot simulation with the mobipick robot inside.
1. (optional) in a second terminal run rviz to visualize the robot `./cmd.bash rosrun rviz rviz -d /root/catkin_ws/src/mobipick_labs/tables_demo_bringup/config/pick_n_place.rviz __ns:=mobipick`.
1. in a second window (or third window if you run rviz as well) start the autonomous planning `./cmd.bash rosrun tables_demo_planning tables_demo_node.py`.
1. (optional) it could also be helpful to run another terminal inside a docker container to call ROS commands and test stuff, just run `./cmd.bash bash` to start one.

### Option 2: GUI Quick Start
- Launch the GUI with `python gui.py`; the top row toggles (Roscore, Sim, Tables Demo, RViz, RQt, Scripts) manage single instances.
- Always start Roscore first—other toggles do it automatically but the master must stay up for everything else.
- User scripts live in `./scripts/`; edit locally, then use the Scripts toggle to run/stop them inside `mobipick_cmd`.
- The Sim/Tables/RViz/RQt toggles send output to their named tabs; use `Update Status` if you need to resync button state with running containers.
- To serve the same controls in a browser start the GUI with `python gui.py --web`. The terminal prints the URL (e.g. `http://127.0.0.1:8080`); open it to access the web dashboard. Use the layout selector to arrange embedded process logs (one, two, or three columns), toggle individual tabs on/off, or pop any tab into a separate window while the backend continues to manage the ROS processes.

## Shutdown
To stop everything call `docker compose down`.
