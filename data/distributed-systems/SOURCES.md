# Distributed Systems / 分布式系统 · editorial references

- **Canonical source:** `data/distributed-systems/chapters/01.tsv`–`16.tsv`; four-field source format `English|中文|abbr|definition`.
- **Aggregated intermediate material:** `data/distributed-systems/parts/*.tsv` is generated solely from 4-chapter groups and is not the editing source.
- **Rebuild:** `node scripts/render_distributed_systems.mjs` (write) or `node scripts/render_distributed_systems.mjs --check` (read-only).
- **Scope:** 400 original short definitions, 16 chapters, 12 contrasts, 8 interview questions and 8 exam questions.
- **Status:** structure/count/English uniqueness reviewed automatically; external reviewer accuracy audit and cross-viewer PDF visual inspection remain pending. Do not mark verified.

## Technical references
1. [Designing Data-Intensive Applications, 2nd ed. (Kleppmann & Riccomini)](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/)
2. [Time, Clocks, and the Ordering of Events in a Distributed System (Lamport, 1978)](https://www.microsoft.com/en-us/research/publication/time-clocks-ordering-events-distributed-system/)
3. [Paxos Made Simple (Lamport, 2001)](https://www.microsoft.com/en-us/research/publication/paxos-made-simple/)
4. [In Search of an Understandable Consensus Algorithm (Ongaro & Ousterhout, 2014)](https://raft.github.io/)
5. [Dynamo: Amazon's Highly Available Key-value Store (DeCandia et al., 2007)](https://www.amazon.science/publications/dynamo-amazons-highly-available-key-value-store)
6. [MapReduce: Simplified Data Processing on Large Clusters (Dean & Ghemawat, 2004)](https://research.google/pubs/mapreduce-simplified-data-processing-on-large-clusters/)
7. [Spanner: TrueTime and external consistency (Google Cloud documentation)](https://docs.cloud.google.com/spanner/docs/true-time-external-consistency)
8. [Jepsen: Consistency Models](https://jepsen.io/consistency/models)

## Editorial caveats

- CAP availability differs from operational SLO availability; CAP's consistency target needs an explicit strong-consistency definition.
- Idempotent RPC, exactly-once messaging and transaction atomicity require clear observable scope and durable deduplication assumptions.
- Quorum counts alone do not establish linearizability in arbitrary leaderless implementations.
- This publication does not claim all papers' authors have endorsed translations or definitions.
