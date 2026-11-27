# Computer Vision · 计算机视觉 — Sources and Review Notes

**Scope:** This is an original educational term handbook for computer vision from image processing and geometry to contemporary deep learning, neural rendering and vision-language models. It does not duplicate the existing GPU Kernel or NLP subject glossaries.

**Canonical manuscript:** `data/computer-vision/chapters/01.tsv` through `20.tsv`, with fields `English|中文|abbr|definition`. `data/computer-vision/parts/*.tsv` are intermediate 4-chapter aggregates.

**Rebuild:** `node scripts/render_computer_vision.mjs`. **Read-only verification:** `node scripts/render_computer_vision.mjs --check`, comparing the derived TSV/Markdown/PDF and their Pages mirrors byte-for-byte.

**Size:** 500 unique English headwords, 20 chapters, 16 concept comparisons, 12 intermediate interview questions and 12 worked exam problems.

**Editorial status:** Programmatic validation of row counts, mandatory fields and case-insensitive unique English headwords is implemented. Independent domain-expert fact review, real PDF visual checks, font fallback, text extraction and accessibility verification are **not yet complete**. Bibliographic sources are references, not proof of item-by-item endorsement.

## Primary books, papers, and official documentation
1. [Szeliski, Computer Vision: Algorithms and Applications (2nd ed.)](https://link.springer.com/book/10.1007/978-3-030-34372-9)
2. [Stanford CS231n: Deep Learning for Computer Vision (2026)](https://cs231n.stanford.edu/2026/schedule.html)
3. [OpenCV Documentation](https://docs.opencv.org/4.x/)
4. [PyTorch Torchvision: Models and Pre-trained Weights](https://docs.pytorch.org/vision/stable/models.html)
5. [COCO: Detection Evaluation Metrics](https://cocodataset.org/dataset/detection-eval.htm)
6. [He et al., Deep Residual Learning for Image Recognition (2015)](https://arxiv.org/abs/1512.03385)
7. [Dosovitskiy et al., An Image Is Worth 16x16 Words (2020)](https://arxiv.org/abs/2010.11929)
8. [Carion et al., End-to-End Object Detection with Transformers (2020)](https://arxiv.org/abs/2005.12872)
9. [Kirillov et al., Segment Anything (2023)](https://arxiv.org/abs/2304.02643)
10. [Mildenhall et al., NeRF: Representing Scenes as Neural Radiance Fields (2020)](https://arxiv.org/abs/2003.08934)
11. [Kerbl et al., 3D Gaussian Splatting for Real-Time Radiance Field Rendering (2023)](https://arxiv.org/abs/2308.04079)
12. [Radford et al., Learning Transferable Visual Models from Natural Language Supervision (2021)](https://arxiv.org/abs/2103.00020)
13. [Ho et al., Denoising Diffusion Probabilistic Models (2020)](https://arxiv.org/abs/2006.11239)
14. [KITTI Vision Benchmark Suite](https://www.cvlibs.net/datasets/kitti/)
15. [ImageNet Project](https://www.image-net.org/)

## Review nuances
1. The camera intrinsic matrix K and extrinsic pose [R|t] use coordinate-system conventions that must be specified; world-to-camera vs camera-to-world cannot be exchanged blindly.
2. Morphological dilation and convolution dilation rate are distinct homonymous operations; English headwords are intentionally disambiguated.
3. Monocular depth may lack scale; metric depth requires calibration, known baseline, or another scale reference.
4. AP50 alone is **not** COCO AP averaged over the ten IoU thresholds from .50 to .95.
5. Semantic, instance and panoptic segmentation have different targets and matching criteria.
6. NeRF and 3D Gaussian Splatting are distinct representation/rendering methods; speed and image quality comparisons require matched experimental settings.
7. VLM factual statements require evidence, independent of benchmark classification accuracy.
8. Sensitive visual data requires privacy/retention safeguards; general CV performance does not imply safety.
