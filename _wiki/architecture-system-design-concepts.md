---
layout: page
title: "Architecture — System Design Concepts"
domain: "Architecture"
---

## Overview

30 core building blocks of scalable system design, grouped by concern. Understanding these makes system behaviour predictable — each concept naturally forces the next question, building a mental model of how production systems work.

---

## Foundation — Networking & Communication

| Concept | Core idea |
|---|---|
| **Client–Server** | Client sends request → server processes → response. Every web app is this loop. |
| **IP Address** | Unique address per server. Clients need it to reach a server. |
| **DNS** | Maps human-readable domain → IP address. Like a phone book. |
| **Proxy** | Middleman on the *client* side — hides client IP, used in VPNs. |
| **Reverse Proxy** | Middleman on the *server* side — hides server IP, controls/filters incoming traffic. |
| **Latency** | Round-trip time. Reduced by deploying servers geographically closer to users. |
| **HTTP / HTTPS** | HTTP = transport protocol (plain text). HTTPS adds SSL/TLS encryption. HTTP defines *how* data moves, not what it means. |

---

## APIs & Data Formats

| Concept | Core idea |
|---|---|
| **APIs** | Abstraction layer between client and server. Client asks for data → gets structured response (usually JSON). Doesn't need to know internal logic. |
| **REST API** | Stateless, resource-based HTTP API. Standard verbs: GET/POST/PUT/PATCH/DELETE. Problem: fixed responses can over- or under-fetch data. |
| **GraphQL** | Client specifies exactly what fields it wants. One request instead of multiple REST calls. Server returns exactly that structure. |
| **WebSockets** | Persistent bidirectional connection. Eliminates polling for real-time use cases: chat, dashboards, gaming. |
| **Webhooks** | Server-to-server event notification. Provider calls *your* URL when an event happens. "Don't call me, I'll call you." |

---

## Storage & Data Management

| Concept | Core idea |
|---|---|
| **Databases** | Persistent, reliable storage. Client → Server → DB → Server → Client. |
| **SQL vs NoSQL** | SQL: structured, ACID, joins — good for consistency (banking, orders). NoSQL: flexible, scalable — good for speed/volume (recommendations, logs). Modern systems use both. |
| **Database Indexing** | Pointer structure on a column → skips full table scan. Speeds up reads; slightly slows writes. Index columns used frequently in WHERE clauses. |
| **Replication** | Primary DB handles writes; read replicas share read load. Replicas can be promoted if primary fails. Write bottleneck remains. |
| **Sharding (Horizontal Partitioning)** | Split data by rows across servers using a shard key (user ID, region). Each shard handles a subset. Reduces per-server load. |
| **Vertical Partitioning** | Split a wide table by columns into focused sub-tables. Faster queries because less data scanned per request. |
| **Denormalization** | Combine related data into fewer tables to eliminate JOINs. Trades storage duplication for faster reads. Best for read-heavy systems. |
| **Blob Storage** | Store large unstructured files (images, video, PDFs) in object storage (S3, Azure Blob). Unique URL per file, petabyte scale, cost-per-byte. |

---

## Scaling & Performance

| Concept | Core idea |
|---|---|
| **Vertical Scaling** | Upgrade single machine (more CPU/RAM). Simple but has hardware ceiling and creates a single point of failure. |
| **Horizontal Scaling** | Add more machines. Traffic distributed across them. No SPOF; cost-effective; unlimited ceiling. Requires a load balancer. |
| **Load Balancers** | Sit between clients and servers; distribute traffic. Algorithms: Round Robin (even order), Least Connections (busy-aware), IP Hashing (session affinity). |
| **Caching** | Store hot data in memory (Redis, Memcached) to avoid DB round-trips. Cache-Aside: check cache → miss → query DB → populate cache. TTL prevents stale data. |
| **CDN** | Edge servers worldwide cache static assets. User's request hits nearest server → lower latency. Used by Netflix, YouTube. Works with Blob Storage. |

---

## Distributed Systems

| Concept | Core idea |
|---|---|
| **CAP Theorem** | In distributed systems you can only guarantee 2 of 3: Consistency (latest data), Availability (always responds), Partition Tolerance (survives network split). P is non-negotiable → choose CP or AP. CP: SQL (correct, sometimes unavailable). AP: Cassandra/DynamoDB (available, eventually consistent). |
| **Microservices** | Split monolith into single-responsibility services with their own data stores. Independent scaling, safer deploys, fault isolation. Adds coordination complexity. |
| **Message Queues** | Async inter-service communication via queue (Kafka, RabbitMQ, SQS). Producer → queue → consumer. Decouples services, handles traffic spikes, tolerates consumer downtime. |
| **Rate Limiting** | Cap requests per client per time window. Algorithms: Fixed Window, Sliding Window, Token Bucket. Returns HTTP 429 when exceeded. Typically handled by API Gateway. |
| **API Gateway** | Single entry point to all microservices. Handles auth, rate limiting, routing, logging centrally. Clients don't need to know service topology. |
| **Idempotency** | Multiple identical requests → same result as one. Use unique request IDs + deduplication check before processing. Critical for payments, bookings, retries. |

---

## Quick Mental Model

```
Client → DNS → IP → Proxy/Reverse Proxy
       → Load Balancer → App Servers (horizontal)
       → API Gateway → Microservices
       → Cache (Redis) → Database (SQL/NoSQL)
       → Blob Storage / CDN (static assets)
       → Message Queue (async work)
```

Failures in distributed systems are inevitable → design for: replication (DB), sharding (data size), caching (latency), rate limiting (abuse), idempotency (retries), CAP trade-offs (consistency vs availability).

---

## See Also

- [Architecture — System Design Patterns](/wiki/architecture-system-design-patterns/) — 15 battle-tested implementation patterns (Circuit Breaker, CQRS, Saga, Outbox, Sharding, etc.)
- [Architecture — System Design Learning](/wiki/architecture-system-design-learning/) — How to learn system design, resources, and learning methodology
- [C++ — Lock-Free Ring Buffers](/wiki/c-lock-free-ring-buffers/) — Specific implementation in the low-latency context

