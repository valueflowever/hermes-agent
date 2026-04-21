# Hermes Agent Changelog

This file consolidates the historical release notes that were previously split across the standalone `RELEASE_v*.md` documents.

## Included Releases

- [Hermes Agent v0.8.0 (v2026.4.8)](#v0-8-0) — April 8, 2026
- [Hermes Agent v0.7.0 (v2026.4.3)](#v0-7-0) — April 3, 2026
- [Hermes Agent v0.6.0 (v2026.3.30)](#v0-6-0) — March 30, 2026
- [Hermes Agent v0.5.0 (v2026.3.28)](#v0-5-0) — March 28, 2026
- [Hermes Agent v0.4.0 (v2026.3.23)](#v0-4-0) — March 23, 2026
- [Hermes Agent v0.3.0 (v2026.3.17)](#v0-3-0) — March 17, 2026
- [Hermes Agent v0.2.0 (v2026.3.12)](#v0-2-0) — March 12, 2026

---

<a id="v0-8-0"></a>

## Hermes Agent v0.8.0 (v2026.4.8)

**Release Date:** April 8, 2026

> The intelligence release — background task auto-notifications, free MiMo v2 Pro on Nous Portal, live model switching across all platforms, self-optimized GPT/Codex guidance, native Google AI Studio, smart inactivity timeouts, approval buttons, MCP OAuth 2.1, and 209 merged PRs with 82 resolved issues.

---

### ✨ Highlights

- **Background Process Auto-Notifications (`notify_on_complete`)** — Background tasks can now automatically notify the agent when they finish. Start a long-running process (AI model training, test suites, deployments, builds) and the agent gets notified on completion — no polling needed. The agent can keep working on other things and pick up results when they land. ([#5779](https://github.com/NousResearch/hermes-agent/pull/5779))

- **Free Xiaomi MiMo v2 Pro on Nous Portal** — Nous Portal now supports the free-tier Xiaomi MiMo v2 Pro model for auxiliary tasks (compression, vision, summarization), with free-tier model gating and pricing display in model selection. ([#6018](https://github.com/NousResearch/hermes-agent/pull/6018), [#5880](https://github.com/NousResearch/hermes-agent/pull/5880))

- **Live Model Switching (`/model` Command)** — Switch models and providers mid-session from CLI, Telegram, Discord, Slack, or any gateway platform. Aggregator-aware resolution keeps you on OpenRouter/Nous when possible, with automatic cross-provider fallback when needed. Interactive model pickers on Telegram and Discord with inline buttons. ([#5181](https://github.com/NousResearch/hermes-agent/pull/5181), [#5742](https://github.com/NousResearch/hermes-agent/pull/5742))

- **Self-Optimized GPT/Codex Tool-Use Guidance** — The agent diagnosed and patched 5 failure modes in GPT and Codex tool calling through automated behavioral benchmarking, dramatically improving reliability on OpenAI models. Includes execution discipline guidance and thinking-only prefill continuation for structured reasoning. ([#6120](https://github.com/NousResearch/hermes-agent/pull/6120), [#5414](https://github.com/NousResearch/hermes-agent/pull/5414), [#5931](https://github.com/NousResearch/hermes-agent/pull/5931))

- **Google AI Studio (Gemini) Native Provider** — Direct access to Gemini models through Google's AI Studio API. Includes automatic models.dev registry integration for real-time context length detection across any provider. ([#5577](https://github.com/NousResearch/hermes-agent/pull/5577))

- **Inactivity-Based Agent Timeouts** — Gateway and cron timeouts now track actual tool activity instead of wall-clock time. Long-running tasks that are actively working will never be killed — only truly idle agents time out. ([#5389](https://github.com/NousResearch/hermes-agent/pull/5389), [#5440](https://github.com/NousResearch/hermes-agent/pull/5440))

- **Approval Buttons on Slack & Telegram** — Dangerous command approval via native platform buttons instead of typing `/approve`. Slack gets thread context preservation; Telegram gets emoji reactions for approval status. ([#5890](https://github.com/NousResearch/hermes-agent/pull/5890), [#5975](https://github.com/NousResearch/hermes-agent/pull/5975))

- **MCP OAuth 2.1 PKCE + OSV Malware Scanning** — Full standards-compliant OAuth for MCP server authentication, plus automatic malware scanning of MCP extension packages via the OSV vulnerability database. ([#5420](https://github.com/NousResearch/hermes-agent/pull/5420), [#5305](https://github.com/NousResearch/hermes-agent/pull/5305))

- **Centralized Logging & Config Validation** — Structured logging to `~/.hermes/logs/` (agent.log + errors.log) with the `hermes logs` command for tailing and filtering. Config structure validation catches malformed YAML at startup before it causes cryptic failures. ([#5430](https://github.com/NousResearch/hermes-agent/pull/5430), [#5426](https://github.com/NousResearch/hermes-agent/pull/5426))

- **Plugin System Expansion** — Plugins can now register CLI subcommands, receive request-scoped API hooks with correlation IDs, prompt for required env vars during install, and hook into session lifecycle events (finalize/reset). ([#5295](https://github.com/NousResearch/hermes-agent/pull/5295), [#5427](https://github.com/NousResearch/hermes-agent/pull/5427), [#5470](https://github.com/NousResearch/hermes-agent/pull/5470), [#6129](https://github.com/NousResearch/hermes-agent/pull/6129))

- **Matrix Tier 1 & Platform Hardening** — Matrix gets reactions, read receipts, rich formatting, and room management. Discord adds channel controls and ignored channels. Signal gets full MEDIA: tag delivery. Mattermost gets file attachments. Comprehensive reliability fixes across all platforms. ([#5275](https://github.com/NousResearch/hermes-agent/pull/5275), [#5975](https://github.com/NousResearch/hermes-agent/pull/5975), [#5602](https://github.com/NousResearch/hermes-agent/pull/5602))

- **Security Hardening Pass** — Consolidated SSRF protections, timing attack mitigations, tar traversal prevention, credential leakage guards, cron path traversal hardening, and cross-session isolation. Terminal workdir sanitization across all backends. ([#5944](https://github.com/NousResearch/hermes-agent/pull/5944), [#5613](https://github.com/NousResearch/hermes-agent/pull/5613), [#5629](https://github.com/NousResearch/hermes-agent/pull/5629))

---

### 🏗️ Core Agent & Architecture

#### Provider & Model Support
- **Native Google AI Studio (Gemini) provider** with models.dev integration for automatic context length detection ([#5577](https://github.com/NousResearch/hermes-agent/pull/5577))
- **`/model` command — full provider+model system overhaul** — live switching across CLI and all gateway platforms with aggregator-aware resolution ([#5181](https://github.com/NousResearch/hermes-agent/pull/5181))
- **Interactive model picker for Telegram and Discord** — inline button-based model selection ([#5742](https://github.com/NousResearch/hermes-agent/pull/5742))
- **Nous Portal free-tier model gating** with pricing display in model selection ([#5880](https://github.com/NousResearch/hermes-agent/pull/5880))
- **Model pricing display** for OpenRouter and Nous Portal providers ([#5416](https://github.com/NousResearch/hermes-agent/pull/5416))
- **xAI (Grok) prompt caching** via `x-grok-conv-id` header ([#5604](https://github.com/NousResearch/hermes-agent/pull/5604))
- **Grok added to tool-use enforcement models** for direct xAI usage ([#5595](https://github.com/NousResearch/hermes-agent/pull/5595))
- **MiniMax TTS provider** (speech-2.8) ([#4963](https://github.com/NousResearch/hermes-agent/pull/4963))
- **Non-agentic model warning** — warns users when loading Hermes LLM models not designed for tool use ([#5378](https://github.com/NousResearch/hermes-agent/pull/5378))
- **Ollama Cloud auth, /model switch persistence**, and alias tab completion ([#5269](https://github.com/NousResearch/hermes-agent/pull/5269))
- **Preserve dots in OpenCode Go model names** (minimax-m2.7, glm-4.5, kimi-k2.5) ([#5597](https://github.com/NousResearch/hermes-agent/pull/5597))
- **MiniMax models 404 fix** — strip /v1 from Anthropic base URL for OpenCode Go ([#4918](https://github.com/NousResearch/hermes-agent/pull/4918))
- **Provider credential reset windows** honored in pooled failover ([#5188](https://github.com/NousResearch/hermes-agent/pull/5188))
- **OAuth token sync** between credential pool and credentials file ([#4981](https://github.com/NousResearch/hermes-agent/pull/4981))
- **Stale OAuth credentials** no longer block OpenRouter users on auto-detect ([#5746](https://github.com/NousResearch/hermes-agent/pull/5746))
- **Codex OAuth credential pool disconnect** + expired token import fix ([#5681](https://github.com/NousResearch/hermes-agent/pull/5681))
- **Codex pool entry sync** from `~/.codex/auth.json` on exhaustion — @GratefulDave ([#5610](https://github.com/NousResearch/hermes-agent/pull/5610))
- **Auxiliary client payment fallback** — retry with next provider on 402 ([#5599](https://github.com/NousResearch/hermes-agent/pull/5599))
- **Auxiliary client resolves named custom providers** and 'main' alias ([#5978](https://github.com/NousResearch/hermes-agent/pull/5978))
- **Use mimo-v2-pro** for non-vision auxiliary tasks on Nous free tier ([#6018](https://github.com/NousResearch/hermes-agent/pull/6018))
- **Vision auto-detection** tries main provider first ([#6041](https://github.com/NousResearch/hermes-agent/pull/6041))
- **Provider re-ordering and Quick Install** — @austinpickett ([#4664](https://github.com/NousResearch/hermes-agent/pull/4664))
- **Nous OAuth access_token** no longer used as inference API key — @SHL0MS ([#5564](https://github.com/NousResearch/hermes-agent/pull/5564))
- **HERMES_PORTAL_BASE_URL env var** respected during Nous login — @benbarclay ([#5745](https://github.com/NousResearch/hermes-agent/pull/5745))
- **Env var overrides** for Nous portal/inference URLs ([#5419](https://github.com/NousResearch/hermes-agent/pull/5419))
- **Z.AI endpoint auto-detect** via probe and cache ([#5763](https://github.com/NousResearch/hermes-agent/pull/5763))
- **MiniMax context lengths, model catalog, thinking guard, aux model, and config base_url** corrections ([#6082](https://github.com/NousResearch/hermes-agent/pull/6082))
- **Community provider/model resolution fixes** — salvaged 4 community PRs + MiniMax aux URL ([#5983](https://github.com/NousResearch/hermes-agent/pull/5983))

#### Agent Loop & Conversation
- **Self-optimized GPT/Codex tool-use guidance** via automated behavioral benchmarking — agent self-diagnosed and patched 5 failure modes ([#6120](https://github.com/NousResearch/hermes-agent/pull/6120))
- **GPT/Codex execution discipline guidance** in system prompts ([#5414](https://github.com/NousResearch/hermes-agent/pull/5414))
- **Thinking-only prefill continuation** for structured reasoning responses ([#5931](https://github.com/NousResearch/hermes-agent/pull/5931))
- **Accept reasoning-only responses** without retries — set content to "(empty)" instead of infinite retry ([#5278](https://github.com/NousResearch/hermes-agent/pull/5278))
- **Jittered retry backoff** — exponential backoff with jitter for API retries ([#6048](https://github.com/NousResearch/hermes-agent/pull/6048))
- **Smart thinking block signature management** — preserve and manage Anthropic thinking signatures across turns ([#6112](https://github.com/NousResearch/hermes-agent/pull/6112))
- **Coerce tool call arguments** to match JSON Schema types — fixes models that send strings instead of numbers/booleans ([#5265](https://github.com/NousResearch/hermes-agent/pull/5265))
- **Save oversized tool results to file** instead of destructive truncation ([#5210](https://github.com/NousResearch/hermes-agent/pull/5210))
- **Sandbox-aware tool result persistence** ([#6085](https://github.com/NousResearch/hermes-agent/pull/6085))
- **Streaming fallback** improved after edit failures ([#6110](https://github.com/NousResearch/hermes-agent/pull/6110))
- **Codex empty-output gaps** covered in fallback + normalizer + auxiliary client ([#5724](https://github.com/NousResearch/hermes-agent/pull/5724), [#5730](https://github.com/NousResearch/hermes-agent/pull/5730), [#5734](https://github.com/NousResearch/hermes-agent/pull/5734))
- **Codex stream output backfill** from output_item.done events ([#5689](https://github.com/NousResearch/hermes-agent/pull/5689))
- **Stream consumer creates new message** after tool boundaries ([#5739](https://github.com/NousResearch/hermes-agent/pull/5739))
- **Codex validation aligned** with normalization for empty stream output ([#5940](https://github.com/NousResearch/hermes-agent/pull/5940))
- **Bridge tool-calls** in copilot-acp adapter ([#5460](https://github.com/NousResearch/hermes-agent/pull/5460))
- **Filter transcript-only roles** from chat-completions payload ([#4880](https://github.com/NousResearch/hermes-agent/pull/4880))
- **Context compaction failures fixed** on temperature-restricted models — @MadKangYu ([#5608](https://github.com/NousResearch/hermes-agent/pull/5608))
- **Sanitize tool_calls for all strict APIs** (Fireworks, Mistral, etc.) — @lumethegreat ([#5183](https://github.com/NousResearch/hermes-agent/pull/5183))

#### Memory & Sessions
- **Supermemory memory provider** — new memory plugin with multi-container, search_mode, identity template, and env var override ([#5737](https://github.com/NousResearch/hermes-agent/pull/5737), [#5933](https://github.com/NousResearch/hermes-agent/pull/5933))
- **Shared thread sessions** by default — multi-user thread support across gateway platforms ([#5391](https://github.com/NousResearch/hermes-agent/pull/5391))
- **Subagent sessions linked to parent** and hidden from session list ([#5309](https://github.com/NousResearch/hermes-agent/pull/5309))
- **Profile-scoped memory isolation** and clone support ([#4845](https://github.com/NousResearch/hermes-agent/pull/4845))
- **Thread gateway user_id to memory plugins** for per-user scoping ([#5895](https://github.com/NousResearch/hermes-agent/pull/5895))
- **Honcho plugin drift overhaul** + plugin CLI registration system ([#5295](https://github.com/NousResearch/hermes-agent/pull/5295))
- **Honcho holographic prompt and trust score** rendering preserved ([#4872](https://github.com/NousResearch/hermes-agent/pull/4872))
- **Honcho doctor fix** — use recall_mode instead of memory_mode — @techguysimon ([#5645](https://github.com/NousResearch/hermes-agent/pull/5645))
- **RetainDB** — API routes, write queue, dialectic, agent model, file tools fixes ([#5461](https://github.com/NousResearch/hermes-agent/pull/5461))
- **Hindsight memory plugin overhaul** + memory setup wizard fixes ([#5094](https://github.com/NousResearch/hermes-agent/pull/5094))
- **mem0 API v2 compat**, prefetch context fencing, secret redaction ([#5423](https://github.com/NousResearch/hermes-agent/pull/5423))
- **mem0 env vars merged** with mem0.json instead of either/or ([#4939](https://github.com/NousResearch/hermes-agent/pull/4939))
- **Clean user message** used for all memory provider operations ([#4940](https://github.com/NousResearch/hermes-agent/pull/4940))
- **Silent memory flush failure** on /new and /resume fixed — @ryanautomated ([#5640](https://github.com/NousResearch/hermes-agent/pull/5640))
- **OpenViking atexit safety net** for session commit ([#5664](https://github.com/NousResearch/hermes-agent/pull/5664))
- **OpenViking tenant-scoping headers** for multi-tenant servers ([#4936](https://github.com/NousResearch/hermes-agent/pull/4936))
- **ByteRover brv query** runs synchronously before LLM call ([#4831](https://github.com/NousResearch/hermes-agent/pull/4831))

---

### 📱 Messaging Platforms (Gateway)

#### Gateway Core
- **Inactivity-based agent timeout** — replaces wall-clock timeout with smart activity tracking; long-running active tasks never killed ([#5389](https://github.com/NousResearch/hermes-agent/pull/5389))
- **Approval buttons for Slack & Telegram** + Slack thread context preservation ([#5890](https://github.com/NousResearch/hermes-agent/pull/5890))
- **Live-stream /update output** + forward interactive prompts to user ([#5180](https://github.com/NousResearch/hermes-agent/pull/5180))
- **Infinite timeout support** + periodic notifications + actionable error messages ([#4959](https://github.com/NousResearch/hermes-agent/pull/4959))
- **Duplicate message prevention** — gateway dedup + partial stream guard ([#4878](https://github.com/NousResearch/hermes-agent/pull/4878))
- **Webhook delivery_info persistence** + full session id in /status ([#5942](https://github.com/NousResearch/hermes-agent/pull/5942))
- **Tool preview truncation** respects tool_preview_length in all/new progress modes ([#5937](https://github.com/NousResearch/hermes-agent/pull/5937))
- **Short preview truncation** restored for all/new tool progress modes ([#4935](https://github.com/NousResearch/hermes-agent/pull/4935))
- **Update-pending state** written atomically to prevent corruption ([#4923](https://github.com/NousResearch/hermes-agent/pull/4923))
- **Approval session key isolated** per turn ([#4884](https://github.com/NousResearch/hermes-agent/pull/4884))
- **Active-session guard bypass** for /approve, /deny, /stop, /new ([#4926](https://github.com/NousResearch/hermes-agent/pull/4926), [#5765](https://github.com/NousResearch/hermes-agent/pull/5765))
- **Typing indicator paused** during approval waits ([#5893](https://github.com/NousResearch/hermes-agent/pull/5893))
- **Caption check** uses exact line-by-line match instead of substring (all platforms) ([#5939](https://github.com/NousResearch/hermes-agent/pull/5939))
- **MEDIA: tags stripped** from streamed gateway messages ([#5152](https://github.com/NousResearch/hermes-agent/pull/5152))
- **MEDIA: tags extracted** from cron delivery before sending ([#5598](https://github.com/NousResearch/hermes-agent/pull/5598))
- **Profile-aware service units** + voice transcription cleanup ([#5972](https://github.com/NousResearch/hermes-agent/pull/5972))
- **Thread-safe PairingStore** with atomic writes — @CharlieKerfoot ([#5656](https://github.com/NousResearch/hermes-agent/pull/5656))
- **Sanitize media URLs** in base platform logs — @WAXLYY ([#5631](https://github.com/NousResearch/hermes-agent/pull/5631))
- **Reduce Telegram fallback IP activation log noise** — @MadKangYu ([#5615](https://github.com/NousResearch/hermes-agent/pull/5615))
- **Cron static method wrappers** to prevent self-binding ([#5299](https://github.com/NousResearch/hermes-agent/pull/5299))
- **Stale 'hermes login' replaced** with 'hermes auth' + credential removal re-seeding fix ([#5670](https://github.com/NousResearch/hermes-agent/pull/5670))

#### Telegram
- **Group topics skill binding** for supergroup forum topics ([#4886](https://github.com/NousResearch/hermes-agent/pull/4886))
- **Emoji reactions** for approval status and notifications ([#5975](https://github.com/NousResearch/hermes-agent/pull/5975))
- **Duplicate message delivery prevented** on send timeout ([#5153](https://github.com/NousResearch/hermes-agent/pull/5153))
- **Command names sanitized** to strip invalid characters ([#5596](https://github.com/NousResearch/hermes-agent/pull/5596))
- **Per-platform disabled skills** respected in Telegram menu and gateway dispatch ([#4799](https://github.com/NousResearch/hermes-agent/pull/4799))
- **/approve and /deny** routed through running-agent guard ([#4798](https://github.com/NousResearch/hermes-agent/pull/4798))

#### Discord
- **Channel controls** — ignored_channels and no_thread_channels config options ([#5975](https://github.com/NousResearch/hermes-agent/pull/5975))
- **Skills registered as native slash commands** via shared gateway logic ([#5603](https://github.com/NousResearch/hermes-agent/pull/5603))
- **/approve, /deny, /queue, /background, /btw** registered as native slash commands ([#4800](https://github.com/NousResearch/hermes-agent/pull/4800), [#5477](https://github.com/NousResearch/hermes-agent/pull/5477))
- **Unnecessary members intent** removed on startup + token lock leak fix ([#5302](https://github.com/NousResearch/hermes-agent/pull/5302))

#### Slack
- **Thread engagement** — auto-respond in bot-started and mentioned threads ([#5897](https://github.com/NousResearch/hermes-agent/pull/5897))
- **mrkdwn in edit_message** + thread replies without @mentions ([#5733](https://github.com/NousResearch/hermes-agent/pull/5733))

#### Matrix
- **Tier 1 feature parity** — reactions, read receipts, rich formatting, room management ([#5275](https://github.com/NousResearch/hermes-agent/pull/5275))
- **MATRIX_REQUIRE_MENTION and MATRIX_AUTO_THREAD** support ([#5106](https://github.com/NousResearch/hermes-agent/pull/5106))
- **Comprehensive reliability** — encrypted media, auth recovery, cron E2EE, Synapse compat ([#5271](https://github.com/NousResearch/hermes-agent/pull/5271))
- **CJK input, E2EE, and reconnect** fixes ([#5665](https://github.com/NousResearch/hermes-agent/pull/5665))

#### Signal
- **Full MEDIA: tag delivery** — send_image_file, send_voice, and send_video implemented ([#5602](https://github.com/NousResearch/hermes-agent/pull/5602))

#### Mattermost
- **File attachments** — set message type to DOCUMENT when post has file attachments — @nericervin ([#5609](https://github.com/NousResearch/hermes-agent/pull/5609))

#### Feishu
- **Interactive card approval buttons** ([#6043](https://github.com/NousResearch/hermes-agent/pull/6043))
- **Reconnect and ACL** fixes ([#5665](https://github.com/NousResearch/hermes-agent/pull/5665))

#### Webhooks
- **`{__raw__}` template token** and thread_id passthrough for forum topics ([#5662](https://github.com/NousResearch/hermes-agent/pull/5662))

---

### 🖥️ CLI & User Experience

#### Interactive CLI
- **Defer response content** until reasoning block completes ([#5773](https://github.com/NousResearch/hermes-agent/pull/5773))
- **Ghost status-bar lines cleared** on terminal resize ([#4960](https://github.com/NousResearch/hermes-agent/pull/4960))
- **Normalise \r\n and \r line endings** in pasted text ([#4849](https://github.com/NousResearch/hermes-agent/pull/4849))
- **ChatConsole errors, curses scroll, skin-aware banner, git state** banner fixes ([#5974](https://github.com/NousResearch/hermes-agent/pull/5974))
- **Native Windows image paste** support ([#5917](https://github.com/NousResearch/hermes-agent/pull/5917))
- **--yolo and other flags** no longer silently dropped when placed before 'chat' subcommand ([#5145](https://github.com/NousResearch/hermes-agent/pull/5145))

#### Setup & Configuration
- **Config structure validation** — detect malformed YAML at startup with actionable error messages ([#5426](https://github.com/NousResearch/hermes-agent/pull/5426))
- **Centralized logging** to `~/.hermes/logs/` — agent.log (INFO+), errors.log (WARNING+) with `hermes logs` command ([#5430](https://github.com/NousResearch/hermes-agent/pull/5430))
- **Docs links added** to setup wizard sections ([#5283](https://github.com/NousResearch/hermes-agent/pull/5283))
- **Doctor diagnostics** — sync provider checks, config migration, WAL and mem0 diagnostics ([#5077](https://github.com/NousResearch/hermes-agent/pull/5077))
- **Timeout debug logging** and user-facing diagnostics improved ([#5370](https://github.com/NousResearch/hermes-agent/pull/5370))
- **Reasoning effort unified** to config.yaml only ([#6118](https://github.com/NousResearch/hermes-agent/pull/6118))
- **Permanent command allowlist** loaded on startup ([#5076](https://github.com/NousResearch/hermes-agent/pull/5076))
- **`hermes auth remove`** now clears env-seeded credentials permanently ([#5285](https://github.com/NousResearch/hermes-agent/pull/5285))
- **Bundled skills synced to all profiles** during update ([#5795](https://github.com/NousResearch/hermes-agent/pull/5795))
- **`hermes update` no longer kills** freshly-restarted gateway service ([#5448](https://github.com/NousResearch/hermes-agent/pull/5448))
- **Subprocess.run() timeouts** added to all gateway CLI commands ([#5424](https://github.com/NousResearch/hermes-agent/pull/5424))
- **Actionable error message** when Codex refresh token is reused — @tymrtn ([#5612](https://github.com/NousResearch/hermes-agent/pull/5612))
- **Google-workspace skill scripts** can now run directly — @xinbenlv ([#5624](https://github.com/NousResearch/hermes-agent/pull/5624))

#### Cron System
- **Inactivity-based cron timeout** — replaces wall-clock; active tasks run indefinitely ([#5440](https://github.com/NousResearch/hermes-agent/pull/5440))
- **Pre-run script injection** for data collection and change detection ([#5082](https://github.com/NousResearch/hermes-agent/pull/5082))
- **Delivery failure tracking** in job status ([#6042](https://github.com/NousResearch/hermes-agent/pull/6042))
- **Delivery guidance** in cron prompts — stops send_message thrashing ([#5444](https://github.com/NousResearch/hermes-agent/pull/5444))
- **MEDIA files delivered** as native platform attachments ([#5921](https://github.com/NousResearch/hermes-agent/pull/5921))
- **[SILENT] suppression** works anywhere in response — @auspic7 ([#5654](https://github.com/NousResearch/hermes-agent/pull/5654))
- **Cron path traversal** hardening ([#5147](https://github.com/NousResearch/hermes-agent/pull/5147))

---

### 🔧 Tool System

#### Terminal & Execution
- **Execute_code on remote backends** — code execution now works on Docker, SSH, Modal, and other remote terminal backends ([#5088](https://github.com/NousResearch/hermes-agent/pull/5088))
- **Exit code context** for common CLI tools in terminal results — helps agent understand what went wrong ([#5144](https://github.com/NousResearch/hermes-agent/pull/5144))
- **Progressive subdirectory hint discovery** — agent learns project structure as it navigates ([#5291](https://github.com/NousResearch/hermes-agent/pull/5291))
- **notify_on_complete for background processes** — get notified when long-running tasks finish ([#5779](https://github.com/NousResearch/hermes-agent/pull/5779))
- **Docker env config** — explicit container environment variables via docker_env config ([#4738](https://github.com/NousResearch/hermes-agent/pull/4738))
- **Approval metadata included** in terminal tool results ([#5141](https://github.com/NousResearch/hermes-agent/pull/5141))
- **Workdir parameter sanitized** in terminal tool across all backends ([#5629](https://github.com/NousResearch/hermes-agent/pull/5629))
- **Detached process crash recovery** state corrected ([#6101](https://github.com/NousResearch/hermes-agent/pull/6101))
- **Agent-browser paths with spaces** preserved — @Vasanthdev2004 ([#6077](https://github.com/NousResearch/hermes-agent/pull/6077))
- **Portable base64 encoding** for image reading on macOS — @CharlieKerfoot ([#5657](https://github.com/NousResearch/hermes-agent/pull/5657))

#### Browser
- **Switch managed browser provider** from Browserbase to Browser Use — @benbarclay ([#5750](https://github.com/NousResearch/hermes-agent/pull/5750))
- **Firecrawl cloud browser** provider — @alt-glitch ([#5628](https://github.com/NousResearch/hermes-agent/pull/5628))
- **JS evaluation** via browser_console expression parameter ([#5303](https://github.com/NousResearch/hermes-agent/pull/5303))
- **Windows browser** fixes ([#5665](https://github.com/NousResearch/hermes-agent/pull/5665))

#### MCP
- **MCP OAuth 2.1 PKCE** — full standards-compliant OAuth client support ([#5420](https://github.com/NousResearch/hermes-agent/pull/5420))
- **OSV malware check** for MCP extension packages ([#5305](https://github.com/NousResearch/hermes-agent/pull/5305))
- **Prefer structuredContent over text** + no_mcp sentinel ([#5979](https://github.com/NousResearch/hermes-agent/pull/5979))
- **Unknown toolsets warning suppressed** for MCP server names ([#5279](https://github.com/NousResearch/hermes-agent/pull/5279))

#### Web & Files
- **.zip document support** + auto-mount cache dirs into remote backends ([#4846](https://github.com/NousResearch/hermes-agent/pull/4846))
- **Redact query secrets** in send_message errors — @WAXLYY ([#5650](https://github.com/NousResearch/hermes-agent/pull/5650))

#### Delegation
- **Credential pool sharing** + workspace path hints for subagents ([#5748](https://github.com/NousResearch/hermes-agent/pull/5748))

#### ACP (VS Code / Zed / JetBrains)
- **Aggregate ACP improvements** — auth compat, protocol fixes, command ads, delegation, SSE events ([#5292](https://github.com/NousResearch/hermes-agent/pull/5292))

---

### 🧩 Skills Ecosystem

#### Skills System
- **Skill config interface** — skills can declare required config.yaml settings, prompted during setup, injected at load time ([#5635](https://github.com/NousResearch/hermes-agent/pull/5635))
- **Plugin CLI registration system** — plugins register their own CLI subcommands without touching main.py ([#5295](https://github.com/NousResearch/hermes-agent/pull/5295))
- **Request-scoped API hooks** with tool call correlation IDs for plugins ([#5427](https://github.com/NousResearch/hermes-agent/pull/5427))
- **Session lifecycle hooks** — on_session_finalize and on_session_reset for CLI + gateway ([#6129](https://github.com/NousResearch/hermes-agent/pull/6129))
- **Prompt for required env vars** during plugin install — @kshitijk4poor ([#5470](https://github.com/NousResearch/hermes-agent/pull/5470))
- **Plugin name validation** — reject names that resolve to plugins root ([#5368](https://github.com/NousResearch/hermes-agent/pull/5368))
- **pre_llm_call plugin context** moved to user message to preserve prompt cache ([#5146](https://github.com/NousResearch/hermes-agent/pull/5146))

#### New & Updated Skills
- **popular-web-designs** — 54 production website design systems ([#5194](https://github.com/NousResearch/hermes-agent/pull/5194))
- **p5js creative coding** — @SHL0MS ([#5600](https://github.com/NousResearch/hermes-agent/pull/5600))
- **manim-video** — mathematical and technical animations — @SHL0MS ([#4930](https://github.com/NousResearch/hermes-agent/pull/4930))
- **llm-wiki** — Karpathy's LLM Wiki skill ([#5635](https://github.com/NousResearch/hermes-agent/pull/5635))
- **gitnexus-explorer** — codebase indexing and knowledge serving ([#5208](https://github.com/NousResearch/hermes-agent/pull/5208))
- **research-paper-writing** — AI-Scientist & GPT-Researcher patterns — @SHL0MS ([#5421](https://github.com/NousResearch/hermes-agent/pull/5421))
- **blogwatcher** updated to JulienTant's fork ([#5759](https://github.com/NousResearch/hermes-agent/pull/5759))
- **claude-code skill** comprehensive rewrite v2.0 + v2.2 ([#5155](https://github.com/NousResearch/hermes-agent/pull/5155), [#5158](https://github.com/NousResearch/hermes-agent/pull/5158))
- **Code verification skills** consolidated into one ([#4854](https://github.com/NousResearch/hermes-agent/pull/4854))
- **Manim CE reference docs** expanded — geometry, animations, LaTeX — @leotrs ([#5791](https://github.com/NousResearch/hermes-agent/pull/5791))
- **Manim-video references** — design thinking, updaters, paper explainer, decorations, production quality — @SHL0MS ([#5588](https://github.com/NousResearch/hermes-agent/pull/5588), [#5408](https://github.com/NousResearch/hermes-agent/pull/5408))

---

### 🔒 Security & Reliability

#### Security Hardening
- **Consolidated security** — SSRF protections, timing attack mitigations, tar traversal prevention, credential leakage guards ([#5944](https://github.com/NousResearch/hermes-agent/pull/5944))
- **Cross-session isolation** + cron path traversal hardening ([#5613](https://github.com/NousResearch/hermes-agent/pull/5613))
- **Workdir parameter sanitized** in terminal tool across all backends ([#5629](https://github.com/NousResearch/hermes-agent/pull/5629))
- **Approval 'once' session escalation** prevented + cron delivery platform validation ([#5280](https://github.com/NousResearch/hermes-agent/pull/5280))
- **Profile-scoped Google Workspace OAuth tokens** protected ([#4910](https://github.com/NousResearch/hermes-agent/pull/4910))

#### Reliability
- **Aggressive worktree and branch cleanup** to prevent accumulation ([#6134](https://github.com/NousResearch/hermes-agent/pull/6134))
- **O(n²) catastrophic backtracking** in redact regex fixed — 100x improvement on large outputs ([#4962](https://github.com/NousResearch/hermes-agent/pull/4962))
- **Runtime stability fixes** across core, web, delegate, and browser tools ([#4843](https://github.com/NousResearch/hermes-agent/pull/4843))
- **API server streaming fix** + conversation history support ([#5977](https://github.com/NousResearch/hermes-agent/pull/5977))
- **OpenViking API endpoint paths** and response parsing corrected ([#5078](https://github.com/NousResearch/hermes-agent/pull/5078))

---

### 🐛 Notable Bug Fixes

- **9 community bugfixes salvaged** — gateway, cron, deps, macOS launchd in one batch ([#5288](https://github.com/NousResearch/hermes-agent/pull/5288))
- **Batch core bug fixes** — model config, session reset, alias fallback, launchctl, delegation, atomic writes ([#5630](https://github.com/NousResearch/hermes-agent/pull/5630))
- **Batch gateway/platform fixes** — matrix E2EE, CJK input, Windows browser, Feishu reconnect + ACL ([#5665](https://github.com/NousResearch/hermes-agent/pull/5665))
- **Stale test skips removed**, regex backtracking, file search bug, and test flakiness ([#4969](https://github.com/NousResearch/hermes-agent/pull/4969))
- **Nix flake** — read version, regen uv.lock, add hermes_logging — @alt-glitch ([#5651](https://github.com/NousResearch/hermes-agent/pull/5651))
- **Lowercase variable redaction** regression tests ([#5185](https://github.com/NousResearch/hermes-agent/pull/5185))

---

### 🧪 Testing

- **57 failing CI tests repaired** across 14 files ([#5823](https://github.com/NousResearch/hermes-agent/pull/5823))
- **Test suite re-architecture** + CI failure fixes — @alt-glitch ([#5946](https://github.com/NousResearch/hermes-agent/pull/5946))
- **Codebase-wide lint cleanup** — unused imports, dead code, and inefficient patterns ([#5821](https://github.com/NousResearch/hermes-agent/pull/5821))
- **browser_close tool removed** — auto-cleanup handles it ([#5792](https://github.com/NousResearch/hermes-agent/pull/5792))

---

### 📚 Documentation

- **Comprehensive documentation audit** — fix stale info, expand thin pages, add depth ([#5393](https://github.com/NousResearch/hermes-agent/pull/5393))
- **40+ discrepancies fixed** between documentation and codebase ([#5818](https://github.com/NousResearch/hermes-agent/pull/5818))
- **13 features documented** from last week's PRs ([#5815](https://github.com/NousResearch/hermes-agent/pull/5815))
- **Guides section overhaul** — fix existing + add 3 new tutorials ([#5735](https://github.com/NousResearch/hermes-agent/pull/5735))
- **Salvaged 4 docs PRs** — docker setup, post-update validation, local LLM guide, signal-cli install ([#5727](https://github.com/NousResearch/hermes-agent/pull/5727))
- **Discord configuration reference** ([#5386](https://github.com/NousResearch/hermes-agent/pull/5386))
- **Community FAQ entries** for common workflows and troubleshooting ([#4797](https://github.com/NousResearch/hermes-agent/pull/4797))
- **WSL2 networking guide** for local model servers ([#5616](https://github.com/NousResearch/hermes-agent/pull/5616))
- **Honcho CLI reference** + plugin CLI registration docs ([#5308](https://github.com/NousResearch/hermes-agent/pull/5308))
- **Obsidian Headless setup** for servers in llm-wiki ([#5660](https://github.com/NousResearch/hermes-agent/pull/5660))
- **Hermes Mod visual skin editor** added to skins page ([#6095](https://github.com/NousResearch/hermes-agent/pull/6095))

---

### 👥 Contributors

#### Core
- **@teknium1** — 179 PRs

#### Top Community Contributors
- **@SHL0MS** (7 PRs) — p5js creative coding skill, manim-video skill + 5 reference expansions, research-paper-writing, Nous OAuth fix, manim font fix
- **@alt-glitch** (3 PRs) — Firecrawl cloud browser provider, test re-architecture + CI fixes, Nix flake fixes
- **@benbarclay** (2 PRs) — Browser Use managed provider switch, Nous portal base URL fix
- **@CharlieKerfoot** (2 PRs) — macOS portable base64 encoding, thread-safe PairingStore
- **@WAXLYY** (2 PRs) — send_message secret redaction, gateway media URL sanitization
- **@MadKangYu** (2 PRs) — Telegram log noise reduction, context compaction fix for temperature-restricted models

#### All Contributors
@alt-glitch, @austinpickett, @auspic7, @benbarclay, @CharlieKerfoot, @GratefulDave, @kshitijk4poor, @leotrs, @lumethegreat, @MadKangYu, @nericervin, @ryanautomated, @SHL0MS, @techguysimon, @tymrtn, @Vasanthdev2004, @WAXLYY, @xinbenlv

---

**Full Changelog**: [v2026.4.3...v2026.4.8](https://github.com/NousResearch/hermes-agent/compare/v2026.4.3...v2026.4.8)
---

<a id="v0-7-0"></a>

## Hermes Agent v0.7.0 (v2026.4.3)

**Release Date:** April 3, 2026

> The resilience release — pluggable memory providers, credential pool rotation, Camofox anti-detection browser, inline diff previews, gateway hardening across race conditions and approval routing, and deep security fixes across 168 PRs and 46 resolved issues.

---

### ✨ Highlights

- **Pluggable Memory Provider Interface** — Memory is now an extensible plugin system. Third-party memory backends (Honcho, vector stores, custom DBs) implement a simple provider ABC and register via the plugin system. Built-in memory is the default provider. Honcho integration restored to full parity as the reference plugin with profile-scoped host/peer resolution. ([#4623](https://github.com/NousResearch/hermes-agent/pull/4623), [#4616](https://github.com/NousResearch/hermes-agent/pull/4616), [#4355](https://github.com/NousResearch/hermes-agent/pull/4355))

- **Same-Provider Credential Pools** — Configure multiple API keys for the same provider with automatic rotation. Thread-safe `least_used` strategy distributes load across keys, and 401 failures trigger automatic rotation to the next credential. Set up via the setup wizard or `credential_pool` config. ([#4188](https://github.com/NousResearch/hermes-agent/pull/4188), [#4300](https://github.com/NousResearch/hermes-agent/pull/4300), [#4361](https://github.com/NousResearch/hermes-agent/pull/4361))

- **Camofox Anti-Detection Browser Backend** — New local browser backend using Camoufox for stealth browsing. Persistent sessions with VNC URL discovery for visual debugging, configurable SSRF bypass for local backends, auto-install via `hermes tools`. ([#4008](https://github.com/NousResearch/hermes-agent/pull/4008), [#4419](https://github.com/NousResearch/hermes-agent/pull/4419), [#4292](https://github.com/NousResearch/hermes-agent/pull/4292))

- **Inline Diff Previews** — File write and patch operations now show inline diffs in the tool activity feed, giving you visual confirmation of what changed before the agent moves on. ([#4411](https://github.com/NousResearch/hermes-agent/pull/4411), [#4423](https://github.com/NousResearch/hermes-agent/pull/4423))

- **API Server Session Continuity & Tool Streaming** — The API server (Open WebUI integration) now streams tool progress events in real-time and supports `X-Hermes-Session-Id` headers for persistent sessions across requests. Sessions persist to the shared SessionDB. ([#4092](https://github.com/NousResearch/hermes-agent/pull/4092), [#4478](https://github.com/NousResearch/hermes-agent/pull/4478), [#4802](https://github.com/NousResearch/hermes-agent/pull/4802))

- **ACP: Client-Provided MCP Servers** — Editor integrations (VS Code, Zed, JetBrains) can now register their own MCP servers, which Hermes picks up as additional agent tools. Your editor's MCP ecosystem flows directly into the agent. ([#4705](https://github.com/NousResearch/hermes-agent/pull/4705))

- **Gateway Hardening** — Major stability pass across race conditions, photo media delivery, flood control, stuck sessions, approval routing, and compression death spirals. The gateway is substantially more reliable in production. ([#4727](https://github.com/NousResearch/hermes-agent/pull/4727), [#4750](https://github.com/NousResearch/hermes-agent/pull/4750), [#4798](https://github.com/NousResearch/hermes-agent/pull/4798), [#4557](https://github.com/NousResearch/hermes-agent/pull/4557))

- **Security: Secret Exfiltration Blocking** — Browser URLs and LLM responses are now scanned for secret patterns, blocking exfiltration attempts via URL encoding, base64, or prompt injection. Credential directory protections expanded to `.docker`, `.azure`, `.config/gh`. Execute_code sandbox output is redacted. ([#4483](https://github.com/NousResearch/hermes-agent/pull/4483), [#4360](https://github.com/NousResearch/hermes-agent/pull/4360), [#4305](https://github.com/NousResearch/hermes-agent/pull/4305), [#4327](https://github.com/NousResearch/hermes-agent/pull/4327))

---

### 🏗️ Core Agent & Architecture

#### Provider & Model Support
- **Same-provider credential pools** — configure multiple API keys with automatic `least_used` rotation and 401 failover ([#4188](https://github.com/NousResearch/hermes-agent/pull/4188), [#4300](https://github.com/NousResearch/hermes-agent/pull/4300))
- **Credential pool preserved through smart routing** — pool state survives fallback provider switches and defers eager fallback on 429 ([#4361](https://github.com/NousResearch/hermes-agent/pull/4361))
- **Per-turn primary runtime restoration** — after fallback provider use, the agent automatically restores the primary provider on the next turn with transport recovery ([#4624](https://github.com/NousResearch/hermes-agent/pull/4624))
- **`developer` role for GPT-5 and Codex models** — uses OpenAI's recommended system message role for newer models ([#4498](https://github.com/NousResearch/hermes-agent/pull/4498))
- **Google model operational guidance** — Gemini and Gemma models get provider-specific prompting guidance ([#4641](https://github.com/NousResearch/hermes-agent/pull/4641))
- **Anthropic long-context tier 429 handling** — automatically reduces context to 200k when hitting tier limits ([#4747](https://github.com/NousResearch/hermes-agent/pull/4747))
- **URL-based auth for third-party Anthropic endpoints** + CI test fixes ([#4148](https://github.com/NousResearch/hermes-agent/pull/4148))
- **Bearer auth for MiniMax Anthropic endpoints** ([#4028](https://github.com/NousResearch/hermes-agent/pull/4028))
- **Fireworks context length detection** ([#4158](https://github.com/NousResearch/hermes-agent/pull/4158))
- **Standard DashScope international endpoint** for Alibaba provider ([#4133](https://github.com/NousResearch/hermes-agent/pull/4133), closes [#3912](https://github.com/NousResearch/hermes-agent/issues/3912))
- **Custom providers context_length** honored in hygiene compression ([#4085](https://github.com/NousResearch/hermes-agent/pull/4085))
- **Non-sk-ant keys** treated as regular API keys, not OAuth tokens ([#4093](https://github.com/NousResearch/hermes-agent/pull/4093))
- **Claude-sonnet-4.6** added to OpenRouter and Nous model lists ([#4157](https://github.com/NousResearch/hermes-agent/pull/4157))
- **Qwen 3.6 Plus Preview** added to model lists ([#4376](https://github.com/NousResearch/hermes-agent/pull/4376))
- **MiniMax M2.7** added to hermes model picker and OpenCode ([#4208](https://github.com/NousResearch/hermes-agent/pull/4208))
- **Auto-detect models from server probe** in custom endpoint setup ([#4218](https://github.com/NousResearch/hermes-agent/pull/4218))
- **Config.yaml single source of truth** for endpoint URLs — no more env var vs config.yaml conflicts ([#4165](https://github.com/NousResearch/hermes-agent/pull/4165))
- **Setup wizard no longer overwrites** custom endpoint config ([#4180](https://github.com/NousResearch/hermes-agent/pull/4180), closes [#4172](https://github.com/NousResearch/hermes-agent/issues/4172))
- **Unified setup wizard provider selection** with `hermes model` — single code path for both flows ([#4200](https://github.com/NousResearch/hermes-agent/pull/4200))
- **Root-level provider config** no longer overrides `model.provider` ([#4329](https://github.com/NousResearch/hermes-agent/pull/4329))
- **Rate-limit pairing rejection messages** to prevent spam ([#4081](https://github.com/NousResearch/hermes-agent/pull/4081))

#### Agent Loop & Conversation
- **Preserve Anthropic thinking block signatures** across tool-use turns ([#4626](https://github.com/NousResearch/hermes-agent/pull/4626))
- **Classify think-only empty responses** before retrying — prevents infinite retry loops on models that produce thinking blocks without content ([#4645](https://github.com/NousResearch/hermes-agent/pull/4645))
- **Prevent compression death spiral** from API disconnects — stops the loop where compression triggers, fails, compresses again ([#4750](https://github.com/NousResearch/hermes-agent/pull/4750), closes [#2153](https://github.com/NousResearch/hermes-agent/issues/2153))
- **Persist compressed context** to gateway session after mid-run compression ([#4095](https://github.com/NousResearch/hermes-agent/pull/4095))
- **Context-exceeded error messages** now include actionable guidance ([#4155](https://github.com/NousResearch/hermes-agent/pull/4155), closes [#4061](https://github.com/NousResearch/hermes-agent/issues/4061))
- **Strip orphaned think/reasoning tags** from user-facing responses ([#4311](https://github.com/NousResearch/hermes-agent/pull/4311), closes [#4285](https://github.com/NousResearch/hermes-agent/issues/4285))
- **Harden Codex responses preflight** and stream error handling ([#4313](https://github.com/NousResearch/hermes-agent/pull/4313))
- **Deterministic call_id fallbacks** instead of random UUIDs for prompt cache consistency ([#3991](https://github.com/NousResearch/hermes-agent/pull/3991))
- **Context pressure warning spam** prevented after compression ([#4012](https://github.com/NousResearch/hermes-agent/pull/4012))
- **AsyncOpenAI created lazily** in trajectory compressor to avoid closed event loop errors ([#4013](https://github.com/NousResearch/hermes-agent/pull/4013))

#### Memory & Sessions
- **Pluggable memory provider interface** — ABC-based plugin system for custom memory backends with profile isolation ([#4623](https://github.com/NousResearch/hermes-agent/pull/4623))
- **Honcho full integration parity** restored as reference memory provider plugin ([#4355](https://github.com/NousResearch/hermes-agent/pull/4355)) — @erosika
- **Honcho profile-scoped** host and peer resolution ([#4616](https://github.com/NousResearch/hermes-agent/pull/4616))
- **Memory flush state persisted** to prevent redundant re-flushes on gateway restart ([#4481](https://github.com/NousResearch/hermes-agent/pull/4481))
- **Memory provider tools** routed through sequential execution path ([#4803](https://github.com/NousResearch/hermes-agent/pull/4803))
- **Honcho config** written to instance-local path for profile isolation ([#4037](https://github.com/NousResearch/hermes-agent/pull/4037))
- **API server sessions** persist to shared SessionDB ([#4802](https://github.com/NousResearch/hermes-agent/pull/4802))
- **Token usage persisted** for non-CLI sessions ([#4627](https://github.com/NousResearch/hermes-agent/pull/4627))
- **Quote dotted terms in FTS5 queries** — fixes session search for terms containing dots ([#4549](https://github.com/NousResearch/hermes-agent/pull/4549))

---

### 📱 Messaging Platforms (Gateway)

#### Gateway Core
- **Race condition fixes** — photo media loss, flood control, stuck sessions, and STT config issues resolved in one hardening pass ([#4727](https://github.com/NousResearch/hermes-agent/pull/4727))
- **Approval routing through running-agent guard** — `/approve` and `/deny` now route correctly when the agent is blocked waiting for approval instead of being swallowed as interrupts ([#4798](https://github.com/NousResearch/hermes-agent/pull/4798), [#4557](https://github.com/NousResearch/hermes-agent/pull/4557), closes [#4542](https://github.com/NousResearch/hermes-agent/issues/4542))
- **Resume agent after /approve** — tool result is no longer lost when executing blocked commands ([#4418](https://github.com/NousResearch/hermes-agent/pull/4418))
- **DM thread sessions seeded** with parent transcript to preserve context ([#4559](https://github.com/NousResearch/hermes-agent/pull/4559))
- **Skill-aware slash commands** — gateway dynamically registers installed skills as slash commands with paginated `/commands` list and Telegram 100-command cap ([#3934](https://github.com/NousResearch/hermes-agent/pull/3934), [#4005](https://github.com/NousResearch/hermes-agent/pull/4005), [#4006](https://github.com/NousResearch/hermes-agent/pull/4006), [#4010](https://github.com/NousResearch/hermes-agent/pull/4010), [#4023](https://github.com/NousResearch/hermes-agent/pull/4023))
- **Per-platform disabled skills** respected in Telegram menu and gateway dispatch ([#4799](https://github.com/NousResearch/hermes-agent/pull/4799))
- **Remove user-facing compression warnings** — cleaner message flow ([#4139](https://github.com/NousResearch/hermes-agent/pull/4139))
- **`-v/-q` flags wired to stderr logging** for gateway service ([#4474](https://github.com/NousResearch/hermes-agent/pull/4474))
- **HERMES_HOME remapped** to target user in system service unit ([#4456](https://github.com/NousResearch/hermes-agent/pull/4456))
- **Honor default for invalid bool-like config values** ([#4029](https://github.com/NousResearch/hermes-agent/pull/4029))
- **setsid instead of systemd-run** for `/update` command to avoid systemd permission issues ([#4104](https://github.com/NousResearch/hermes-agent/pull/4104), closes [#4017](https://github.com/NousResearch/hermes-agent/issues/4017))
- **'Initializing agent...'** shown on first message for better UX ([#4086](https://github.com/NousResearch/hermes-agent/pull/4086))
- **Allow running gateway service as root** for LXC/container environments ([#4732](https://github.com/NousResearch/hermes-agent/pull/4732))

#### Telegram
- **32-char limit on command names** with collision avoidance ([#4211](https://github.com/NousResearch/hermes-agent/pull/4211))
- **Priority order enforced** in menu — core > plugins > skills ([#4023](https://github.com/NousResearch/hermes-agent/pull/4023))
- **Capped at 50 commands** — API rejects above ~60 ([#4006](https://github.com/NousResearch/hermes-agent/pull/4006))
- **Skip empty/whitespace text** to prevent 400 errors ([#4388](https://github.com/NousResearch/hermes-agent/pull/4388))
- **E2E gateway tests** added ([#4497](https://github.com/NousResearch/hermes-agent/pull/4497)) — @pefontana

#### Discord
- **Button-based approval UI** — register `/approve` and `/deny` slash commands with interactive button prompts ([#4800](https://github.com/NousResearch/hermes-agent/pull/4800))
- **Configurable reactions** — `discord.reactions` config option to disable message processing reactions ([#4199](https://github.com/NousResearch/hermes-agent/pull/4199))
- **Skip reactions and auto-threading** for unauthorized users ([#4387](https://github.com/NousResearch/hermes-agent/pull/4387))

#### Slack
- **Reply in thread** — `slack.reply_in_thread` config option for threaded responses ([#4643](https://github.com/NousResearch/hermes-agent/pull/4643), closes [#2662](https://github.com/NousResearch/hermes-agent/issues/2662))

#### WhatsApp
- **Enforce require_mention in group chats** ([#4730](https://github.com/NousResearch/hermes-agent/pull/4730))

#### Webhook
- **Platform support fixes** — skip home channel prompt, disable tool progress for webhook adapters ([#4660](https://github.com/NousResearch/hermes-agent/pull/4660))

#### Matrix
- **E2EE decryption hardening** — request missing keys, auto-trust devices, retry buffered events ([#4083](https://github.com/NousResearch/hermes-agent/pull/4083))

---

### 🖥️ CLI & User Experience

#### New Slash Commands
- **`/yolo`** — toggle dangerous command approvals on/off for the session ([#3990](https://github.com/NousResearch/hermes-agent/pull/3990))
- **`/btw`** — ephemeral side questions that don't affect the main conversation context ([#4161](https://github.com/NousResearch/hermes-agent/pull/4161))
- **`/profile`** — show active profile info without leaving the chat session ([#4027](https://github.com/NousResearch/hermes-agent/pull/4027))

#### Interactive CLI
- **Inline diff previews** for write and patch operations in the tool activity feed ([#4411](https://github.com/NousResearch/hermes-agent/pull/4411), [#4423](https://github.com/NousResearch/hermes-agent/pull/4423))
- **TUI pinned to bottom** on startup — no more large blank spaces between response and input ([#4412](https://github.com/NousResearch/hermes-agent/pull/4412), [#4359](https://github.com/NousResearch/hermes-agent/pull/4359), closes [#4398](https://github.com/NousResearch/hermes-agent/issues/4398), [#4421](https://github.com/NousResearch/hermes-agent/issues/4421))
- **`/history` and `/resume`** now surface recent sessions directly instead of requiring search ([#4728](https://github.com/NousResearch/hermes-agent/pull/4728))
- **Cache tokens shown** in `/insights` overview so total adds up ([#4428](https://github.com/NousResearch/hermes-agent/pull/4428))
- **`--max-turns` CLI flag** for `hermes chat` to limit agent iterations ([#4314](https://github.com/NousResearch/hermes-agent/pull/4314))
- **Detect dragged file paths** instead of treating them as slash commands ([#4533](https://github.com/NousResearch/hermes-agent/pull/4533)) — @rolme
- **Allow empty strings and falsy values** in `config set` ([#4310](https://github.com/NousResearch/hermes-agent/pull/4310), closes [#4277](https://github.com/NousResearch/hermes-agent/issues/4277))
- **Voice mode in WSL** when PulseAudio bridge is configured ([#4317](https://github.com/NousResearch/hermes-agent/pull/4317))
- **Respect `NO_COLOR` env var** and `TERM=dumb` for accessibility ([#4079](https://github.com/NousResearch/hermes-agent/pull/4079), closes [#4066](https://github.com/NousResearch/hermes-agent/issues/4066)) — @SHL0MS
- **Correct shell reload instruction** for macOS/zsh users ([#4025](https://github.com/NousResearch/hermes-agent/pull/4025))
- **Zero exit code** on successful quiet mode queries ([#4613](https://github.com/NousResearch/hermes-agent/pull/4613), closes [#4601](https://github.com/NousResearch/hermes-agent/issues/4601)) — @devorun
- **on_session_end hook fires** on interrupted exits ([#4159](https://github.com/NousResearch/hermes-agent/pull/4159))
- **Profile list display** reads `model.default` key correctly ([#4160](https://github.com/NousResearch/hermes-agent/pull/4160))
- **Browser and TTS** shown in reconfigure menu ([#4041](https://github.com/NousResearch/hermes-agent/pull/4041))
- **Web backend priority** detection simplified ([#4036](https://github.com/NousResearch/hermes-agent/pull/4036))

#### Setup & Configuration
- **Allowed_users preserved** during setup and quiet unconfigured provider warnings ([#4551](https://github.com/NousResearch/hermes-agent/pull/4551)) — @kshitijk4poor
- **Save API key to model config** for custom endpoints ([#4202](https://github.com/NousResearch/hermes-agent/pull/4202), closes [#4182](https://github.com/NousResearch/hermes-agent/issues/4182))
- **Claude Code credentials gated** behind explicit Hermes config in wizard trigger ([#4210](https://github.com/NousResearch/hermes-agent/pull/4210))
- **Atomic writes in save_config_value** to prevent config loss on interrupt ([#4298](https://github.com/NousResearch/hermes-agent/pull/4298), [#4320](https://github.com/NousResearch/hermes-agent/pull/4320))
- **Scopes field written** to Claude Code credentials on token refresh ([#4126](https://github.com/NousResearch/hermes-agent/pull/4126))

#### Update System
- **Fork detection and upstream sync** in `hermes update` ([#4744](https://github.com/NousResearch/hermes-agent/pull/4744))
- **Preserve working optional extras** when one extra fails during update ([#4550](https://github.com/NousResearch/hermes-agent/pull/4550))
- **Handle conflicted git index** during hermes update ([#4735](https://github.com/NousResearch/hermes-agent/pull/4735))
- **Avoid launchd restart race** on macOS ([#4736](https://github.com/NousResearch/hermes-agent/pull/4736))
- **Missing subprocess.run() timeouts** added to doctor and status commands ([#4009](https://github.com/NousResearch/hermes-agent/pull/4009))

---

### 🔧 Tool System

#### Browser
- **Camofox anti-detection browser backend** — local stealth browsing with auto-install via `hermes tools` ([#4008](https://github.com/NousResearch/hermes-agent/pull/4008))
- **Persistent Camofox sessions** with VNC URL discovery for visual debugging ([#4419](https://github.com/NousResearch/hermes-agent/pull/4419))
- **Skip SSRF check for local backends** (Camofox, headless Chromium) ([#4292](https://github.com/NousResearch/hermes-agent/pull/4292))
- **Configurable SSRF check** via `browser.allow_private_urls` ([#4198](https://github.com/NousResearch/hermes-agent/pull/4198)) — @nils010485
- **CAMOFOX_PORT=9377** added to Docker commands ([#4340](https://github.com/NousResearch/hermes-agent/pull/4340))

#### File Operations
- **Inline diff previews** on write and patch actions ([#4411](https://github.com/NousResearch/hermes-agent/pull/4411), [#4423](https://github.com/NousResearch/hermes-agent/pull/4423))
- **Stale file detection** on write and patch — warns when file was modified externally since last read ([#4345](https://github.com/NousResearch/hermes-agent/pull/4345))
- **Staleness timestamp refreshed** after writes ([#4390](https://github.com/NousResearch/hermes-agent/pull/4390))
- **Size guard, dedup, and device blocking** on read_file ([#4315](https://github.com/NousResearch/hermes-agent/pull/4315))

#### MCP
- **Stability fix pack** — reload timeout, shutdown cleanup, event loop handler, OAuth non-blocking ([#4757](https://github.com/NousResearch/hermes-agent/pull/4757), closes [#4462](https://github.com/NousResearch/hermes-agent/issues/4462), [#2537](https://github.com/NousResearch/hermes-agent/issues/2537))

#### ACP (Editor Integration)
- **Client-provided MCP servers** registered as agent tools — editors pass their MCP servers to Hermes ([#4705](https://github.com/NousResearch/hermes-agent/pull/4705))

#### Skills System
- **Size limits for agent writes** and **fuzzy matching for skill patch** — prevents oversized skill writes and improves edit reliability ([#4414](https://github.com/NousResearch/hermes-agent/pull/4414))
- **Validate hub bundle paths** before install — blocks path traversal in skill bundles ([#3986](https://github.com/NousResearch/hermes-agent/pull/3986))
- **Unified hermes-agent and hermes-agent-setup** into single skill ([#4332](https://github.com/NousResearch/hermes-agent/pull/4332))
- **Skill metadata type check** in extract_skill_conditions ([#4479](https://github.com/NousResearch/hermes-agent/pull/4479))

#### New/Updated Skills
- **research-paper-writing** — full end-to-end research pipeline (replaced ml-paper-writing) ([#4654](https://github.com/NousResearch/hermes-agent/pull/4654)) — @SHL0MS
- **ascii-video** — text readability techniques and external layout oracle ([#4054](https://github.com/NousResearch/hermes-agent/pull/4054)) — @SHL0MS
- **youtube-transcript** updated for youtube-transcript-api v1.x ([#4455](https://github.com/NousResearch/hermes-agent/pull/4455)) — @el-analista
- **Skills browse and search page** added to documentation site ([#4500](https://github.com/NousResearch/hermes-agent/pull/4500)) — @IAvecilla

---

### 🔒 Security & Reliability

#### Security Hardening
- **Block secret exfiltration** via browser URLs and LLM responses — scans for secret patterns in URL encoding, base64, and prompt injection vectors ([#4483](https://github.com/NousResearch/hermes-agent/pull/4483))
- **Redact secrets from execute_code sandbox output** ([#4360](https://github.com/NousResearch/hermes-agent/pull/4360))
- **Protect `.docker`, `.azure`, `.config/gh` credential directories** from read/write via file tools and terminal ([#4305](https://github.com/NousResearch/hermes-agent/pull/4305), [#4327](https://github.com/NousResearch/hermes-agent/pull/4327)) — @memosr
- **GitHub OAuth token patterns** added to redaction + snapshot redact flag ([#4295](https://github.com/NousResearch/hermes-agent/pull/4295))
- **Reject private and loopback IPs** in Telegram DoH fallback ([#4129](https://github.com/NousResearch/hermes-agent/pull/4129))
- **Reject path traversal** in credential file registration ([#4316](https://github.com/NousResearch/hermes-agent/pull/4316))
- **Validate tar archive member paths** on profile import — blocks zip-slip attacks ([#4318](https://github.com/NousResearch/hermes-agent/pull/4318))
- **Exclude auth.json and .env** from profile exports ([#4475](https://github.com/NousResearch/hermes-agent/pull/4475))

#### Reliability
- **Prevent compression death spiral** from API disconnects ([#4750](https://github.com/NousResearch/hermes-agent/pull/4750), closes [#2153](https://github.com/NousResearch/hermes-agent/issues/2153))
- **Handle `is_closed` as method** in OpenAI SDK — prevents false positive client closure detection ([#4416](https://github.com/NousResearch/hermes-agent/pull/4416), closes [#4377](https://github.com/NousResearch/hermes-agent/issues/4377))
- **Exclude matrix from [all] extras** — python-olm is upstream-broken, prevents install failures ([#4615](https://github.com/NousResearch/hermes-agent/pull/4615), closes [#4178](https://github.com/NousResearch/hermes-agent/issues/4178))
- **OpenCode model routing** repaired ([#4508](https://github.com/NousResearch/hermes-agent/pull/4508))
- **Docker container image** optimized ([#4034](https://github.com/NousResearch/hermes-agent/pull/4034)) — @bcross

#### Windows & Cross-Platform
- **Voice mode in WSL** with PulseAudio bridge ([#4317](https://github.com/NousResearch/hermes-agent/pull/4317))
- **Homebrew packaging** preparation ([#4099](https://github.com/NousResearch/hermes-agent/pull/4099))
- **CI fork conditionals** to prevent workflow failures on forks ([#4107](https://github.com/NousResearch/hermes-agent/pull/4107))

---

### 🐛 Notable Bug Fixes

- **Gateway approval blocked agent thread** — approval now blocks the agent thread like CLI does, preventing tool result loss ([#4557](https://github.com/NousResearch/hermes-agent/pull/4557), closes [#4542](https://github.com/NousResearch/hermes-agent/issues/4542))
- **Compression death spiral** from API disconnects — detected and halted instead of looping ([#4750](https://github.com/NousResearch/hermes-agent/pull/4750), closes [#2153](https://github.com/NousResearch/hermes-agent/issues/2153))
- **Anthropic thinking blocks lost** across tool-use turns ([#4626](https://github.com/NousResearch/hermes-agent/pull/4626))
- **Profile model config ignored** with `-p` flag — model.model now promoted to model.default correctly ([#4160](https://github.com/NousResearch/hermes-agent/pull/4160), closes [#4486](https://github.com/NousResearch/hermes-agent/issues/4486))
- **CLI blank space** between response and input area ([#4412](https://github.com/NousResearch/hermes-agent/pull/4412), [#4359](https://github.com/NousResearch/hermes-agent/pull/4359), closes [#4398](https://github.com/NousResearch/hermes-agent/issues/4398))
- **Dragged file paths** treated as slash commands instead of file references ([#4533](https://github.com/NousResearch/hermes-agent/pull/4533)) — @rolme
- **Orphaned `</think>` tags** leaking into user-facing responses ([#4311](https://github.com/NousResearch/hermes-agent/pull/4311), closes [#4285](https://github.com/NousResearch/hermes-agent/issues/4285))
- **OpenAI SDK `is_closed`** is a method not property — false positive client closure ([#4416](https://github.com/NousResearch/hermes-agent/pull/4416), closes [#4377](https://github.com/NousResearch/hermes-agent/issues/4377))
- **MCP OAuth server** could block Hermes startup instead of degrading gracefully ([#4757](https://github.com/NousResearch/hermes-agent/pull/4757), closes [#4462](https://github.com/NousResearch/hermes-agent/issues/4462))
- **MCP event loop closed** on shutdown with HTTP servers ([#4757](https://github.com/NousResearch/hermes-agent/pull/4757), closes [#2537](https://github.com/NousResearch/hermes-agent/issues/2537))
- **Alibaba provider** hardcoded to wrong endpoint ([#4133](https://github.com/NousResearch/hermes-agent/pull/4133), closes [#3912](https://github.com/NousResearch/hermes-agent/issues/3912))
- **Slack reply_in_thread** missing config option ([#4643](https://github.com/NousResearch/hermes-agent/pull/4643), closes [#2662](https://github.com/NousResearch/hermes-agent/issues/2662))
- **Quiet mode exit code** — successful `-q` queries no longer exit nonzero ([#4613](https://github.com/NousResearch/hermes-agent/pull/4613), closes [#4601](https://github.com/NousResearch/hermes-agent/issues/4601))
- **Mobile sidebar** shows only close button due to backdrop-filter issue in docs site ([#4207](https://github.com/NousResearch/hermes-agent/pull/4207)) — @xsmyile
- **Config restore reverted** by stale-branch squash merge — `_config_version` fixed ([#4440](https://github.com/NousResearch/hermes-agent/pull/4440))

---

### 🧪 Testing

- **Telegram gateway E2E tests** — full integration test suite for the Telegram adapter ([#4497](https://github.com/NousResearch/hermes-agent/pull/4497)) — @pefontana
- **11 real test failures fixed** plus sys.modules cascade poisoner resolved ([#4570](https://github.com/NousResearch/hermes-agent/pull/4570))
- **7 CI failures resolved** across hooks, plugins, and skill tests ([#3936](https://github.com/NousResearch/hermes-agent/pull/3936))
- **Codex 401 refresh tests** updated for CI compatibility ([#4166](https://github.com/NousResearch/hermes-agent/pull/4166))
- **Stale OPENAI_BASE_URL test** fixed ([#4217](https://github.com/NousResearch/hermes-agent/pull/4217))

---

### 📚 Documentation

- **Comprehensive documentation audit** — 9 HIGH and 20+ MEDIUM gaps fixed across 21 files ([#4087](https://github.com/NousResearch/hermes-agent/pull/4087))
- **Site navigation restructured** — features and platforms promoted to top-level ([#4116](https://github.com/NousResearch/hermes-agent/pull/4116))
- **Tool progress streaming** documented for API server and Open WebUI ([#4138](https://github.com/NousResearch/hermes-agent/pull/4138))
- **Telegram webhook mode** documentation ([#4089](https://github.com/NousResearch/hermes-agent/pull/4089))
- **Local LLM provider guides** — comprehensive setup guides with context length warnings ([#4294](https://github.com/NousResearch/hermes-agent/pull/4294))
- **WhatsApp allowlist behavior** clarified with `WHATSAPP_ALLOW_ALL_USERS` documentation ([#4293](https://github.com/NousResearch/hermes-agent/pull/4293))
- **Slack configuration options** — new config section in Slack docs ([#4644](https://github.com/NousResearch/hermes-agent/pull/4644))
- **Terminal backends section** expanded + docs build fixes ([#4016](https://github.com/NousResearch/hermes-agent/pull/4016))
- **Adding-providers guide** updated for unified setup flow ([#4201](https://github.com/NousResearch/hermes-agent/pull/4201))
- **ACP Zed config** fixed ([#4743](https://github.com/NousResearch/hermes-agent/pull/4743))
- **Community FAQ** entries for common workflows and troubleshooting ([#4797](https://github.com/NousResearch/hermes-agent/pull/4797))
- **Skills browse and search page** on docs site ([#4500](https://github.com/NousResearch/hermes-agent/pull/4500)) — @IAvecilla

---

### 👥 Contributors

#### Core
- **@teknium1** — 135 commits across all subsystems

#### Top Community Contributors
- **@kshitijk4poor** — 13 commits: preserve allowed_users during setup ([#4551](https://github.com/NousResearch/hermes-agent/pull/4551)), and various fixes
- **@erosika** — 12 commits: Honcho full integration parity restored as memory provider plugin ([#4355](https://github.com/NousResearch/hermes-agent/pull/4355))
- **@pefontana** — 9 commits: Telegram gateway E2E test suite ([#4497](https://github.com/NousResearch/hermes-agent/pull/4497))
- **@bcross** — 5 commits: Docker container image optimization ([#4034](https://github.com/NousResearch/hermes-agent/pull/4034))
- **@SHL0MS** — 4 commits: NO_COLOR/TERM=dumb support ([#4079](https://github.com/NousResearch/hermes-agent/pull/4079)), ascii-video skill updates ([#4054](https://github.com/NousResearch/hermes-agent/pull/4054)), research-paper-writing skill ([#4654](https://github.com/NousResearch/hermes-agent/pull/4654))

#### All Contributors
@0xbyt4, @arasovic, @Bartok9, @bcross, @binhnt92, @camden-lowrance, @curtitoo, @Dakota, @Dave Tist, @Dean Kerr, @devorun, @dieutx, @Dilee, @el-analista, @erosika, @Gutslabs, @IAvecilla, @Jack, @Johannnnn506, @kshitijk4poor, @Laura Batalha, @Leegenux, @Lume, @MacroAnarchy, @maymuneth, @memosr, @NexVeridian, @Nick, @nils010485, @pefontana, @Penov, @rolme, @SHL0MS, @txchen, @xsmyile

#### Issues Resolved from Community
@acsezen ([#2537](https://github.com/NousResearch/hermes-agent/issues/2537)), @arasovic ([#4285](https://github.com/NousResearch/hermes-agent/issues/4285)), @camden-lowrance ([#4462](https://github.com/NousResearch/hermes-agent/issues/4462)), @devorun ([#4601](https://github.com/NousResearch/hermes-agent/issues/4601)), @eloklam ([#4486](https://github.com/NousResearch/hermes-agent/issues/4486)), @HenkDz ([#3719](https://github.com/NousResearch/hermes-agent/issues/3719)), @hypotyposis ([#2153](https://github.com/NousResearch/hermes-agent/issues/2153)), @kazamak ([#4178](https://github.com/NousResearch/hermes-agent/issues/4178)), @lstep ([#4366](https://github.com/NousResearch/hermes-agent/issues/4366)), @Mark-Lok ([#4542](https://github.com/NousResearch/hermes-agent/issues/4542)), @NoJster ([#4421](https://github.com/NousResearch/hermes-agent/issues/4421)), @patp ([#2662](https://github.com/NousResearch/hermes-agent/issues/2662)), @pr0n ([#4601](https://github.com/NousResearch/hermes-agent/issues/4601)), @saulmc ([#4377](https://github.com/NousResearch/hermes-agent/issues/4377)), @SHL0MS ([#4060](https://github.com/NousResearch/hermes-agent/issues/4060), [#4061](https://github.com/NousResearch/hermes-agent/issues/4061), [#4066](https://github.com/NousResearch/hermes-agent/issues/4066), [#4172](https://github.com/NousResearch/hermes-agent/issues/4172), [#4277](https://github.com/NousResearch/hermes-agent/issues/4277)), @Z-Mackintosh ([#4398](https://github.com/NousResearch/hermes-agent/issues/4398))

---

**Full Changelog**: [v2026.3.30...v2026.4.3](https://github.com/NousResearch/hermes-agent/compare/v2026.3.30...v2026.4.3)
---

<a id="v0-6-0"></a>

## Hermes Agent v0.6.0 (v2026.3.30)

**Release Date:** March 30, 2026

> The multi-instance release — Profiles for running isolated agent instances, MCP server mode, Docker container, fallback provider chains, two new messaging platforms (Feishu/Lark and WeCom), Telegram webhook mode, Slack multi-workspace OAuth, 95 PRs and 16 resolved issues in 2 days.

---

### ✨ Highlights

- **Profiles — Multi-Instance Hermes** — Run multiple isolated Hermes instances from the same installation. Each profile gets its own config, memory, sessions, skills, and gateway service. Create with `hermes profile create`, switch with `hermes -p <name>`, export/import for sharing. Full token-lock isolation prevents two profiles from using the same bot credential. ([#3681](https://github.com/NousResearch/hermes-agent/pull/3681))

- **MCP Server Mode** — Expose Hermes conversations and sessions to any MCP-compatible client (Claude Desktop, Cursor, VS Code, etc.) via `hermes mcp serve`. Browse conversations, read messages, search across sessions, and manage attachments — all through the Model Context Protocol. Supports both stdio and Streamable HTTP transports. ([#3795](https://github.com/NousResearch/hermes-agent/pull/3795))

- **Docker Container** — Official Dockerfile for running Hermes Agent in a container. Supports both CLI and gateway modes with volume-mounted config. ([#3668](https://github.com/NousResearch/hermes-agent/pull/3668), closes [#850](https://github.com/NousResearch/hermes-agent/issues/850))

- **Ordered Fallback Provider Chain** — Configure multiple inference providers with automatic failover. When your primary provider returns errors or is unreachable, Hermes automatically tries the next provider in the chain. Configure via `fallback_providers` in config.yaml. ([#3813](https://github.com/NousResearch/hermes-agent/pull/3813), closes [#1734](https://github.com/NousResearch/hermes-agent/issues/1734))

- **Feishu/Lark Platform Support** — Full gateway adapter for Feishu (飞书) and Lark with event subscriptions, message cards, group chat, image/file attachments, and interactive card callbacks. ([#3799](https://github.com/NousResearch/hermes-agent/pull/3799), [#3817](https://github.com/NousResearch/hermes-agent/pull/3817), closes [#1788](https://github.com/NousResearch/hermes-agent/issues/1788))

- **WeCom (Enterprise WeChat) Platform Support** — New gateway adapter for WeCom (企业微信) with text/image/voice messages, group chats, and callback verification. ([#3847](https://github.com/NousResearch/hermes-agent/pull/3847))

- **Slack Multi-Workspace OAuth** — Connect a single Hermes gateway to multiple Slack workspaces via OAuth token file. Each workspace gets its own bot token, resolved dynamically per incoming event. ([#3903](https://github.com/NousResearch/hermes-agent/pull/3903))

- **Telegram Webhook Mode & Group Controls** — Run the Telegram adapter in webhook mode as an alternative to polling — faster response times and better for production deployments behind a reverse proxy. New group mention gating controls when the bot responds: always, only when @mentioned, or via regex triggers. ([#3880](https://github.com/NousResearch/hermes-agent/pull/3880), [#3870](https://github.com/NousResearch/hermes-agent/pull/3870))

- **Exa Search Backend** — Add Exa as an alternative web search and content extraction backend alongside Firecrawl and DuckDuckGo. Set `EXA_API_KEY` and configure as preferred backend. ([#3648](https://github.com/NousResearch/hermes-agent/pull/3648))

- **Skills & Credentials on Remote Backends** — Mount skill directories and credential files into Modal and Docker containers, so remote terminal sessions have access to the same skills and secrets as local execution. ([#3890](https://github.com/NousResearch/hermes-agent/pull/3890), [#3671](https://github.com/NousResearch/hermes-agent/pull/3671), closes [#3665](https://github.com/NousResearch/hermes-agent/issues/3665), [#3433](https://github.com/NousResearch/hermes-agent/issues/3433))

---

### 🏗️ Core Agent & Architecture

#### Provider & Model Support
- **Ordered fallback provider chain** — automatic failover across multiple configured providers ([#3813](https://github.com/NousResearch/hermes-agent/pull/3813))
- **Fix api_mode on provider switch** — switching providers via `hermes model` now correctly clears stale `api_mode` instead of hardcoding `chat_completions`, fixing 404s for providers with Anthropic-compatible endpoints ([#3726](https://github.com/NousResearch/hermes-agent/pull/3726), [#3857](https://github.com/NousResearch/hermes-agent/pull/3857), closes [#3685](https://github.com/NousResearch/hermes-agent/issues/3685))
- **Stop silent OpenRouter fallback** — when no provider is configured, Hermes now raises a clear error instead of silently routing to OpenRouter ([#3807](https://github.com/NousResearch/hermes-agent/pull/3807), [#3862](https://github.com/NousResearch/hermes-agent/pull/3862))
- **Gemini 3.1 preview models** — added to OpenRouter and Nous Portal catalogs ([#3803](https://github.com/NousResearch/hermes-agent/pull/3803), closes [#3753](https://github.com/NousResearch/hermes-agent/issues/3753))
- **Gemini direct API context length** — full context length resolution for direct Google AI endpoints ([#3876](https://github.com/NousResearch/hermes-agent/pull/3876))
- **gpt-5.4-mini** added to Codex fallback catalog ([#3855](https://github.com/NousResearch/hermes-agent/pull/3855))
- **Curated model lists preferred** over live API probe when the probe returns fewer models ([#3856](https://github.com/NousResearch/hermes-agent/pull/3856), [#3867](https://github.com/NousResearch/hermes-agent/pull/3867))
- **User-friendly 429 rate limit messages** with Retry-After countdown ([#3809](https://github.com/NousResearch/hermes-agent/pull/3809))
- **Auxiliary client placeholder key** for local servers without auth requirements ([#3842](https://github.com/NousResearch/hermes-agent/pull/3842))
- **INFO-level logging** for auxiliary provider resolution ([#3866](https://github.com/NousResearch/hermes-agent/pull/3866))

#### Agent Loop & Conversation
- **Subagent status reporting** — reports `completed` status when summary exists instead of generic failure ([#3829](https://github.com/NousResearch/hermes-agent/pull/3829))
- **Session log file updated during compression** — prevents stale file references after context compression ([#3835](https://github.com/NousResearch/hermes-agent/pull/3835))
- **Omit empty tools param** — sends no `tools` parameter when empty instead of `None`, fixing compatibility with strict providers ([#3820](https://github.com/NousResearch/hermes-agent/pull/3820))

#### Profiles & Multi-Instance
- **Profiles system** — `hermes profile create/list/switch/delete/export/import/rename`. Each profile gets isolated HERMES_HOME, gateway service, CLI wrapper. Token locks prevent credential collisions. Tab completion for profile names. ([#3681](https://github.com/NousResearch/hermes-agent/pull/3681))
- **Profile-aware display paths** — all user-facing `~/.hermes` paths replaced with `display_hermes_home()` to show the correct profile directory ([#3623](https://github.com/NousResearch/hermes-agent/pull/3623))
- **Lazy display_hermes_home imports** — prevents `ImportError` during `hermes update` when modules cache stale bytecode ([#3776](https://github.com/NousResearch/hermes-agent/pull/3776))
- **HERMES_HOME for protected paths** — `.env` write-deny path now respects HERMES_HOME instead of hardcoded `~/.hermes` ([#3840](https://github.com/NousResearch/hermes-agent/pull/3840))

---

### 📱 Messaging Platforms (Gateway)

#### New Platforms
- **Feishu/Lark** — Full adapter with event subscriptions, message cards, group chat, image/file attachments, interactive card callbacks ([#3799](https://github.com/NousResearch/hermes-agent/pull/3799), [#3817](https://github.com/NousResearch/hermes-agent/pull/3817))
- **WeCom (Enterprise WeChat)** — Text/image/voice messages, group chats, callback verification ([#3847](https://github.com/NousResearch/hermes-agent/pull/3847))

#### Telegram
- **Webhook mode** — run as webhook endpoint instead of polling for production deployments ([#3880](https://github.com/NousResearch/hermes-agent/pull/3880))
- **Group mention gating & regex triggers** — configurable bot response behavior in groups: always, @mention-only, or regex-matched ([#3870](https://github.com/NousResearch/hermes-agent/pull/3870))
- **Gracefully handle deleted reply targets** — no more crashes when the message being replied to was deleted ([#3858](https://github.com/NousResearch/hermes-agent/pull/3858), closes [#3229](https://github.com/NousResearch/hermes-agent/issues/3229))

#### Discord
- **Message processing reactions** — adds a reaction emoji while processing and removes it when done, giving visual feedback in channels ([#3871](https://github.com/NousResearch/hermes-agent/pull/3871))
- **DISCORD_IGNORE_NO_MENTION** — skip messages that @mention other users/bots but not Hermes ([#3640](https://github.com/NousResearch/hermes-agent/pull/3640))
- **Clean up deferred "thinking..."** — properly removes the "thinking..." indicator after slash commands complete ([#3674](https://github.com/NousResearch/hermes-agent/pull/3674), closes [#3595](https://github.com/NousResearch/hermes-agent/issues/3595))

#### Slack
- **Multi-workspace OAuth** — connect to multiple Slack workspaces from a single gateway via OAuth token file ([#3903](https://github.com/NousResearch/hermes-agent/pull/3903))

#### WhatsApp
- **Persistent aiohttp session** — reuse HTTP sessions across requests instead of creating new ones per message ([#3818](https://github.com/NousResearch/hermes-agent/pull/3818))
- **LID↔phone alias resolution** — correctly match Linked ID and phone number formats in allowlists ([#3830](https://github.com/NousResearch/hermes-agent/pull/3830))
- **Skip reply prefix in bot mode** — cleaner message formatting when running as a WhatsApp bot ([#3931](https://github.com/NousResearch/hermes-agent/pull/3931))

#### Matrix
- **Native voice messages via MSC3245** — send voice messages as proper Matrix voice events instead of file attachments ([#3877](https://github.com/NousResearch/hermes-agent/pull/3877))

#### Mattermost
- **Configurable mention behavior** — respond to messages without requiring @mention ([#3664](https://github.com/NousResearch/hermes-agent/pull/3664))

#### Signal
- **URL-encode phone numbers** and correct attachment RPC parameter — fixes delivery failures with certain phone number formats ([#3670](https://github.com/NousResearch/hermes-agent/pull/3670)) — @kshitijk4poor

#### Email
- **Close SMTP/IMAP connections on failure** — prevents connection leaks during error scenarios ([#3804](https://github.com/NousResearch/hermes-agent/pull/3804))

#### Gateway Core
- **Atomic config writes** — use atomic file writes for config.yaml to prevent data loss during crashes ([#3800](https://github.com/NousResearch/hermes-agent/pull/3800))
- **Home channel env overrides** — apply environment variable overrides for home channels consistently ([#3796](https://github.com/NousResearch/hermes-agent/pull/3796), [#3808](https://github.com/NousResearch/hermes-agent/pull/3808))
- **Replace print() with logger** — BasePlatformAdapter now uses proper logging instead of print statements ([#3669](https://github.com/NousResearch/hermes-agent/pull/3669))
- **Cron delivery labels** — resolve human-friendly delivery labels via channel directory ([#3860](https://github.com/NousResearch/hermes-agent/pull/3860), closes [#1945](https://github.com/NousResearch/hermes-agent/issues/1945))
- **Cron [SILENT] tightening** — prevent agents from prefixing reports with [SILENT] to suppress delivery ([#3901](https://github.com/NousResearch/hermes-agent/pull/3901))
- **Background task media delivery** and vision download timeout fixes ([#3919](https://github.com/NousResearch/hermes-agent/pull/3919))
- **Boot-md hook** — example built-in hook to run a BOOT.md file on gateway startup ([#3733](https://github.com/NousResearch/hermes-agent/pull/3733))

---

### 🖥️ CLI & User Experience

#### Interactive CLI
- **Configurable tool preview length** — show full file paths by default instead of truncating at 40 chars ([#3841](https://github.com/NousResearch/hermes-agent/pull/3841))
- **Tool token context display** — `hermes tools` checklist now shows estimated token cost per toolset ([#3805](https://github.com/NousResearch/hermes-agent/pull/3805))
- **/bg spinner TUI fix** — route background task spinner through the TUI widget to prevent status bar collision ([#3643](https://github.com/NousResearch/hermes-agent/pull/3643))
- **Prevent status bar wrapping** into duplicate rows ([#3883](https://github.com/NousResearch/hermes-agent/pull/3883)) — @kshitijk4poor
- **Handle closed stdout ValueError** in safe print paths — fixes crashes when stdout is closed during gateway thread shutdown ([#3843](https://github.com/NousResearch/hermes-agent/pull/3843), closes [#3534](https://github.com/NousResearch/hermes-agent/issues/3534))
- **Remove input() from /tools disable** — eliminates freeze in terminal when disabling tools ([#3918](https://github.com/NousResearch/hermes-agent/pull/3918))
- **TTY guard for interactive CLI commands** — prevent CPU spin when launched without a terminal ([#3933](https://github.com/NousResearch/hermes-agent/pull/3933))
- **Argparse entrypoint** — use argparse in the top-level launcher for cleaner error handling ([#3874](https://github.com/NousResearch/hermes-agent/pull/3874))
- **Lazy-initialized tools show yellow** in banner instead of red, reducing false alarm about "missing" tools ([#3822](https://github.com/NousResearch/hermes-agent/pull/3822))
- **Honcho tools shown in banner** when configured ([#3810](https://github.com/NousResearch/hermes-agent/pull/3810))

#### Setup & Configuration
- **Auto-install matrix-nio** during `hermes setup` when Matrix is selected ([#3802](https://github.com/NousResearch/hermes-agent/pull/3802), [#3873](https://github.com/NousResearch/hermes-agent/pull/3873))
- **Session export stdout support** — export sessions to stdout with `-` for piping ([#3641](https://github.com/NousResearch/hermes-agent/pull/3641), closes [#3609](https://github.com/NousResearch/hermes-agent/issues/3609))
- **Configurable approval timeouts** — set how long dangerous command approval prompts wait before auto-denying ([#3886](https://github.com/NousResearch/hermes-agent/pull/3886), closes [#3765](https://github.com/NousResearch/hermes-agent/issues/3765))
- **Clear __pycache__ during update** — prevents stale bytecode ImportError after `hermes update` ([#3819](https://github.com/NousResearch/hermes-agent/pull/3819))

---

### 🔧 Tool System

#### MCP
- **MCP Server Mode** — `hermes mcp serve` exposes conversations, sessions, and attachments to MCP clients via stdio or Streamable HTTP ([#3795](https://github.com/NousResearch/hermes-agent/pull/3795))
- **Dynamic tool discovery** — respond to `notifications/tools/list_changed` events to pick up new tools from MCP servers without reconnecting ([#3812](https://github.com/NousResearch/hermes-agent/pull/3812))
- **Non-deprecated HTTP transport** — switched from `sse_client` to `streamable_http_client` ([#3646](https://github.com/NousResearch/hermes-agent/pull/3646))

#### Web Tools
- **Exa search backend** — alternative to Firecrawl and DuckDuckGo for web search and extraction ([#3648](https://github.com/NousResearch/hermes-agent/pull/3648))

#### Browser
- **Guard against None LLM responses** in browser snapshot and vision tools ([#3642](https://github.com/NousResearch/hermes-agent/pull/3642))

#### Terminal & Remote Backends
- **Mount skill directories** into Modal and Docker containers ([#3890](https://github.com/NousResearch/hermes-agent/pull/3890))
- **Mount credential files** into remote backends with mtime+size caching ([#3671](https://github.com/NousResearch/hermes-agent/pull/3671))
- **Preserve partial output** when commands time out instead of losing everything ([#3868](https://github.com/NousResearch/hermes-agent/pull/3868))
- **Stop marking persisted env vars as missing** on remote backends ([#3650](https://github.com/NousResearch/hermes-agent/pull/3650))

#### Audio
- **.aac format support** in transcription tool ([#3865](https://github.com/NousResearch/hermes-agent/pull/3865), closes [#1963](https://github.com/NousResearch/hermes-agent/issues/1963))
- **Audio download retry** — retry logic for `cache_audio_from_url` matching the existing image download pattern ([#3401](https://github.com/NousResearch/hermes-agent/pull/3401)) — @binhnt92

#### Vision
- **Reject non-image files** and enforce website-only policy for vision analysis ([#3845](https://github.com/NousResearch/hermes-agent/pull/3845))

#### Tool Schema
- **Ensure name field** always present in tool definitions, fixing `KeyError: 'name'` crashes ([#3811](https://github.com/NousResearch/hermes-agent/pull/3811), closes [#3729](https://github.com/NousResearch/hermes-agent/issues/3729))

#### ACP (Editor Integration)
- **Complete session management surface** for VS Code/Zed/JetBrains clients — proper task lifecycle, cancel support, session persistence ([#3675](https://github.com/NousResearch/hermes-agent/pull/3675))

---

### 🧩 Skills & Plugins

#### Skills System
- **External skill directories** — configure additional skill directories via `skills.external_dirs` in config.yaml ([#3678](https://github.com/NousResearch/hermes-agent/pull/3678))
- **Category path traversal blocked** — prevents `../` attacks in skill category names ([#3844](https://github.com/NousResearch/hermes-agent/pull/3844))
- **parallel-cli moved to optional-skills** — reduces default skill footprint ([#3673](https://github.com/NousResearch/hermes-agent/pull/3673)) — @kshitijk4poor

#### New Skills
- **memento-flashcards** — spaced repetition flashcard system ([#3827](https://github.com/NousResearch/hermes-agent/pull/3827))
- **songwriting-and-ai-music** — songwriting craft and AI music generation prompts ([#3834](https://github.com/NousResearch/hermes-agent/pull/3834))
- **SiYuan Note** — integration with SiYuan note-taking app ([#3742](https://github.com/NousResearch/hermes-agent/pull/3742))
- **Scrapling** — web scraping skill using Scrapling library ([#3742](https://github.com/NousResearch/hermes-agent/pull/3742))
- **one-three-one-rule** — communication framework skill ([#3797](https://github.com/NousResearch/hermes-agent/pull/3797))

#### Plugin System
- **Plugin enable/disable commands** — `hermes plugins enable/disable <name>` for managing plugin state without removing them ([#3747](https://github.com/NousResearch/hermes-agent/pull/3747))
- **Plugin message injection** — plugins can now inject messages into the conversation stream on behalf of the user via `ctx.inject_message()` ([#3778](https://github.com/NousResearch/hermes-agent/pull/3778)) — @winglian
- **Honcho self-hosted support** — allow local Honcho instances without requiring an API key ([#3644](https://github.com/NousResearch/hermes-agent/pull/3644))

---

### 🔒 Security & Reliability

#### Security Hardening
- **Hardened dangerous command detection** — expanded pattern matching for risky shell commands and added file tool path guards for sensitive locations (`/etc/`, `/boot/`, docker.sock) ([#3872](https://github.com/NousResearch/hermes-agent/pull/3872))
- **Sensitive path write checks** in approval system — catch writes to system config files through file tools, not just terminal ([#3859](https://github.com/NousResearch/hermes-agent/pull/3859))
- **Secret redaction expansion** — now covers ElevenLabs, Tavily, and Exa API keys ([#3920](https://github.com/NousResearch/hermes-agent/pull/3920))
- **Vision file rejection** — reject non-image files passed to vision analysis to prevent information disclosure ([#3845](https://github.com/NousResearch/hermes-agent/pull/3845))
- **Category path traversal blocking** — prevent directory traversal in skill category names ([#3844](https://github.com/NousResearch/hermes-agent/pull/3844))

#### Reliability
- **Atomic config.yaml writes** — prevent data loss during gateway crashes ([#3800](https://github.com/NousResearch/hermes-agent/pull/3800))
- **Clear __pycache__ on update** — prevent stale bytecode from causing ImportError after updates ([#3819](https://github.com/NousResearch/hermes-agent/pull/3819))
- **Lazy imports for update safety** — prevent ImportError chains during `hermes update` when modules reference new functions ([#3776](https://github.com/NousResearch/hermes-agent/pull/3776))
- **Restore terminalbench2 from patch corruption** — recovered file damaged by patch tool's secret redaction ([#3801](https://github.com/NousResearch/hermes-agent/pull/3801))
- **Terminal timeout preserves partial output** — no more lost command output on timeout ([#3868](https://github.com/NousResearch/hermes-agent/pull/3868))

---

### 🐛 Notable Bug Fixes

- **OpenClaw migration model config overwrite** — migration no longer overwrites model config dict with a string ([#3924](https://github.com/NousResearch/hermes-agent/pull/3924)) — @0xbyt4
- **OpenClaw migration expanded** — covers full data footprint including sessions, cron, memory ([#3869](https://github.com/NousResearch/hermes-agent/pull/3869))
- **Telegram deleted reply targets** — gracefully handle replies to deleted messages instead of crashing ([#3858](https://github.com/NousResearch/hermes-agent/pull/3858))
- **Discord "thinking..." persistence** — properly cleans up deferred response indicators ([#3674](https://github.com/NousResearch/hermes-agent/pull/3674))
- **WhatsApp LID↔phone aliases** — fixes allowlist matching failures with Linked ID format ([#3830](https://github.com/NousResearch/hermes-agent/pull/3830))
- **Signal URL-encoded phone numbers** — fixes delivery failures with certain formats ([#3670](https://github.com/NousResearch/hermes-agent/pull/3670))
- **Email connection leaks** — properly close SMTP/IMAP connections on error ([#3804](https://github.com/NousResearch/hermes-agent/pull/3804))
- **_safe_print ValueError** — no more gateway thread crashes on closed stdout ([#3843](https://github.com/NousResearch/hermes-agent/pull/3843))
- **Tool schema KeyError 'name'** — ensure name field always present in tool definitions ([#3811](https://github.com/NousResearch/hermes-agent/pull/3811))
- **api_mode stale on provider switch** — correctly clear when switching providers via `hermes model` ([#3857](https://github.com/NousResearch/hermes-agent/pull/3857))

---

### 🧪 Testing

- Resolved 10+ CI failures across hooks, tiktoken, plugins, and skill tests ([#3848](https://github.com/NousResearch/hermes-agent/pull/3848), [#3721](https://github.com/NousResearch/hermes-agent/pull/3721), [#3936](https://github.com/NousResearch/hermes-agent/pull/3936))

---

### 📚 Documentation

- **Comprehensive OpenClaw migration guide** — step-by-step guide for migrating from OpenClaw/Claw3D to Hermes Agent ([#3864](https://github.com/NousResearch/hermes-agent/pull/3864), [#3900](https://github.com/NousResearch/hermes-agent/pull/3900))
- **Credential file passthrough docs** — document how to forward credential files and env vars to remote backends ([#3677](https://github.com/NousResearch/hermes-agent/pull/3677))
- **DuckDuckGo requirements clarified** — note runtime dependency on duckduckgo-search package ([#3680](https://github.com/NousResearch/hermes-agent/pull/3680))
- **Skills catalog updated** — added red-teaming category and optional skills listing ([#3745](https://github.com/NousResearch/hermes-agent/pull/3745))
- **Feishu docs MDX fix** — escape angle-bracket URLs that break Docusaurus build ([#3902](https://github.com/NousResearch/hermes-agent/pull/3902))

---

### 👥 Contributors

#### Core
- **@teknium1** — 90 PRs across all subsystems

#### Community Contributors
- **@kshitijk4poor** — 3 PRs: Signal phone number fix ([#3670](https://github.com/NousResearch/hermes-agent/pull/3670)), parallel-cli to optional-skills ([#3673](https://github.com/NousResearch/hermes-agent/pull/3673)), status bar wrapping fix ([#3883](https://github.com/NousResearch/hermes-agent/pull/3883))
- **@winglian** — 1 PR: Plugin message injection interface ([#3778](https://github.com/NousResearch/hermes-agent/pull/3778))
- **@binhnt92** — 1 PR: Audio download retry logic ([#3401](https://github.com/NousResearch/hermes-agent/pull/3401))
- **@0xbyt4** — 1 PR: OpenClaw migration model config fix ([#3924](https://github.com/NousResearch/hermes-agent/pull/3924))

#### Issues Resolved from Community
@Material-Scientist ([#850](https://github.com/NousResearch/hermes-agent/issues/850)), @hanxu98121 ([#1734](https://github.com/NousResearch/hermes-agent/issues/1734)), @penwyp ([#1788](https://github.com/NousResearch/hermes-agent/issues/1788)), @dan-and ([#1945](https://github.com/NousResearch/hermes-agent/issues/1945)), @AdrianScott ([#1963](https://github.com/NousResearch/hermes-agent/issues/1963)), @clawdbot47 ([#3229](https://github.com/NousResearch/hermes-agent/issues/3229)), @alanfwilliams ([#3404](https://github.com/NousResearch/hermes-agent/issues/3404)), @kentimsit ([#3433](https://github.com/NousResearch/hermes-agent/issues/3433)), @hayka-pacha ([#3534](https://github.com/NousResearch/hermes-agent/issues/3534)), @primmer ([#3595](https://github.com/NousResearch/hermes-agent/issues/3595)), @dagelf ([#3609](https://github.com/NousResearch/hermes-agent/issues/3609)), @HenkDz ([#3685](https://github.com/NousResearch/hermes-agent/issues/3685)), @tmdgusya ([#3729](https://github.com/NousResearch/hermes-agent/issues/3729)), @TypQxQ ([#3753](https://github.com/NousResearch/hermes-agent/issues/3753)), @acsezen ([#3765](https://github.com/NousResearch/hermes-agent/issues/3765))

---

**Full Changelog**: [v2026.3.28...v2026.3.30](https://github.com/NousResearch/hermes-agent/compare/v2026.3.28...v2026.3.30)
---

<a id="v0-5-0"></a>

## Hermes Agent v0.5.0 (v2026.3.28)

**Release Date:** March 28, 2026

> The hardening release — Hugging Face provider, /model command overhaul, Telegram Private Chat Topics, native Modal SDK, plugin lifecycle hooks, tool-use enforcement for GPT models, Nix flake, 50+ security and reliability fixes, and a comprehensive supply chain audit.

---

### ✨ Highlights

- **Nous Portal now supports 400+ models** — The Nous Research inference portal has expanded dramatically, giving Hermes Agent users access to over 400 models through a single provider endpoint

- **Hugging Face as a first-class inference provider** — Full integration with HF Inference API including curated agentic model picker that maps to OpenRouter analogues, live `/models` endpoint probe, and setup wizard flow ([#3419](https://github.com/NousResearch/hermes-agent/pull/3419), [#3440](https://github.com/NousResearch/hermes-agent/pull/3440))

- **Telegram Private Chat Topics** — Project-based conversations with functional skill binding per topic, enabling isolated workflows within a single Telegram chat ([#3163](https://github.com/NousResearch/hermes-agent/pull/3163))

- **Native Modal SDK backend** — Replaced swe-rex dependency with native Modal SDK (`Sandbox.create.aio` + `exec.aio`), eliminating tunnels and simplifying the Modal terminal backend ([#3538](https://github.com/NousResearch/hermes-agent/pull/3538))

- **Plugin lifecycle hooks activated** — `pre_llm_call`, `post_llm_call`, `on_session_start`, and `on_session_end` hooks now fire in the agent loop and CLI/gateway, completing the plugin hook system ([#3542](https://github.com/NousResearch/hermes-agent/pull/3542))

- **Improved OpenAI Model Reliability** — Added `GPT_TOOL_USE_GUIDANCE` to prevent GPT models from describing intended actions instead of making tool calls, plus automatic stripping of stale budget warnings from conversation history that caused models to avoid tools across turns ([#3528](https://github.com/NousResearch/hermes-agent/pull/3528))

- **Nix flake** — Full uv2nix build, NixOS module with persistent container mode, auto-generated config keys from Python source, and suffix PATHs for agent-friendliness ([#20](https://github.com/NousResearch/hermes-agent/pull/20), [#3274](https://github.com/NousResearch/hermes-agent/pull/3274), [#3061](https://github.com/NousResearch/hermes-agent/pull/3061)) by @alt-glitch

- **Supply chain hardening** — Removed compromised `litellm` dependency, pinned all dependency version ranges, regenerated `uv.lock` with hashes, added CI workflow scanning PRs for supply chain attack patterns, and bumped deps to fix CVEs ([#2796](https://github.com/NousResearch/hermes-agent/pull/2796), [#2810](https://github.com/NousResearch/hermes-agent/pull/2810), [#2812](https://github.com/NousResearch/hermes-agent/pull/2812), [#2816](https://github.com/NousResearch/hermes-agent/pull/2816), [#3073](https://github.com/NousResearch/hermes-agent/pull/3073))

- **Anthropic output limits fix** — Replaced hardcoded 16K `max_tokens` with per-model native output limits (128K for Opus 4.6, 64K for Sonnet 4.6), fixing "Response truncated" and thinking-budget exhaustion on direct Anthropic API ([#3426](https://github.com/NousResearch/hermes-agent/pull/3426), [#3444](https://github.com/NousResearch/hermes-agent/pull/3444))

---

### 🏗️ Core Agent & Architecture

#### New Provider: Hugging Face
- First-class Hugging Face Inference API integration with auth, setup wizard, and model picker ([#3419](https://github.com/NousResearch/hermes-agent/pull/3419))
- Curated model list mapping OpenRouter agentic defaults to HF equivalents — providers with 8+ curated models skip live `/models` probe for speed ([#3440](https://github.com/NousResearch/hermes-agent/pull/3440))
- Added glm-5-turbo to Z.AI provider model list ([#3095](https://github.com/NousResearch/hermes-agent/pull/3095))

#### Provider & Model Improvements
- `/model` command overhaul — extracted shared `switch_model()` pipeline for CLI and gateway, custom endpoint support, provider-aware routing ([#2795](https://github.com/NousResearch/hermes-agent/pull/2795), [#2799](https://github.com/NousResearch/hermes-agent/pull/2799))
- Removed `/model` slash command from CLI and gateway in favor of `hermes model` subcommand ([#3080](https://github.com/NousResearch/hermes-agent/pull/3080))
- Preserve `custom` provider instead of silently remapping to `openrouter` ([#2792](https://github.com/NousResearch/hermes-agent/pull/2792))
- Read root-level `provider` and `base_url` from config.yaml into model config ([#3112](https://github.com/NousResearch/hermes-agent/pull/3112))
- Align Nous Portal model slugs with OpenRouter naming ([#3253](https://github.com/NousResearch/hermes-agent/pull/3253))
- Fix Alibaba provider default endpoint and model list ([#3484](https://github.com/NousResearch/hermes-agent/pull/3484))
- Allow MiniMax users to override `/v1` → `/anthropic` auto-correction ([#3553](https://github.com/NousResearch/hermes-agent/pull/3553))
- Migrate OAuth token refresh to `platform.claude.com` with fallback ([#3246](https://github.com/NousResearch/hermes-agent/pull/3246))

#### Agent Loop & Conversation
- **Improved OpenAI model reliability** — `GPT_TOOL_USE_GUIDANCE` prevents GPT models from describing actions instead of calling tools + automatic budget warning stripping from history ([#3528](https://github.com/NousResearch/hermes-agent/pull/3528))
- **Surface lifecycle events** — All retry, fallback, and compression events now surface to the user as formatted messages ([#3153](https://github.com/NousResearch/hermes-agent/pull/3153))
- **Anthropic output limits** — Per-model native output limits instead of hardcoded 16K `max_tokens` ([#3426](https://github.com/NousResearch/hermes-agent/pull/3426))
- **Thinking-budget exhaustion detection** — Skip useless continuation retries when model uses all output tokens on reasoning ([#3444](https://github.com/NousResearch/hermes-agent/pull/3444))
- Always prefer streaming for API calls to prevent hung subagents ([#3120](https://github.com/NousResearch/hermes-agent/pull/3120))
- Restore safe non-streaming fallback after stream failures ([#3020](https://github.com/NousResearch/hermes-agent/pull/3020))
- Give subagents independent iteration budgets ([#3004](https://github.com/NousResearch/hermes-agent/pull/3004))
- Update `api_key` in `_try_activate_fallback` for subagent auth ([#3103](https://github.com/NousResearch/hermes-agent/pull/3103))
- Graceful return on max retries instead of crashing thread ([untagged commit](https://github.com/NousResearch/hermes-agent))
- Count compression restarts toward retry limit ([#3070](https://github.com/NousResearch/hermes-agent/pull/3070))
- Include tool tokens in preflight estimate, guard context probe persistence ([#3164](https://github.com/NousResearch/hermes-agent/pull/3164))
- Update context compressor limits after fallback activation ([#3305](https://github.com/NousResearch/hermes-agent/pull/3305))
- Validate empty user messages to prevent Anthropic API 400 errors ([#3322](https://github.com/NousResearch/hermes-agent/pull/3322))
- GLM reasoning-only and max-length handling ([#3010](https://github.com/NousResearch/hermes-agent/pull/3010))
- Increase API timeout default from 900s to 1800s for slow-thinking models ([#3431](https://github.com/NousResearch/hermes-agent/pull/3431))
- Send `max_tokens` for Claude/OpenRouter + retry SSE connection errors ([#3497](https://github.com/NousResearch/hermes-agent/pull/3497))
- Prevent AsyncOpenAI/httpx cross-loop deadlock in gateway mode ([#2701](https://github.com/NousResearch/hermes-agent/pull/2701)) by @ctlst

#### Streaming & Reasoning
- **Persist reasoning across gateway session turns** with new schema v6 columns (`reasoning`, `reasoning_details`, `codex_reasoning_items`) ([#2974](https://github.com/NousResearch/hermes-agent/pull/2974))
- Detect and kill stale SSE connections ([untagged commit](https://github.com/NousResearch/hermes-agent))
- Fix stale stream detector race causing spurious `RemoteProtocolError` ([untagged commit](https://github.com/NousResearch/hermes-agent))
- Skip duplicate callback for `<think>`-extracted reasoning during streaming ([#3116](https://github.com/NousResearch/hermes-agent/pull/3116))
- Preserve reasoning fields in `rewrite_transcript` ([#3311](https://github.com/NousResearch/hermes-agent/pull/3311))
- Preserve Gemini thought signatures in streamed tool calls ([#2997](https://github.com/NousResearch/hermes-agent/pull/2997))
- Ensure first delta is fired during reasoning updates ([untagged commit](https://github.com/NousResearch/hermes-agent))

#### Session & Memory
- **Session search recent sessions mode** — Omit query to browse recent sessions with titles, previews, and timestamps ([#2533](https://github.com/NousResearch/hermes-agent/pull/2533))
- **Session config surfacing** on `/new`, `/reset`, and auto-reset ([#3321](https://github.com/NousResearch/hermes-agent/pull/3321))
- **Third-party session isolation** — `--source` flag for isolating sessions by origin ([#3255](https://github.com/NousResearch/hermes-agent/pull/3255))
- Add `/resume` CLI handler, session log truncation guard, `reopen_session` API ([#3315](https://github.com/NousResearch/hermes-agent/pull/3315))
- Clear compressor summary and turn counter on `/clear` and `/new` ([#3102](https://github.com/NousResearch/hermes-agent/pull/3102))
- Surface silent SessionDB failures that cause session data loss ([#2999](https://github.com/NousResearch/hermes-agent/pull/2999))
- Session search fallback preview on summarization failure ([#3478](https://github.com/NousResearch/hermes-agent/pull/3478))
- Prevent stale memory overwrites by flush agent ([#2687](https://github.com/NousResearch/hermes-agent/pull/2687))

#### Context Compression
- Replace dead `summary_target_tokens` with ratio-based scaling ([#2554](https://github.com/NousResearch/hermes-agent/pull/2554))
- Expose `compression.target_ratio`, `protect_last_n`, and `threshold` in `DEFAULT_CONFIG` ([untagged commit](https://github.com/NousResearch/hermes-agent))
- Restore sane defaults and cap summary at 12K tokens ([untagged commit](https://github.com/NousResearch/hermes-agent))
- Preserve transcript on `/compress` and hygiene compression ([#3556](https://github.com/NousResearch/hermes-agent/pull/3556))
- Update context pressure warnings and token estimates after compaction ([untagged commit](https://github.com/NousResearch/hermes-agent))

#### Architecture & Dependencies
- **Remove mini-swe-agent dependency** — Inline Docker and Modal backends directly ([#2804](https://github.com/NousResearch/hermes-agent/pull/2804))
- **Replace swe-rex with native Modal SDK** for Modal backend ([#3538](https://github.com/NousResearch/hermes-agent/pull/3538))
- **Plugin lifecycle hooks** — `pre_llm_call`, `post_llm_call`, `on_session_start`, `on_session_end` now fire in the agent loop ([#3542](https://github.com/NousResearch/hermes-agent/pull/3542))
- Fix plugin toolsets invisible in `hermes tools` and standalone processes ([#3457](https://github.com/NousResearch/hermes-agent/pull/3457))
- Consolidate `get_hermes_home()` and `parse_reasoning_effort()` ([#3062](https://github.com/NousResearch/hermes-agent/pull/3062))
- Remove unused Hermes-native PKCE OAuth flow ([#3107](https://github.com/NousResearch/hermes-agent/pull/3107))
- Remove ~100 unused imports across 55 files ([#3016](https://github.com/NousResearch/hermes-agent/pull/3016))
- Fix 154 f-strings, simplify getattr/URL patterns, remove dead code ([#3119](https://github.com/NousResearch/hermes-agent/pull/3119))

---

### 📱 Messaging Platforms (Gateway)

#### Telegram
- **Private Chat Topics** — Project-based conversations with functional skill binding per topic, enabling isolated workflows within a single Telegram chat ([#3163](https://github.com/NousResearch/hermes-agent/pull/3163))
- **Auto-discover fallback IPs via DNS-over-HTTPS** when `api.telegram.org` is unreachable ([#3376](https://github.com/NousResearch/hermes-agent/pull/3376))
- **Configurable reply threading mode** ([#2907](https://github.com/NousResearch/hermes-agent/pull/2907))
- Fall back to no `thread_id` on "Message thread not found" BadRequest ([#3390](https://github.com/NousResearch/hermes-agent/pull/3390))
- Self-reschedule reconnect when `start_polling` fails after 502 ([#3268](https://github.com/NousResearch/hermes-agent/pull/3268))

#### Discord
- Stop phantom typing indicator after agent turn completes ([#3003](https://github.com/NousResearch/hermes-agent/pull/3003))

#### Slack
- Send tool call progress messages to correct Slack thread ([#3063](https://github.com/NousResearch/hermes-agent/pull/3063))
- Scope progress thread fallback to Slack only ([#3488](https://github.com/NousResearch/hermes-agent/pull/3488))

#### WhatsApp
- Download documents, audio, and video media from messages ([#2978](https://github.com/NousResearch/hermes-agent/pull/2978))

#### Matrix
- Add missing Matrix entry in `PLATFORMS` dict ([#3473](https://github.com/NousResearch/hermes-agent/pull/3473))
- Harden e2ee access-token handling ([#3562](https://github.com/NousResearch/hermes-agent/pull/3562))
- Add backoff for `SyncError` in sync loop ([#3280](https://github.com/NousResearch/hermes-agent/pull/3280))

#### Signal
- Track SSE keepalive comments as connection activity ([#3316](https://github.com/NousResearch/hermes-agent/pull/3316))

#### Email
- Prevent unbounded growth of `_seen_uids` in EmailAdapter ([#3490](https://github.com/NousResearch/hermes-agent/pull/3490))

#### Gateway Core
- **Config-gated `/verbose` command** for messaging platforms — toggle tool output verbosity from chat ([#3262](https://github.com/NousResearch/hermes-agent/pull/3262))
- **Background review notifications** delivered to user chat ([#3293](https://github.com/NousResearch/hermes-agent/pull/3293))
- **Retry transient send failures** and notify user on exhaustion ([#3288](https://github.com/NousResearch/hermes-agent/pull/3288))
- Recover from hung agents — `/stop` hard-kills session lock ([#3104](https://github.com/NousResearch/hermes-agent/pull/3104))
- Thread-safe `SessionStore` — protect `_entries` with `threading.Lock` ([#3052](https://github.com/NousResearch/hermes-agent/pull/3052))
- Fix gateway token double-counting with cached agents — use absolute set instead of increment ([#3306](https://github.com/NousResearch/hermes-agent/pull/3306), [#3317](https://github.com/NousResearch/hermes-agent/pull/3317))
- Fingerprint full auth token in agent cache signature ([#3247](https://github.com/NousResearch/hermes-agent/pull/3247))
- Silence background agent terminal output ([#3297](https://github.com/NousResearch/hermes-agent/pull/3297))
- Include per-platform `ALLOW_ALL` and `SIGNAL_GROUP` in startup allowlist check ([#3313](https://github.com/NousResearch/hermes-agent/pull/3313))
- Include user-local bin paths in systemd unit PATH ([#3527](https://github.com/NousResearch/hermes-agent/pull/3527))
- Track background task references in `GatewayRunner` ([#3254](https://github.com/NousResearch/hermes-agent/pull/3254))
- Add request timeouts to HA, Email, Mattermost, SMS adapters ([#3258](https://github.com/NousResearch/hermes-agent/pull/3258))
- Add media download retry to Mattermost, Slack, and base cache ([#3323](https://github.com/NousResearch/hermes-agent/pull/3323))
- Detect virtualenv path instead of hardcoding `venv/` ([#2797](https://github.com/NousResearch/hermes-agent/pull/2797))
- Use `TERMINAL_CWD` for context file discovery, not process cwd ([untagged commit](https://github.com/NousResearch/hermes-agent))
- Stop loading hermes repo AGENTS.md into gateway sessions (~10k wasted tokens) ([#2891](https://github.com/NousResearch/hermes-agent/pull/2891))

---

### 🖥️ CLI & User Experience

#### Interactive CLI
- **Configurable busy input mode** + fix `/queue` always working ([#3298](https://github.com/NousResearch/hermes-agent/pull/3298))
- **Preserve user input on multiline paste** ([#3065](https://github.com/NousResearch/hermes-agent/pull/3065))
- **Tool generation callback** — streaming "preparing terminal…" updates during tool argument generation ([untagged commit](https://github.com/NousResearch/hermes-agent))
- Show tool progress for substantive tools, not just "preparing" ([untagged commit](https://github.com/NousResearch/hermes-agent))
- Buffer reasoning preview chunks and fix duplicate display ([#3013](https://github.com/NousResearch/hermes-agent/pull/3013))
- Prevent reasoning box from rendering 3x during tool-calling loops ([#3405](https://github.com/NousResearch/hermes-agent/pull/3405))
- Eliminate "Event loop is closed" / "Press ENTER to continue" during idle — three-layer fix with `neuter_async_httpx_del()`, custom exception handler, and stale client cleanup ([#3398](https://github.com/NousResearch/hermes-agent/pull/3398))
- Fix status bar shows 26K instead of 260K for token counts with trailing zeros ([#3024](https://github.com/NousResearch/hermes-agent/pull/3024))
- Fix status bar duplicates and degrades during long sessions ([#3291](https://github.com/NousResearch/hermes-agent/pull/3291))
- Refresh TUI before background task output to prevent status bar overlap ([#3048](https://github.com/NousResearch/hermes-agent/pull/3048))
- Suppress KawaiiSpinner animation under `patch_stdout` ([#2994](https://github.com/NousResearch/hermes-agent/pull/2994))
- Skip KawaiiSpinner when TUI handles tool progress ([#2973](https://github.com/NousResearch/hermes-agent/pull/2973))
- Guard `isatty()` against closed streams via `_is_tty` property ([#3056](https://github.com/NousResearch/hermes-agent/pull/3056))
- Ensure single closure of streaming boxes during tool generation ([untagged commit](https://github.com/NousResearch/hermes-agent))
- Cap context pressure percentage at 100% in display ([#3480](https://github.com/NousResearch/hermes-agent/pull/3480))
- Clean up HTML error messages in CLI display ([#3069](https://github.com/NousResearch/hermes-agent/pull/3069))
- Show HTTP status code and 400 body in API error output ([#3096](https://github.com/NousResearch/hermes-agent/pull/3096))
- Extract useful info from HTML error pages, dump debug on max retries ([untagged commit](https://github.com/NousResearch/hermes-agent))
- Prevent TypeError on startup when `base_url` is None ([#3068](https://github.com/NousResearch/hermes-agent/pull/3068))
- Prevent update crash in non-TTY environments ([#3094](https://github.com/NousResearch/hermes-agent/pull/3094))
- Handle EOFError in sessions delete/prune confirmation prompts ([#3101](https://github.com/NousResearch/hermes-agent/pull/3101))
- Catch KeyboardInterrupt during `flush_memories` on exit and in exit cleanup handlers ([#3025](https://github.com/NousResearch/hermes-agent/pull/3025), [#3257](https://github.com/NousResearch/hermes-agent/pull/3257))
- Guard `.strip()` against None values from YAML config ([#3552](https://github.com/NousResearch/hermes-agent/pull/3552))
- Guard `config.get()` against YAML null values to prevent AttributeError ([#3377](https://github.com/NousResearch/hermes-agent/pull/3377))
- Store asyncio task references to prevent GC mid-execution ([#3267](https://github.com/NousResearch/hermes-agent/pull/3267))

#### Setup & Configuration
- Use explicit key mapping for returning-user menu dispatch instead of positional index ([#3083](https://github.com/NousResearch/hermes-agent/pull/3083))
- Use `sys.executable` for pip in update commands to fix PEP 668 ([#3099](https://github.com/NousResearch/hermes-agent/pull/3099))
- Harden `hermes update` against diverged history, non-main branches, and gateway edge cases ([#3492](https://github.com/NousResearch/hermes-agent/pull/3492))
- OpenClaw migration overwrites defaults and setup wizard skips imported sections — fixed ([#3282](https://github.com/NousResearch/hermes-agent/pull/3282))
- Stop recursive AGENTS.md walk, load top-level only ([#3110](https://github.com/NousResearch/hermes-agent/pull/3110))
- Add macOS Homebrew paths to browser and terminal PATH resolution ([#2713](https://github.com/NousResearch/hermes-agent/pull/2713))
- YAML boolean handling for `tool_progress` config ([#3300](https://github.com/NousResearch/hermes-agent/pull/3300))
- Reset default SOUL.md to baseline identity text ([#3159](https://github.com/NousResearch/hermes-agent/pull/3159))
- Reject relative cwd paths for container terminal backends ([untagged commit](https://github.com/NousResearch/hermes-agent))
- Add explicit `hermes-api-server` toolset for API server platform ([#3304](https://github.com/NousResearch/hermes-agent/pull/3304))
- Reorder setup wizard providers — OpenRouter first ([untagged commit](https://github.com/NousResearch/hermes-agent))

---

### 🔧 Tool System

#### API Server
- **Idempotency-Key support**, body size limit, and OpenAI error envelope ([#2903](https://github.com/NousResearch/hermes-agent/pull/2903))
- Allow Idempotency-Key in CORS headers ([#3530](https://github.com/NousResearch/hermes-agent/pull/3530))
- Cancel orphaned agent + true interrupt on SSE disconnect ([#3427](https://github.com/NousResearch/hermes-agent/pull/3427))
- Fix streaming breaks when agent makes tool calls ([#2985](https://github.com/NousResearch/hermes-agent/pull/2985))

#### Terminal & File Operations
- Handle addition-only hunks in V4A patch parser ([#3325](https://github.com/NousResearch/hermes-agent/pull/3325))
- Exponential backoff for persistent shell polling ([#2996](https://github.com/NousResearch/hermes-agent/pull/2996))
- Add timeout to subprocess calls in `context_references` ([#3469](https://github.com/NousResearch/hermes-agent/pull/3469))

#### Browser & Vision
- Handle 402 insufficient credits error in vision tool ([#2802](https://github.com/NousResearch/hermes-agent/pull/2802))
- Fix `browser_vision` ignores `auxiliary.vision.timeout` config ([#2901](https://github.com/NousResearch/hermes-agent/pull/2901))
- Make browser command timeout configurable via config.yaml ([#2801](https://github.com/NousResearch/hermes-agent/pull/2801))

#### MCP
- MCP toolset resolution for runtime and config ([#3252](https://github.com/NousResearch/hermes-agent/pull/3252))
- Add MCP tool name collision protection ([#3077](https://github.com/NousResearch/hermes-agent/pull/3077))

#### Auxiliary LLM
- Guard aux LLM calls against None content + reasoning fallback + retry ([#3449](https://github.com/NousResearch/hermes-agent/pull/3449))
- Catch ImportError from `build_anthropic_client` in vision auto-detection ([#3312](https://github.com/NousResearch/hermes-agent/pull/3312))

#### Other Tools
- Add request timeouts to `send_message_tool` HTTP calls ([#3162](https://github.com/NousResearch/hermes-agent/pull/3162)) by @memosr
- Auto-repair `jobs.json` with invalid control characters ([#3537](https://github.com/NousResearch/hermes-agent/pull/3537))
- Enable fine-grained tool streaming for Claude/OpenRouter ([#3497](https://github.com/NousResearch/hermes-agent/pull/3497))

---

### 🧩 Skills Ecosystem

#### Skills System
- **Env var passthrough** for skills and user config — skills can declare environment variables to pass through ([#2807](https://github.com/NousResearch/hermes-agent/pull/2807))
- Cache skills prompt with shared `skill_utils` module for faster TTFT ([#3421](https://github.com/NousResearch/hermes-agent/pull/3421))
- Avoid redundant file re-read for skill conditions ([#2992](https://github.com/NousResearch/hermes-agent/pull/2992))
- Use Git Trees API to prevent silent subdirectory loss during install ([#2995](https://github.com/NousResearch/hermes-agent/pull/2995))
- Fix skills-sh install for deeply nested repo structures ([#2980](https://github.com/NousResearch/hermes-agent/pull/2980))
- Handle null metadata in skill frontmatter ([untagged commit](https://github.com/NousResearch/hermes-agent))
- Preserve trust for skills-sh identifiers + reduce resolution churn ([#3251](https://github.com/NousResearch/hermes-agent/pull/3251))
- Agent-created skills were incorrectly treated as untrusted community content — fixed ([untagged commit](https://github.com/NousResearch/hermes-agent))

#### New Skills
- **G0DM0D3 godmode jailbreaking skill** + docs ([#3157](https://github.com/NousResearch/hermes-agent/pull/3157))
- **Docker management skill** added to optional-skills ([#3060](https://github.com/NousResearch/hermes-agent/pull/3060))
- **OpenClaw migration v2** — 17 new modules, terminal recap for migrating from OpenClaw to Hermes ([#2906](https://github.com/NousResearch/hermes-agent/pull/2906))

---

### 🔒 Security & Reliability

#### Security Hardening
- **SSRF protection** added to `browser_navigate` ([#3058](https://github.com/NousResearch/hermes-agent/pull/3058))
- **SSRF protection** added to `vision_tools` and `web_tools` (hardened) ([#2679](https://github.com/NousResearch/hermes-agent/pull/2679))
- **Restrict subagent toolsets** to parent's enabled set ([#3269](https://github.com/NousResearch/hermes-agent/pull/3269))
- **Prevent zip-slip path traversal** in self-update ([#3250](https://github.com/NousResearch/hermes-agent/pull/3250))
- **Prevent shell injection** in `_expand_path` via `~user` path suffix ([#2685](https://github.com/NousResearch/hermes-agent/pull/2685))
- **Normalize input** before dangerous command detection ([#3260](https://github.com/NousResearch/hermes-agent/pull/3260))
- Make tirith block verdicts approvable instead of hard-blocking ([#3428](https://github.com/NousResearch/hermes-agent/pull/3428))
- Remove compromised `litellm`/`typer`/`platformdirs` from deps ([#2796](https://github.com/NousResearch/hermes-agent/pull/2796))
- Pin all dependency version ranges ([#2810](https://github.com/NousResearch/hermes-agent/pull/2810))
- Regenerate `uv.lock` with hashes, use lockfile in setup ([#2812](https://github.com/NousResearch/hermes-agent/pull/2812))
- Bump dependencies to fix CVEs + regenerate `uv.lock` ([#3073](https://github.com/NousResearch/hermes-agent/pull/3073))
- Supply chain audit CI workflow for PR scanning ([#2816](https://github.com/NousResearch/hermes-agent/pull/2816))

#### Reliability
- **SQLite WAL write-lock contention** causing 15-20s TUI freeze — fixed ([#3385](https://github.com/NousResearch/hermes-agent/pull/3385))
- **SQLite concurrency hardening** + session transcript integrity ([#3249](https://github.com/NousResearch/hermes-agent/pull/3249))
- Prevent recurring cron job re-fire on gateway crash/restart loop ([#3396](https://github.com/NousResearch/hermes-agent/pull/3396))
- Mark cron session as ended after job completes ([#2998](https://github.com/NousResearch/hermes-agent/pull/2998))

---

### ⚡ Performance

- **TTFT startup optimizations** — salvaged easy-win startup improvements ([#3395](https://github.com/NousResearch/hermes-agent/pull/3395))
- Cache skills prompt with shared `skill_utils` module ([#3421](https://github.com/NousResearch/hermes-agent/pull/3421))
- Avoid redundant file re-read for skill conditions in prompt builder ([#2992](https://github.com/NousResearch/hermes-agent/pull/2992))

---

### 🐛 Notable Bug Fixes

- Fix gateway token double-counting with cached agents ([#3306](https://github.com/NousResearch/hermes-agent/pull/3306), [#3317](https://github.com/NousResearch/hermes-agent/pull/3317))
- Fix "Event loop is closed" / "Press ENTER to continue" during idle sessions ([#3398](https://github.com/NousResearch/hermes-agent/pull/3398))
- Fix reasoning box rendering 3x during tool-calling loops ([#3405](https://github.com/NousResearch/hermes-agent/pull/3405))
- Fix status bar shows 26K instead of 260K for token counts ([#3024](https://github.com/NousResearch/hermes-agent/pull/3024))
- Fix `/queue` always working regardless of config ([#3298](https://github.com/NousResearch/hermes-agent/pull/3298))
- Fix phantom Discord typing indicator after agent turn ([#3003](https://github.com/NousResearch/hermes-agent/pull/3003))
- Fix Slack progress messages appearing in wrong thread ([#3063](https://github.com/NousResearch/hermes-agent/pull/3063))
- Fix WhatsApp media downloads (documents, audio, video) ([#2978](https://github.com/NousResearch/hermes-agent/pull/2978))
- Fix Telegram "Message thread not found" killing progress messages ([#3390](https://github.com/NousResearch/hermes-agent/pull/3390))
- Fix OpenClaw migration overwriting defaults ([#3282](https://github.com/NousResearch/hermes-agent/pull/3282))
- Fix returning-user setup menu dispatching wrong section ([#3083](https://github.com/NousResearch/hermes-agent/pull/3083))
- Fix `hermes update` PEP 668 "externally-managed-environment" error ([#3099](https://github.com/NousResearch/hermes-agent/pull/3099))
- Fix subagents hitting `max_iterations` prematurely via shared budget ([#3004](https://github.com/NousResearch/hermes-agent/pull/3004))
- Fix YAML boolean handling for `tool_progress` config ([#3300](https://github.com/NousResearch/hermes-agent/pull/3300))
- Fix `config.get()` crashes on YAML null values ([#3377](https://github.com/NousResearch/hermes-agent/pull/3377))
- Fix `.strip()` crash on None values from YAML config ([#3552](https://github.com/NousResearch/hermes-agent/pull/3552))
- Fix hung agents on gateway — `/stop` now hard-kills session lock ([#3104](https://github.com/NousResearch/hermes-agent/pull/3104))
- Fix `_custom` provider silently remapped to `openrouter` ([#2792](https://github.com/NousResearch/hermes-agent/pull/2792))
- Fix Matrix missing from `PLATFORMS` dict ([#3473](https://github.com/NousResearch/hermes-agent/pull/3473))
- Fix Email adapter unbounded `_seen_uids` growth ([#3490](https://github.com/NousResearch/hermes-agent/pull/3490))

---

### 🧪 Testing

- Pin `agent-client-protocol` < 0.9 to handle breaking upstream release ([#3320](https://github.com/NousResearch/hermes-agent/pull/3320))
- Catch anthropic ImportError in vision auto-detection tests ([#3312](https://github.com/NousResearch/hermes-agent/pull/3312))
- Update retry-exhaust test for new graceful return behavior ([#3320](https://github.com/NousResearch/hermes-agent/pull/3320))
- Add regression tests for null metadata frontmatter ([untagged commit](https://github.com/NousResearch/hermes-agent))

---

### 📚 Documentation

- Update all docs for `/model` command overhaul and custom provider support ([#2800](https://github.com/NousResearch/hermes-agent/pull/2800))
- Fix stale and incorrect documentation across 18 files ([#2805](https://github.com/NousResearch/hermes-agent/pull/2805))
- Document 9 previously undocumented features ([#2814](https://github.com/NousResearch/hermes-agent/pull/2814))
- Add missing skills, CLI commands, and messaging env vars to docs ([#2809](https://github.com/NousResearch/hermes-agent/pull/2809))
- Fix api-server response storage documentation — SQLite, not in-memory ([#2819](https://github.com/NousResearch/hermes-agent/pull/2819))
- Quote pip install extras to fix zsh glob errors ([#2815](https://github.com/NousResearch/hermes-agent/pull/2815))
- Unify hooks documentation — add plugin hooks to hooks page, add `session:end` event ([untagged commit](https://github.com/NousResearch/hermes-agent))
- Clarify two-mode behavior in `session_search` schema description ([untagged commit](https://github.com/NousResearch/hermes-agent))
- Fix Discord Public Bot setting for Discord-provided invite link ([#3519](https://github.com/NousResearch/hermes-agent/pull/3519)) by @mehmoodosman
- Revise v0.4.0 changelog — fix feature attribution, reorder sections ([untagged commit](https://github.com/NousResearch/hermes-agent))

---

### 👥 Contributors

#### Core
- **@teknium1** — 157 PRs covering the full scope of this release

#### Community Contributors
- **@alt-glitch** (Siddharth Balyan) — 2 PRs: Nix flake with uv2nix build, NixOS module, and persistent container mode ([#20](https://github.com/NousResearch/hermes-agent/pull/20)); auto-generated config keys and suffix PATHs for Nix builds ([#3061](https://github.com/NousResearch/hermes-agent/pull/3061), [#3274](https://github.com/NousResearch/hermes-agent/pull/3274))
- **@ctlst** — 1 PR: Prevent AsyncOpenAI/httpx cross-loop deadlock in gateway mode ([#2701](https://github.com/NousResearch/hermes-agent/pull/2701))
- **@memosr** (memosr.eth) — 1 PR: Add request timeouts to `send_message_tool` HTTP calls ([#3162](https://github.com/NousResearch/hermes-agent/pull/3162))
- **@mehmoodosman** (Osman Mehmood) — 1 PR: Fix Discord docs for Public Bot setting ([#3519](https://github.com/NousResearch/hermes-agent/pull/3519))

#### All Contributors
@alt-glitch, @ctlst, @mehmoodosman, @memosr, @teknium1

---

**Full Changelog**: [v2026.3.23...v2026.3.28](https://github.com/NousResearch/hermes-agent/compare/v2026.3.23...v2026.3.28)
---

<a id="v0-4-0"></a>

## Hermes Agent v0.4.0 (v2026.3.23)

**Release Date:** March 23, 2026

> The platform expansion release — OpenAI-compatible API server, 6 new messaging adapters, 4 new inference providers, MCP server management with OAuth 2.1, @ context references, gateway prompt caching, streaming enabled by default, and a sweeping reliability pass with 200+ bug fixes.

---

### ✨ Highlights

- **OpenAI-compatible API server** — Expose Hermes as an `/v1/chat/completions` endpoint with a new `/api/jobs` REST API for cron job management, hardened with input limits, field whitelists, SQLite-backed response persistence, and CORS origin protection ([#1756](https://github.com/NousResearch/hermes-agent/pull/1756), [#2450](https://github.com/NousResearch/hermes-agent/pull/2450), [#2456](https://github.com/NousResearch/hermes-agent/pull/2456), [#2451](https://github.com/NousResearch/hermes-agent/pull/2451), [#2472](https://github.com/NousResearch/hermes-agent/pull/2472))

- **6 new messaging platform adapters** — Signal, DingTalk, SMS (Twilio), Mattermost, Matrix, and Webhook adapters join Telegram, Discord, and WhatsApp. Gateway auto-reconnects failed platforms with exponential backoff ([#2206](https://github.com/NousResearch/hermes-agent/pull/2206), [#1685](https://github.com/NousResearch/hermes-agent/pull/1685), [#1688](https://github.com/NousResearch/hermes-agent/pull/1688), [#1683](https://github.com/NousResearch/hermes-agent/pull/1683), [#2166](https://github.com/NousResearch/hermes-agent/pull/2166), [#2584](https://github.com/NousResearch/hermes-agent/pull/2584))

- **@ context references** — Claude Code-style `@file` and `@url` context injection with tab completions in the CLI ([#2343](https://github.com/NousResearch/hermes-agent/pull/2343), [#2482](https://github.com/NousResearch/hermes-agent/pull/2482))

- **4 new inference providers** — GitHub Copilot (OAuth + token validation), Alibaba Cloud / DashScope, Kilo Code, and OpenCode Zen/Go ([#1924](https://github.com/NousResearch/hermes-agent/pull/1924), [#1879](https://github.com/NousResearch/hermes-agent/pull/1879) by @mchzimm, [#1673](https://github.com/NousResearch/hermes-agent/pull/1673), [#1666](https://github.com/NousResearch/hermes-agent/pull/1666), [#1650](https://github.com/NousResearch/hermes-agent/pull/1650))

- **MCP server management CLI** — `hermes mcp` commands for installing, configuring, and authenticating MCP servers with full OAuth 2.1 PKCE flow ([#2465](https://github.com/NousResearch/hermes-agent/pull/2465))

- **Gateway prompt caching** — Cache AIAgent instances per session, preserving Anthropic prompt cache across turns for dramatic cost reduction on long conversations ([#2282](https://github.com/NousResearch/hermes-agent/pull/2282), [#2284](https://github.com/NousResearch/hermes-agent/pull/2284), [#2361](https://github.com/NousResearch/hermes-agent/pull/2361))

- **Context compression overhaul** — Structured summaries with iterative updates, token-budget tail protection, configurable summary endpoint, and fallback model support ([#2323](https://github.com/NousResearch/hermes-agent/pull/2323), [#1727](https://github.com/NousResearch/hermes-agent/pull/1727), [#2224](https://github.com/NousResearch/hermes-agent/pull/2224))

- **Streaming enabled by default** — CLI streaming on by default with proper spinner/tool progress display during streaming mode, plus extensive linebreak and concatenation fixes ([#2340](https://github.com/NousResearch/hermes-agent/pull/2340), [#2161](https://github.com/NousResearch/hermes-agent/pull/2161), [#2258](https://github.com/NousResearch/hermes-agent/pull/2258))

---

### 🖥️ CLI & User Experience

#### New Commands & Interactions
- **@ context completions** — Tab-completable `@file`/`@url` references that inject file content or web pages into the conversation ([#2482](https://github.com/NousResearch/hermes-agent/pull/2482), [#2343](https://github.com/NousResearch/hermes-agent/pull/2343))
- **`/statusbar`** — Toggle a persistent config bar showing model + provider info in the prompt ([#2240](https://github.com/NousResearch/hermes-agent/pull/2240), [#1917](https://github.com/NousResearch/hermes-agent/pull/1917))
- **`/queue`** — Queue prompts for the agent without interrupting the current run ([#2191](https://github.com/NousResearch/hermes-agent/pull/2191), [#2469](https://github.com/NousResearch/hermes-agent/pull/2469))
- **`/permission`** — Switch approval mode dynamically during a session ([#2207](https://github.com/NousResearch/hermes-agent/pull/2207))
- **`/browser`** — Interactive browser sessions from the CLI ([#2273](https://github.com/NousResearch/hermes-agent/pull/2273), [#1814](https://github.com/NousResearch/hermes-agent/pull/1814))
- **`/cost`** — Live pricing and usage tracking in gateway mode ([#2180](https://github.com/NousResearch/hermes-agent/pull/2180))
- **`/approve` and `/deny`** — Replaced bare text approval in gateway with explicit commands ([#2002](https://github.com/NousResearch/hermes-agent/pull/2002))

#### Streaming & Display
- Streaming enabled by default in CLI ([#2340](https://github.com/NousResearch/hermes-agent/pull/2340))
- Show spinners and tool progress during streaming mode ([#2161](https://github.com/NousResearch/hermes-agent/pull/2161))
- Show reasoning/thinking blocks when `show_reasoning` enabled ([#2118](https://github.com/NousResearch/hermes-agent/pull/2118))
- Context pressure warnings for CLI and gateway ([#2159](https://github.com/NousResearch/hermes-agent/pull/2159))
- Fix: streaming chunks concatenated without whitespace ([#2258](https://github.com/NousResearch/hermes-agent/pull/2258))
- Fix: iteration boundary linebreak prevents stream concatenation ([#2413](https://github.com/NousResearch/hermes-agent/pull/2413))
- Fix: defer streaming linebreak to prevent blank line stacking ([#2473](https://github.com/NousResearch/hermes-agent/pull/2473))
- Fix: suppress spinner animation in non-TTY environments ([#2216](https://github.com/NousResearch/hermes-agent/pull/2216))
- Fix: display provider and endpoint in API error messages ([#2266](https://github.com/NousResearch/hermes-agent/pull/2266))
- Fix: resolve garbled ANSI escape codes in status printouts ([#2448](https://github.com/NousResearch/hermes-agent/pull/2448))
- Fix: update gold ANSI color to true-color format ([#2246](https://github.com/NousResearch/hermes-agent/pull/2246))
- Fix: normalize toolset labels and use skin colors in banner ([#1912](https://github.com/NousResearch/hermes-agent/pull/1912))

#### CLI Polish
- Fix: prevent 'Press ENTER to continue...' on exit ([#2555](https://github.com/NousResearch/hermes-agent/pull/2555))
- Fix: flush stdout during agent loop to prevent macOS display freeze ([#1654](https://github.com/NousResearch/hermes-agent/pull/1654))
- Fix: show human-readable error when `hermes setup` hits permissions error ([#2196](https://github.com/NousResearch/hermes-agent/pull/2196))
- Fix: `/stop` command crash + UnboundLocalError in streaming media delivery ([#2463](https://github.com/NousResearch/hermes-agent/pull/2463))
- Fix: allow custom/local endpoints without API key ([#2556](https://github.com/NousResearch/hermes-agent/pull/2556))
- Fix: Kitty keyboard protocol Shift+Enter for Ghostty/WezTerm (attempted + reverted due to prompt_toolkit crash) ([#2345](https://github.com/NousResearch/hermes-agent/pull/2345), [#2349](https://github.com/NousResearch/hermes-agent/pull/2349))

#### Configuration
- **`${ENV_VAR}` substitution** in config.yaml ([#2684](https://github.com/NousResearch/hermes-agent/pull/2684))
- **Real-time config reload** — config.yaml changes apply without restart ([#2210](https://github.com/NousResearch/hermes-agent/pull/2210))
- **`custom_models.yaml`** for user-managed model additions ([#2214](https://github.com/NousResearch/hermes-agent/pull/2214))
- **Priority-based context file selection** + CLAUDE.md support ([#2301](https://github.com/NousResearch/hermes-agent/pull/2301))
- **Merge nested YAML sections** instead of replacing on config update ([#2213](https://github.com/NousResearch/hermes-agent/pull/2213))
- Fix: config.yaml provider key overrides env var silently ([#2272](https://github.com/NousResearch/hermes-agent/pull/2272))
- Fix: log warning instead of silently swallowing config.yaml errors ([#2683](https://github.com/NousResearch/hermes-agent/pull/2683))
- Fix: disabled toolsets re-enable themselves after `hermes tools` ([#2268](https://github.com/NousResearch/hermes-agent/pull/2268))
- Fix: platform default toolsets silently override tool deselection ([#2624](https://github.com/NousResearch/hermes-agent/pull/2624))
- Fix: honor bare YAML `approvals.mode: off` ([#2620](https://github.com/NousResearch/hermes-agent/pull/2620))
- Fix: `hermes update` use `.[all]` extras with fallback ([#1728](https://github.com/NousResearch/hermes-agent/pull/1728))
- Fix: `hermes update` prompt before resetting working tree on stash conflicts ([#2390](https://github.com/NousResearch/hermes-agent/pull/2390))
- Fix: use git pull --rebase in update/install to avoid divergent branch error ([#2274](https://github.com/NousResearch/hermes-agent/pull/2274))
- Fix: add zprofile fallback and create zshrc on fresh macOS installs ([#2320](https://github.com/NousResearch/hermes-agent/pull/2320))
- Fix: remove `ANTHROPIC_BASE_URL` env var to avoid collisions ([#1675](https://github.com/NousResearch/hermes-agent/pull/1675))
- Fix: don't ask IMAP password if already in keyring or env ([#2212](https://github.com/NousResearch/hermes-agent/pull/2212))
- Fix: OpenCode Zen/Go show OpenRouter models instead of their own ([#2277](https://github.com/NousResearch/hermes-agent/pull/2277))

---

### 🏗️ Core Agent & Architecture

#### New Providers
- **GitHub Copilot** — Full OAuth auth, API routing, token validation, and 400k context. ([#1924](https://github.com/NousResearch/hermes-agent/pull/1924), [#1896](https://github.com/NousResearch/hermes-agent/pull/1896), [#1879](https://github.com/NousResearch/hermes-agent/pull/1879) by @mchzimm, [#2507](https://github.com/NousResearch/hermes-agent/pull/2507))
- **Alibaba Cloud / DashScope** — Full integration with DashScope v1 runtime, model dot preservation, and 401 auth fixes ([#1673](https://github.com/NousResearch/hermes-agent/pull/1673), [#2332](https://github.com/NousResearch/hermes-agent/pull/2332), [#2459](https://github.com/NousResearch/hermes-agent/pull/2459))
- **Kilo Code** — First-class inference provider ([#1666](https://github.com/NousResearch/hermes-agent/pull/1666))
- **OpenCode Zen and OpenCode Go** — New provider backends ([#1650](https://github.com/NousResearch/hermes-agent/pull/1650), [#2393](https://github.com/NousResearch/hermes-agent/pull/2393) by @0xbyt4)
- **NeuTTS** — Local TTS provider backend with built-in setup flow, replacing the old optional skill ([#1657](https://github.com/NousResearch/hermes-agent/pull/1657), [#1664](https://github.com/NousResearch/hermes-agent/pull/1664))

#### Provider Improvements
- **Eager fallback** to backup model on rate-limit errors ([#1730](https://github.com/NousResearch/hermes-agent/pull/1730))
- **Endpoint metadata** for custom model context and pricing; query local servers for actual context window size ([#1906](https://github.com/NousResearch/hermes-agent/pull/1906), [#2091](https://github.com/NousResearch/hermes-agent/pull/2091) by @dusterbloom)
- **Context length detection overhaul** — models.dev integration, provider-aware resolution, fuzzy matching for custom endpoints, `/v1/props` for llama.cpp ([#2158](https://github.com/NousResearch/hermes-agent/pull/2158), [#2051](https://github.com/NousResearch/hermes-agent/pull/2051), [#2403](https://github.com/NousResearch/hermes-agent/pull/2403))
- **Model catalog updates** — gpt-5.4-mini, gpt-5.4-nano, healer-alpha, haiku-4.5, minimax-m2.7, claude 4.6 at 1M context ([#1913](https://github.com/NousResearch/hermes-agent/pull/1913), [#1915](https://github.com/NousResearch/hermes-agent/pull/1915), [#1900](https://github.com/NousResearch/hermes-agent/pull/1900), [#2155](https://github.com/NousResearch/hermes-agent/pull/2155), [#2474](https://github.com/NousResearch/hermes-agent/pull/2474))
- **Custom endpoint improvements** — `model.base_url` in config.yaml, `api_mode` override for responses API, allow endpoints without API key, fail fast on missing keys ([#2330](https://github.com/NousResearch/hermes-agent/pull/2330), [#1651](https://github.com/NousResearch/hermes-agent/pull/1651), [#2556](https://github.com/NousResearch/hermes-agent/pull/2556), [#2445](https://github.com/NousResearch/hermes-agent/pull/2445), [#1994](https://github.com/NousResearch/hermes-agent/pull/1994), [#1998](https://github.com/NousResearch/hermes-agent/pull/1998))
- Inject model and provider into system prompt ([#1929](https://github.com/NousResearch/hermes-agent/pull/1929))
- Tie `api_mode` to provider config instead of env var ([#1656](https://github.com/NousResearch/hermes-agent/pull/1656))
- Fix: prevent Anthropic token leaking to third-party `anthropic_messages` providers ([#2389](https://github.com/NousResearch/hermes-agent/pull/2389))
- Fix: prevent Anthropic fallback from inheriting non-Anthropic `base_url` ([#2388](https://github.com/NousResearch/hermes-agent/pull/2388))
- Fix: `auxiliary_is_nous` flag never resets — leaked Nous tags to other providers ([#1713](https://github.com/NousResearch/hermes-agent/pull/1713))
- Fix: Anthropic `tool_choice 'none'` still allowed tool calls ([#1714](https://github.com/NousResearch/hermes-agent/pull/1714))
- Fix: Mistral parser nested JSON fallback extraction ([#2335](https://github.com/NousResearch/hermes-agent/pull/2335))
- Fix: MiniMax 401 auth resolved by defaulting to `anthropic_messages` ([#2103](https://github.com/NousResearch/hermes-agent/pull/2103))
- Fix: case-insensitive model family matching ([#2350](https://github.com/NousResearch/hermes-agent/pull/2350))
- Fix: ignore placeholder provider keys in activation checks ([#2358](https://github.com/NousResearch/hermes-agent/pull/2358))
- Fix: Preserve Ollama model:tag colons in context length detection ([#2149](https://github.com/NousResearch/hermes-agent/pull/2149))
- Fix: recognize Claude Code OAuth credentials in startup gate ([#1663](https://github.com/NousResearch/hermes-agent/pull/1663))
- Fix: detect Claude Code version dynamically for OAuth user-agent ([#1670](https://github.com/NousResearch/hermes-agent/pull/1670))
- Fix: OAuth flag stale after refresh/fallback ([#1890](https://github.com/NousResearch/hermes-agent/pull/1890))
- Fix: auxiliary client skips expired Codex JWT ([#2397](https://github.com/NousResearch/hermes-agent/pull/2397))

#### Agent Loop
- **Gateway prompt caching** — Cache AIAgent per session, keep assistant turns, fix session restore ([#2282](https://github.com/NousResearch/hermes-agent/pull/2282), [#2284](https://github.com/NousResearch/hermes-agent/pull/2284), [#2361](https://github.com/NousResearch/hermes-agent/pull/2361))
- **Context compression overhaul** — Structured summaries, iterative updates, token-budget tail protection, configurable `summary_base_url` ([#2323](https://github.com/NousResearch/hermes-agent/pull/2323), [#1727](https://github.com/NousResearch/hermes-agent/pull/1727), [#2224](https://github.com/NousResearch/hermes-agent/pull/2224))
- **Pre-call sanitization and post-call tool guardrails** ([#1732](https://github.com/NousResearch/hermes-agent/pull/1732))
- **Auto-recover** from provider-rejected `tool_choice` by retrying without ([#2174](https://github.com/NousResearch/hermes-agent/pull/2174))
- **Background memory/skill review** replaces inline nudges ([#2235](https://github.com/NousResearch/hermes-agent/pull/2235))
- **SOUL.md as primary agent identity** instead of hardcoded default ([#1922](https://github.com/NousResearch/hermes-agent/pull/1922))
- Fix: prevent silent tool result loss during context compression ([#1993](https://github.com/NousResearch/hermes-agent/pull/1993))
- Fix: handle empty/null function arguments in tool call recovery ([#2163](https://github.com/NousResearch/hermes-agent/pull/2163))
- Fix: handle API refusal responses gracefully instead of crashing ([#2156](https://github.com/NousResearch/hermes-agent/pull/2156))
- Fix: prevent stuck agent loop on malformed tool calls ([#2114](https://github.com/NousResearch/hermes-agent/pull/2114))
- Fix: return JSON parse error to model instead of dispatching with empty args ([#2342](https://github.com/NousResearch/hermes-agent/pull/2342))
- Fix: consecutive assistant message merge drops content on mixed types ([#1703](https://github.com/NousResearch/hermes-agent/pull/1703))
- Fix: message role alternation violations in JSON recovery and error handler ([#1722](https://github.com/NousResearch/hermes-agent/pull/1722))
- Fix: `compression_attempts` resets each iteration — allowed unlimited compressions ([#1723](https://github.com/NousResearch/hermes-agent/pull/1723))
- Fix: `length_continue_retries` never resets — later truncations got fewer retries ([#1717](https://github.com/NousResearch/hermes-agent/pull/1717))
- Fix: compressor summary role violated consecutive-role constraint ([#1720](https://github.com/NousResearch/hermes-agent/pull/1720), [#1743](https://github.com/NousResearch/hermes-agent/pull/1743))
- Fix: remove hardcoded `gemini-3-flash-preview` as default summary model ([#2464](https://github.com/NousResearch/hermes-agent/pull/2464))
- Fix: correctly handle empty tool results ([#2201](https://github.com/NousResearch/hermes-agent/pull/2201))
- Fix: crash on None entry in `tool_calls` list ([#2209](https://github.com/NousResearch/hermes-agent/pull/2209) by @0xbyt4, [#2316](https://github.com/NousResearch/hermes-agent/pull/2316))
- Fix: per-thread persistent event loops in worker threads ([#2214](https://github.com/NousResearch/hermes-agent/pull/2214) by @jquesnelle)
- Fix: prevent 'event loop already running' when async tools run in parallel ([#2207](https://github.com/NousResearch/hermes-agent/pull/2207))
- Fix: strip ANSI at the source — clean terminal output before it reaches the model ([#2115](https://github.com/NousResearch/hermes-agent/pull/2115))
- Fix: skip top-level `cache_control` on role:tool for OpenRouter ([#2391](https://github.com/NousResearch/hermes-agent/pull/2391))
- Fix: delegate tool — save parent tool names before child construction mutates global ([#2083](https://github.com/NousResearch/hermes-agent/pull/2083) by @ygd58, [#1894](https://github.com/NousResearch/hermes-agent/pull/1894))
- Fix: only strip last assistant message if empty string ([#2326](https://github.com/NousResearch/hermes-agent/pull/2326))

#### Session & Memory
- **Session search** and management slash commands ([#2198](https://github.com/NousResearch/hermes-agent/pull/2198))
- **Auto session titles** and `.hermes.md` project config ([#1712](https://github.com/NousResearch/hermes-agent/pull/1712))
- Fix: concurrent memory writes silently drop entries — added file locking ([#1726](https://github.com/NousResearch/hermes-agent/pull/1726))
- Fix: search all sources by default in `session_search` ([#1892](https://github.com/NousResearch/hermes-agent/pull/1892))
- Fix: handle hyphenated FTS5 queries and preserve quoted literals ([#1776](https://github.com/NousResearch/hermes-agent/pull/1776))
- Fix: skip corrupt lines in `load_transcript` instead of crashing ([#1744](https://github.com/NousResearch/hermes-agent/pull/1744))
- Fix: normalize session keys to prevent case-sensitive duplicates ([#2157](https://github.com/NousResearch/hermes-agent/pull/2157))
- Fix: prevent `session_search` crash when no sessions exist ([#2194](https://github.com/NousResearch/hermes-agent/pull/2194))
- Fix: reset token counters on new session for accurate usage display ([#2101](https://github.com/NousResearch/hermes-agent/pull/2101) by @InB4DevOps)
- Fix: prevent stale memory overwrites by flush agent ([#2687](https://github.com/NousResearch/hermes-agent/pull/2687))
- Fix: remove synthetic error message injection, fix session resume after repeated failures ([#2303](https://github.com/NousResearch/hermes-agent/pull/2303))
- Fix: quiet mode with `--resume` now passes conversation_history ([#2357](https://github.com/NousResearch/hermes-agent/pull/2357))
- Fix: unify resume logic in batch mode ([#2331](https://github.com/NousResearch/hermes-agent/pull/2331))

#### Honcho Memory
- Honcho config fixes and @ context reference integration ([#2343](https://github.com/NousResearch/hermes-agent/pull/2343))
- Self-hosted / Docker configuration documentation ([#2475](https://github.com/NousResearch/hermes-agent/pull/2475))

---

### 📱 Messaging Platforms (Gateway)

#### New Platform Adapters
- **Signal Messenger** — Full adapter with attachment handling, group message filtering, and Note to Self echo-back protection ([#2206](https://github.com/NousResearch/hermes-agent/pull/2206), [#2400](https://github.com/NousResearch/hermes-agent/pull/2400), [#2297](https://github.com/NousResearch/hermes-agent/pull/2297), [#2156](https://github.com/NousResearch/hermes-agent/pull/2156))
- **DingTalk** — Adapter with gateway wiring and setup docs ([#1685](https://github.com/NousResearch/hermes-agent/pull/1685), [#1690](https://github.com/NousResearch/hermes-agent/pull/1690), [#1692](https://github.com/NousResearch/hermes-agent/pull/1692))
- **SMS (Twilio)** ([#1688](https://github.com/NousResearch/hermes-agent/pull/1688))
- **Mattermost** — With @-mention-only channel filter ([#1683](https://github.com/NousResearch/hermes-agent/pull/1683), [#2443](https://github.com/NousResearch/hermes-agent/pull/2443))
- **Matrix** — With vision support and image caching ([#1683](https://github.com/NousResearch/hermes-agent/pull/1683), [#2520](https://github.com/NousResearch/hermes-agent/pull/2520))
- **Webhook** — Platform adapter for external event triggers ([#2166](https://github.com/NousResearch/hermes-agent/pull/2166))
- **OpenAI-compatible API server** — `/v1/chat/completions` endpoint with `/api/jobs` cron management ([#1756](https://github.com/NousResearch/hermes-agent/pull/1756), [#2450](https://github.com/NousResearch/hermes-agent/pull/2450), [#2456](https://github.com/NousResearch/hermes-agent/pull/2456))

#### Telegram Improvements
- MarkdownV2 support — strikethrough, spoiler, blockquotes, escape parentheses/braces/backslashes/backticks ([#2199](https://github.com/NousResearch/hermes-agent/pull/2199), [#2200](https://github.com/NousResearch/hermes-agent/pull/2200) by @llbn, [#2386](https://github.com/NousResearch/hermes-agent/pull/2386))
- Auto-detect HTML tags and use `parse_mode=HTML` ([#1709](https://github.com/NousResearch/hermes-agent/pull/1709))
- Telegram group vision support + thread-based sessions ([#2153](https://github.com/NousResearch/hermes-agent/pull/2153))
- Auto-reconnect polling after network interruption ([#2517](https://github.com/NousResearch/hermes-agent/pull/2517))
- Aggregate split text messages before dispatching ([#1674](https://github.com/NousResearch/hermes-agent/pull/1674))
- Fix: streaming config bridge, not-modified, flood control ([#1782](https://github.com/NousResearch/hermes-agent/pull/1782), [#1783](https://github.com/NousResearch/hermes-agent/pull/1783))
- Fix: edited_message event crashes ([#2074](https://github.com/NousResearch/hermes-agent/pull/2074))
- Fix: retry 409 polling conflicts before giving up ([#2312](https://github.com/NousResearch/hermes-agent/pull/2312))
- Fix: topic delivery via `platform:chat_id:thread_id` format ([#2455](https://github.com/NousResearch/hermes-agent/pull/2455))

#### Discord Improvements
- Document caching and text-file injection ([#2503](https://github.com/NousResearch/hermes-agent/pull/2503))
- Persistent typing indicator for DMs ([#2468](https://github.com/NousResearch/hermes-agent/pull/2468))
- Discord DM vision — inline images + attachment analysis ([#2186](https://github.com/NousResearch/hermes-agent/pull/2186))
- Persist thread participation across gateway restarts ([#1661](https://github.com/NousResearch/hermes-agent/pull/1661))
- Fix: gateway crash on non-ASCII guild names ([#2302](https://github.com/NousResearch/hermes-agent/pull/2302))
- Fix: thread permission errors ([#2073](https://github.com/NousResearch/hermes-agent/pull/2073))
- Fix: slash event routing in threads ([#2460](https://github.com/NousResearch/hermes-agent/pull/2460))
- Fix: remove bugged followup messages + `/ask` command ([#1836](https://github.com/NousResearch/hermes-agent/pull/1836))
- Fix: graceful WebSocket reconnection ([#2127](https://github.com/NousResearch/hermes-agent/pull/2127))
- Fix: voice channel TTS when streaming enabled ([#2322](https://github.com/NousResearch/hermes-agent/pull/2322))

#### WhatsApp & Other Adapters
- WhatsApp: outbound `send_message` routing ([#1769](https://github.com/NousResearch/hermes-agent/pull/1769) by @sai-samarth), LID format self-chat ([#1667](https://github.com/NousResearch/hermes-agent/pull/1667)), `reply_prefix` config fix ([#1923](https://github.com/NousResearch/hermes-agent/pull/1923)), restart on bridge child exit ([#2334](https://github.com/NousResearch/hermes-agent/pull/2334)), image/bridge improvements ([#2181](https://github.com/NousResearch/hermes-agent/pull/2181))
- Matrix: correct `reply_to_message_id` parameter ([#1895](https://github.com/NousResearch/hermes-agent/pull/1895)), bare media types fix ([#1736](https://github.com/NousResearch/hermes-agent/pull/1736))
- Mattermost: MIME types for media attachments ([#2329](https://github.com/NousResearch/hermes-agent/pull/2329))

#### Gateway Core
- **Auto-reconnect** failed platforms with exponential backoff ([#2584](https://github.com/NousResearch/hermes-agent/pull/2584))
- **Notify users when session auto-resets** ([#2519](https://github.com/NousResearch/hermes-agent/pull/2519))
- **Reply-to message context** for out-of-session replies ([#1662](https://github.com/NousResearch/hermes-agent/pull/1662))
- **Ignore unauthorized DMs** config option ([#1919](https://github.com/NousResearch/hermes-agent/pull/1919))
- Fix: `/reset` in thread-mode resets global session instead of thread ([#2254](https://github.com/NousResearch/hermes-agent/pull/2254))
- Fix: deliver MEDIA: files after streaming responses ([#2382](https://github.com/NousResearch/hermes-agent/pull/2382))
- Fix: cap interrupt recursion depth to prevent resource exhaustion ([#1659](https://github.com/NousResearch/hermes-agent/pull/1659))
- Fix: detect stopped processes and release stale locks on `--replace` ([#2406](https://github.com/NousResearch/hermes-agent/pull/2406), [#1908](https://github.com/NousResearch/hermes-agent/pull/1908))
- Fix: PID-based wait with force-kill for gateway restart ([#1902](https://github.com/NousResearch/hermes-agent/pull/1902))
- Fix: prevent `--replace` mode from killing the caller process ([#2185](https://github.com/NousResearch/hermes-agent/pull/2185))
- Fix: `/model` shows active fallback model instead of config default ([#1660](https://github.com/NousResearch/hermes-agent/pull/1660))
- Fix: `/title` command fails when session doesn't exist in SQLite yet ([#2379](https://github.com/NousResearch/hermes-agent/pull/2379) by @ten-jampa)
- Fix: process `/queue`'d messages after agent completion ([#2469](https://github.com/NousResearch/hermes-agent/pull/2469))
- Fix: strip orphaned `tool_results` + let `/reset` bypass running agent ([#2180](https://github.com/NousResearch/hermes-agent/pull/2180))
- Fix: prevent agents from starting gateway outside systemd management ([#2617](https://github.com/NousResearch/hermes-agent/pull/2617))
- Fix: prevent systemd restart storm on gateway connection failure ([#2327](https://github.com/NousResearch/hermes-agent/pull/2327))
- Fix: include resolved node path in systemd unit ([#1767](https://github.com/NousResearch/hermes-agent/pull/1767) by @sai-samarth)
- Fix: send error details to user in gateway outer exception handler ([#1966](https://github.com/NousResearch/hermes-agent/pull/1966))
- Fix: improve error handling for 429 usage limits and 500 context overflow ([#1839](https://github.com/NousResearch/hermes-agent/pull/1839))
- Fix: add all missing platform allowlist env vars to startup warning check ([#2628](https://github.com/NousResearch/hermes-agent/pull/2628))
- Fix: media delivery fails for file paths containing spaces ([#2621](https://github.com/NousResearch/hermes-agent/pull/2621))
- Fix: duplicate session-key collision in multi-platform gateway ([#2171](https://github.com/NousResearch/hermes-agent/pull/2171))
- Fix: Matrix and Mattermost never report as connected ([#1711](https://github.com/NousResearch/hermes-agent/pull/1711))
- Fix: PII redaction config never read — missing yaml import ([#1701](https://github.com/NousResearch/hermes-agent/pull/1701))
- Fix: NameError on skill slash commands ([#1697](https://github.com/NousResearch/hermes-agent/pull/1697))
- Fix: persist watcher metadata in checkpoint for crash recovery ([#1706](https://github.com/NousResearch/hermes-agent/pull/1706))
- Fix: pass `message_thread_id` in send_image_file, send_document, send_video ([#2339](https://github.com/NousResearch/hermes-agent/pull/2339))
- Fix: media-group aggregation on rapid successive photo messages ([#2160](https://github.com/NousResearch/hermes-agent/pull/2160))

---

### 🔧 Tool System

#### MCP Enhancements
- **MCP server management CLI** + OAuth 2.1 PKCE auth ([#2465](https://github.com/NousResearch/hermes-agent/pull/2465))
- **Expose MCP servers as standalone toolsets** ([#1907](https://github.com/NousResearch/hermes-agent/pull/1907))
- **Interactive MCP tool configuration** in `hermes tools` ([#1694](https://github.com/NousResearch/hermes-agent/pull/1694))
- Fix: MCP-OAuth port mismatch, path traversal, and shared handler state ([#2552](https://github.com/NousResearch/hermes-agent/pull/2552))
- Fix: preserve MCP tool registrations across session resets ([#2124](https://github.com/NousResearch/hermes-agent/pull/2124))
- Fix: concurrent file access crash + duplicate MCP registration ([#2154](https://github.com/NousResearch/hermes-agent/pull/2154))
- Fix: normalise MCP schemas + expand session list columns ([#2102](https://github.com/NousResearch/hermes-agent/pull/2102))
- Fix: `tool_choice` `mcp_` prefix handling ([#1775](https://github.com/NousResearch/hermes-agent/pull/1775))

#### Web Tool Backends
- **Tavily** as web search/extract/crawl backend ([#1731](https://github.com/NousResearch/hermes-agent/pull/1731))
- **Parallel** as alternative web search/extract backend ([#1696](https://github.com/NousResearch/hermes-agent/pull/1696))
- **Configurable web backend** — Firecrawl/BeautifulSoup/Playwright selection ([#2256](https://github.com/NousResearch/hermes-agent/pull/2256))
- Fix: whitespace-only env vars bypass web backend detection ([#2341](https://github.com/NousResearch/hermes-agent/pull/2341))

#### New Tools
- **IMAP email** reading and sending ([#2173](https://github.com/NousResearch/hermes-agent/pull/2173))
- **STT (speech-to-text)** tool using Whisper API ([#2072](https://github.com/NousResearch/hermes-agent/pull/2072))
- **Route-aware pricing estimates** ([#1695](https://github.com/NousResearch/hermes-agent/pull/1695))

#### Tool Improvements
- TTS: `base_url` support for OpenAI TTS provider ([#2064](https://github.com/NousResearch/hermes-agent/pull/2064) by @hanai)
- Vision: configurable timeout, tilde expansion in file paths, DM vision with multi-image and base64 fallback ([#2480](https://github.com/NousResearch/hermes-agent/pull/2480), [#2585](https://github.com/NousResearch/hermes-agent/pull/2585), [#2211](https://github.com/NousResearch/hermes-agent/pull/2211))
- Browser: race condition fix in session creation ([#1721](https://github.com/NousResearch/hermes-agent/pull/1721)), TypeError on unexpected LLM params ([#1735](https://github.com/NousResearch/hermes-agent/pull/1735))
- File tools: strip ANSI escape codes from write_file and patch content ([#2532](https://github.com/NousResearch/hermes-agent/pull/2532)), include pagination args in repeated search key ([#1824](https://github.com/NousResearch/hermes-agent/pull/1824) by @cutepawss), improve fuzzy matching accuracy + position calculation refactor ([#2096](https://github.com/NousResearch/hermes-agent/pull/2096), [#1681](https://github.com/NousResearch/hermes-agent/pull/1681))
- Code execution: resource leak and double socket close fix ([#2381](https://github.com/NousResearch/hermes-agent/pull/2381))
- Delegate: thread safety for concurrent subagent delegation ([#1672](https://github.com/NousResearch/hermes-agent/pull/1672)), preserve parent agent's tool list after delegation ([#1778](https://github.com/NousResearch/hermes-agent/pull/1778))
- Fix: make concurrent tool batching path-aware for file mutations ([#1914](https://github.com/NousResearch/hermes-agent/pull/1914))
- Fix: chunk long messages in `send_message_tool` before platform dispatch ([#1646](https://github.com/NousResearch/hermes-agent/pull/1646))
- Fix: add missing 'messaging' toolset ([#1718](https://github.com/NousResearch/hermes-agent/pull/1718))
- Fix: prevent unavailable tool names from leaking into model schemas ([#2072](https://github.com/NousResearch/hermes-agent/pull/2072))
- Fix: pass visited set by reference to prevent diamond dependency duplication ([#2311](https://github.com/NousResearch/hermes-agent/pull/2311))
- Fix: Daytona sandbox lookup migrated from `find_one` to `get/list` ([#2063](https://github.com/NousResearch/hermes-agent/pull/2063) by @rovle)

---

### 🧩 Skills Ecosystem

#### Skills System Improvements
- **Agent-created skills** — Caution-level findings allowed, dangerous skills ask instead of block ([#1840](https://github.com/NousResearch/hermes-agent/pull/1840), [#2446](https://github.com/NousResearch/hermes-agent/pull/2446))
- **`--yes` flag** to bypass confirmation in `/skills install` and uninstall ([#1647](https://github.com/NousResearch/hermes-agent/pull/1647))
- **Disabled skills respected** across banner, system prompt, and slash commands ([#1897](https://github.com/NousResearch/hermes-agent/pull/1897))
- Fix: skills custom_tools import crash + sandbox file_tools integration ([#2239](https://github.com/NousResearch/hermes-agent/pull/2239))
- Fix: agent-created skills with pip requirements crash on install ([#2145](https://github.com/NousResearch/hermes-agent/pull/2145))
- Fix: race condition in `Skills.__init__` when `hub.yaml` missing ([#2242](https://github.com/NousResearch/hermes-agent/pull/2242))
- Fix: validate skill metadata before install and block duplicates ([#2241](https://github.com/NousResearch/hermes-agent/pull/2241))
- Fix: skills hub inspect/resolve — 4 bugs in inspect, redirects, discovery, tap list ([#2447](https://github.com/NousResearch/hermes-agent/pull/2447))
- Fix: agent-created skills keep working after session reset ([#2121](https://github.com/NousResearch/hermes-agent/pull/2121))

#### New Skills
- **OCR-and-documents** — PDF/DOCX/XLS/PPTX/image OCR with optional GPU ([#2236](https://github.com/NousResearch/hermes-agent/pull/2236), [#2461](https://github.com/NousResearch/hermes-agent/pull/2461))
- **Huggingface-hub** bundled skill ([#1921](https://github.com/NousResearch/hermes-agent/pull/1921))
- **Sherlock OSINT** username search ([#1671](https://github.com/NousResearch/hermes-agent/pull/1671))
- **Meme-generation** — Image generator with Pillow ([#2344](https://github.com/NousResearch/hermes-agent/pull/2344))
- **Bioinformatics** gateway skill — index to 400+ bio skills ([#2387](https://github.com/NousResearch/hermes-agent/pull/2387))
- **Inference.sh** skill (terminal-based) ([#1686](https://github.com/NousResearch/hermes-agent/pull/1686))
- **Base blockchain** optional skill ([#1643](https://github.com/NousResearch/hermes-agent/pull/1643))
- **3D-model-viewer** optional skill ([#2226](https://github.com/NousResearch/hermes-agent/pull/2226))
- **FastMCP** optional skill ([#2113](https://github.com/NousResearch/hermes-agent/pull/2113))
- **Hermes-agent-setup** skill ([#1905](https://github.com/NousResearch/hermes-agent/pull/1905))

---

### 🔌 Plugin System Enhancements

- **TUI extension hooks** — Build custom CLIs on top of Hermes ([#2333](https://github.com/NousResearch/hermes-agent/pull/2333))
- **`hermes plugins install/remove/list`** commands ([#2337](https://github.com/NousResearch/hermes-agent/pull/2337))
- **Slash command registration** for plugins ([#2359](https://github.com/NousResearch/hermes-agent/pull/2359))
- **`session:end` lifecycle event** hook ([#1725](https://github.com/NousResearch/hermes-agent/pull/1725))
- Fix: require opt-in for project plugin discovery ([#2215](https://github.com/NousResearch/hermes-agent/pull/2215))

---

### 🔒 Security & Reliability

#### Security
- **SSRF protection** for vision_tools and web_tools ([#2679](https://github.com/NousResearch/hermes-agent/pull/2679))
- **Shell injection prevention** in `_expand_path` via `~user` path suffix ([#2685](https://github.com/NousResearch/hermes-agent/pull/2685))
- **Block untrusted browser-origin** API server access ([#2451](https://github.com/NousResearch/hermes-agent/pull/2451))
- **Block sandbox backend creds** from subprocess env ([#1658](https://github.com/NousResearch/hermes-agent/pull/1658))
- **Block @ references** from reading secrets outside workspace ([#2601](https://github.com/NousResearch/hermes-agent/pull/2601) by @Gutslabs)
- **Malicious code pattern pre-exec scanner** for terminal_tool ([#2245](https://github.com/NousResearch/hermes-agent/pull/2245))
- **Harden terminal safety** and sandbox file writes ([#1653](https://github.com/NousResearch/hermes-agent/pull/1653))
- **PKCE verifier leak** fix + OAuth refresh Content-Type ([#1775](https://github.com/NousResearch/hermes-agent/pull/1775))
- **Eliminate SQL string formatting** in `execute()` calls ([#2061](https://github.com/NousResearch/hermes-agent/pull/2061) by @dusterbloom)
- **Harden jobs API** — input limits, field whitelist, startup check ([#2456](https://github.com/NousResearch/hermes-agent/pull/2456))

#### Reliability
- Thread locks on 4 SessionDB methods ([#1704](https://github.com/NousResearch/hermes-agent/pull/1704))
- File locking for concurrent memory writes ([#1726](https://github.com/NousResearch/hermes-agent/pull/1726))
- Handle OpenRouter errors gracefully ([#2112](https://github.com/NousResearch/hermes-agent/pull/2112))
- Guard print() calls against OSError ([#1668](https://github.com/NousResearch/hermes-agent/pull/1668))
- Safely handle non-string inputs in redacting formatter ([#2392](https://github.com/NousResearch/hermes-agent/pull/2392), [#1700](https://github.com/NousResearch/hermes-agent/pull/1700))
- ACP: preserve session provider on model switch, persist sessions to disk ([#2380](https://github.com/NousResearch/hermes-agent/pull/2380), [#2071](https://github.com/NousResearch/hermes-agent/pull/2071))
- API server: persist ResponseStore to SQLite across restarts ([#2472](https://github.com/NousResearch/hermes-agent/pull/2472))
- Fix: `fetch_nous_models` always TypeError from positional args ([#1699](https://github.com/NousResearch/hermes-agent/pull/1699))
- Fix: resolve merge conflict markers in cli.py breaking startup ([#2347](https://github.com/NousResearch/hermes-agent/pull/2347))
- Fix: `minisweagent_path.py` missing from wheel ([#2098](https://github.com/NousResearch/hermes-agent/pull/2098) by @JiwaniZakir)

#### Cron System
- **`[SILENT]` response** — cron agents can suppress delivery ([#1833](https://github.com/NousResearch/hermes-agent/pull/1833))
- **Scale missed-job grace window** with schedule frequency ([#2449](https://github.com/NousResearch/hermes-agent/pull/2449))
- **Recover recent one-shot jobs** ([#1918](https://github.com/NousResearch/hermes-agent/pull/1918))
- Fix: normalize `repeat<=0` to None — jobs deleted after first run when LLM passes -1 ([#2612](https://github.com/NousResearch/hermes-agent/pull/2612) by @Mibayy)
- Fix: Matrix added to scheduler delivery platform_map ([#2167](https://github.com/NousResearch/hermes-agent/pull/2167) by @buntingszn)
- Fix: naive ISO timestamps without timezone — jobs fire at wrong time ([#1729](https://github.com/NousResearch/hermes-agent/pull/1729))
- Fix: `get_due_jobs` reads `jobs.json` twice — race condition ([#1716](https://github.com/NousResearch/hermes-agent/pull/1716))
- Fix: silent jobs return empty response for delivery skip ([#2442](https://github.com/NousResearch/hermes-agent/pull/2442))
- Fix: stop injecting cron outputs into gateway session history ([#2313](https://github.com/NousResearch/hermes-agent/pull/2313))
- Fix: close abandoned coroutine when `asyncio.run()` raises RuntimeError ([#2317](https://github.com/NousResearch/hermes-agent/pull/2317))

---

### 🧪 Testing

- Resolve all consistently failing tests ([#2488](https://github.com/NousResearch/hermes-agent/pull/2488))
- Replace `FakePath` with `monkeypatch` for Python 3.12 compat ([#2444](https://github.com/NousResearch/hermes-agent/pull/2444))
- Align Hermes setup and full-suite expectations ([#1710](https://github.com/NousResearch/hermes-agent/pull/1710))

---

### 📚 Documentation

- Comprehensive docs update for recent features ([#1693](https://github.com/NousResearch/hermes-agent/pull/1693), [#2183](https://github.com/NousResearch/hermes-agent/pull/2183))
- Alibaba Cloud and DingTalk setup guides ([#1687](https://github.com/NousResearch/hermes-agent/pull/1687), [#1692](https://github.com/NousResearch/hermes-agent/pull/1692))
- Detailed skills documentation ([#2244](https://github.com/NousResearch/hermes-agent/pull/2244))
- Honcho self-hosted / Docker configuration ([#2475](https://github.com/NousResearch/hermes-agent/pull/2475))
- Context length detection FAQ and quickstart references ([#2179](https://github.com/NousResearch/hermes-agent/pull/2179))
- Fix docs inconsistencies across reference and user guides ([#1995](https://github.com/NousResearch/hermes-agent/pull/1995))
- Fix MCP install commands — use uv, not bare pip ([#1909](https://github.com/NousResearch/hermes-agent/pull/1909))
- Replace ASCII diagrams with Mermaid/lists ([#2402](https://github.com/NousResearch/hermes-agent/pull/2402))
- Gemini OAuth provider implementation plan ([#2467](https://github.com/NousResearch/hermes-agent/pull/2467))
- Discord Server Members Intent marked as required ([#2330](https://github.com/NousResearch/hermes-agent/pull/2330))
- Fix MDX build error in api-server.md ([#1787](https://github.com/NousResearch/hermes-agent/pull/1787))
- Align venv path to match installer ([#2114](https://github.com/NousResearch/hermes-agent/pull/2114))
- New skills added to hub index ([#2281](https://github.com/NousResearch/hermes-agent/pull/2281))

---

### 👥 Contributors

#### Core
- **@teknium1** (Teknium) — 280 PRs

#### Community Contributors
- **@mchzimm** (to_the_max) — GitHub Copilot provider integration ([#1879](https://github.com/NousResearch/hermes-agent/pull/1879))
- **@jquesnelle** (Jeffrey Quesnelle) — Per-thread persistent event loops fix ([#2214](https://github.com/NousResearch/hermes-agent/pull/2214))
- **@llbn** (lbn) — Telegram MarkdownV2 strikethrough, spoiler, blockquotes, and escape fixes ([#2199](https://github.com/NousResearch/hermes-agent/pull/2199), [#2200](https://github.com/NousResearch/hermes-agent/pull/2200))
- **@dusterbloom** — SQL injection prevention + local server context window querying ([#2061](https://github.com/NousResearch/hermes-agent/pull/2061), [#2091](https://github.com/NousResearch/hermes-agent/pull/2091))
- **@0xbyt4** — Anthropic tool_calls None guard + OpenCode-Go provider config fix ([#2209](https://github.com/NousResearch/hermes-agent/pull/2209), [#2393](https://github.com/NousResearch/hermes-agent/pull/2393))
- **@sai-samarth** (Saisamarth) — WhatsApp send_message routing + systemd node path ([#1769](https://github.com/NousResearch/hermes-agent/pull/1769), [#1767](https://github.com/NousResearch/hermes-agent/pull/1767))
- **@Gutslabs** (Guts) — Block @ references from reading secrets ([#2601](https://github.com/NousResearch/hermes-agent/pull/2601))
- **@Mibayy** (Mibay) — Cron job repeat normalization ([#2612](https://github.com/NousResearch/hermes-agent/pull/2612))
- **@ten-jampa** (Tenzin Jampa) — Gateway /title command fix ([#2379](https://github.com/NousResearch/hermes-agent/pull/2379))
- **@cutepawss** (lila) — File tools search pagination fix ([#1824](https://github.com/NousResearch/hermes-agent/pull/1824))
- **@hanai** (Hanai) — OpenAI TTS base_url support ([#2064](https://github.com/NousResearch/hermes-agent/pull/2064))
- **@rovle** (Lovre Pešut) — Daytona sandbox API migration ([#2063](https://github.com/NousResearch/hermes-agent/pull/2063))
- **@buntingszn** (bunting szn) — Matrix cron delivery support ([#2167](https://github.com/NousResearch/hermes-agent/pull/2167))
- **@InB4DevOps** — Token counter reset on new session ([#2101](https://github.com/NousResearch/hermes-agent/pull/2101))
- **@JiwaniZakir** (Zakir Jiwani) — Missing file in wheel fix ([#2098](https://github.com/NousResearch/hermes-agent/pull/2098))
- **@ygd58** (buray) — Delegate tool parent tool names fix ([#2083](https://github.com/NousResearch/hermes-agent/pull/2083))

---

**Full Changelog**: [v2026.3.17...v2026.3.23](https://github.com/NousResearch/hermes-agent/compare/v2026.3.17...v2026.3.23)
---

<a id="v0-3-0"></a>

## Hermes Agent v0.3.0 (v2026.3.17)

**Release Date:** March 17, 2026

> The streaming, plugins, and provider release — unified real-time token delivery, first-class plugin architecture, rebuilt provider system with Vercel AI Gateway, native Anthropic provider, smart approvals, live Chrome CDP browser connect, ACP IDE integration, Honcho memory, voice mode, persistent shell, and 50+ bug fixes across every platform.

---

### ✨ Highlights

- **Unified Streaming Infrastructure** — Real-time token-by-token delivery in CLI and all gateway platforms. Responses stream as they're generated instead of arriving as a block. ([#1538](https://github.com/NousResearch/hermes-agent/pull/1538))

- **First-Class Plugin Architecture** — Drop Python files into `~/.hermes/plugins/` to extend Hermes with custom tools, commands, and hooks. No forking required. ([#1544](https://github.com/NousResearch/hermes-agent/pull/1544), [#1555](https://github.com/NousResearch/hermes-agent/pull/1555))

- **Native Anthropic Provider** — Direct Anthropic API calls with Claude Code credential auto-discovery, OAuth PKCE flows, and native prompt caching. No OpenRouter middleman needed. ([#1097](https://github.com/NousResearch/hermes-agent/pull/1097))

- **Smart Approvals + /stop Command** — Codex-inspired approval system that learns which commands are safe and remembers your preferences. `/stop` kills the current agent run immediately. ([#1543](https://github.com/NousResearch/hermes-agent/pull/1543))

- **Honcho Memory Integration** — Async memory writes, configurable recall modes, session title integration, and multi-user isolation in gateway mode. By @erosika. ([#736](https://github.com/NousResearch/hermes-agent/pull/736))

- **Voice Mode** — Push-to-talk in CLI, voice notes in Telegram/Discord, Discord voice channel support, and local Whisper transcription via faster-whisper. ([#1299](https://github.com/NousResearch/hermes-agent/pull/1299), [#1185](https://github.com/NousResearch/hermes-agent/pull/1185), [#1429](https://github.com/NousResearch/hermes-agent/pull/1429))

- **Concurrent Tool Execution** — Multiple independent tool calls now run in parallel via ThreadPoolExecutor, significantly reducing latency for multi-tool turns. ([#1152](https://github.com/NousResearch/hermes-agent/pull/1152))

- **PII Redaction** — When `privacy.redact_pii` is enabled, personally identifiable information is automatically scrubbed before sending context to LLM providers. ([#1542](https://github.com/NousResearch/hermes-agent/pull/1542))

- **`/browser connect` via CDP** — Attach browser tools to a live Chrome instance through Chrome DevTools Protocol. Debug, inspect, and interact with pages you already have open. ([#1549](https://github.com/NousResearch/hermes-agent/pull/1549))

- **Vercel AI Gateway Provider** — Route Hermes through Vercel's AI Gateway for access to their model catalog and infrastructure. ([#1628](https://github.com/NousResearch/hermes-agent/pull/1628))

- **Centralized Provider Router** — Rebuilt provider system with `call_llm` API, unified `/model` command, auto-detect provider on model switch, and direct endpoint overrides for auxiliary/delegation clients. ([#1003](https://github.com/NousResearch/hermes-agent/pull/1003), [#1506](https://github.com/NousResearch/hermes-agent/pull/1506), [#1375](https://github.com/NousResearch/hermes-agent/pull/1375))

- **ACP Server (IDE Integration)** — VS Code, Zed, and JetBrains can now connect to Hermes as an agent backend, with full slash command support. ([#1254](https://github.com/NousResearch/hermes-agent/pull/1254), [#1532](https://github.com/NousResearch/hermes-agent/pull/1532))

- **Persistent Shell Mode** — Local and SSH terminal backends can maintain shell state across tool calls — cd, env vars, and aliases persist. By @alt-glitch. ([#1067](https://github.com/NousResearch/hermes-agent/pull/1067), [#1483](https://github.com/NousResearch/hermes-agent/pull/1483))

- **Agentic On-Policy Distillation (OPD)** — New RL training environment for distilling agent policies, expanding the Atropos training ecosystem. ([#1149](https://github.com/NousResearch/hermes-agent/pull/1149))

---

### 🏗️ Core Agent & Architecture

#### Provider & Model Support
- **Centralized provider router** with `call_llm` API and unified `/model` command — switch models and providers seamlessly ([#1003](https://github.com/NousResearch/hermes-agent/pull/1003))
- **Vercel AI Gateway** provider support ([#1628](https://github.com/NousResearch/hermes-agent/pull/1628))
- **Auto-detect provider** when switching models via `/model` ([#1506](https://github.com/NousResearch/hermes-agent/pull/1506))
- **Direct endpoint overrides** for auxiliary and delegation clients — point vision/subagent calls at specific endpoints ([#1375](https://github.com/NousResearch/hermes-agent/pull/1375))
- **Native Anthropic auxiliary vision** — use Claude's native vision API instead of routing through OpenAI-compatible endpoints ([#1377](https://github.com/NousResearch/hermes-agent/pull/1377))
- Anthropic OAuth flow improvements — auto-run `claude setup-token`, reauthentication, PKCE state persistence, identity fingerprinting ([#1132](https://github.com/NousResearch/hermes-agent/pull/1132), [#1360](https://github.com/NousResearch/hermes-agent/pull/1360), [#1396](https://github.com/NousResearch/hermes-agent/pull/1396), [#1597](https://github.com/NousResearch/hermes-agent/pull/1597))
- Fix adaptive thinking without `budget_tokens` for Claude 4.6 models — by @ASRagab ([#1128](https://github.com/NousResearch/hermes-agent/pull/1128))
- Fix Anthropic cache markers through adapter — by @brandtcormorant ([#1216](https://github.com/NousResearch/hermes-agent/pull/1216))
- Retry Anthropic 429/529 errors and surface details to users — by @0xbyt4 ([#1585](https://github.com/NousResearch/hermes-agent/pull/1585))
- Fix Anthropic adapter max_tokens, fallback crash, proxy base_url — by @0xbyt4 ([#1121](https://github.com/NousResearch/hermes-agent/pull/1121))
- Fix DeepSeek V3 parser dropping multiple parallel tool calls — by @mr-emmett-one ([#1365](https://github.com/NousResearch/hermes-agent/pull/1365), [#1300](https://github.com/NousResearch/hermes-agent/pull/1300))
- Accept unlisted models with warning instead of rejecting ([#1047](https://github.com/NousResearch/hermes-agent/pull/1047), [#1102](https://github.com/NousResearch/hermes-agent/pull/1102))
- Skip reasoning params for unsupported OpenRouter models ([#1485](https://github.com/NousResearch/hermes-agent/pull/1485))
- MiniMax Anthropic API compatibility fix ([#1623](https://github.com/NousResearch/hermes-agent/pull/1623))
- Custom endpoint `/models` verification and `/v1` base URL suggestion ([#1480](https://github.com/NousResearch/hermes-agent/pull/1480))
- Resolve delegation providers from `custom_providers` config ([#1328](https://github.com/NousResearch/hermes-agent/pull/1328))
- Kimi model additions and User-Agent fix ([#1039](https://github.com/NousResearch/hermes-agent/pull/1039))
- Strip `call_id`/`response_item_id` for Mistral compatibility ([#1058](https://github.com/NousResearch/hermes-agent/pull/1058))

#### Agent Loop & Conversation
- **Anthropic Context Editing API** support ([#1147](https://github.com/NousResearch/hermes-agent/pull/1147))
- Improved context compaction handoff summaries — compressor now preserves more actionable state ([#1273](https://github.com/NousResearch/hermes-agent/pull/1273))
- Sync session_id after mid-run context compression ([#1160](https://github.com/NousResearch/hermes-agent/pull/1160))
- Session hygiene threshold tuned to 50% for more proactive compression ([#1096](https://github.com/NousResearch/hermes-agent/pull/1096), [#1161](https://github.com/NousResearch/hermes-agent/pull/1161))
- Include session ID in system prompt via `--pass-session-id` flag ([#1040](https://github.com/NousResearch/hermes-agent/pull/1040))
- Prevent closed OpenAI client reuse across retries ([#1391](https://github.com/NousResearch/hermes-agent/pull/1391))
- Sanitize chat payloads and provider precedence ([#1253](https://github.com/NousResearch/hermes-agent/pull/1253))
- Handle dict tool call arguments from Codex and local backends ([#1393](https://github.com/NousResearch/hermes-agent/pull/1393), [#1440](https://github.com/NousResearch/hermes-agent/pull/1440))

#### Memory & Sessions
- **Improve memory prioritization** — user preferences and corrections weighted above procedural knowledge ([#1548](https://github.com/NousResearch/hermes-agent/pull/1548))
- Tighter memory and session recall guidance in system prompts ([#1329](https://github.com/NousResearch/hermes-agent/pull/1329))
- Persist CLI token counts to session DB for `/insights` ([#1498](https://github.com/NousResearch/hermes-agent/pull/1498))
- Keep Honcho recall out of the cached system prefix ([#1201](https://github.com/NousResearch/hermes-agent/pull/1201))
- Correct `seed_ai_identity` to use `session.add_messages()` ([#1475](https://github.com/NousResearch/hermes-agent/pull/1475))
- Isolate Honcho session routing for multi-user gateway ([#1500](https://github.com/NousResearch/hermes-agent/pull/1500))

---

### 📱 Messaging Platforms (Gateway)

#### Gateway Core
- **System gateway service mode** — run as a system-level systemd service, not just user-level ([#1371](https://github.com/NousResearch/hermes-agent/pull/1371))
- **Gateway install scope prompts** — choose user vs system scope during setup ([#1374](https://github.com/NousResearch/hermes-agent/pull/1374))
- **Reasoning hot reload** — change reasoning settings without restarting the gateway ([#1275](https://github.com/NousResearch/hermes-agent/pull/1275))
- Default group sessions to per-user isolation — no more shared state across users in group chats ([#1495](https://github.com/NousResearch/hermes-agent/pull/1495), [#1417](https://github.com/NousResearch/hermes-agent/pull/1417))
- Harden gateway restart recovery ([#1310](https://github.com/NousResearch/hermes-agent/pull/1310))
- Cancel active runs during shutdown ([#1427](https://github.com/NousResearch/hermes-agent/pull/1427))
- SSL certificate auto-detection for NixOS and non-standard systems ([#1494](https://github.com/NousResearch/hermes-agent/pull/1494))
- Auto-detect D-Bus session bus for `systemctl --user` on headless servers ([#1601](https://github.com/NousResearch/hermes-agent/pull/1601))
- Auto-enable systemd linger during gateway install on headless servers ([#1334](https://github.com/NousResearch/hermes-agent/pull/1334))
- Fall back to module entrypoint when `hermes` is not on PATH ([#1355](https://github.com/NousResearch/hermes-agent/pull/1355))
- Fix dual gateways on macOS launchd after `hermes update` ([#1567](https://github.com/NousResearch/hermes-agent/pull/1567))
- Remove recursive ExecStop from systemd units ([#1530](https://github.com/NousResearch/hermes-agent/pull/1530))
- Prevent logging handler accumulation in gateway mode ([#1251](https://github.com/NousResearch/hermes-agent/pull/1251))
- Restart on retryable startup failures — by @jplew ([#1517](https://github.com/NousResearch/hermes-agent/pull/1517))
- Backfill model on gateway sessions after agent runs ([#1306](https://github.com/NousResearch/hermes-agent/pull/1306))
- PID-based gateway kill and deferred config write ([#1499](https://github.com/NousResearch/hermes-agent/pull/1499))

#### Telegram
- Buffer media groups to prevent self-interruption from photo bursts ([#1341](https://github.com/NousResearch/hermes-agent/pull/1341), [#1422](https://github.com/NousResearch/hermes-agent/pull/1422))
- Retry on transient TLS failures during connect and send ([#1535](https://github.com/NousResearch/hermes-agent/pull/1535))
- Harden polling conflict handling ([#1339](https://github.com/NousResearch/hermes-agent/pull/1339))
- Escape chunk indicators and inline code in MarkdownV2 ([#1478](https://github.com/NousResearch/hermes-agent/pull/1478), [#1626](https://github.com/NousResearch/hermes-agent/pull/1626))
- Check updater/app state before disconnect ([#1389](https://github.com/NousResearch/hermes-agent/pull/1389))

#### Discord
- `/thread` command with `auto_thread` config and media metadata fixes ([#1178](https://github.com/NousResearch/hermes-agent/pull/1178))
- Auto-thread on @mention, skip mention text in bot threads ([#1438](https://github.com/NousResearch/hermes-agent/pull/1438))
- Retry without reply reference for system messages ([#1385](https://github.com/NousResearch/hermes-agent/pull/1385))
- Preserve native document and video attachment support ([#1392](https://github.com/NousResearch/hermes-agent/pull/1392))
- Defer discord adapter annotations to avoid optional import crashes ([#1314](https://github.com/NousResearch/hermes-agent/pull/1314))

#### Slack
- Thread handling overhaul — progress messages, responses, and session isolation all respect threads ([#1103](https://github.com/NousResearch/hermes-agent/pull/1103))
- Formatting, reactions, user resolution, and command improvements ([#1106](https://github.com/NousResearch/hermes-agent/pull/1106))
- Fix MAX_MESSAGE_LENGTH 3900 → 39000 ([#1117](https://github.com/NousResearch/hermes-agent/pull/1117))
- File upload fallback preserves thread context — by @0xbyt4 ([#1122](https://github.com/NousResearch/hermes-agent/pull/1122))
- Improve setup guidance ([#1387](https://github.com/NousResearch/hermes-agent/pull/1387))

#### Email
- Fix IMAP UID tracking and SMTP TLS verification ([#1305](https://github.com/NousResearch/hermes-agent/pull/1305))
- Add `skip_attachments` option via config.yaml ([#1536](https://github.com/NousResearch/hermes-agent/pull/1536))

#### Home Assistant
- Event filtering closed by default ([#1169](https://github.com/NousResearch/hermes-agent/pull/1169))

---

### 🖥️ CLI & User Experience

#### Interactive CLI
- **Persistent CLI status bar** — always-visible model, provider, and token counts ([#1522](https://github.com/NousResearch/hermes-agent/pull/1522))
- **File path autocomplete** in the input prompt ([#1545](https://github.com/NousResearch/hermes-agent/pull/1545))
- **`/plan` command** — generate implementation plans from specs ([#1372](https://github.com/NousResearch/hermes-agent/pull/1372), [#1381](https://github.com/NousResearch/hermes-agent/pull/1381))
- **Major `/rollback` improvements** — richer checkpoint history, clearer UX ([#1505](https://github.com/NousResearch/hermes-agent/pull/1505))
- **Preload CLI skills on launch** — skills are ready before the first prompt ([#1359](https://github.com/NousResearch/hermes-agent/pull/1359))
- **Centralized slash command registry** — all commands defined once, consumed everywhere ([#1603](https://github.com/NousResearch/hermes-agent/pull/1603))
- `/bg` alias for `/background` ([#1590](https://github.com/NousResearch/hermes-agent/pull/1590))
- Prefix matching for slash commands — `/mod` resolves to `/model` ([#1320](https://github.com/NousResearch/hermes-agent/pull/1320))
- `/new`, `/reset`, `/clear` now start genuinely fresh sessions ([#1237](https://github.com/NousResearch/hermes-agent/pull/1237))
- Accept session ID prefixes for session actions ([#1425](https://github.com/NousResearch/hermes-agent/pull/1425))
- TUI prompt and accent output now respect active skin ([#1282](https://github.com/NousResearch/hermes-agent/pull/1282))
- Centralize tool emoji metadata in registry + skin integration ([#1484](https://github.com/NousResearch/hermes-agent/pull/1484))
- "View full command" option added to dangerous command approval — by @teknium1 based on design by community ([#887](https://github.com/NousResearch/hermes-agent/pull/887))
- Non-blocking startup update check and banner deduplication ([#1386](https://github.com/NousResearch/hermes-agent/pull/1386))
- `/reasoning` command output ordering and inline think extraction fixes ([#1031](https://github.com/NousResearch/hermes-agent/pull/1031))
- Verbose mode shows full untruncated output ([#1472](https://github.com/NousResearch/hermes-agent/pull/1472))
- Fix `/status` to report live state and tokens ([#1476](https://github.com/NousResearch/hermes-agent/pull/1476))
- Seed a default global SOUL.md ([#1311](https://github.com/NousResearch/hermes-agent/pull/1311))

#### Setup & Configuration
- **OpenClaw migration** during first-time setup — by @kshitijk4poor ([#981](https://github.com/NousResearch/hermes-agent/pull/981))
- `hermes claw migrate` command + migration docs ([#1059](https://github.com/NousResearch/hermes-agent/pull/1059))
- Smart vision setup that respects the user's chosen provider ([#1323](https://github.com/NousResearch/hermes-agent/pull/1323))
- Handle headless setup flows end-to-end ([#1274](https://github.com/NousResearch/hermes-agent/pull/1274))
- Prefer curses over `simple_term_menu` in setup.py ([#1487](https://github.com/NousResearch/hermes-agent/pull/1487))
- Show effective model and provider in `/status` ([#1284](https://github.com/NousResearch/hermes-agent/pull/1284))
- Config set examples use placeholder syntax ([#1322](https://github.com/NousResearch/hermes-agent/pull/1322))
- Reload .env over stale shell overrides ([#1434](https://github.com/NousResearch/hermes-agent/pull/1434))
- Fix is_coding_plan NameError crash — by @0xbyt4 ([#1123](https://github.com/NousResearch/hermes-agent/pull/1123))
- Add missing packages to setuptools config — by @alt-glitch ([#912](https://github.com/NousResearch/hermes-agent/pull/912))
- Installer: clarify why sudo is needed at every prompt ([#1602](https://github.com/NousResearch/hermes-agent/pull/1602))

---

### 🔧 Tool System

#### Terminal & Execution
- **Persistent shell mode** for local and SSH backends — maintain shell state across tool calls — by @alt-glitch ([#1067](https://github.com/NousResearch/hermes-agent/pull/1067), [#1483](https://github.com/NousResearch/hermes-agent/pull/1483))
- **Tirith pre-exec command scanning** — security layer that analyzes commands before execution ([#1256](https://github.com/NousResearch/hermes-agent/pull/1256))
- Strip Hermes provider env vars from all subprocess environments ([#1157](https://github.com/NousResearch/hermes-agent/pull/1157), [#1172](https://github.com/NousResearch/hermes-agent/pull/1172), [#1399](https://github.com/NousResearch/hermes-agent/pull/1399), [#1419](https://github.com/NousResearch/hermes-agent/pull/1419)) — initial fix by @eren-karakus0
- SSH preflight check ([#1486](https://github.com/NousResearch/hermes-agent/pull/1486))
- Docker backend: make cwd workspace mount explicit opt-in ([#1534](https://github.com/NousResearch/hermes-agent/pull/1534))
- Add project root to PYTHONPATH in execute_code sandbox ([#1383](https://github.com/NousResearch/hermes-agent/pull/1383))
- Eliminate execute_code progress spam on gateway platforms ([#1098](https://github.com/NousResearch/hermes-agent/pull/1098))
- Clearer docker backend preflight errors ([#1276](https://github.com/NousResearch/hermes-agent/pull/1276))

#### Browser
- **`/browser connect`** — attach browser tools to a live Chrome instance via CDP ([#1549](https://github.com/NousResearch/hermes-agent/pull/1549))
- Improve browser cleanup, local browser PATH setup, and screenshot recovery ([#1333](https://github.com/NousResearch/hermes-agent/pull/1333))

#### MCP
- **Selective tool loading** with utility policies — filter which MCP tools are available ([#1302](https://github.com/NousResearch/hermes-agent/pull/1302))
- Auto-reload MCP tools when `mcp_servers` config changes without restart ([#1474](https://github.com/NousResearch/hermes-agent/pull/1474))
- Resolve npx stdio connection failures ([#1291](https://github.com/NousResearch/hermes-agent/pull/1291))
- Preserve MCP toolsets when saving platform tool config ([#1421](https://github.com/NousResearch/hermes-agent/pull/1421))

#### Vision
- Unify vision backend gating ([#1367](https://github.com/NousResearch/hermes-agent/pull/1367))
- Surface actual error reason instead of generic message ([#1338](https://github.com/NousResearch/hermes-agent/pull/1338))
- Make Claude image handling work end-to-end ([#1408](https://github.com/NousResearch/hermes-agent/pull/1408))

#### Cron
- **Compress cron management into one tool** — single `cronjob` tool replaces multiple commands ([#1343](https://github.com/NousResearch/hermes-agent/pull/1343))
- Suppress duplicate cron sends to auto-delivery targets ([#1357](https://github.com/NousResearch/hermes-agent/pull/1357))
- Persist cron sessions to SQLite ([#1255](https://github.com/NousResearch/hermes-agent/pull/1255))
- Per-job runtime overrides (provider, model, base_url) ([#1398](https://github.com/NousResearch/hermes-agent/pull/1398))
- Atomic write in `save_job_output` to prevent data loss on crash ([#1173](https://github.com/NousResearch/hermes-agent/pull/1173))
- Preserve thread context for `deliver=origin` ([#1437](https://github.com/NousResearch/hermes-agent/pull/1437))

#### Patch Tool
- Avoid corrupting pipe chars in V4A patch apply ([#1286](https://github.com/NousResearch/hermes-agent/pull/1286))
- Permissive `block_anchor` thresholds and unicode normalization ([#1539](https://github.com/NousResearch/hermes-agent/pull/1539))

#### Delegation
- Add observability metadata to subagent results (model, tokens, duration, tool trace) ([#1175](https://github.com/NousResearch/hermes-agent/pull/1175))

---

### 🧩 Skills Ecosystem

#### Skills System
- **Integrate skills.sh** as a hub source alongside ClawHub ([#1303](https://github.com/NousResearch/hermes-agent/pull/1303))
- Secure skill env setup on load ([#1153](https://github.com/NousResearch/hermes-agent/pull/1153))
- Honor policy table for dangerous verdicts ([#1330](https://github.com/NousResearch/hermes-agent/pull/1330))
- Harden ClawHub skill search exact matches ([#1400](https://github.com/NousResearch/hermes-agent/pull/1400))
- Fix ClawHub skill install — use `/download` ZIP endpoint ([#1060](https://github.com/NousResearch/hermes-agent/pull/1060))
- Avoid mislabeling local skills as builtin — by @arceus77-7 ([#862](https://github.com/NousResearch/hermes-agent/pull/862))

#### New Skills
- **Linear** project management ([#1230](https://github.com/NousResearch/hermes-agent/pull/1230))
- **X/Twitter** via x-cli ([#1285](https://github.com/NousResearch/hermes-agent/pull/1285))
- **Telephony** — Twilio, SMS, and AI calls ([#1289](https://github.com/NousResearch/hermes-agent/pull/1289))
- **1Password** — by @arceus77-7 ([#883](https://github.com/NousResearch/hermes-agent/pull/883), [#1179](https://github.com/NousResearch/hermes-agent/pull/1179))
- **NeuroSkill BCI** integration ([#1135](https://github.com/NousResearch/hermes-agent/pull/1135))
- **Blender MCP** for 3D modeling ([#1531](https://github.com/NousResearch/hermes-agent/pull/1531))
- **OSS Security Forensics** ([#1482](https://github.com/NousResearch/hermes-agent/pull/1482))
- **Parallel CLI** research skill ([#1301](https://github.com/NousResearch/hermes-agent/pull/1301))
- **OpenCode** CLI skill ([#1174](https://github.com/NousResearch/hermes-agent/pull/1174))
- **ASCII Video** skill refactored — by @SHL0MS ([#1213](https://github.com/NousResearch/hermes-agent/pull/1213), [#1598](https://github.com/NousResearch/hermes-agent/pull/1598))

---

### 🎙️ Voice Mode

- Voice mode foundation — push-to-talk CLI, Telegram/Discord voice notes ([#1299](https://github.com/NousResearch/hermes-agent/pull/1299))
- Free local Whisper transcription via faster-whisper ([#1185](https://github.com/NousResearch/hermes-agent/pull/1185))
- Discord voice channel reliability fixes ([#1429](https://github.com/NousResearch/hermes-agent/pull/1429))
- Restore local STT fallback for gateway voice notes ([#1490](https://github.com/NousResearch/hermes-agent/pull/1490))
- Honor `stt.enabled: false` across gateway transcription ([#1394](https://github.com/NousResearch/hermes-agent/pull/1394))
- Fix bogus incapability message on Telegram voice notes (Issue [#1033](https://github.com/NousResearch/hermes-agent/issues/1033))

---

### 🔌 ACP (IDE Integration)

- Restore ACP server implementation ([#1254](https://github.com/NousResearch/hermes-agent/pull/1254))
- Support slash commands in ACP adapter ([#1532](https://github.com/NousResearch/hermes-agent/pull/1532))

---

### 🧪 RL Training

- **Agentic On-Policy Distillation (OPD)** environment — new RL training environment for agent policy distillation ([#1149](https://github.com/NousResearch/hermes-agent/pull/1149))
- Make tinker-atropos RL training fully optional ([#1062](https://github.com/NousResearch/hermes-agent/pull/1062))

---

### 🔒 Security & Reliability

#### Security Hardening
- **Tirith pre-exec command scanning** — static analysis of terminal commands before execution ([#1256](https://github.com/NousResearch/hermes-agent/pull/1256))
- **PII redaction** when `privacy.redact_pii` is enabled ([#1542](https://github.com/NousResearch/hermes-agent/pull/1542))
- Strip Hermes provider/gateway/tool env vars from all subprocess environments ([#1157](https://github.com/NousResearch/hermes-agent/pull/1157), [#1172](https://github.com/NousResearch/hermes-agent/pull/1172), [#1399](https://github.com/NousResearch/hermes-agent/pull/1399), [#1419](https://github.com/NousResearch/hermes-agent/pull/1419))
- Docker cwd workspace mount now explicit opt-in — never auto-mount host directories ([#1534](https://github.com/NousResearch/hermes-agent/pull/1534))
- Escape parens and braces in fork bomb regex pattern ([#1397](https://github.com/NousResearch/hermes-agent/pull/1397))
- Harden `.worktreeinclude` path containment ([#1388](https://github.com/NousResearch/hermes-agent/pull/1388))
- Use description as `pattern_key` to prevent approval collisions ([#1395](https://github.com/NousResearch/hermes-agent/pull/1395))

#### Reliability
- Guard init-time stdio writes ([#1271](https://github.com/NousResearch/hermes-agent/pull/1271))
- Session log writes reuse shared atomic JSON helper ([#1280](https://github.com/NousResearch/hermes-agent/pull/1280))
- Atomic temp cleanup protected on interrupts ([#1401](https://github.com/NousResearch/hermes-agent/pull/1401))

---

### 🐛 Notable Bug Fixes

- **`/status` always showing 0 tokens** — now reports live state (Issue [#1465](https://github.com/NousResearch/hermes-agent/issues/1465), [#1476](https://github.com/NousResearch/hermes-agent/pull/1476))
- **Custom model endpoints not working** — restored config-saved endpoint resolution (Issue [#1460](https://github.com/NousResearch/hermes-agent/issues/1460), [#1373](https://github.com/NousResearch/hermes-agent/pull/1373))
- **MCP tools not visible until restart** — auto-reload on config change (Issue [#1036](https://github.com/NousResearch/hermes-agent/issues/1036), [#1474](https://github.com/NousResearch/hermes-agent/pull/1474))
- **`hermes tools` removing MCP tools** — preserve MCP toolsets when saving (Issue [#1247](https://github.com/NousResearch/hermes-agent/issues/1247), [#1421](https://github.com/NousResearch/hermes-agent/pull/1421))
- **Terminal subprocesses inheriting `OPENAI_BASE_URL`** breaking external tools (Issue [#1002](https://github.com/NousResearch/hermes-agent/issues/1002), [#1399](https://github.com/NousResearch/hermes-agent/pull/1399))
- **Background process lost on gateway restart** — improved recovery (Issue [#1144](https://github.com/NousResearch/hermes-agent/issues/1144))
- **Cron jobs not persisting state** — now stored in SQLite (Issue [#1416](https://github.com/NousResearch/hermes-agent/issues/1416), [#1255](https://github.com/NousResearch/hermes-agent/pull/1255))
- **Cronjob `deliver: origin` not preserving thread context** (Issue [#1219](https://github.com/NousResearch/hermes-agent/issues/1219), [#1437](https://github.com/NousResearch/hermes-agent/pull/1437))
- **Gateway systemd service failing to auto-restart** when browser processes orphaned (Issue [#1617](https://github.com/NousResearch/hermes-agent/issues/1617))
- **`/background` completion report cut off in Telegram** (Issue [#1443](https://github.com/NousResearch/hermes-agent/issues/1443))
- **Model switching not taking effect** (Issue [#1244](https://github.com/NousResearch/hermes-agent/issues/1244), [#1183](https://github.com/NousResearch/hermes-agent/pull/1183))
- **`hermes doctor` reporting cronjob as unavailable** (Issue [#878](https://github.com/NousResearch/hermes-agent/issues/878), [#1180](https://github.com/NousResearch/hermes-agent/pull/1180))
- **WhatsApp bridge messages not received** from mobile (Issue [#1142](https://github.com/NousResearch/hermes-agent/issues/1142))
- **Setup wizard hanging on headless SSH** (Issue [#905](https://github.com/NousResearch/hermes-agent/issues/905), [#1274](https://github.com/NousResearch/hermes-agent/pull/1274))
- **Log handler accumulation** degrading gateway performance (Issue [#990](https://github.com/NousResearch/hermes-agent/issues/990), [#1251](https://github.com/NousResearch/hermes-agent/pull/1251))
- **Gateway NULL model in DB** (Issue [#987](https://github.com/NousResearch/hermes-agent/issues/987), [#1306](https://github.com/NousResearch/hermes-agent/pull/1306))
- **Strict endpoints rejecting replayed tool_calls** (Issue [#893](https://github.com/NousResearch/hermes-agent/issues/893))
- **Remaining hardcoded `~/.hermes` paths** — all now respect `HERMES_HOME` (Issue [#892](https://github.com/NousResearch/hermes-agent/issues/892), [#1233](https://github.com/NousResearch/hermes-agent/pull/1233))
- **Delegate tool not working with custom inference providers** (Issue [#1011](https://github.com/NousResearch/hermes-agent/issues/1011), [#1328](https://github.com/NousResearch/hermes-agent/pull/1328))
- **Skills Guard blocking official skills** (Issue [#1006](https://github.com/NousResearch/hermes-agent/issues/1006), [#1330](https://github.com/NousResearch/hermes-agent/pull/1330))
- **Setup writing provider before model selection** (Issue [#1182](https://github.com/NousResearch/hermes-agent/issues/1182))
- **`GatewayConfig.get()` AttributeError** crashing all message handling (Issue [#1158](https://github.com/NousResearch/hermes-agent/issues/1158), [#1287](https://github.com/NousResearch/hermes-agent/pull/1287))
- **`/update` hard-failing with "command not found"** (Issue [#1049](https://github.com/NousResearch/hermes-agent/issues/1049))
- **Image analysis failing silently** (Issue [#1034](https://github.com/NousResearch/hermes-agent/issues/1034), [#1338](https://github.com/NousResearch/hermes-agent/pull/1338))
- **API `BadRequestError` from `'dict'` object has no attribute `'strip'`** (Issue [#1071](https://github.com/NousResearch/hermes-agent/issues/1071))
- **Slash commands requiring exact full name** — now uses prefix matching (Issue [#928](https://github.com/NousResearch/hermes-agent/issues/928), [#1320](https://github.com/NousResearch/hermes-agent/pull/1320))
- **Gateway stops responding when terminal is closed on headless** (Issue [#1005](https://github.com/NousResearch/hermes-agent/issues/1005))

---

### 🧪 Testing

- Cover empty cached Anthropic tool-call turns ([#1222](https://github.com/NousResearch/hermes-agent/pull/1222))
- Fix stale CI assumptions in parser and quick-command coverage ([#1236](https://github.com/NousResearch/hermes-agent/pull/1236))
- Fix gateway async tests without implicit event loop ([#1278](https://github.com/NousResearch/hermes-agent/pull/1278))
- Make gateway async tests xdist-safe ([#1281](https://github.com/NousResearch/hermes-agent/pull/1281))
- Cross-timezone naive timestamp regression for cron ([#1319](https://github.com/NousResearch/hermes-agent/pull/1319))
- Isolate codex provider tests from local env ([#1335](https://github.com/NousResearch/hermes-agent/pull/1335))
- Lock retry replacement semantics ([#1379](https://github.com/NousResearch/hermes-agent/pull/1379))
- Improve error logging in session search tool — by @aydnOktay ([#1533](https://github.com/NousResearch/hermes-agent/pull/1533))

---

### 📚 Documentation

- Comprehensive SOUL.md guide ([#1315](https://github.com/NousResearch/hermes-agent/pull/1315))
- Voice mode documentation ([#1316](https://github.com/NousResearch/hermes-agent/pull/1316), [#1362](https://github.com/NousResearch/hermes-agent/pull/1362))
- Provider contribution guide ([#1361](https://github.com/NousResearch/hermes-agent/pull/1361))
- ACP and internal systems implementation guides ([#1259](https://github.com/NousResearch/hermes-agent/pull/1259))
- Expand Docusaurus coverage across CLI, tools, skills, and skins ([#1232](https://github.com/NousResearch/hermes-agent/pull/1232))
- Terminal backend and Windows troubleshooting ([#1297](https://github.com/NousResearch/hermes-agent/pull/1297))
- Skills hub reference section ([#1317](https://github.com/NousResearch/hermes-agent/pull/1317))
- Checkpoint, /rollback, and git worktrees guide ([#1493](https://github.com/NousResearch/hermes-agent/pull/1493), [#1524](https://github.com/NousResearch/hermes-agent/pull/1524))
- CLI status bar and /usage reference ([#1523](https://github.com/NousResearch/hermes-agent/pull/1523))
- Fallback providers + /background command docs ([#1430](https://github.com/NousResearch/hermes-agent/pull/1430))
- Gateway service scopes docs ([#1378](https://github.com/NousResearch/hermes-agent/pull/1378))
- Slack thread reply behavior docs ([#1407](https://github.com/NousResearch/hermes-agent/pull/1407))
- Redesigned landing page with Nous blue palette — by @austinpickett ([#974](https://github.com/NousResearch/hermes-agent/pull/974))
- Fix several documentation typos — by @JackTheGit ([#953](https://github.com/NousResearch/hermes-agent/pull/953))
- Stabilize website diagrams ([#1405](https://github.com/NousResearch/hermes-agent/pull/1405))
- CLI vs messaging quick reference in README ([#1491](https://github.com/NousResearch/hermes-agent/pull/1491))
- Add search to Docusaurus ([#1053](https://github.com/NousResearch/hermes-agent/pull/1053))
- Home Assistant integration docs ([#1170](https://github.com/NousResearch/hermes-agent/pull/1170))

---

### 👥 Contributors

#### Core
- **@teknium1** — 220+ PRs spanning every area of the codebase

#### Top Community Contributors

- **@0xbyt4** (4 PRs) — Anthropic adapter fixes (max_tokens, fallback crash, 429/529 retry), Slack file upload thread context, setup NameError fix
- **@erosika** (1 PR) — Honcho memory integration: async writes, memory modes, session title integration
- **@SHL0MS** (2 PRs) — ASCII video skill design patterns and refactoring
- **@alt-glitch** (2 PRs) — Persistent shell mode for local/SSH backends, setuptools packaging fix
- **@arceus77-7** (2 PRs) — 1Password skill, fix skills list mislabeling
- **@kshitijk4poor** (1 PR) — OpenClaw migration during setup wizard
- **@ASRagab** (1 PR) — Fix adaptive thinking for Claude 4.6 models
- **@eren-karakus0** (1 PR) — Strip Hermes provider env vars from subprocess environment
- **@mr-emmett-one** (1 PR) — Fix DeepSeek V3 parser multi-tool call support
- **@jplew** (1 PR) — Gateway restart on retryable startup failures
- **@brandtcormorant** (1 PR) — Fix Anthropic cache control for empty text blocks
- **@aydnOktay** (1 PR) — Improve error logging in session search tool
- **@austinpickett** (1 PR) — Landing page redesign with Nous blue palette
- **@JackTheGit** (1 PR) — Documentation typo fixes

#### All Contributors

@0xbyt4, @alt-glitch, @arceus77-7, @ASRagab, @austinpickett, @aydnOktay, @brandtcormorant, @eren-karakus0, @erosika, @JackTheGit, @jplew, @kshitijk4poor, @mr-emmett-one, @SHL0MS, @teknium1

---

**Full Changelog**: [v2026.3.12...v2026.3.17](https://github.com/NousResearch/hermes-agent/compare/v2026.3.12...v2026.3.17)
---

<a id="v0-2-0"></a>

## Hermes Agent v0.2.0 (v2026.3.12)

**Release Date:** March 12, 2026

> First tagged release since v0.1.0 (the initial pre-public foundation). In just over two weeks, Hermes Agent went from a small internal project to a full-featured AI agent platform — thanks to an explosion of community contributions. This release covers **216 merged pull requests** from **63 contributors**, resolving **119 issues**.

---

### ✨ Highlights

- **Multi-Platform Messaging Gateway** — Telegram, Discord, Slack, WhatsApp, Signal, Email (IMAP/SMTP), and Home Assistant platforms with unified session management, media attachments, and per-platform tool configuration.

- **MCP (Model Context Protocol) Client** — Native MCP support with stdio and HTTP transports, reconnection, resource/prompt discovery, and sampling (server-initiated LLM requests). ([#291](https://github.com/NousResearch/hermes-agent/pull/291) — @0xbyt4, [#301](https://github.com/NousResearch/hermes-agent/pull/301), [#753](https://github.com/NousResearch/hermes-agent/pull/753))

- **Skills Ecosystem** — 70+ bundled and optional skills across 15+ categories with a Skills Hub for community discovery, per-platform enable/disable, conditional activation based on tool availability, and prerequisite validation. ([#743](https://github.com/NousResearch/hermes-agent/pull/743) — @teyrebaz33, [#785](https://github.com/NousResearch/hermes-agent/pull/785) — @teyrebaz33)

- **Centralized Provider Router** — Unified `call_llm()`/`async_call_llm()` API replaces scattered provider logic across vision, summarization, compression, and trajectory saving. All auxiliary consumers route through a single code path with automatic credential resolution. ([#1003](https://github.com/NousResearch/hermes-agent/pull/1003))

- **ACP Server** — VS Code, Zed, and JetBrains editor integration via the Agent Communication Protocol standard. ([#949](https://github.com/NousResearch/hermes-agent/pull/949))

- **CLI Skin/Theme Engine** — Data-driven visual customization: banners, spinners, colors, branding. 7 built-in skins + custom YAML skins.

- **Git Worktree Isolation** — `hermes -w` launches isolated agent sessions in git worktrees for safe parallel work on the same repo. ([#654](https://github.com/NousResearch/hermes-agent/pull/654))

- **Filesystem Checkpoints & Rollback** — Automatic snapshots before destructive operations with `/rollback` to restore. ([#824](https://github.com/NousResearch/hermes-agent/pull/824))

- **3,289 Tests** — From near-zero test coverage to a comprehensive test suite covering agent, gateway, tools, cron, and CLI.

---

### 🏗️ Core Agent & Architecture

#### Provider & Model Support
- Centralized provider router with `resolve_provider_client()` + `call_llm()` API ([#1003](https://github.com/NousResearch/hermes-agent/pull/1003))
- Nous Portal as first-class provider in setup ([#644](https://github.com/NousResearch/hermes-agent/issues/644))
- OpenAI Codex (Responses API) with ChatGPT subscription support ([#43](https://github.com/NousResearch/hermes-agent/pull/43)) — @grp06
- Codex OAuth vision support + multimodal content adapter
- Validate `/model` against live API instead of hardcoded lists
- Self-hosted Firecrawl support ([#460](https://github.com/NousResearch/hermes-agent/pull/460)) — @caentzminger
- Kimi Code API support ([#635](https://github.com/NousResearch/hermes-agent/pull/635)) — @christomitov
- MiniMax model ID update ([#473](https://github.com/NousResearch/hermes-agent/pull/473)) — @tars90percent
- OpenRouter provider routing configuration (provider_preferences)
- Nous credential refresh on 401 errors ([#571](https://github.com/NousResearch/hermes-agent/pull/571), [#269](https://github.com/NousResearch/hermes-agent/pull/269)) — @rewbs
- z.ai/GLM, Kimi/Moonshot, MiniMax, Azure OpenAI as first-class providers
- Unified `/model` and `/provider` into single view

#### Agent Loop & Conversation
- Simple fallback model for provider resilience ([#740](https://github.com/NousResearch/hermes-agent/pull/740))
- Shared iteration budget across parent + subagent delegation
- Iteration budget pressure via tool result injection
- Configurable subagent provider/model with full credential resolution
- Handle 413 payload-too-large via compression instead of aborting ([#153](https://github.com/NousResearch/hermes-agent/pull/153)) — @tekelala
- Retry with rebuilt payload after compression ([#616](https://github.com/NousResearch/hermes-agent/pull/616)) — @tripledoublev
- Auto-compress pathologically large gateway sessions ([#628](https://github.com/NousResearch/hermes-agent/issues/628))
- Tool call repair middleware — auto-lowercase and invalid tool handler
- Reasoning effort configuration and `/reasoning` command ([#921](https://github.com/NousResearch/hermes-agent/pull/921))
- Detect and block file re-read/search loops after context compression ([#705](https://github.com/NousResearch/hermes-agent/pull/705)) — @0xbyt4

#### Session & Memory
- Session naming with unique titles, auto-lineage, rich listing, and resume by name ([#720](https://github.com/NousResearch/hermes-agent/pull/720))
- Interactive session browser with search filtering ([#733](https://github.com/NousResearch/hermes-agent/pull/733))
- Display previous messages when resuming a session ([#734](https://github.com/NousResearch/hermes-agent/pull/734))
- Honcho AI-native cross-session user modeling ([#38](https://github.com/NousResearch/hermes-agent/pull/38)) — @erosika
- Proactive async memory flush on session expiry
- Smart context length probing with persistent caching + banner display
- `/resume` command for switching to named sessions in gateway
- Session reset policy for messaging platforms

---

### 📱 Messaging Platforms (Gateway)

#### Telegram
- Native file attachments: send_document + send_video
- Document file processing for PDF, text, and Office files — @tekelala
- Forum topic session isolation ([#766](https://github.com/NousResearch/hermes-agent/pull/766)) — @spanishflu-est1918
- Browser screenshot sharing via MEDIA: protocol ([#657](https://github.com/NousResearch/hermes-agent/pull/657))
- Location support for find-nearby skill
- TTS voice message accumulation fix ([#176](https://github.com/NousResearch/hermes-agent/pull/176)) — @Bartok9
- Improved error handling and logging ([#763](https://github.com/NousResearch/hermes-agent/pull/763)) — @aydnOktay
- Italic regex newline fix + 43 format tests ([#204](https://github.com/NousResearch/hermes-agent/pull/204)) — @0xbyt4

#### Discord
- Channel topic included in session context ([#248](https://github.com/NousResearch/hermes-agent/pull/248)) — @Bartok9
- DISCORD_ALLOW_BOTS config for bot message filtering ([#758](https://github.com/NousResearch/hermes-agent/pull/758))
- Document and video support ([#784](https://github.com/NousResearch/hermes-agent/pull/784))
- Improved error handling and logging ([#761](https://github.com/NousResearch/hermes-agent/pull/761)) — @aydnOktay

#### Slack
- App_mention 404 fix + document/video support ([#784](https://github.com/NousResearch/hermes-agent/pull/784))
- Structured logging replacing print statements — @aydnOktay

#### WhatsApp
- Native media sending — images, videos, documents ([#292](https://github.com/NousResearch/hermes-agent/pull/292)) — @satelerd
- Multi-user session isolation ([#75](https://github.com/NousResearch/hermes-agent/pull/75)) — @satelerd
- Cross-platform port cleanup replacing Linux-only fuser ([#433](https://github.com/NousResearch/hermes-agent/pull/433)) — @Farukest
- DM interrupt key mismatch fix ([#350](https://github.com/NousResearch/hermes-agent/pull/350)) — @Farukest

#### Signal
- Full Signal messenger gateway via signal-cli-rest-api ([#405](https://github.com/NousResearch/hermes-agent/issues/405))
- Media URL support in message events ([#871](https://github.com/NousResearch/hermes-agent/pull/871))

#### Email (IMAP/SMTP)
- New email gateway platform — @0xbyt4

#### Home Assistant
- REST tools + WebSocket gateway integration ([#184](https://github.com/NousResearch/hermes-agent/pull/184)) — @0xbyt4
- Service discovery and enhanced setup
- Toolset mapping fix ([#538](https://github.com/NousResearch/hermes-agent/pull/538)) — @Himess

#### Gateway Core
- Expose subagent tool calls and thinking to users ([#186](https://github.com/NousResearch/hermes-agent/pull/186)) — @cutepawss
- Configurable background process watcher notifications ([#840](https://github.com/NousResearch/hermes-agent/pull/840))
- `edit_message()` for Telegram/Discord/Slack with fallback
- `/compress`, `/usage`, `/update` slash commands
- Eliminated 3x SQLite message duplication in gateway sessions ([#873](https://github.com/NousResearch/hermes-agent/pull/873))
- Stabilize system prompt across gateway turns for cache hits ([#754](https://github.com/NousResearch/hermes-agent/pull/754))
- MCP server shutdown on gateway exit ([#796](https://github.com/NousResearch/hermes-agent/pull/796)) — @0xbyt4
- Pass session_db to AIAgent, fixing session_search error ([#108](https://github.com/NousResearch/hermes-agent/pull/108)) — @Bartok9
- Persist transcript changes in /retry, /undo; fix /reset attribute ([#217](https://github.com/NousResearch/hermes-agent/pull/217)) — @Farukest
- UTF-8 encoding fix preventing Windows crashes ([#369](https://github.com/NousResearch/hermes-agent/pull/369)) — @ch3ronsa

---

### 🖥️ CLI & User Experience

#### Interactive CLI
- Data-driven skin/theme engine — 7 built-in skins (default, ares, mono, slate, poseidon, sisyphus, charizard) + custom YAML skins
- `/personality` command with custom personality + disable support ([#773](https://github.com/NousResearch/hermes-agent/pull/773)) — @teyrebaz33
- User-defined quick commands that bypass the agent loop ([#746](https://github.com/NousResearch/hermes-agent/pull/746)) — @teyrebaz33
- `/reasoning` command for effort level and display toggle ([#921](https://github.com/NousResearch/hermes-agent/pull/921))
- `/verbose` slash command to toggle debug at runtime ([#94](https://github.com/NousResearch/hermes-agent/pull/94)) — @cesareth
- `/insights` command — usage analytics, cost estimation & activity patterns ([#552](https://github.com/NousResearch/hermes-agent/pull/552))
- `/background` command for managing background processes
- `/help` formatting with command categories
- Bell-on-complete — terminal bell when agent finishes ([#738](https://github.com/NousResearch/hermes-agent/pull/738))
- Up/down arrow history navigation
- Clipboard image paste (Alt+V / Ctrl+V)
- Loading indicators for slow slash commands ([#882](https://github.com/NousResearch/hermes-agent/pull/882))
- Spinner flickering fix under patch_stdout ([#91](https://github.com/NousResearch/hermes-agent/pull/91)) — @0xbyt4
- `--quiet/-Q` flag for programmatic single-query mode
- `--fuck-it-ship-it` flag to bypass all approval prompts ([#724](https://github.com/NousResearch/hermes-agent/pull/724)) — @dmahan93
- Tools summary flag ([#767](https://github.com/NousResearch/hermes-agent/pull/767)) — @luisv-1
- Terminal blinking fix on SSH ([#284](https://github.com/NousResearch/hermes-agent/pull/284)) — @ygd58
- Multi-line paste detection fix ([#84](https://github.com/NousResearch/hermes-agent/pull/84)) — @0xbyt4

#### Setup & Configuration
- Modular setup wizard with section subcommands and tool-first UX
- Container resource configuration prompts
- Backend validation for required binaries
- Config migration system (currently v7)
- API keys properly routed to .env instead of config.yaml ([#469](https://github.com/NousResearch/hermes-agent/pull/469)) — @ygd58
- Atomic write for .env to prevent API key loss on crash ([#954](https://github.com/NousResearch/hermes-agent/pull/954))
- `hermes tools` — per-platform tool enable/disable with curses UI
- `hermes doctor` for health checks across all configured providers
- `hermes update` with auto-restart for gateway service
- Show update-available notice in CLI banner
- Multiple named custom providers
- Shell config detection improvement for PATH setup ([#317](https://github.com/NousResearch/hermes-agent/pull/317)) — @mehmetkr-31
- Consistent HERMES_HOME and .env path resolution ([#51](https://github.com/NousResearch/hermes-agent/pull/51), [#48](https://github.com/NousResearch/hermes-agent/pull/48)) — @deankerr
- Docker backend fix on macOS + subagent auth for Nous Portal ([#46](https://github.com/NousResearch/hermes-agent/pull/46)) — @rsavitt

---

### 🔧 Tool System

#### MCP (Model Context Protocol)
- Native MCP client with stdio + HTTP transports ([#291](https://github.com/NousResearch/hermes-agent/pull/291) — @0xbyt4, [#301](https://github.com/NousResearch/hermes-agent/pull/301))
- Sampling support — server-initiated LLM requests ([#753](https://github.com/NousResearch/hermes-agent/pull/753))
- Resource and prompt discovery
- Automatic reconnection and security hardening
- Banner integration, `/reload-mcp` command
- `hermes tools` UI integration

#### Browser
- Local browser backend — zero-cost headless Chromium (no Browserbase needed)
- Console/errors tool, annotated screenshots, auto-recording, dogfood QA skill ([#745](https://github.com/NousResearch/hermes-agent/pull/745))
- Screenshot sharing via MEDIA: on all messaging platforms ([#657](https://github.com/NousResearch/hermes-agent/pull/657))

#### Terminal & Execution
- `execute_code` sandbox with json_parse, shell_quote, retry helpers
- Docker: custom volume mounts ([#158](https://github.com/NousResearch/hermes-agent/pull/158)) — @Indelwin
- Daytona cloud sandbox backend ([#451](https://github.com/NousResearch/hermes-agent/pull/451)) — @rovle
- SSH backend fix ([#59](https://github.com/NousResearch/hermes-agent/pull/59)) — @deankerr
- Shell noise filtering and login shell execution for environment consistency
- Head+tail truncation for execute_code stdout overflow
- Configurable background process notification modes

#### File Operations
- Filesystem checkpoints and `/rollback` command ([#824](https://github.com/NousResearch/hermes-agent/pull/824))
- Structured tool result hints (next-action guidance) for patch and search_files ([#722](https://github.com/NousResearch/hermes-agent/issues/722))
- Docker volumes passed to sandbox container config ([#687](https://github.com/NousResearch/hermes-agent/pull/687)) — @manuelschipper

---

### 🧩 Skills Ecosystem

#### Skills System
- Per-platform skill enable/disable ([#743](https://github.com/NousResearch/hermes-agent/pull/743)) — @teyrebaz33
- Conditional skill activation based on tool availability ([#785](https://github.com/NousResearch/hermes-agent/pull/785)) — @teyrebaz33
- Skill prerequisites — hide skills with unmet dependencies ([#659](https://github.com/NousResearch/hermes-agent/pull/659)) — @kshitijk4poor
- Optional skills — shipped but not activated by default
- `hermes skills browse` — paginated hub browsing
- Skills sub-category organization
- Platform-conditional skill loading
- Atomic skill file writes ([#551](https://github.com/NousResearch/hermes-agent/pull/551)) — @aydnOktay
- Skills sync data loss prevention ([#563](https://github.com/NousResearch/hermes-agent/pull/563)) — @0xbyt4
- Dynamic skill slash commands for CLI and gateway

#### New Skills (selected)
- **ASCII Art** — pyfiglet (571 fonts), cowsay, image-to-ascii ([#209](https://github.com/NousResearch/hermes-agent/pull/209)) — @0xbyt4
- **ASCII Video** — Full production pipeline ([#854](https://github.com/NousResearch/hermes-agent/pull/854)) — @SHL0MS
- **DuckDuckGo Search** — Firecrawl fallback ([#267](https://github.com/NousResearch/hermes-agent/pull/267)) — @gamedevCloudy; DDGS API expansion ([#598](https://github.com/NousResearch/hermes-agent/pull/598)) — @areu01or00
- **Solana Blockchain** — Wallet balances, USD pricing, token names ([#212](https://github.com/NousResearch/hermes-agent/pull/212)) — @gizdusum
- **AgentMail** — Agent-owned email inboxes ([#330](https://github.com/NousResearch/hermes-agent/pull/330)) — @teyrebaz33
- **Polymarket** — Prediction market data (read-only) ([#629](https://github.com/NousResearch/hermes-agent/pull/629))
- **OpenClaw Migration** — Official migration tool ([#570](https://github.com/NousResearch/hermes-agent/pull/570)) — @unmodeled-tyler
- **Domain Intelligence** — Passive recon: subdomains, SSL, WHOIS, DNS ([#136](https://github.com/NousResearch/hermes-agent/pull/136)) — @FurkanL0
- **Superpowers** — Software development skills ([#137](https://github.com/NousResearch/hermes-agent/pull/137)) — @kaos35
- **Hermes-Atropos** — RL environment development skill ([#815](https://github.com/NousResearch/hermes-agent/pull/815))
- Plus: arXiv search, OCR/documents, Excalidraw diagrams, YouTube transcripts, GIF search, Pokémon player, Minecraft modpack server, OpenHue (Philips Hue), Google Workspace, Notion, PowerPoint, Obsidian, find-nearby, and 40+ MLOps skills

---

### 🔒 Security & Reliability

#### Security Hardening
- Path traversal fix in skill_view — prevented reading arbitrary files ([#220](https://github.com/NousResearch/hermes-agent/issues/220)) — @Farukest
- Shell injection prevention in sudo password piping ([#65](https://github.com/NousResearch/hermes-agent/pull/65)) — @leonsgithub
- Dangerous command detection: multiline bypass fix ([#233](https://github.com/NousResearch/hermes-agent/pull/233)) — @Farukest; tee/process substitution patterns ([#280](https://github.com/NousResearch/hermes-agent/pull/280)) — @dogiladeveloper
- Symlink boundary check fix in skills_guard ([#386](https://github.com/NousResearch/hermes-agent/pull/386)) — @Farukest
- Symlink bypass fix in write deny list on macOS ([#61](https://github.com/NousResearch/hermes-agent/pull/61)) — @0xbyt4
- Multi-word prompt injection bypass prevention ([#192](https://github.com/NousResearch/hermes-agent/pull/192)) — @0xbyt4
- Cron prompt injection scanner bypass fix ([#63](https://github.com/NousResearch/hermes-agent/pull/63)) — @0xbyt4
- Enforce 0600/0700 file permissions on sensitive files ([#757](https://github.com/NousResearch/hermes-agent/pull/757))
- .env file permissions restricted to owner-only ([#529](https://github.com/NousResearch/hermes-agent/pull/529)) — @Himess
- `--force` flag properly blocked from overriding dangerous verdicts ([#388](https://github.com/NousResearch/hermes-agent/pull/388)) — @Farukest
- FTS5 query sanitization + DB connection leak fix ([#565](https://github.com/NousResearch/hermes-agent/pull/565)) — @0xbyt4
- Expand secret redaction patterns + config toggle to disable
- In-memory permanent allowlist to prevent data leak ([#600](https://github.com/NousResearch/hermes-agent/pull/600)) — @alireza78a

#### Atomic Writes (data loss prevention)
- sessions.json ([#611](https://github.com/NousResearch/hermes-agent/pull/611)) — @alireza78a
- Cron jobs ([#146](https://github.com/NousResearch/hermes-agent/pull/146)) — @alireza78a
- .env config ([#954](https://github.com/NousResearch/hermes-agent/pull/954))
- Process checkpoints ([#298](https://github.com/NousResearch/hermes-agent/pull/298)) — @aydnOktay
- Batch runner ([#297](https://github.com/NousResearch/hermes-agent/pull/297)) — @aydnOktay
- Skill files ([#551](https://github.com/NousResearch/hermes-agent/pull/551)) — @aydnOktay

#### Reliability
- Guard all print() against OSError for systemd/headless environments ([#963](https://github.com/NousResearch/hermes-agent/pull/963))
- Reset all retry counters at start of run_conversation ([#607](https://github.com/NousResearch/hermes-agent/pull/607)) — @0xbyt4
- Return deny on approval callback timeout instead of None ([#603](https://github.com/NousResearch/hermes-agent/pull/603)) — @0xbyt4
- Fix None message content crashes across codebase ([#277](https://github.com/NousResearch/hermes-agent/pull/277))
- Fix context overrun crash with local LLM backends ([#403](https://github.com/NousResearch/hermes-agent/pull/403)) — @ch3ronsa
- Prevent `_flush_sentinel` from leaking to external APIs ([#227](https://github.com/NousResearch/hermes-agent/pull/227)) — @Farukest
- Prevent conversation_history mutation in callers ([#229](https://github.com/NousResearch/hermes-agent/pull/229)) — @Farukest
- Fix systemd restart loop ([#614](https://github.com/NousResearch/hermes-agent/pull/614)) — @voidborne-d
- Close file handles and sockets to prevent fd leaks ([#568](https://github.com/NousResearch/hermes-agent/pull/568) — @alireza78a, [#296](https://github.com/NousResearch/hermes-agent/pull/296) — @alireza78a, [#709](https://github.com/NousResearch/hermes-agent/pull/709) — @memosr)
- Prevent data loss in clipboard PNG conversion ([#602](https://github.com/NousResearch/hermes-agent/pull/602)) — @0xbyt4
- Eliminate shell noise from terminal output ([#293](https://github.com/NousResearch/hermes-agent/pull/293)) — @0xbyt4
- Timezone-aware now() for prompt, cron, and execute_code ([#309](https://github.com/NousResearch/hermes-agent/pull/309)) — @areu01or00

#### Windows Compatibility
- Guard POSIX-only process functions ([#219](https://github.com/NousResearch/hermes-agent/pull/219)) — @Farukest
- Windows native support via Git Bash + ZIP-based update fallback
- pywinpty for PTY support ([#457](https://github.com/NousResearch/hermes-agent/pull/457)) — @shitcoinsherpa
- Explicit UTF-8 encoding on all config/data file I/O ([#458](https://github.com/NousResearch/hermes-agent/pull/458)) — @shitcoinsherpa
- Windows-compatible path handling ([#354](https://github.com/NousResearch/hermes-agent/pull/354), [#390](https://github.com/NousResearch/hermes-agent/pull/390)) — @Farukest
- Regex-based search output parsing for drive-letter paths ([#533](https://github.com/NousResearch/hermes-agent/pull/533)) — @Himess
- Auth store file lock for Windows ([#455](https://github.com/NousResearch/hermes-agent/pull/455)) — @shitcoinsherpa

---

### 🐛 Notable Bug Fixes

- Fix DeepSeek V3 tool call parser silently dropping multi-line JSON arguments ([#444](https://github.com/NousResearch/hermes-agent/pull/444)) — @PercyDikec
- Fix gateway transcript losing 1 message per turn due to offset mismatch ([#395](https://github.com/NousResearch/hermes-agent/pull/395)) — @PercyDikec
- Fix /retry command silently discarding the agent's final response ([#441](https://github.com/NousResearch/hermes-agent/pull/441)) — @PercyDikec
- Fix max-iterations retry returning empty string after think-block stripping ([#438](https://github.com/NousResearch/hermes-agent/pull/438)) — @PercyDikec
- Fix max-iterations retry using hardcoded max_tokens ([#436](https://github.com/NousResearch/hermes-agent/pull/436)) — @Farukest
- Fix Codex status dict key mismatch ([#448](https://github.com/NousResearch/hermes-agent/pull/448)) and visibility filter ([#446](https://github.com/NousResearch/hermes-agent/pull/446)) — @PercyDikec
- Strip \<think\> blocks from final user-facing responses ([#174](https://github.com/NousResearch/hermes-agent/pull/174)) — @Bartok9
- Fix \<think\> block regex stripping visible content when model discusses tags literally ([#786](https://github.com/NousResearch/hermes-agent/issues/786))
- Fix Mistral 422 errors from leftover finish_reason in assistant messages ([#253](https://github.com/NousResearch/hermes-agent/pull/253)) — @Sertug17
- Fix OPENROUTER_API_KEY resolution order across all code paths ([#295](https://github.com/NousResearch/hermes-agent/pull/295)) — @0xbyt4
- Fix OPENAI_BASE_URL API key priority ([#420](https://github.com/NousResearch/hermes-agent/pull/420)) — @manuelschipper
- Fix Anthropic "prompt is too long" 400 error not detected as context length error ([#813](https://github.com/NousResearch/hermes-agent/issues/813))
- Fix SQLite session transcript accumulating duplicate messages — 3-4x token inflation ([#860](https://github.com/NousResearch/hermes-agent/issues/860))
- Fix setup wizard skipping API key prompts on first install ([#748](https://github.com/NousResearch/hermes-agent/pull/748))
- Fix setup wizard showing OpenRouter model list for Nous Portal ([#575](https://github.com/NousResearch/hermes-agent/pull/575)) — @PercyDikec
- Fix provider selection not persisting when switching via hermes model ([#881](https://github.com/NousResearch/hermes-agent/pull/881))
- Fix Docker backend failing when docker not in PATH on macOS ([#889](https://github.com/NousResearch/hermes-agent/pull/889))
- Fix ClawHub Skills Hub adapter for API endpoint changes ([#286](https://github.com/NousResearch/hermes-agent/pull/286)) — @BP602
- Fix Honcho auto-enable when API key is present ([#243](https://github.com/NousResearch/hermes-agent/pull/243)) — @Bartok9
- Fix duplicate 'skills' subparser crash on Python 3.11+ ([#898](https://github.com/NousResearch/hermes-agent/issues/898))
- Fix memory tool entry parsing when content contains section sign ([#162](https://github.com/NousResearch/hermes-agent/pull/162)) — @aydnOktay
- Fix piped install silently aborting when interactive prompts fail ([#72](https://github.com/NousResearch/hermes-agent/pull/72)) — @cutepawss
- Fix false positives in recursive delete detection ([#68](https://github.com/NousResearch/hermes-agent/pull/68)) — @cutepawss
- Fix Ruff lint warnings across codebase ([#608](https://github.com/NousResearch/hermes-agent/pull/608)) — @JackTheGit
- Fix Anthropic native base URL fail-fast ([#173](https://github.com/NousResearch/hermes-agent/pull/173)) — @adavyas
- Fix install.sh creating ~/.hermes before moving Node.js directory ([#53](https://github.com/NousResearch/hermes-agent/pull/53)) — @JoshuaMart
- Fix SystemExit traceback during atexit cleanup on Ctrl+C ([#55](https://github.com/NousResearch/hermes-agent/pull/55)) — @bierlingm
- Restore missing MIT license file ([#620](https://github.com/NousResearch/hermes-agent/pull/620)) — @stablegenius49

---

### 🧪 Testing

- **3,289 tests** across agent, gateway, tools, cron, and CLI
- Parallelized test suite with pytest-xdist ([#802](https://github.com/NousResearch/hermes-agent/pull/802)) — @OutThisLife
- Unit tests batch 1: 8 core modules ([#60](https://github.com/NousResearch/hermes-agent/pull/60)) — @0xbyt4
- Unit tests batch 2: 8 more modules ([#62](https://github.com/NousResearch/hermes-agent/pull/62)) — @0xbyt4
- Unit tests batch 3: 8 untested modules ([#191](https://github.com/NousResearch/hermes-agent/pull/191)) — @0xbyt4
- Unit tests batch 4: 5 security/logic-critical modules ([#193](https://github.com/NousResearch/hermes-agent/pull/193)) — @0xbyt4
- AIAgent (run_agent.py) unit tests ([#67](https://github.com/NousResearch/hermes-agent/pull/67)) — @0xbyt4
- Trajectory compressor tests ([#203](https://github.com/NousResearch/hermes-agent/pull/203)) — @0xbyt4
- Clarify tool tests ([#121](https://github.com/NousResearch/hermes-agent/pull/121)) — @Bartok9
- Telegram format tests — 43 tests for italic/bold/code rendering ([#204](https://github.com/NousResearch/hermes-agent/pull/204)) — @0xbyt4
- Vision tools type hints + 42 tests ([#792](https://github.com/NousResearch/hermes-agent/pull/792))
- Compressor tool-call boundary regression tests ([#648](https://github.com/NousResearch/hermes-agent/pull/648)) — @intertwine
- Test structure reorganization ([#34](https://github.com/NousResearch/hermes-agent/pull/34)) — @0xbyt4
- Shell noise elimination + fix 36 test failures ([#293](https://github.com/NousResearch/hermes-agent/pull/293)) — @0xbyt4

---

### 🔬 RL & Evaluation Environments

- WebResearchEnv — Multi-step web research RL environment ([#434](https://github.com/NousResearch/hermes-agent/pull/434)) — @jackx707
- Modal sandbox concurrency limits to avoid deadlocks ([#621](https://github.com/NousResearch/hermes-agent/pull/621)) — @voteblake
- Hermes-atropos-environments bundled skill ([#815](https://github.com/NousResearch/hermes-agent/pull/815))
- Local vLLM instance support for evaluation — @dmahan93
- YC-Bench long-horizon agent benchmark environment
- OpenThoughts-TBLite evaluation environment and scripts

---

### 📚 Documentation

- Full documentation website (Docusaurus) with 37+ pages
- Comprehensive platform setup guides for Telegram, Discord, Slack, WhatsApp, Signal, Email
- AGENTS.md — development guide for AI coding assistants
- CONTRIBUTING.md ([#117](https://github.com/NousResearch/hermes-agent/pull/117)) — @Bartok9
- Slash commands reference ([#142](https://github.com/NousResearch/hermes-agent/pull/142)) — @Bartok9
- Comprehensive AGENTS.md accuracy audit ([#732](https://github.com/NousResearch/hermes-agent/pull/732))
- Skin/theme system documentation
- MCP documentation and examples
- Docs accuracy audit — 35+ corrections
- Documentation typo fixes ([#825](https://github.com/NousResearch/hermes-agent/pull/825), [#439](https://github.com/NousResearch/hermes-agent/pull/439)) — @JackTheGit
- CLI config precedence and terminology standardization ([#166](https://github.com/NousResearch/hermes-agent/pull/166), [#167](https://github.com/NousResearch/hermes-agent/pull/167), [#168](https://github.com/NousResearch/hermes-agent/pull/168)) — @Jr-kenny
- Telegram token regex documentation ([#713](https://github.com/NousResearch/hermes-agent/pull/713)) — @VolodymyrBg

---

### 👥 Contributors

Thank you to the 63 contributors who made this release possible! In just over two weeks, the Hermes Agent community came together to ship an extraordinary amount of work.

#### Core
- **@teknium1** — 43 PRs: Project lead, core architecture, provider router, sessions, skills, CLI, documentation

#### Top Community Contributors
- **@0xbyt4** — 40 PRs: MCP client, Home Assistant, security fixes (symlink, prompt injection, cron), extensive test coverage (6 batches), ascii-art skill, shell noise elimination, skills sync, Telegram formatting, and dozens more
- **@Farukest** — 16 PRs: Security hardening (path traversal, dangerous command detection, symlink boundary), Windows compatibility (POSIX guards, path handling), WhatsApp fixes, max-iterations retry, gateway fixes
- **@aydnOktay** — 11 PRs: Atomic writes (process checkpoints, batch runner, skill files), error handling improvements across Telegram, Discord, code execution, transcription, TTS, and skills
- **@Bartok9** — 9 PRs: CONTRIBUTING.md, slash commands reference, Discord channel topics, think-block stripping, TTS fix, Honcho fix, session count fix, clarify tests
- **@PercyDikec** — 7 PRs: DeepSeek V3 parser fix, /retry response discard, gateway transcript offset, Codex status/visibility, max-iterations retry, setup wizard fix
- **@teyrebaz33** — 5 PRs: Skills enable/disable system, quick commands, personality customization, conditional skill activation
- **@alireza78a** — 5 PRs: Atomic writes (cron, sessions), fd leak prevention, security allowlist, code execution socket cleanup
- **@shitcoinsherpa** — 3 PRs: Windows support (pywinpty, UTF-8 encoding, auth store lock)
- **@Himess** — 3 PRs: Cron/HomeAssistant/Daytona fix, Windows drive-letter parsing, .env permissions
- **@satelerd** — 2 PRs: WhatsApp native media, multi-user session isolation
- **@rovle** — 1 PR: Daytona cloud sandbox backend (4 commits)
- **@erosika** — 1 PR: Honcho AI-native memory integration
- **@dmahan93** — 1 PR: --fuck-it-ship-it flag + RL environment work
- **@SHL0MS** — 1 PR: ASCII video skill

#### All Contributors
@0xbyt4, @BP602, @Bartok9, @Farukest, @FurkanL0, @Himess, @Indelwin, @JackTheGit, @JoshuaMart, @Jr-kenny, @OutThisLife, @PercyDikec, @SHL0MS, @Sertug17, @VencentSoliman, @VolodymyrBg, @adavyas, @alireza78a, @areu01or00, @aydnOktay, @batuhankocyigit, @bierlingm, @caentzminger, @cesareth, @ch3ronsa, @christomitov, @cutepawss, @deankerr, @dmahan93, @dogiladeveloper, @dragonkhoi, @erosika, @gamedevCloudy, @gizdusum, @grp06, @intertwine, @jackx707, @jdblackstar, @johnh4098, @kaos35, @kshitijk4poor, @leonsgithub, @luisv-1, @manuelschipper, @mehmetkr-31, @memosr, @PeterFile, @rewbs, @rovle, @rsavitt, @satelerd, @spanishflu-est1918, @stablegenius49, @tars90percent, @tekelala, @teknium1, @teyrebaz33, @tripledoublev, @unmodeled-tyler, @voidborne-d, @voteblake, @ygd58

---

**Full Changelog**: [v0.1.0...v2026.3.12](https://github.com/NousResearch/hermes-agent/compare/v0.1.0...v2026.3.12)
