# CUDA bilingual glossary: official technical sources and review status

- **Canonical manuscript:** `data/cuda/chapters/01.tsv`–`16.tsv`. Format: `English|中文|abbr|definition`. 
- **Intermediate files:** `data/cuda/parts/*.tsv` are generated aggregates, not the authoritative edit source.
- **Rebuild:** `node scripts/render_cuda.mjs` to generate, `node scripts/render_cuda.mjs --check` to compare five derived artifacts in read-only mode.
- **Content:** 400 unique English headwords, 16 chapters, 14 concept comparisons, 10 intermediate interview Q&As and 10 worked exam questions.
- **Basis:** NVIDIA documentation URLs below (accessed November 2026). CUDA release documentation and GPU compute capabilities differ.
- **Editorial status:** structural and duplicate checks passed; manual cross-GPU experiments, independent expert fact review, PDF accessibility and cross-reader glyph review are outstanding.

## Official references
1. [NVIDIA CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/)
2. [NVIDIA CUDA C++ Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/)
3. [CUDA Runtime API Reference](https://docs.nvidia.com/cuda/cuda-runtime-api/)
4. [CUDA Driver API Reference](https://docs.nvidia.com/cuda/cuda-driver-api/)
5. [Parallel Thread Execution ISA](https://docs.nvidia.com/cuda/parallel-thread-execution/)
6. [Nsight Compute Profiling Guide](https://docs.nvidia.com/nsight-compute/ProfilingGuide/)
7. [Nsight Systems Documentation](https://docs.nvidia.com/nsight-systems/)
8. [Compute Sanitizer Documentation](https://docs.nvidia.com/compute-sanitizer/)
9. [NVIDIA CUDA Libraries](https://developer.nvidia.com/gpu-accelerated-libraries)
10. [NCCL User Guide](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/)
11. [NVIDIA CUTLASS Documentation](https://docs.nvidia.com/cutlass/)
12. [NVIDIA CUDA Compatibility Guide](https://docs.nvidia.com/deploy/cuda-compatibility/)

## Special cautions

1. Warp size, thread block clusters, memory synchronization details and Tensor Core precision are hardware- and toolkit-version sensitive.
2. Local memory is private per thread, not necessarily physically on-chip; its accesses may incur device DRAM traffic.
3. Occupancy is distinct from measured utilization or achieved throughput; higher occupancy is not universally better.
4. CUDA streams allow potential concurrency but cannot guarantee it without available resources and correct dependency handling.
5. A memory fence provides ordering semantics but is not an all-thread barrier. Atomicity does not automatically imply arbitrary memory ordering.
6. `cudaMemcpyAsync` and `cudaMallocAsync` require adherence to memory-type, pooling and stream-ordering rules.
7. Numeric reproducibility needs explicit operation, architecture, compiler and reduction-order assumptions.
