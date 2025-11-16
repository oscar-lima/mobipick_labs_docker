Images derive from different base images, check details below

v1.1 (NOTE: this image is in dockerhub), derived FROM ozkrelo/mobipick_labs:noetic

- install programs: ipython3, vim, nano, git-core, tree, python3-pygments, mlocate
- customized terminal with mobipick_labs_scripts from oscar-lima
- switch to a different branch in mir_robot (from oscar-lima remote) to enable path follower critic.
  this should not be necessary if https://github.com/DFKI-NI/mir_robot/pull/146 is merged
  the purpose of this change is to enhance the robot navigation in simulation.

v1.2, derived FROM ozkrelo/mobipick:noetic-v1.1

- install program python3-pip via apt
- install precommit via pip
- update alternatives for python is python3
- now derives from an image that has mir pkgs installed from apt
