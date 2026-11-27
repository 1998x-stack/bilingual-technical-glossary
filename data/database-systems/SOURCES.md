# Database Systems | 数据库系统 — sources and editorial notes

**Positioning:** This volume focuses on internal DBMS structures and algorithms, complementing `glossaries/sql-database.md`, which focuses more heavily on SQL syntax and operations. Reused cross-cutting concepts have distinct systems-level explanations.

**Canonical source:** `data/database-systems/chapters/01.tsv`–`16.tsv`, fields `English|中文|abbr|definition`. Intermediate `data/database-systems/parts/*.tsv` is a convenience compilation.

**Build:** `node scripts/render_database_systems.mjs`, or `node scripts/render_database_systems.mjs --check` for deterministic read-only verification.

**Scope:** 400 bilingual terms across 16 chapters; 14 distinctions; 10 intermediate interview questions; 10 exam questions with answers and arithmetic.

**Validation:** 400 unique English headwords, nonempty required fields, correct chapter counts and PDF object structure verified. Independent expert editorial review, reader visual inspection, and engine-version-specific experiments are still required.

## References
1. [CMU 15-445/645: Database Systems (Fall 2026)](https://15445.courses.cs.cmu.edu/fall2026/)
2. [PostgreSQL Documentation: Concurrency Control and MVCC](https://www.postgresql.org/docs/current/mvcc.html)
3. [PostgreSQL Documentation: Write-Ahead Logging](https://www.postgresql.org/docs/current/wal.html)
4. [PostgreSQL Documentation: Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html)
5. [SQLite: Architecture of SQLite](https://www.sqlite.org/arch.html)
6. [SQLite: Query Planning](https://www.sqlite.org/queryplanner.html)
7. [RocksDB Wiki: Compaction](https://github.com/facebook/rocksdb/wiki/Compaction)
8. [RocksDB Wiki: RocksDB Overview](https://github.com/facebook/rocksdb/wiki/RocksDB-Overview)
9. [Mohan et al. (1992): ARIES Recovery Algorithm (IBM)](https://research.ibm.com/publications/aries-a-transaction-recovery-method-supporting-fine-granularity-locking-and-partial-rollbacks-using-write-ahead-logging)
10. [CockroachDB Documentation: Architecture Overview](https://www.cockroachlabs.com/docs/stable/architecture/overview.html)
11. [Jepsen: Consistency Models](https://jepsen.io/consistency/models)

## Semantic cautions
- SQL isolation level names do not imply identical allowed outcomes across database products. Always check a specific implementation and version.
- MVCC is a storage/concurrency technique, not a guarantee of serializability.
- Storage layout varies: B+ tree leaf nodes may contain row data or pointers, depending on clustered vs secondary index design.
- WAL's log-before-data ordering must be maintained; group commit and the storage durability model affect the exact guarantee.
- B-tree, LSM, hashing and bitmap indexes have workload-dependent costs.
- Distributed quorum counts alone are insufficient to establish linearizability.
- Query optimizers use estimated cardinalities; physical plan choices and metrics vary by data distribution.
