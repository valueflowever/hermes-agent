<p align="center">
  <img src="assets/banner.png" alt="Hermes Agent" width="100%">
</p>

# Hermes Agent ☤

<p align="center">
  <a href="https://hermes-agent.nousresearch.com/docs/"><img src="https://img.shields.io/badge/Docs-hermes--agent.nousresearch.com-FFD700?style=for-the-badge" alt="Documentation"></a>
  <a href="https://discord.gg/NousResearch"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord"></a>
  <a href="https://github.com/NousResearch/hermes-agent/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License: MIT"></a>
  <a href="https://nousresearch.com"><img src="https://img.shields.io/badge/Built%20by-Nous%20Research-blueviolet?style=for-the-badge" alt="Built by Nous Research"></a>
</p>

**由 [Nous Research](https://nousresearch.com) 打造的自我改进型 AI Agent。** 它是少数内置完整学习闭环的 Agent 之一：会从经验中创建技能，在使用过程中持续改进技能，主动提醒自己沉淀知识，搜索过往对话，并在跨会话过程中不断加深对你的理解。你可以把它跑在 5 美元的 VPS、GPU 集群，或空闲时几乎零成本的无服务器基础设施上。它不绑定在你的笔记本上，你甚至可以在 Telegram 上和它对话，同时让它在云端 VM 上工作。

你可以使用任何自己喜欢的模型：[Nous Portal](https://portal.nousresearch.com)、[OpenRouter](https://openrouter.ai)（200+ 模型）、[z.ai/GLM](https://z.ai)、[Kimi/Moonshot](https://platform.moonshot.ai)、[MiniMax](https://www.minimax.io)、OpenAI，或者你自己的接口端点。通过 `hermes model` 就能切换，无需改代码，也没有平台锁定。

最近一轮能力增强里，Hermes 还新增了结构化记忆、失败路由（failure routes）、按任务相关性注入的选择性记忆召回、最终回复内部审查，以及在 `session_search` 中对 session 标题和预览的回退匹配。

<table>
<tr><td><b>真正可用的终端界面</b></td><td>完整的 TUI，支持多行编辑、slash 命令自动补全、会话历史、中断并重定向，以及工具流式输出。</td></tr>
<tr><td><b>出现在你工作的地方</b></td><td>Telegram、Discord、Slack、WhatsApp、Signal 和 CLI，全都由同一个 gateway 进程支持。支持语音备忘录转写与跨平台会话连续性。</td></tr>
<tr><td><b>闭环学习系统</b></td><td>由 Agent 维护的持久记忆、结构化记忆元数据、failure routes 与周期性提醒。复杂任务后可自动创建技能，技能在使用中持续自我优化。系统提示保持稳定以保住 prompt cache，同时还能在任务执行前按相关性召回 memory/user/failure 片段。基于 FTS5 的 session 搜索配合 LLM 摘要与标题/预览回退匹配，实现更稳健的跨会话回忆。集成 <a href="https://github.com/plastic-labs/honcho">Honcho</a> 辩证式用户建模，并兼容 <a href="https://agentskills.io">agentskills.io</a> 开放标准。</td></tr>
<tr><td><b>回复质量闸门</b></td><td>候选答案在展示给用户前可先通过内部 review gate 审查；不合格草稿会先在内部返工，而不是直接暴露给用户。失败路线还可以沉淀进 failure memory，减少重复犯错。</td></tr>
<tr><td><b>定时自动化</b></td><td>内置 cron 调度器，可将结果投递到任意平台。日报、夜间备份、每周审计，都可以用自然语言配置并无人值守运行。</td></tr>
<tr><td><b>可委派、可并行</b></td><td>可派生隔离的子 Agent 并行处理多个工作流。还可以编写 Python 脚本通过 RPC 调用工具，把多步流水线压缩成零上下文成本的单回合执行。</td></tr>
<tr><td><b>不只跑在你的电脑上</b></td><td>提供六种终端后端：local、Docker、SSH、Daytona、Singularity 和 Modal。Daytona 与 Modal 支持无服务器持久化，Agent 的环境在空闲时休眠、按需唤醒，两次会话之间成本几乎为零。既能跑在 5 美元 VPS 上，也能跑在 GPU 集群里。</td></tr>
<tr><td><b>面向研究</b></td><td>支持批量轨迹生成、Atropos RL 环境，以及用于训练下一代工具调用模型的轨迹压缩。</td></tr>
</table>

---

## 快速安装

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

支持 Linux、macOS、WSL2，以及通过 Termux 运行的 Android。安装脚本会自动处理对应平台的初始化配置。

> **Android / Termux：** 已验证的手动安装路径见 [Termux 指南](https://hermes-agent.nousresearch.com/docs/getting-started/termux)。在 Termux 上，Hermes 会安装精简过的 `.[termux]` extra，因为完整的 `.[all]` 目前会拉入与 Android 不兼容的语音依赖。
>
> **Windows：** 不支持原生 Windows。请先安装 [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install)，然后在 WSL2 中运行上面的命令。

安装完成后：

```bash
source ~/.bashrc    # 重新加载 shell（或：source ~/.zshrc）
hermes              # 开始聊天！
```

---

## 快速开始

```bash
hermes              # 交互式 CLI，开始一段会话
hermes model        # 选择你的 LLM 提供商和模型
hermes tools        # 配置启用哪些工具
hermes config set   # 设置单个配置项
hermes gateway      # 启动消息网关（Telegram、Discord 等）
hermes setup        # 运行完整安装向导（一次性配置全部内容）
hermes claw migrate # 从 OpenClaw 迁移（如果你原来在用 OpenClaw）
hermes update       # 更新到最新版本
hermes doctor       # 诊断问题
```

📖 **[完整文档 →](https://hermes-agent.nousresearch.com/docs/)**

## 本轮新增能力

- **结构化记忆条目：** `memory` 现在除了纯文本，还支持 `kind`、`name`、`description`、`tags`，让后续召回更准、更可维护。
- **Failure routes：** 被证明是死路或被用户明确否定的做法，可以写入 `~/.hermes/memories/failures/*.md`。相似任务再次出现时，这些文件会作为硬约束被选择性召回。
- **任务时记忆覆盖：** Hermes 不会在会话中途重写系统提示，而是在每次 API 调用前，仅补充和当前请求强相关的 memory / user / failure 片段，兼顾 recall 与 prompt cache。
- **最终回复内审：** 开启 `agent.output_review` 后，候选答案会先经过内部质量检查；如果太空、偏题、缺验证或泄露内部过程，会先返工再展示。
- **更稳健的历史检索：** `session_search` 在 FTS 正文搜索不足时，会回退匹配 session 的标题和预览，更容易找回“我们之前做过这个”的上下文。

常用配置开关包括：

```yaml
memory:
  failure_memory_enabled: true
  memory_recall_enabled: true

agent:
  output_review:
    enabled: true

auxiliary:
  response_review:
    provider: auto
```

## 近期稳定性加固

除了上面的能力增强，最近一轮还重点做了运行稳定性和生产可用性收尾：

- **Gateway 审批链更稳：** 危险命令审批提示不再被 Tirith 的同步检查阻塞，消息网关会先把审批请求发出去，再做安全检查与降级处理。
- **中断与子 Agent 更可靠：** 修复了启动前中断、跨线程中断传播，以及部分工具/子 Agent 路径里“看不到 stop 信号”的问题。
- **Provider / streaming 兼容性更好：** 对忽略 `stream=True` 的 OpenAI-compatible 后端做了兼容回退，修复了部分 tool-call dict 参数、辅助 provider 选择与 Codex token 污染问题。
- **多实例 / 多 profile 更安全：** pairing 存储、cron lock、部分 gateway 路径现在按当前 `HERMES_HOME` 动态解析，减少并行测试和多 profile 部署下的状态串扰。
- **长连接与关机清理更完整：** Home Assistant websocket、gateway shutdown、Matrix sync store、Telegram/Feishu 边界路径都补了容错和资源清理。

如果你准备把 Hermes 用在长期运行或多平台 gateway 场景，这些改动会明显降低“偶发挂住、状态泄漏、测试全绿但真实环境不稳”的概率。

## 发布前验证

如果你要在自己的环境里做一次发布前确认，建议至少跑这三层回归：

```bash
python -m pytest tests/ -q --ignore=tests/integration --ignore=tests/e2e --tb=short -n auto
python -m pytest tests/integration/ -q -n auto -m integration -o addopts=""
python -m pytest tests/e2e/ -q -n auto -o addopts=""
```

维护 Hermes 本体时，建议再补一轮更严格的 warning-as-error 回归，尽早把资源泄漏、未 awaited coroutine 和第三方弃用提示收掉：

```bash
python -m pytest tests/ -q --ignore=tests/integration --ignore=tests/e2e --tb=short -n auto \
  -W error::pytest.PytestUnraisableExceptionWarning \
  -W error::RuntimeWarning \
  -W error::DeprecationWarning
```

## CLI 与消息平台速查

Hermes 有两个入口：你可以通过 `hermes` 启动终端 UI，也可以运行 gateway 后，从 Telegram、Discord、Slack、WhatsApp、Signal 或 Email 与它对话。进入会话后，很多 slash 命令在两个界面中是共用的。

| 操作 | CLI | 消息平台 |
|---------|-----|---------------------|
| 开始聊天 | `hermes` | 运行 `hermes gateway setup` + `hermes gateway start`，然后给机器人发消息 |
| 开启新会话 | `/new` 或 `/reset` | `/new` 或 `/reset` |
| 切换模型 | `/model [provider:model]` | `/model [provider:model]` |
| 设置人格 | `/personality [name]` | `/personality [name]` |
| 重试或撤销上一轮 | `/retry`, `/undo` | `/retry`, `/undo` |
| 压缩上下文 / 查看占用 | `/compress`, `/usage`, `/insights [--days N]` | `/compress`, `/usage`, `/insights [days]` |
| 浏览技能 | `/skills` 或 `/<skill-name>` | `/skills` 或 `/<skill-name>` |
| 中断当前工作 | `Ctrl+C` 或直接发送新消息 | `/stop` 或直接发送新消息 |
| 平台相关状态 | `/platforms` | `/status`, `/sethome` |

完整命令列表见 [CLI 指南](https://hermes-agent.nousresearch.com/docs/user-guide/cli) 与 [消息网关指南](https://hermes-agent.nousresearch.com/docs/user-guide/messaging)。

---

## 文档

所有文档都在 **[hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs/)**：

| 部分 | 内容 |
|---------|---------------|
| [Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart) | 2 分钟完成安装、设置与首次对话 |
| [CLI Usage](https://hermes-agent.nousresearch.com/docs/user-guide/cli) | 命令、快捷键、人格、会话 |
| [Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration) | 配置文件、Provider、模型与全部选项 |
| [Messaging Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/messaging) | Telegram、Discord、Slack、WhatsApp、Signal、Home Assistant |
| [Security](https://hermes-agent.nousresearch.com/docs/user-guide/security) | 命令审批、私聊配对、容器隔离 |
| [Tools & Toolsets](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools) | 40+ 工具、toolset 系统、终端后端 |
| [Skills System](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) | 程序性记忆、Skills Hub、技能创建 |
| [Memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory) | 持久记忆、用户画像、failure routes、相关性召回、最佳实践 |
| [MCP Integration](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) | 接入任意 MCP 服务器扩展能力 |
| [Cron Scheduling](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron) | 带平台投递的定时任务 |
| [Context Files](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files) | 影响每次对话的项目上下文文件 |
| [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture) | 项目结构、agent loop、关键类 |
| [Contributing](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing) | 开发环境、PR 流程、代码风格 |
| [CLI Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands) | 所有命令和 flag |
| [Environment Variables](https://hermes-agent.nousresearch.com/docs/reference/environment-variables) | 完整环境变量参考 |

---

## 从 OpenClaw 迁移

如果你正在从 OpenClaw 迁移，Hermes 可以自动导入你的设置、记忆、技能和 API Key。

**首次安装时：** 安装向导（`hermes setup`）会自动检测 `~/.openclaw`，并在开始配置前询问是否迁移。

**安装后任意时刻：**

```bash
hermes claw migrate              # 交互式迁移（完整预设）
hermes claw migrate --dry-run    # 预览将会迁移什么
hermes claw migrate --preset user-data   # 不迁移密钥，仅迁移用户数据
hermes claw migrate --overwrite  # 覆盖已有冲突项
```

可导入内容包括：
- **SOUL.md**：人格文件
- **Memories**：`MEMORY.md` 与 `USER.md` 条目
- **Skills**：用户创建的技能 → `~/.hermes/skills/openclaw-imports/`
- **Command allowlist**：审批白名单模式
- **Messaging settings**：平台配置、允许用户、工作目录
- **API keys**：白名单内密钥（Telegram、OpenRouter、OpenAI、Anthropic、ElevenLabs）
- **TTS assets**：工作区音频资源
- **Workspace instructions**：`AGENTS.md`（配合 `--workspace-target`）

查看全部选项请运行 `hermes claw migrate --help`，或者使用 `openclaw-migration` skill，让 Agent 以交互方式带你完成迁移并预览 dry-run。

---

## 参与贡献

欢迎贡献！开发环境、代码风格与 PR 流程见 [Contributing Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing)。

贡献者快速开始：

```bash
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv venv --python 3.11
source venv/bin/activate
uv pip install -e ".[all,dev]"
python -m pytest tests/ -q
```

> **RL Training（可选）：** 如果你要参与 RL / Tinker-Atropos 集成开发：
> ```bash
> git submodule update --init tinker-atropos
> uv pip install -e "./tinker-atropos"
> ```

---

## 社区

- 💬 [Discord](https://discord.gg/NousResearch)
- 📚 [Skills Hub](https://agentskills.io)
- 🐛 [Issues](https://github.com/NousResearch/hermes-agent/issues)
- 💡 [Discussions](https://github.com/NousResearch/hermes-agent/discussions)
- 🔌 [HermesClaw](https://github.com/AaronWong1999/hermesclaw) — 社区版微信桥接：可在同一个微信账号上同时运行 Hermes Agent 与 OpenClaw。

---

## 许可证

MIT，见 [LICENSE](LICENSE)。

由 [Nous Research](https://nousresearch.com) 构建。
