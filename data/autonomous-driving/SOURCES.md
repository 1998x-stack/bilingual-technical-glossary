# Autonomous Driving / 自动驾驶系统 — Source and Editorial Notes

**Scope:** 500 original bilingual terms, 20 chapters × 25, 16 concept contrasts, 12 medium-level interview questions and 12 worked examination problems. Complements Robotics, Computer Vision and Computer Graphics.

**Canonical text:** `data/autonomous-driving/chapters/01.tsv` through `20.tsv`; line format `English|中文|abbr|definition`. `data/autonomous-driving/parts/` are intermediate aggregates.

**Rebuild and check:** `node scripts/render_autonomous_driving.mjs`; `node scripts/render_autonomous_driving.mjs --check` for byte-identical Markdown/PDF and Pages mirrors.

**Technical edition boundary:** SAE J3016_202609 is the current public SAE revision checked for this manuscript (published 2026-09-20); the ISO 26262-1:2018 standard remains published while an ISO/DIS draft exists. Do not equate Level 2 driver support with Level 4 ADS functionality. Standards text is independently paraphrased; no copyrighted normative content is reproduced in full.

**Validation status:** Chapter sizes, bilingual required fields, headword uniqueness and PDF object layout checked programmatically. Independent automotive safety/engineering expert review, vehicle testing, PDF visual text extraction and accessibility review are still pending.

## Authoritative sources and papers
1. [SAE J3016_202609 — Driving Automation Taxonomy (current revision September 2026)](https://saemobilus.sae.org/standards/j3016_202609-taxonomy-definitions-terms-related-driving-automation-systems-road-motor-vehicles)
2. [Autoware Documentation — Autonomous Driving Stack](https://docs.autoware.org/main/design/autoware-architecture-v2/)
3. [ASAM OpenDRIVE — Road Network Description Standard](https://www.asam.net/standards/detail/opendrive/)
4. [ASAM OpenSCENARIO V2.0.0 — Scenario Description Standard](https://www.asam.net/standards/detail/openscenario/v200/)
5. [CARLA Simulator — Official Website](https://carla.org/)
6. [CARLA 1.0 — November 2026 Release Notes](https://carla.org/2026/11/17/release-1.0/)
7. [ISO 26262-1:2018 — Functional Safety Vocabulary](https://www.iso.org/standard/68383.html)
8. [ISO 21448:2022 — Safety of the Intended Functionality](https://www.iso.org/standard/77490.html)
9. [Waymo Open Dataset](https://waymo.com/open/)
10. [nuScenes — Multimodal Autonomous Driving Dataset](https://www.nuscenes.org/)
11. [KITTI Vision Benchmark Suite](https://www.cvlibs.net/datasets/kitti/)
12. [Argoverse Dataset](https://www.argoverse.org/)
13. [Lanelet2 — High-definition Road Map Framework](https://github.com/fzi-forschungszentrum-informatik/Lanelet2)
14. [Mobileye RSS — On a Formal Model of Safe and Scalable Self-driving Cars](https://arxiv.org/abs/1708.06374)
15. [Autoware Foundation Repository](https://github.com/autowarefoundation/autoware)

## Key review cautions
1. J3016 levels apply to engaged driving-automation functions, not a permanent model badge for the entire vehicle.
2. The ODD includes multiple simultaneous restrictions. An ADS function outside its ODD requires appropriate transition or fallback behavior.
3. TTC and THW are not interchangeable. TTC estimates an impact time only under a chosen relative-motion model.
4. Low offline error on logged driving trajectories cannot establish closed-loop driving safety.
5. Fusion requires both geometric calibration and timestamp alignment; ignoring either can create large systematic errors.
6. A high-fidelity scenario simulator cannot by itself validate safety in all real-world traffic conditions.
7. ISO 26262 and ISO 21448 SOTIF address different risk origins; they require system-specific evidence and do not promise zero risk.
8. A deployed fleet must implement secure software delivery, incident investigation, independent safeguards and operational risk controls.
