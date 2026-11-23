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

<a id="current-state-status-reviewed-2026-11-19"></a>

## Current state (status reviewed 2026-11-20)

The governed-room MVP and experimental Codex integration are implemented and
published on their repositories' `main` branches. Native worker verification is
complete for the tested revisions; full Codex room-stack and live-provider
acceptance remain open. Published v1.1 and verified local released consumers/
profile are distinguished from canonical runtimes in the [workspace guide](https://github.com/thoughtkhoral/thought-khoral/blob/main/docs/workspace-status.md).

| Area | Verified or implemented | Remaining boundary |
| --- | --- | --- |
| Governed-room MVP | Authenticated rooms, ordered events, mention-aware delivery, human `/decisions` and audited deletion. The default deterministic-stack smoke passed at its recorded source inputs. | Local development evidence; no production acceptance. |
| Codex conversation POC | Explicit human targeting, authorized room-wide history, shared continue/fresh-session controls, model/effort settings and context status. Component and composed synthetic checks passed. | Full opt-in room-stack, rendered-browser/Keycloak and live-provider verification remain open. |
| Native Codex worker | Linux AMD64/ARM64 tests passed on Rust 1.85.0 and 1.93.1: 46 tests per cell. Both package-policy captures passed using the pinned Rust 1.93.1 builder. | Worker/package evidence does not establish live account access or full room-stack acceptance. |
| Contracts | Conversation v1.0.0 is unchanged; v1.1.0 is published at verified source `f1c8621`, with verified downloads. Release tooling, released broker/UI consumers and the packaged profile are integrated and pushed to main. | Complete package/environment/operator preflight, then assembled-stack, browser and separately authorized live acceptance. |
| Memory engine | Incubating room-scoped, in-memory ingestion/provenance proof with fixture extraction and an inactive draft adapter. | No active memory proposer, Codex memory integration, Cognee or durable storage. |
| Specifications and docs | Current workspace specs distinguish published artifacts, canonical mains and local prepared branches; derived guides follow those sources. Published link checks cover all seven components. | This local refresh is not a claim of a new published CI run or runtime/browser/provider acceptance. |

Recent evidence: the [latest verified worker run](https://github.com/thoughtkhoral/thought-khoral-codex-agent/actions/runs/44604155672)
passed all four native compiler cells and both package/capture jobs. The
[approved native acceptance record](https://github.com/thoughtkhoral/thought-khoral-codex-agent/blob/main/.ai/specs/how/linux-worker-acceptance.md)
retains exact source, lock, proof and artifact identities. The
[published documentation check](https://github.com/thoughtkhoral/.github/actions/runs/44604555518)
also passed across all seven components.

### Next verification milestone

Complete **Codex Task 9 packaged room-stack and rendered-browser verification**.
Then perform the separately configured and authorized live multi-human checks:
an intervening room fact, worker restart and continuation, explicit fresh session,
settings restoration, denied-model behavior, context telemetry and tool/egress
isolation. See the [coordinated acceptance plan](https://github.com/thoughtkhoral/thought-khoral/blob/main/.ai/specs/how/codex-room-conversations-implementation-plan.md)
for the exact criteria and evidence limits.

Contract v1.1 publication is complete. Prepared source-branch integration,
image publication and production readiness remain separate gates. Open remote-agent admission is deferred. The former `Decision:` prefix
parser is retired; human actions retain authority over active decisions.

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
