import mobipick_api

print('pick multimeter_1 test')

mobipick = mobipick_api.Robot('mobipick')

# move to table 3 where multimeter_1 is located
# mobipick.base.move(21.0, 7.0, 3.141592)

# perceive table 3
mobipick.arm_cam.perceive(observation_list=['observe100cm_right'])

# if multimeter_1 is inside the pose selector, pick it
if mobipick.arm_cam.is_object_inside_pose_selector('multimeter_1'):
    mobipick.arm.pick_object('multimeter_1', 'table_3', planning_scene_ignore_list=[], timeout=50.0)
else:
    print('failed to pick multimeter_1')
