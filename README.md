# Mobipick Lab docker
Docker (compose) environment for the DFKI MobiPick lab (https://github.com/DFKI-NI/mobipick_labs)

# Dependencies
Install docker (or mobi) and docker compose, install [nvidia-docker2](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/nvidia-docker.html) if you have an nvidia graphics card.

# Usage

## Mobipick Labs Docker GUI
Typing Docker commands can be repetitive and error-prone. To simplify this, we developed a graphical interface that allows you to:

- Start or stop simulations by toggling containers with a single click
- Launch tools such as RViz and RQT, open a terminal, commit containers, and more

The GUI is practical and easy to use. Try it here: https://github.com/oscar-lima/mobipick_labs_docker_gui

## Command line usage
If you prefer command line, and just want to run the simulation without planning and without rviz you can use `mobipick.bash`. It will download all required container and start the mobipick-gazebo environment for the tables demo (see `command:` in `docker compose.yml`).

To run custom ROS commands just prefix them with `./cmd.bash`. This starts a new docker container with your command connected to the ROScore of the mobipick-container instance.

### Run Mobipick tables demo on simulation with Gazebo
1. open a first terminal and run `./mobipick.bash` to start the Gazebo robot simulation with the mobipick robot inside.
1. (optional) in a second terminal run rviz to visualize the robot `./cmd.bash rosrun rviz rviz -d /root/catkin_ws/src/mobipick_labs/tables_demo_bringup/config/pick_n_place.rviz __ns:=mobipick`.
1. in a second window (or third window if you run rviz as well) start the autonomous planning `./cmd.bash rosrun tables_demo_planning tables_demo_node.py`.
1. (optional) it could also be helpful to run another terminal inside a docker container to call ROS commands and test stuff, just run `./cmd.bash bash` to start one.

### Shutdown
To stop everything call `docker compose down`.

## Credit
Most if not all credit goes to our colleague from DFKI RIC Andreas Bresser, see: https://github.com/brean/mobipick_labs_docker
We forked and introduced some fixes for a research workshop at a time where Andreas was very busy but this is mostly his work. Thank you Andreas!
