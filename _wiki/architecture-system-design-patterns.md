---
layout: page
title: "Architecture — System Design Patterns"
---

## Overview

15 battle-tested patterns for building distributed systems. Organised by primary concern: resilience, data flow, reliability, infrastructure, scalability. The rule: start simple, apply patterns when the specific problem arises. Over-engineering with patterns upfront is as harmful as under-engineering.

---

## Resilience Patterns

### 1. Circuit Breaker

Prevents cascading failures. Cuts off requests to a failing service after a failure threshold is reached.

**States:** CLOSED (normal) → OPEN (blocking) → HALF_OPEN (testing recovery) → CLOSED

```
[CLOSED] → failures exceed threshold → [OPEN] → timeout passes → [HALF_OPEN] → success → [CLOSED]
```

Use when: calling external services or downstream dependencies that can fail intermittently.

### 2. Bulkhead

Isolates system components with separate resource pools (thread pools, connection pools). A failure in one pool cannot exhaust resources from others.

```
paymentThreadPool   = 10 threads
searchThreadPool    = 20 threads
reportingThreadPool = 5 threads
```

If reporting goes down, payment and search continue unaffected.

### 3. Retry with Exponential Backoff

For transient failures — back off exponentially between retries and add jitter to avoid thundering herd.

```
delay = min(1000 * 2^attempt, 30000) + random_jitter
```

Don't retry immediately — a struggling service needs breathing room.

### 4. Back Pressure

When consumers can't keep up, signal producers to slow down rather than letting queues grow unbounded.

```
Producer → [Queue 1000/1000] → Consumer (overwhelmed)
→ apply back pressure
Producer (slowed) → [Queue 800/1000] → Consumer (recovering)
```

---

## Data Flow Patterns

### 5. Saga

Manages distributed transactions across multiple services using compensating actions instead of 2PC locking.

**Each step has a compensating rollback:**

```
reserve_inventory → process_payment → ship_order
       ↓ failure             ↓ failure
   (no rollback)    release_inventory   refund_payment + release_inventory
```

Use for: order fulfilment, booking workflows, anything spanning multiple services.

### 6. Two-Phase Commit (2PC)

Atomic operation across multiple databases. Phase 1: all participants vote "ready". Phase 2: coordinator commits or aborts.

```
Coordinator → Prepare → [DB1, DB2 vote Yes] → Commit
```

Heavy but guarantees atomicity. Use only when eventual consistency is not acceptable.

### 7. CQRS (Command Query Responsibility Segregation)

Separate write model (normalised, transactional DB) from read model (denormalised, cached, read replica). Optimise each independently.

```
Write path: POST /orders → normalised SQL DB
Read path:  GET /order-summary → Redis cache / read replica
```

Adds complexity. Justified for high-read/high-write systems with different performance requirements.

### 8. Event Sourcing

Store all state changes as immutable events instead of current state. Current state is derived by replaying events.

```
events: [DEPOSITED(100), WITHDRAWN(30), DEPOSITED(50)]
balance = replay(events) → 120
```

Benefits: full audit trail, time travel, easy event replay. Cost: query complexity, eventual consistency between projections.

---

## Reliability Patterns

### 9. Outbox Pattern

Guarantees event publishing without distributed transactions. Write to an `outbox` table in the same DB transaction as the business operation. A separate poller reads the outbox and publishes to the message queue.

```sql
BEGIN;
  INSERT INTO orders ...;
  INSERT INTO outbox (event_type, payload) VALUES ('ORDER_CREATED', ...);
COMMIT;
-- Separate process polls outbox → publishes to Kafka/RabbitMQ
```

Solves: "wrote to DB but failed to publish event" inconsistency.

### 10. Dead Letter Queue (DLQ)

Route unprocessable messages to a separate queue for inspection and retry instead of blocking the main queue.

```
Queue → [Processor] → fails 3× → Dead Letter Queue → [Manual Review / Retry]
```

Prevents "poison messages" from halting all processing.

### 11. Leader Election

In clustered systems, elect a single coordinator to avoid split-brain and ensure consistent decisions (e.g., scheduled jobs, distributed locks).

Tools: etcd, ZooKeeper, Consul. Node acquires a lease with TTL; if it dies, lease expires and another node can acquire it.

---

## Infrastructure Patterns

### 12. Strangler Fig

Gradually replace a legacy system by routing increasing traffic percentages to the new implementation. No big-bang rewrite.

```
Router → 10% → New API
       → 90% → Legacy API
```

Increment over weeks/months. If new system is healthy, increase traffic share. Roll back is trivial.

### 13. Sidecar

Deploy auxiliary concerns (logging, auth, monitoring, service mesh proxy) as a separate container alongside the main app. Main app stays focused; sidecar handles cross-cutting concerns.

```yaml
containers:
  - name: app          # business logic
  - name: log-sidecar  # fluentd
  - name: auth-proxy   # envoy / istio
```

---

## Scalability Patterns

### 14. Cache-Aside

Application manages cache explicitly. Check cache first; on miss load from DB and populate cache.

```
GET user → check cache
  → hit  → return cached value
  → miss → query DB → cache.set(key, value, ttl=3600) → return
```

Most common caching pattern. Application controls cache lifecycle.

### 15. Sharding

Partition data across nodes using a shard key. Distributes both storage and query load.

```python
shard_id = hash(user_id) % num_shards
db_connections[shard_id].insert(user)
```

Choose shard key carefully — a hot key creates uneven load. Common keys: user ID (hash), region, date range.

---

## Pattern Selection Guide

| Problem | Pattern |
|---|---|
| Downstream service failing | Circuit Breaker |
| Resource exhaustion spreading | Bulkhead |
| Transient network errors | Retry + Backoff |
| Consumer overwhelmed | Back Pressure |
| Multi-service transaction | Saga |
| Event publish + DB write atomicity | Outbox |
| Unprocessable messages blocking queue | Dead Letter Queue |
| Split-brain in cluster | Leader Election |
| Replacing legacy system | Strangler Fig |
| Read/write performance mismatch | CQRS |
| Full audit trail needed | Event Sourcing |
| Cross-cutting concerns (logging/auth) | Sidecar |
| Hot data, slow DB reads | Cache-Aside |
| Data too large for one node | Sharding |

---

## See Also

- [Architecture — System Design Concepts](/wiki/architecture-system-design-concepts/) — 30 foundational concepts (caching, replication, sharding, CAP theorem, etc.)
- [Architecture — System Design Learning](/wiki/architecture-system-design-learning/) — Resources and methodology for learning system design
- [C++ — Lock-Free Ring Buffers](/wiki/c-lock-free-ring-buffers/) — Low-latency system design at the implementation level

