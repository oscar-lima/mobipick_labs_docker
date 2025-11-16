# mobipick labs docker structure

Hierarchy is expressed in spaces, meaning they derive "from"
e.g. ozkrelo/noetic-ros-core:ubuntu20250530 derives from ozkrelo/focal-snapshot:20250530
e.g. 2 ozkrelo/x_mobipick_labs:noetic-v1.2 derives from ozkrelo/mobipick_labs:noetic

```
ozkrelo/focal-snapshot:20250530
  ozkrelo/noetic-ros-core:ubuntu20250530
            ENTRYPOINT ["/ros_entrypoint.sh"], CMD ["bash"]
    ozkrelo/mir:noetic (has mir pkgs only from source)
            ENTRYPOINT ["/entrypoint.sh"]
      ozkrelo/mobipick:noetic (deprecated)
      ozkrelo/mobipick:noetic-v1.1 (+ mir pkgs from apt)
        ozkrelo/mobipick_labs:noetic (deprecated)
        ozkrelo/mobipick_labs:noetic-v1 (+ mir pkgs from apt)

          ozkrelo/x_mobipick_labs:noetic-v1.1
          ozkrelo/x_mobipick_labs:noetic-v1.2

           *ozkrelo/x_mobipick_labs:oscar_user_from_1.2
                                        ENTRYPOINT ["/usr/local/bin/entrypoint_user.sh"]
                                        CMD ["bash"]

             ozkrelo/x_mobipick_labs:gpt_ws_from_oscar_user
             ozkrelo/x_mobipick_labs:rae_ws_from_oscar_user
```
