# Robotics / 机器人学 — Sources and Editorial Notes

**Scope:** A standalone robotics foundations-to-embodied-AI terminology volume, complementary to the existing Computer Vision, Computer Graphics, Machine Learning, AI Agent and GPU Kernel handbooks.

**Canonical sources:** `data/robotics/chapters/01.tsv`–`20.tsv`. Each data row has `English|中文|abbr|definition`. Files under `data/robotics/parts/` are intermediate compiled aggregates.

**Rebuild:** `node scripts/render_robotics.mjs`. Read-only reproducibility check: `node scripts/render_robotics.mjs --check`. The generated Markdown and PDF mirrors must be byte-identical.

**Content:** 500 unique English headwords in 20 chapters, 16 concept comparisons, 12 medium-difficulty interview questions with answers, and 12 medium-difficulty exam problems with worked solutions.

**Validation:** Programmatic checks cover row shape, nonempty mandatory fields, unique English headwords, chapter totals and PDF object layout. Independent mechanical engineering/robotics expert review, physical-hardware validation, PDF reader visual inspection and accessibility review are pending.

## Core references
1. [Lynch and Park, Modern Robotics: Mechanics, Planning, and Control](https://modernrobotics.northwestern.edu/)
2. [Siciliano et al., Robotics: Modelling, Planning and Control](https://link.springer.com/book/10.1007/978-1-84628-642-1)
3. [Corke, Robotics, Vision and Control](https://petercorke.com/rvc/)
4. [LaValle, Planning Algorithms](https://lavalle.pl/planning/)
5. [Thrun, Burgard and Fox, Probabilistic Robotics](https://mitpress.mit.edu/9780262201629/probabilistic-robotics/)
6. [MIT Underactuated Robotics by Russ Tedrake](https://underactuated.mit.edu/)
7. [ROS 2 Jazzy Documentation](https://docs.ros.org/en/jazzy/)
8. [ROS 2 Topics, Services and Actions Guide](https://docs.ros.org/en/jazzy/How-To-Guides/Topics-Services-Actions.html)
9. [MoveIt 2 Documentation](https://moveit.picknik.ai/main/index.html)
10. [Navigation2 Documentation](https://docs.nav2.org/)
11. [Open Motion Planning Library (OMPL)](https://ompl.kavrakilab.org/)
12. [Gazebo Sim Documentation](https://gazebosim.org/docs/latest/)
13. [MuJoCo Documentation](https://mujoco.readthedocs.io/en/stable/overview.html)
14. [Diffusion Policy (Chi et al.)](https://diffusion-policy.cs.columbia.edu/)
15. [Open X-Embodiment / RT-X](https://robotics-transformer-x.github.io/)

## Important interpretation boundaries
1. SE(3) frame transforms require explicit source/target convention and quaternion component order; do not substitute inverse transforms silently.
2. Full rank of the task Jacobian, singularities and null-space dimension depend on robot configuration and the selected task variables.
3. Holonomic and nonholonomic **constraints** differ by integrability; nonholonomic motion models cannot be treated as unrestricted holonomic XY motion.
4. The robot dynamics equation is convention-dependent in how Coriolis/centrifugal contributions are factored; force sign and wrench ordering vary.
5. An EKF is not a general multimodal belief-state estimator; time synchronization, calibration and correct data association strongly affect SLAM.
6. Sampling-based motion planning is not automatically a valid time-parameterized or collision-free executed trajectory.
7. Force closure and form closure are distinct, and friction-cone assumptions materially affect grasps.
8. ROS 2 Topics, Services and Actions are intended for distinct communication lifecycles; QoS and executor behavior depend on ROS distribution.
9. Robot safety requires independent risk assessment, hardware constraints, testing and functional-safety engineering rather than trusting policy benchmark success alone.
