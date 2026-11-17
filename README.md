# Aspose.Words for C++ — GitHub Copilot Client Agent

Use GitHub Copilot Chat to explore Aspose.Words for C++ with answers and examples grounded in your deployed MCP server's documentation and API tools.

This repository provides the **Aspose Words C++ MCP** custom agent and VS Code client configuration. Deploy the MCP server separately, then connect this client to its HTTP endpoint.

[Setup and troubleshooting](docs/setup.md) · [Validate generated C++](examples/README.md)

## Project family

| Repository | Responsibility |
| --- | --- |
| [context-engine](https://github.com/aspose-core-mcp/context-engine) | Shared ingestion, indexing, retrieval and MCP infrastructure |
| [cpp-plugin](https://github.com/aspose-words-mcp/cpp-plugin) | Words C++ documentation/API extraction and retrieval configuration |
| [cpp-server](https://github.com/aspose-words-mcp/cpp-server) | Deployment helpers combining pinned engine and plugin versions |
| `cpp-client-copilot-agent` (this project) | Custom Copilot agent and VS Code client configuration |

## Quick start

1. Deploy the MCP server and obtain its full HTTP endpoint and authentication requirements.
2. Open `cpp-client-copilot-agent.code-workspace` in VS Code with GitHub Copilot Chat access.
3. Replace the host placeholder in `.vscode/mcp.json` with your actual endpoint. Run **MCP: List Servers**, select **words-cpp**, and start it.
4. Configure authentication as required by your deployment; see [setup](docs/setup.md#authentication).
5. Start a new Copilot chat and choose **Aspose Words C++ MCP**.
6. Ask: **How do I convert DOCX to PDF using Aspose.Words for C++?**

The existing `words-cpp-mcp.code-workspace` remains usable. Both workspace files open this repository. The server identifier stays `words-cpp` to match the agent's tool selection.

## What is included

- `.github/agents/aspose-words-cpp-mcp.agent.md`: existing custom agent and tool selection.
- `.github/copilot-instructions.md`: existing evidence, C++ correctness and validation guidance.
- `.vscode/mcp.json`: HTTP connection configuration with a host placeholder.
- `.vscode/settings.json`: workspace settings.
- `docs/setup.md`: connection setup, authentication and troubleshooting.
- `examples/`: pinned Windows C++ project, build script and starter.
- `showcase/`: C++ questions, Copilot/saved-answer runner, optional compilation and metrics.
- `cpp-client-copilot-agent.code-workspace`: workspace entry point matching the project name.

The instruction and custom-agent files were preserved. The C++ build project and showcase runner are described below; .NET results are not reused as C++ evidence.

## Workflow and evidence

The agent uses MCP documentation and API tools, then inspects local project files and SDK headers when needed. Large saved responses should be read in bounded chunks. Local read, edit and execution tools operate under normal client permissions.

Documentation lookup, header inspection, compilation, execution and output validation are separate checks. A successful tool response does not prove generated code compiles. Actual tool availability, SDK version, compiler, inputs and permissions affect what the agent can verify.

## Compile generated examples

Use the [Windows C++ build project](examples/README.md) with restored Aspose.Words.Cpp 26.9.0 packages and Visual Studio C++ Build Tools. Build the included starter or pass a complete generated source file. Execution is explicit with `-Run`.

## Showcase

See [showcase generation](showcase/README.md) for twelve C++ prompts, saved-answer replay, optional fresh Copilot CLI sessions, verbatim code extraction, compilation and reports. Compilation never executes the generated programs. A [starter showcase](showcase/sample/showcase.md) demonstrates report output and a verified compilation; it is a saved hand-authored answer, not live Copilot evidence. No live Copilot pass rate is claimed.

## Contributing

Include your VS Code version, selected model, SDK version, prompt and relevant diagnostics when reporting an issue. Remove credentials and private endpoint details from logs. Report server deployment or tool issues in the server repository.

## License

[MIT](LICENSE), copyright (c) 2001–2026 Aspose Pty Ltd. Preserve upstream SDK and example attribution when adding material to this project.
