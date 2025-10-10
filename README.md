# Mobipick Lab docker
Docker (compose) environment for the DFKI MobiPick lab (https://github.com/DFKI-NI/mobipick_labs)

# Dependencies
Install docker (or mobi) and docker compose, install [nvidia-docker2](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/nvidia-docker.html) if you have an nvidia graphics card.

# Usage
If you just want to run the simulation without planning and without rviz `mobipick.bash`. It will download all required container and start the mobipick-gazebo environment for the tables demo (see `command:` in `docker compose.yml`).

To run custom ROS commands just prefix them with `./cmd.bash`. This starts a new docker container with your command connected to the ROScore of the mobipick-container instance.

## Shared workspace

- `docker-compose.yml` provides a persistent `workspace` service (`command: sleep infinity`) that keeps the catkin workspace alive between commands.
- The workspace, `mobipick`, and `mobipick_cmd` containers mount the same named volume at `/root/catkin_ws`, so GUI-launched builds, `mobipick.bash`, and `cmd.bash` all share the same source tree.
- The GUI and helper scripts now call `docker compose exec workspace ...` so every action runs inside that long-lived container; you can do the same from a terminal for ad-hoc commands.
- Stop the session with `docker compose stop workspace` (or run `./clean.bash`) when you are finished to free resources.

## Example Run

### Option 1: run each command separately
Instead of starting all docker container and run one terminator for logging you can also start everything in single commands:

1. open a first terminal and run `./mobipick.bash` to start the Gazebo robot simulation with the mobipick robot inside.
1. (optional) in a second terminal run rviz to visualize the robot `./cmd.bash rosrun rviz rviz -d /root/catkin_ws/src/mobipick_labs/tables_demo_bringup/config/pick_n_place.rviz __ns:=mobipick`.
1. in a second window (or third window if you run rviz as well) start the autonomous planning `./cmd.bash rosrun tables_demo_planning tables_demo_node.py`.
1. (optional) it could also be helpful to run another terminal inside a docker container to call ROS commands and test stuff, just run `./cmd.bash bash` to start one.

### Option 2: GUI Quick Start
- Launch the GUI with `python gui.py`; the top row toggles (Roscore, Sim, Tables Demo, RViz, RQt, Scripts) now exec into the `workspace` container so everything shares the same filesystem state.
- Always start Roscore first—other toggles do it automatically but the master must stay up for everything else.
- User scripts live in `./scripts/`; edit locally, then use the Scripts toggle to run/stop them inside the shared workspace container.
- The Sim/Tables/RViz/RQt toggles send output to their named tabs; use `Update Status` if you need to resync button state with running commands.

## Shutdown
To stop everything call `docker compose stop workspace` (and optionally `docker compose down` for the other services) or simply run `./clean.bash`.
