# Code index

Use a chapter’s diagram and code map first. This index resolves the source
behind those links, including implementations that exist only in the inspected
working tree. It records locations, not a complete code audit or source backup.

## How to resolve a reference

**Pinned public source** links were checked against the complete local file
bytes on September 21, 2026. They open the inspected commit, not a moving branch.
**Local snapshot** means no identical public file was verified for this snapshot;
the listed base commit alone does not reproduce its working-tree changes.
Obtain the matching lab checkout/archive and compare the SHA-256 before relying
on its line numbers. Do not substitute an older public file without reviewing
the differences.

Paths are relative to the named repository. With a checkout available, locate
the symbol using `rg -n 'symbol_name' path/to/file.py`. The
[machine-readable map](../assets/code-map.json) includes full hashes, revisions,
symbol line spans and exact public URLs. The optional
`tools/check_code_map.py` checks an available source checkout without importing
robot software; the site build does not require those repositories.

For an agent: read the chapter’s Mermaid source, mapped functions, invariants
and checks together. Code existence does not establish a physical result.
Resolve current behavior against the [source catalog](sources.md), and for
calibration read the source investigation ledger before suggesting a test.

## Code: executor

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_aprilcube_calibration/executor_state_machine.py`.

[Pinned public source](https://github.com/sri299792458/g1-dex3-tabletop/blob/cf1b27704c82d877d23ff5a3c157df3218f02402/src/g1_aprilcube_calibration/executor_state_machine.py); base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `403f2948fcfdd56df3f7ce1a83cac2664105bbbad1193c976fb4dc4b188b3e51`.

| Symbol | Inspected lines |
|---|---|
| `PoseExecutor.acquire` | 248–298 |
| `PoseExecutor.tick` | 834–1095 |
| `PoseExecutor.install_validated_plan` | 572–665 |

## Code: driver

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_aprilcube_calibration/executor_driver.py`.

[Pinned public source](https://github.com/sri299792458/g1-dex3-tabletop/blob/cf1b27704c82d877d23ff5a3c157df3218f02402/src/g1_aprilcube_calibration/executor_driver.py); base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `aac4efb6fe8a6ca2e44f76e074a2729bf3fae8e104e3b16d3e0edca4cda3900f`.

| Symbol | Inspected lines |
|---|---|
| `ExecutorControlDriver._run` | 187–209 |

## Code: lowcmd

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_aprilcube_calibration/transports/unitree_debug_lowcmd.py`.

[Pinned public source](https://github.com/sri299792458/g1-dex3-tabletop/blob/cf1b27704c82d877d23ff5a3c157df3218f02402/src/g1_aprilcube_calibration/transports/unitree_debug_lowcmd.py); base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `8415eb72c1c7816d1bf6f5880a400ce0379054af12e982be481f42fe662cc77a`.

| Symbol | Inspected lines |
|---|---|
| `UnitreeMotionModeManager.enter_debug_guarded` | 133–168 |
| `UnitreeDebugLowCmdTransport.send_command` | 236–279 |

## Code: arm-sdk

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_aprilcube_calibration/transports/unitree_arm_sdk.py`.

**Local snapshot**; base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `18e3f3cc8a0947043061d7c6d89d41e61f957e99961632f4d7e96d37bd9072c7`.

| Symbol | Inspected lines |
|---|---|
| `UnitreeArmSDKTransport.send_command` | 360–403 |

## Code: watchdog

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_aprilcube_calibration/pc2_safety.py`.

[Pinned public source](https://github.com/sri299792458/g1-dex3-tabletop/blob/cf1b27704c82d877d23ff5a3c157df3218f02402/src/g1_aprilcube_calibration/pc2_safety.py); base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `e78b56dda204fa4dc1ececcf5b5c30dc274cad94b488644e141ba36bf822fed8`.

| Symbol | Inspected lines |
|---|---|
| `PC2DampingWatchdog.start` | 123–207 |
| `PC2DampingWatchdog.restore_seated` | 283–300 |
| `PC2DampingWatchdog.restore_zero_torque` | 302–320 |

## Code: watchdog-agent

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_aprilcube_calibration/pc2_watchdog_agent.py`.

[Pinned public source](https://github.com/sri299792458/g1-dex3-tabletop/blob/cf1b27704c82d877d23ff5a3c157df3218f02402/src/g1_aprilcube_calibration/pc2_watchdog_agent.py); base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `8c0d344c25823c40a157218e8b3ca845c527a558f771354872ef245cb8f955c0`.

| Symbol | Inspected lines |
|---|---|
| `run_watchdog` | 343–650 |

## Code: boundary

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_dex3_tabletop/control_boundary.py`.

**Local snapshot**; base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `688e4c962163e4191e86f4a71cf612c769cad26ba571d40713f28676e6b6c675`.

| Symbol | Inspected lines |
|---|---|
| `command_bound_snapshot` | 15–26 |
| `install_plan_at_current_boundary` | 54–129 |

## Code: tabletop

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_dex3_tabletop/hardware_tabletop.py`.

**Local snapshot**; base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `ad93824f2ea4ca8b9fae5b5e9b0be77efbaf94aa1b4811b71f8244e37095ba8e`.

| Symbol | Inspected lines |
|---|---|
| `run_tabletop` | 997–2658 |
| `_restore_seated_control` | 915–924 |

## Code: stack

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_dex3_tabletop/hardware_stack.py`.

**Local snapshot**; base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `8e531ce6acca6002e2755ab10d03ef54e8daaab11f01a144bbd7dc8ee47bfbe5`.

| Symbol | Inspected lines |
|---|---|
| `run_stack` | 570–1680 |
| `_find_direct_stack_plan` | 317–374 |
| `_execute_pick_place` | 377–523 |

## Code: contact

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_aprilcube_calibration/transports/unitree_dex3.py`.

[Pinned public source](https://github.com/sri299792458/g1-dex3-tabletop/blob/cf1b27704c82d877d23ff5a3c157df3218f02402/src/g1_aprilcube_calibration/transports/unitree_dex3.py); base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `1fc3f08a292d9031cf24db65ddbedd0c0be04616c8bc3a2ac90e71e9fdf50be0`.

| Symbol | Inspected lines |
|---|---|
| `classify_dex3_opposed_joint_obstruction` | 355–387 |
| `UnitreeDex3PostureController.command_close_for_retention_test` | 785–827 |
| `UnitreeDex3PostureController.verify_retention_at_lifted_checkpoint` | 1049–1150 |

## Code: perception

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_dex3_tabletop/tabletop_perception.py`.

[Pinned public source](https://github.com/sri299792458/g1-dex3-tabletop/blob/cf1b27704c82d877d23ff5a3c157df3218f02402/src/g1_dex3_tabletop/tabletop_perception.py); base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `8fc4f02598f1740e2d99bbbd8f18c924deaef07b2679850f792ca04e4d5fd2a5`.

| Symbol | Inspected lines |
|---|---|
| `_detect_resting_pose_hypotheses` | 240–317 |
| `_largest_hypothesis_consensus` | 129–227 |
| `observe_resting_cube` | 345–409 |
| `observe_resting_cube_pair` | 412–464 |
| `observe_live_cube_frame` | 36–68 |

## Code: object

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_dex3_tabletop/tabletop_object.py`.

[Pinned public source](https://github.com/sri299792458/g1-dex3-tabletop/blob/cf1b27704c82d877d23ff5a3c157df3218f02402/src/g1_dex3_tabletop/tabletop_object.py); base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `a1a0363cc7b7852fe706ceab32b9cafd840f5016578198cec34c8795c38e5e2b`.

## Code: camera-sync

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_dex3_tabletop/camera_state_sync.py`.

[Pinned public source](https://github.com/sri299792458/g1-dex3-tabletop/blob/cf1b27704c82d877d23ff5a3c157df3218f02402/src/g1_dex3_tabletop/camera_state_sync.py); base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `5d2a2e9056f465dacf5aa7db1bc618dd0a56cc7c062d4f065c9ceaac3c542e30`.

| Symbol | Inspected lines |
|---|---|
| `CameraStateInputBuffer.sample_at` | 144–203 |

## Code: camera-state

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_dex3_tabletop/state_estimation.py`.

[Pinned public source](https://github.com/sri299792458/g1-dex3-tabletop/blob/cf1b27704c82d877d23ff5a3c157df3218f02402/src/g1_dex3_tabletop/state_estimation.py); base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `e3734d2abe6550b050ef380a1c997dc567829f6dc55899b1e36c50e4d0cf247a`.

| Symbol | Inspected lines |
|---|---|
| `AnchoredCameraPoseEstimators.predict` | 215–248 |
| `AnchoredCameraStateEstimator.reset` | 312–320 |
| `AnchoredCameraStateEstimator.estimate` | 327–344 |

## Code: requests

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_dex3_tabletop/tabletop_workflow.py`.

[Pinned public source](https://github.com/sri299792458/g1-dex3-tabletop/blob/cf1b27704c82d877d23ff5a3c157df3218f02402/src/g1_dex3_tabletop/tabletop_workflow.py); base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `b18f70403919412bcb6484b3cb69a448cc49882b2883d265727b23de879d0792`.

| Symbol | Inspected lines |
|---|---|
| `build_tabletop_request` | 53–120 |
| `request_at_clearance_observation` | 136–194 |
| `request_at_estimated_pregrasp` | 197–224 |

## Code: planner-process

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_dex3_tabletop/persistent_planner.py`.

[Pinned public source](https://github.com/sri299792458/g1-dex3-tabletop/blob/cf1b27704c82d877d23ff5a3c157df3218f02402/src/g1_dex3_tabletop/persistent_planner.py); base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `ad28588d0c7098a67b0526479e0533ec293c2e5b2c98de36606d76901616794e`.

| Symbol | Inspected lines |
|---|---|
| `PersistentTabletopPlanner.launch` | 49–78 |
| `PersistentTabletopPlanner.request_payload` | 141–158 |

## Code: planning-session

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_dex3_tabletop/planning/tabletop_session.py`.

[Pinned public source](https://github.com/sri299792458/g1-dex3-tabletop/blob/cf1b27704c82d877d23ff5a3c157df3218f02402/src/g1_dex3_tabletop/planning/tabletop_session.py); base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `19b0c619e2b9a64028f6edc8672b9fad11d7ed4daa1927fa68413d650bb38c54`.

| Symbol | Inspected lines |
|---|---|
| `TabletopPlanningSession.plan_pregrasp_at_clearance` | 317–355 |
| `TabletopPlanningSession.replan_at_pregrasp` | 425–479 |
| `TabletopPlanningSession.plan_pick_place` | 237–266 |

## Code: planner

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_dex3_tabletop/planning/tabletop_planner.py`.

[Pinned public source](https://github.com/sri299792458/g1-dex3-tabletop/blob/cf1b27704c82d877d23ff5a3c157df3218f02402/src/g1_dex3_tabletop/planning/tabletop_planner.py); base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `1b195a6830cf5d7111d5089a4aed0221909913210b34030f23160e11be24f43e`.

| Symbol | Inspected lines |
|---|---|
| `_fresh_branch_start_state` | 2147–2159 |
| `plan_tabletop_task` | 5541–5563 |
| `plan_tabletop_pick_place` | 5700–5906 |
| `RetentionRouteValidator.validate` | 4048–4161 |

## Code: mpc

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_dex3_tabletop/planning/tabletop_mpc.py`.

[Pinned public source](https://github.com/sri299792458/g1-dex3-tabletop/blob/cf1b27704c82d877d23ff5a3c157df3218f02402/src/g1_dex3_tabletop/planning/tabletop_mpc.py); base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `a02750074407347782c0388f6ea8051ac2ed7dea8041e15783f8fc887bfd2862`.

| Symbol | Inspected lines |
|---|---|
| `MovingGraspMPC.update_moving_grasp_goal` | 1934–2084 |
| `MovingGraspMPC.solve_window` | 2269–2584 |

## Code: mpc-buffer

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_dex3_tabletop/mpc_command_buffer.py`.

[Pinned public source](https://github.com/sri299792458/g1-dex3-tabletop/blob/cf1b27704c82d877d23ff5a3c157df3218f02402/src/g1_dex3_tabletop/mpc_command_buffer.py); base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `05b69c7f9b66d146c50f20778428551b0f4442a9e4beb044d4d96781a6051e42`.

| Symbol | Inspected lines |
|---|---|
| `RollingMPCCommandBuffer.install` | 359–472 |
| `RollingMPCCommandBuffer.command` | 540–583 |

## Code: calibration-control

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_dex3_tabletop/calibration/control.py`.

**Local snapshot**; base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `8f552ebe6f5c0a5191c55c611a1602fb5176291eeabfe672c7e5231bc4142c6f`.

| Symbol | Inspected lines |
|---|---|
| `StandingCalibrationControl.acquire` | 104–149 |
| `StandingCalibrationControl.release` | 373–391 |
| `StandingCalibrationControl.close` | 393–439 |

## Code: calibration-adapter

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_dex3_tabletop/calibration/adapter.py`.

**Local snapshot**; base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `43b538b0b0a59c60cd01e3ffbbe4fd35e8886b193ccf48e0985b34734d710a5d`.

| Symbol | Inspected lines |
|---|---|
| `plan_owned_adapter` | 24–70 |

## Code: calibration-collect

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_dex3_tabletop/hardware_bilateral_calibration.py`.

**Local snapshot**; base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `a2b130526d36a0618a8307df9288c8eb0e2fa9b641d317ee43b7a6d27c86a08a`.

| Symbol | Inspected lines |
|---|---|
| `run_collect_bilateral_calibration` | 198–768 |

## Code: calibration-capture

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_dex3_tabletop/calibration/capture.py`.

**Local snapshot**; base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `34537917585aa75753c54a243afe98fb517b10f68872ca379c49ee365705c683`.

| Symbol | Inspected lines |
|---|---|
| `BilateralLiveBurstSource.capture_burst` | 162–230 |
| `select_bilateral_medoid` | 361–386 |

## Code: calibration-session

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_dex3_tabletop/calibration/session.py`.

**Local snapshot**; base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `9359efa609975c490b70049b0f112ec7129752ae879383b91f8cf15b698c9b46`.

| Symbol | Inspected lines |
|---|---|
| `BilateralSessionStore.append_capture` | 461–551 |
| `BilateralSessionStore.build_dataset` | 593–684 |

## Code: calibration-project

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_dex3_tabletop/calibration/projection.py`.

**Local snapshot**; base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `15334a44d48fa036f6bddf9bba7b481db8e1637456179f03d3970018829bd4c4`.

| Symbol | Inspected lines |
|---|---|
| `BilateralCalibrationProjection.project_side` | 204–243 |

## Code: calibration-solve

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_dex3_tabletop/calibration/solver.py`.

**Local snapshot**; base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `b324ae0de2536efe3ed14b89e6dfce7223a36780d2b08411bd0d3219c9205650`.

| Symbol | Inspected lines |
|---|---|
| `solve_bilateral_dataset` | 200–324 |

## Code: calibration-validate

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_dex3_tabletop/calibration/validation.py`.

**Local snapshot**; base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `513b845da9c03cdf531280bb8d29f0a9dc1679704d33974825fe1b36d6d5b725`.

| Symbol | Inspected lines |
|---|---|
| `validate_and_select_bilateral_model` | 342–496 |

## Code: calibration-bundle

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_dex3_tabletop/calibration/bundle.py`.

[Pinned public source](https://github.com/sri299792458/g1-dex3-tabletop/blob/cf1b27704c82d877d23ff5a3c157df3218f02402/src/g1_dex3_tabletop/calibration/bundle.py); base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `8a8b5fca56989f2e905a0bf781b9453d4ade511a1d0c3ecd9dd6f71247848de5`.

| Symbol | Inspected lines |
|---|---|
| `write_bilateral_calibration_bundle` | 34–193 |

## Code: mount

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_aprilcube_calibration/dex3_dorsal_mount.py`.

[Pinned public source](https://github.com/sri299792458/g1-dex3-tabletop/blob/cf1b27704c82d877d23ff5a3c157df3218f02402/src/g1_aprilcube_calibration/dex3_dorsal_mount.py); base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `6e11a194253c91b15d8253b5215555c067291d663d63c824cff388b129ab845e`.

| Symbol | Inspected lines |
|---|---|
| `Dex3DorsalMountSpec` | 28–138 |
| `palm_T_marker_face` | 221–244 |
| `mount_manifest` | 297–352 |

## Code: recorder

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_dex3_tabletop/raw_episode_recording.py`.

**Local snapshot**; base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `92c02eb85b726f2450d3b4b27246bee5a21c188d33ac9dd493a00c56476d6334`.

| Symbol | Inspected lines |
|---|---|
| `tabletop_raw_topics` | 146–151 |
| `RawEpisodeRecorder.start` | 340–404 |
| `RawEpisodeRecorder.stop` | 447–500 |

## Code: conversion

**Repository:** `g1-dex3-tabletop`. **Path:** `src/g1_dex3_tabletop/lerobot_conversion.py`.

[Pinned public source](https://github.com/sri299792458/g1-dex3-tabletop/blob/cf1b27704c82d877d23ff5a3c157df3218f02402/src/g1_dex3_tabletop/lerobot_conversion.py); base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `df65d7f7afcbf1c6fc368c3beb64883eb180aa303261ebfcc31b41f9c8c953fd`.

| Symbol | Inspected lines |
|---|---|
| `index_and_align_episode` | 259–491 |
| `build_numeric_frame` | 573–620 |
| `convert_episode` | 774–1046 |

## Code: descriptors

**Repository:** `g1-aprilcube-demo`. **Path:** `tools/build_dex3_rev1_descriptors.py`.

[Pinned public source](https://github.com/sri299792458/g1-aprilcube-demo/blob/f190470742f43101e9a22affaca80554722706ac/tools/build_dex3_rev1_descriptors.py); base revision `f190470742f43101e9a22affaca80554722706ac`.

File SHA-256: `f541db6c7a74b3b2acadf2e5127a4879e1df5c3f86ef6e8d50d71e6b21d6c109`.

| Symbol | Inspected lines |
|---|---|
| `derive_frame_and_sweep` | 189–230 |
| `build_side` | 431–468 |

## Code: raw-grasps

**Repository:** `g1-aprilcube-demo`. **Path:** `tools/run_aprilcube_raw_grasps.py`.

[Pinned public source](https://github.com/sri299792458/g1-aprilcube-demo/blob/f190470742f43101e9a22affaca80554722706ac/tools/run_aprilcube_raw_grasps.py); base revision `f190470742f43101e9a22affaca80554722706ac`.

File SHA-256: `9a2f3ac3fbbf292024f3d98fe7c738e3f0d352ed8205e44763e9ab42bc317b09`.

| Symbol | Inspected lines |
|---|---|
| `run_atlas` | 204–441 |

## Code: qualification

**Repository:** `g1-aprilcube-demo`. **Path:** `tools/run_isaac_atlas_qualification.py`.

[Pinned public source](https://github.com/sri299792458/g1-aprilcube-demo/blob/f190470742f43101e9a22affaca80554722706ac/tools/run_isaac_atlas_qualification.py); base revision `f190470742f43101e9a22affaca80554722706ac`.

File SHA-256: `b15fae7093cb6001d771dd8fee43397e3b024a6802271389b31c5d1dcf2ecc38`.

| Symbol | Inspected lines |
|---|---|
| `validate_completed_run` | 59–142 |
| `run_shard` | 145–265 |

## Code: shortlist

**Repository:** `g1-aprilcube-demo`. **Path:** `g1_aprilcube_demo/grasping/executable_shortlist.py`.

[Pinned public source](https://github.com/sri299792458/g1-aprilcube-demo/blob/f190470742f43101e9a22affaca80554722706ac/g1_aprilcube_demo/grasping/executable_shortlist.py); base revision `f190470742f43101e9a22affaca80554722706ac`.

File SHA-256: `6b39fb95a0262d5d57035c9898e21e97a83e9fbe2db581486cfe21d5e6dd8697`.

| Symbol | Inspected lines |
|---|---|
| `build_shortlist` | 257–442 |

## Code: support-atlas

**Repository:** `g1-aprilcube-demo`. **Path:** `g1_aprilcube_demo/grasping/support_atlas.py`.

[Pinned public source](https://github.com/sri299792458/g1-aprilcube-demo/blob/f190470742f43101e9a22affaca80554722706ac/g1_aprilcube_demo/grasping/support_atlas.py); base revision `f190470742f43101e9a22affaca80554722706ac`.

File SHA-256: `db06575db31ceaae98f42af3b0bcfb588f9fe151a5eec23b132dd3d605bf228e`.

| Symbol | Inspected lines |
|---|---|
| `evaluate_support` | 462–569 |

## Code: assembly

**Repository:** `g1-aprilcube-demo`. **Path:** `g1_aprilcube_demo/planning/runtime_assembly.py`.

[Pinned public source](https://github.com/sri299792458/g1-aprilcube-demo/blob/f190470742f43101e9a22affaca80554722706ac/g1_aprilcube_demo/planning/runtime_assembly.py); base revision `f190470742f43101e9a22affaca80554722706ac`.

File SHA-256: `e194f52f674655540c94fb19f7112568b52c813923599678e99a7d50ef482e1c`.

| Symbol | Inspected lines |
|---|---|
| `RuntimeAssemblyPlanner` | 189–1499 |

## Code: pressure

**Repository:** `dex3_pressure_tools`. **Path:** `dex3_pressure_tools/pressure_visualizer.py`.

[Pinned public source](https://github.com/sri299792458/dex3_pressure_tools/blob/e0b706df507160799b70732c7cc3244924ce8f5e/dex3_pressure_tools/pressure_visualizer.py); base revision `e0b706df507160799b70732c7cc3244924ce8f5e`.

File SHA-256: `1745ccfc41d50233cb35e17c81072a767672cd0f290e8030025a5be2f3534789`.

| Symbol | Inspected lines |
|---|---|
| `Dex3PressureVisualizer._state_callback` | 263–290 |
| `Dex3PressureVisualizer._finish_baseline` | 292–326 |
| `Dex3PressureVisualizer._publish_timer_callback` | 334–360 |

## Code: pressure-record

**Repository:** `dex3_pressure_tools`. **Path:** `dex3_pressure_tools/session_recorder.py`.

[Pinned public source](https://github.com/sri299792458/dex3_pressure_tools/blob/e0b706df507160799b70732c7cc3244924ce8f5e/dex3_pressure_tools/session_recorder.py); base revision `e0b706df507160799b70732c7cc3244924ce8f5e`.

File SHA-256: `bb7b7d8ff21342b06550d66dd5ccb9e233463f023d9943344dfbf8002d79c97f`.

| Symbol | Inspected lines |
|---|---|
| `Dex3PressureSessionRecorder._state_callback` | 56–66 |

## Code: pilot-state

**Repository:** `g1pilot`. **Path:** `g1pilot/state/robot_state.py`.

[Pinned public source](https://github.com/sri299792458/g1pilot/blob/72acc803edefe583c24f53e76a21d8d4ed10ed14/g1pilot/state/robot_state.py); base revision `72acc803edefe583c24f53e76a21d8d4ed10ed14`.

File SHA-256: `f6f39e37fd58f7c6a7641a6f39f0db867d6f0ac562de02652650977ec35dbcdf`.

| Symbol | Inspected lines |
|---|---|
| `RobotState.callback_lowstate` | 118–167 |

## Code: pilot-arms

**Repository:** `g1pilot`. **Path:** `g1pilot/manipulation/opensot_solver.py`.

[Pinned public source](https://github.com/sri299792458/g1pilot/blob/72acc803edefe583c24f53e76a21d8d4ed10ed14/g1pilot/manipulation/opensot_solver.py); base revision `72acc803edefe583c24f53e76a21d8d4ed10ed14`.

File SHA-256: `188cbcff48446d9add46e43a32d53700c10a6fac00eb21a225783278dde4ccdc`.

| Symbol | Inspected lines |
|---|---|
| `G1CollisionAvoidanceNode.control_loop` | 782–916 |

## Code: pilot-hands

**Repository:** `g1pilot`. **Path:** `g1pilot/manipulation/dx3_hand.py`.

[Pinned public source](https://github.com/sri299792458/g1pilot/blob/72acc803edefe583c24f53e76a21d8d4ed10ed14/g1pilot/manipulation/dx3_hand.py); base revision `72acc803edefe583c24f53e76a21d8d4ed10ed14`.

File SHA-256: `b0016d5276078fb1f46501e16c5c8ec53e929bfff49a1b5fc93ba6fbb91cae56`.

| Symbol | Inspected lines |
|---|---|
| `DX3Controller.initialize_hand_interfaces` | 99–112 |
| `DX3Controller.publish_commands` | 183–189 |

## Code: sim-plant

**Repository:** `g1pilot-dev`. **Path:** `g1pilot/simulation/mujoco_plant.py`.

[Pinned public source](https://github.com/sri299792458/g1pilot/blob/6b5af59b109e2ee687920fdf66ded6182725e945/g1pilot/simulation/mujoco_plant.py); base revision `6b5af59b109e2ee687920fdf66ded6182725e945`.

File SHA-256: `98e19f3305841b159967277f57c17518e1dc2fc66a1f4f563fea5e346777ec98`.

| Symbol | Inspected lines |
|---|---|
| `G1PilotUnitreeBridge` | 280–383 |
| `G1PilotMujocoPlant.build_body_command` | 631–635 |
| `G1PilotMujocoEnv.sim_step` | 592–596 |
| `G1PilotMujocoPlant.run` | 671–704 |

`g1pilot-dev` identifies the isolated July development snapshot of the `g1pilot` repository.

## Code: sim-policy

**Repository:** `g1pilot-dev`. **Path:** `g1pilot/simulation/openhomie_policy.py`.

[Pinned public source](https://github.com/sri299792458/g1pilot/blob/6b5af59b109e2ee687920fdf66ded6182725e945/g1pilot/simulation/openhomie_policy.py); base revision `6b5af59b109e2ee687920fdf66ded6182725e945`.

File SHA-256: `dd7e1901debdbd02a22a3240fc27780aacc021b2568a60a44ef47a4244fd6e86`.

| Symbol | Inspected lines |
|---|---|
| `compute_openhomie_observation` | 45–90 |
| `OpenHomiePolicy.run` | 138–152 |

`g1pilot-dev` identifies the isolated July development snapshot of the `g1pilot` repository.

## Code: sim-launch

**Repository:** `g1pilot-dev`. **Path:** `launch/mujoco_openhomie_manipulation.launch.py`.

[Pinned public source](https://github.com/sri299792458/g1pilot/blob/6b5af59b109e2ee687920fdf66ded6182725e945/launch/mujoco_openhomie_manipulation.launch.py); base revision `6b5af59b109e2ee687920fdf66ded6182725e945`.

File SHA-256: `4ab7113ec0ff88c280422e7d235e86f65fa2e9b87b766820120f678f9f1c7961`.

| Symbol | Inspected lines |
|---|---|
| `_launch_setup` | 21–63 |

`g1pilot-dev` identifies the isolated July development snapshot of the `g1pilot` repository.

## Code: test-stack

**Repository:** `g1-dex3-tabletop`. **Path:** `tests/test_stack_workflow.py`.

**Local snapshot**; base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `f7565ff664fdfb779b5787033f2a16e8fb42dd98ef736f0a499b3634ee126945`.

## Code: test-tabletop

**Repository:** `g1-dex3-tabletop`. **Path:** `tests/test_tabletop_workflow.py`.

[Pinned public source](https://github.com/sri299792458/g1-dex3-tabletop/blob/cf1b27704c82d877d23ff5a3c157df3218f02402/tests/test_tabletop_workflow.py); base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `cb723d6b30d2b804776a204475c450c499d312b8f2c19ea2f6f6c65115aa0900`.

## Code: test-state

**Repository:** `g1-dex3-tabletop`. **Path:** `tests/test_state_estimation.py`.

[Pinned public source](https://github.com/sri299792458/g1-dex3-tabletop/blob/cf1b27704c82d877d23ff5a3c157df3218f02402/tests/test_state_estimation.py); base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `760f1a31851d6d1df7ed9cb7a5528af598991d70e3d2202492979c38a0e94a5b`.

## Code: test-sync

**Repository:** `g1-dex3-tabletop`. **Path:** `tests/test_camera_state_sync.py`.

[Pinned public source](https://github.com/sri299792458/g1-dex3-tabletop/blob/cf1b27704c82d877d23ff5a3c157df3218f02402/tests/test_camera_state_sync.py); base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `5866802b29e39f5cbb247c9c46c8f94d7bd157a2778ae27d684fda4b253fd23e`.

## Code: test-standing

**Repository:** `g1-dex3-tabletop`. **Path:** `tests/test_standing_calibration_control.py`.

**Local snapshot**; base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `81b4f6798371c174fdb0141a3aada2724c48e6c2942f269d79f564df11dcb192`.

## Code: test-calibration

**Repository:** `g1-dex3-tabletop`. **Path:** `tests/test_bilateral_calibration.py`.

**Local snapshot**; base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `ef5664e06b19408e7f5090bb963695f7592091e69130ce7444f01fd173bd7214`.

## Code: test-recorder

**Repository:** `g1-dex3-tabletop`. **Path:** `tests/test_raw_episode_recording.py`.

**Local snapshot**; base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `a8c9a1488de65d6b2c3ef309bb48daf756a98882fb740720610a906bff369795`.

## Code: test-conversion

**Repository:** `g1-dex3-tabletop`. **Path:** `tests/test_lerobot_conversion.py`.

[Pinned public source](https://github.com/sri299792458/g1-dex3-tabletop/blob/cf1b27704c82d877d23ff5a3c157df3218f02402/tests/test_lerobot_conversion.py); base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `443e664ebf2efd3c1913bcee3a7c676d64c7c669191bf488cddfef78cd6f1f64`.

## Code: test-mpc

**Repository:** `g1-dex3-tabletop`. **Path:** `tests/test_mpc_command_buffer.py`.

[Pinned public source](https://github.com/sri299792458/g1-dex3-tabletop/blob/cf1b27704c82d877d23ff5a3c157df3218f02402/tests/test_mpc_command_buffer.py); base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `2a82374e09ba067c2ed2754243c321f3eaead26d7a8aa11eeb2554e62547574e`.

## Code: test-executor

**Repository:** `g1-dex3-tabletop`. **Path:** `tests/test_executor_state_machine.py`.

[Pinned public source](https://github.com/sri299792458/g1-dex3-tabletop/blob/cf1b27704c82d877d23ff5a3c157df3218f02402/tests/test_executor_state_machine.py); base revision `cf1b27704c82d877d23ff5a3c157df3218f02402`.

File SHA-256: `6c98ec5219f641a5660ab497d11c27a145b16a94e3aa0c8ac72fdeec9bbff8de`.

