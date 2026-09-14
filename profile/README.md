# ThoughtKhoral

ThoughtKhoral is a human-led collaborative workspace where people and
role-specific AI agents deliberate together while humans retain authority over
room context and decisions.

The project is organized as independently versioned repositories. The current
focus is a technical MVP for governed, real-time rooms and human confirmation
of facilitator proposals. This is an active development project and is
looking for technical evaluation and feedback.

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
- Deterministic facilitator proposals.
- Human confirmation, editing, or dismissal of draft decisions.

## Active MVP repositories

| Repository | Owns | Evaluation focus |
| --- | --- | --- |
| [Platform](https://github.com/thoughtkhoral/thought-khoral-platform) | Rootless local composition and Kubernetes-manifest validation. | Can the MVP be reproduced and verified locally? |
| [Workspace UI](https://github.com/thoughtkhoral/thought-khoral-workspace-ui) | Browser workspace, chat stream, memory context, and decision controls. | Is the human-in-the-loop room experience understandable? |
| [Room Gateway](https://github.com/thoughtkhoral/thought-khoral-room-gateway) | Authenticated WebSocket rooms, event persistence, replay, and authorization. | Are the runtime and security boundaries clear? |
| [Contracts](https://github.com/thoughtkhoral/thought-khoral-contracts) | Versioned JSON Schema, room protocol documentation, and compatibility fixtures. | Is the protocol durable, inspectable, and sufficient? |

The [project home](https://github.com/thoughtkhoral/thought-khoral) contains the
architecture, specifications, roadmap, and cross-project release coordination.

## Incubating work

These repositories describe future design surfaces and are not runnable MVP
services yet:

- [Memory Engine](https://github.com/thoughtkhoral/thought-khoral-memory-engine) — collective memory, provenance, and temporal lineage.
- [Agent Gateway](https://github.com/thoughtkhoral/thought-khoral-agent-gateway) — mediated A2A/MCP integration and agent isolation.

## Feedback is welcome

The most useful feedback is concrete: an unclear project boundary, a missing
verification step, a protocol or security concern, an unexpected MVP behavior,
or a high-value next step. Open an issue in the repository that owns the
behavior and include enough context to reproduce or evaluate it. See the
[contribution guide](https://github.com/thoughtkhoral/.github/blob/main/CONTRIBUTING.md)
for the issue-first, specification-driven workflow.
