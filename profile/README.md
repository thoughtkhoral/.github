# ThoughtKhoral

ThoughtKhoral is a human-led collaborative workspace where people and
role-specific AI agents deliberate together while humans retain authority over
room context and decisions.

The project is organized as independently versioned repositories. Its current
focus is a technical MVP for governed, real-time rooms and human-controlled
decisions, alongside an experimental provider-free Codex conversation POC.
ThoughtKhoral is in active development and welcomes technical evaluation and
feedback. The [project home](https://github.com/thoughtkhoral/thought-khoral)
and [repository map](https://github.com/thoughtkhoral/thought-khoral/blob/main/docs/repository-map.md)
describe the architecture and cross-project boundaries.

For current project status, interface support, and remaining Codex milestones,
see the [cross-project Codex status guide](https://github.com/thoughtkhoral/thought-khoral/blob/main/docs/codex-conversation-status.md),
the [compatibility matrix](https://github.com/thoughtkhoral/thought-khoral/blob/main/docs/compatibility-matrix.md),
and [capability roadmap](https://github.com/thoughtkhoral/thought-khoral/blob/main/docs/roadmap.md).

## Current state (status reviewed 2026-10-09)

The core MVP demonstrates authenticated rooms, mention-aware message delivery,
a human `/decisions` workflow, and audited decision governance. The former
`Decision:` chat-prefix facilitator is retired; its proposal port is reserved
for a separately approved memory-derived implementation.

The experimental, provider-free Codex conversation POC currently supports:

- Explicit human targeting and authorized room-wide history, including relevant
  discussion that took place while Codex was not responding.
- Shared conversation continuation and explicit fresh-session controls; starting
  a fresh session preserves the room transcript.
- Model and effort controls plus context-usage status in the workspace UI.
- Gateway-mediated room access; the independent worker has no direct room
  database access.
- Provider-free component suites and synthetic composed checks.

Codex acceptance remains open for:

- Packaged-stack acceptance and live tool/egress-isolation checks.
- A separately authorized live multi-human check covering an intervening room
  fact, worker restart and continuation, and a fresh session with the authorized
  room baseline.
- Live settings, denied-model, and context-telemetry checks, plus Linux x86_64
  native tool-policy and Rust 1.85 portability evidence.

The published conversation v1.0.0 artifact is unchanged; the additive v1.1
defaults candidate remains unreleased. These are experimental POC capabilities,
not production-readiness evidence. See the
[cross-project status guide](https://github.com/thoughtkhoral/thought-khoral/blob/main/docs/codex-conversation-status.md)
for exact evidence and gates.

The memory engine remains a separate, incubating room-scoped ingestion proof;
Codex does not use it. A locally controlled deterministic A2A reference agent
is also available. Cognee integration, open remote-agent admission, durable
memory storage, and production deployment remain deferred.

## Start with the MVP

If you are evaluating the system for the first time, follow the repositories in
this order:

1. **Run it:** start with the [local MVP platform](https://github.com/thoughtkhoral/thought-khoral-platform).
2. **Use it:** explore the [workspace UI](https://github.com/thoughtkhoral/thought-khoral-workspace-ui).
3. **Trace it:** inspect the [room gateway](https://github.com/thoughtkhoral/thought-khoral-room-gateway), which owns the authenticated event boundary.
4. **Verify it:** read the [contracts](https://github.com/thoughtkhoral/thought-khoral-contracts), the compatibility authority for the room protocol.

The repository READMEs contain setup and verification details. To evaluate the
separate Codex conversation POC, start with its
[cross-project status and verification guide](https://github.com/thoughtkhoral/thought-khoral/blob/main/docs/codex-conversation-status.md).

## What the MVP demonstrates

- Authenticated, governed rooms.
- Real-time room events with a defined protocol boundary.
- Room-wide and mentioned-only chat delivery with governed audiences.
- Human creation, confirmation, editing, dismissal, and audited deletion of
  decisions through the `/decisions` workflow.

## Active MVP repositories

| Repository | Owns | Evaluation focus |
| --- | --- | --- |
| [Platform](https://github.com/thoughtkhoral/thought-khoral-platform) | Rootless local composition and Kubernetes-manifest validation. | Can the MVP be reproduced and verified locally? |
| [Workspace UI](https://github.com/thoughtkhoral/thought-khoral-workspace-ui) | Browser workspace, chat stream, agent task updates, and decision controls. | Is the human-in-the-loop room experience understandable? |
| [Room Gateway](https://github.com/thoughtkhoral/thought-khoral-room-gateway) | Authenticated WebSocket rooms, event persistence, replay, and authorization. | Are the runtime and security boundaries clear? |
| [Contracts](https://github.com/thoughtkhoral/thought-khoral-contracts) | Versioned room and conversation schemas, protocol documentation, and compatibility fixtures. | Are the protocols durable, inspectable, and sufficient? |

## Incubating work

These repositories have active proofs or experimental integrations, but are not
production services:

- [Memory Engine](https://github.com/thoughtkhoral/thought-khoral-memory-engine) — a room-scoped, provenance-preserving ingestion proof; Codex memory integration, Cognee, and durable storage are deferred.
- [Agent Gateway](https://github.com/thoughtkhoral/thought-khoral-agent-gateway) — a deterministic local A2A reference agent plus opt-in Codex mediation; open remote-agent admission remains deferred.
- [Codex Agent](https://github.com/thoughtkhoral/thought-khoral-codex-agent) — an independent provider-free worker for history-aware room conversations; packaged-stack and live-provider acceptance remain open.

## Feedback is welcome

The most useful feedback is concrete: an unclear project boundary, a missing
verification step, a protocol or security concern, an unexpected MVP behavior,
or a high-value next step. Open an issue in the repository that owns the
behavior and include enough context to reproduce or evaluate it. See the
[contribution guide](https://github.com/thoughtkhoral/.github/blob/main/CONTRIBUTING.md)
for the issue-first, specification-driven workflow. Accepted issues become
approved specification updates before implementation and supporting
documentation.
