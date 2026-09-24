# ThoughtKhoral

ThoughtKhoral is a human-led collaborative workspace where people and
role-specific AI agents deliberate together while humans retain authority over
room context and decisions.

The project is organized as independently versioned repositories. The current
focus is a technical MVP for governed, real-time rooms and human-controlled
decisions. This is an active development project and is
looking for technical evaluation and feedback. The [project home](https://github.com/thoughtkhoral/thought-khoral)
and [repository map](https://github.com/thoughtkhoral/thought-khoral/blob/main/docs/repository-map.md)
describe the architecture and cross-project boundaries.

For current interface support and capability status, see the
[compatibility matrix](https://github.com/thoughtkhoral/thought-khoral/blob/main/docs/compatibility-matrix.md)
and [capability roadmap](https://github.com/thoughtkhoral/thought-khoral/blob/main/docs/roadmap.md).

## Current state

The MVP repositories demonstrate authenticated rooms, mention-aware message
delivery, a human `/decisions` workflow, and audited decision governance. The
former `Decision:` chat-prefix facilitator is retired; its proposal port is
reserved for a separately approved memory-derived implementation. Incubating
work adds a room-scoped memory ingestion proof and a locally controlled
deterministic A2A reference agent. Cognee integration, open remote-agent
admission, and production deployment remain deferred.

## Start with the MVP

If you are evaluating the system for the first time, follow the repositories in
this order:

1. **Run it:** start with the [local MVP platform](https://github.com/thoughtkhoral/thought-khoral-platform).
2. **Use it:** explore the [workspace UI](https://github.com/thoughtkhoral/thought-khoral-workspace-ui).
3. **Trace it:** inspect the [room gateway](https://github.com/thoughtkhoral/thought-khoral-room-gateway), which owns the authenticated event boundary.
4. **Verify it:** read the [contracts](https://github.com/thoughtkhoral/thought-khoral-contracts), the compatibility authority for the room protocol.

The repository READMEs contain setup and verification details; this page is an
orientation to the project boundaries and current maturity.

## What the MVP demonstrates

- Authenticated, governed rooms.
- Real-time room events with a defined protocol boundary.
- Room-wide and mentioned-only chat delivery with governed audiences.
- Human creation, confirmation, editing, dismissal, and audited deletion of
  decisions through `/decisions`.

## Active MVP repositories

| Repository | Owns | Evaluation focus |
| --- | --- | --- |
| [Platform](https://github.com/thoughtkhoral/thought-khoral-platform) | Rootless local composition and Kubernetes-manifest validation. | Can the MVP be reproduced and verified locally? |
| [Workspace UI](https://github.com/thoughtkhoral/thought-khoral-workspace-ui) | Browser workspace, chat stream, agent task updates, and decision controls. | Is the human-in-the-loop room experience understandable? |
| [Room Gateway](https://github.com/thoughtkhoral/thought-khoral-room-gateway) | Authenticated WebSocket rooms, event persistence, replay, and authorization. | Are the runtime and security boundaries clear? |
| [Contracts](https://github.com/thoughtkhoral/thought-khoral-contracts) | Versioned JSON Schema, room protocol documentation, and compatibility fixtures. | Is the protocol durable, inspectable, and sufficient? |

## Incubating work

These repositories have local proofs, but are not production services:

- [Memory Engine](https://github.com/thoughtkhoral/thought-khoral-memory-engine) — a room-scoped, provenance-preserving ingestion proof; Cognee integration remains deferred.
- [Agent Gateway](https://github.com/thoughtkhoral/thought-khoral-agent-gateway) — a locally controlled deterministic A2A reference agent with mediated room context and task updates; remote third-party admission remains deferred.

## Feedback is welcome

The most useful feedback is concrete: an unclear project boundary, a missing
verification step, a protocol or security concern, an unexpected MVP behavior,
or a high-value next step. Open an issue in the repository that owns the
behavior and include enough context to reproduce or evaluate it. See the
[contribution guide](https://github.com/thoughtkhoral/.github/blob/main/CONTRIBUTING.md)
for the issue-first, specification-driven workflow. Accepted issues become
approved specification updates before implementation and supporting
documentation.
