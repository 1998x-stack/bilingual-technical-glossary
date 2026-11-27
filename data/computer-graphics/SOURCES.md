# Computer Graphics | 计算机图形学 — Sources and Editorial Notes

**Positioning:** A new independent graphics and rendering technical handbook, complementary to the Computer Vision and GPU Kernel volumes. It covers scene synthesis rather than image recognition.

**Canonical manuscript:** `data/computer-graphics/chapters/01.tsv` through `20.tsv`; record structure `English|中文|abbr|definition`. The `data/computer-graphics/parts/*.tsv` files are intermediate aggregations.

**Build:** `node scripts/render_computer_graphics.mjs`; read-only deterministic verification: `node scripts/render_computer_graphics.mjs --check`.

**Scope:** 500 unique English headwords, 20 chapters, 16 contrasts, 12 medium interview Q&As and 12 worked exam problems.

**Review status:** Automatic field, unique-term, count and artifact consistency checks can run. Full graphics-domain expert review, cross-reader glyph display/text extraction, and PDF accessibility checks are **not yet completed**. Sources guide terminology but do not establish endorsement of each item.

## Reference textbooks, specifications and implementations
1. [Pharr, Jakob & Humphreys, Physically Based Rendering (4th edition)](https://pbr-book.org/4ed/contents)
2. [Scratchapixel — Computer Graphics and Ray Tracing](https://www.scratchapixel.com/)
3. [Khronos Vulkan Specification](https://docs.vulkan.org/spec/latest/)
4. [Khronos OpenGL Reference Documentation](https://www.khronos.org/opengl/wiki/)
5. [Khronos glTF 2.0 Specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html)
6. [Microsoft Direct3D 12 Graphics Documentation](https://learn.microsoft.com/en-us/windows/win32/direct3d12/direct3d-12-graphics)
7. [Apple Metal Documentation](https://developer.apple.com/metal/)
8. [OpenUSD Documentation](https://openusd.org/release/index.html)
9. [NVIDIA OptiX Programming Guide](https://raytracing-docs.nvidia.com/optix8/guide/index.html)
10. [RenderDoc Graphics Debugger](https://renderdoc.org/)
11. [Blender Manual](https://docs.blender.org/manual/en/latest/)
12. [SIGGRAPH Course: Real-Time Rendering Resources](https://www.realtimerendering.com/)
13. [Mildenhall et al. (2020), NeRF: Representing Scenes as Neural Radiance Fields](https://arxiv.org/abs/2003.08934)
14. [Kerbl et al. (2023), 3D Gaussian Splatting for Real-Time Radiance Field Rendering](https://arxiv.org/abs/2308.04079)
15. [Müller et al. (2022), Instant Neural Graphics Primitives](https://nvlabs.github.io/instant-ngp/)

## Review-sensitive distinctions
1. Distinguish radiance (W/(m²·sr)) from irradiance (W/m²) and radiant flux (W).
2. PBR is not a single shader algorithm; BRDF reflectance, BSDF transmission, Fresnel and energy constraints require consistent conventions.
3. Ray casting, ray tracing and path tracing are related but distinct techniques.
4. Shading and blending should normally operate in linear-light values, not directly on sRGB-encoded RGB.
5. NDC depth conventions, matrix multiplication order, world-to-view transforms, and API synchronization rules vary by environment.
6. Path tracing SPP, denoising and sampling-strategy changes affect noise and bias; visual quality needs reproducible test settings.
7. Not all GPU ray tracing pipelines expose the same shader stages or acceleration features.
8. NeRF and 3DGS comparisons require matched training views, output resolution and quality targets.
