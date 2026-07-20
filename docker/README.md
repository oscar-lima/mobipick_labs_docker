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

          # Mobipick labs
          ozkrelo/mobipick_labs:noetic (used as base for v1.1) TODO: investigate why it was having a deprecated comment
              ozkrelo/mobipick_labs:noetic-v1 (+ mir pkgs from apt) TODO: find dockerfile of this image

          # X Mobipick labs
          ozkrelo/x_mobipick_labs:noetic-v1.1 (TODO
          ozkrelo/x_mobipick_labs:noetic-v1.2 (install precommit, ipython, vim, nano, tree, etc.
                                              clone and activates scripts folder from:
                                                      https://github.com/oscar-lima/mobipick_labs_scripts
                                              improved navigation via path-follower-critic)

            # x Mobipick labs + user baked into image,
            # from here on is no longer possible to pull from docker hub
            # requires to be build inside each machine, inherits the user and PID, UID
            *ozkrelo/x_mobipick_labs:custom_user_from_1.2
                                        ENTRYPOINT ["/usr/local/bin/entrypoint_user.sh"]
                                        CMD ["bash"]
```

# Available images in docker hub, ozkrelo

build June 2026 = J26

image                   tag1                tag2                      tag3
--------------------------------------------------------------------------------------
focal-snapshot        20250530           20260625 (J26)
noetic-ros-core      ubuntu20250530    ubuntu20260625 (J26)
mir                    noetic            noetic-v2.0 (J26)
mobipick               noetic            noetic-v1.1              noetic-v2.0 (J26)
mobipick_labs          noetic            noetic-v2.0  (J26)
x_mobipick_labs        noetic-v1.1       noetic-v1.2              noetic-v2.0 (J26)

NOT available in docker hub: ozkrelo/x_mobipick_labs:oscar_user_from_2.0

# New structure

```
ozkrelo/focal-snapshot/20260625
  ozkrelo/noetic-ros-core/ubuntu20260625
    ozkrelo/mir/noetic-v2.0
      ozkrelo/mobipick/noetic-v2.0
        ozkrelo/mobipick_labs/noetic-v2.0
          ozkrelo/x_mobipick_labs/noetic-v2.0
              ozkrelo/x_mobipick_labs:oscar_user_from_2.0
```

# Custom projects

GPT ws and RAE ws : FROM ozkrelo/x_mobipick_labs:oscar_user_from_1.2
