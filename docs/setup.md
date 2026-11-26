# Client setup

## Prerequisites

- VS Code with GitHub Copilot Chat access.
- The public HTTP endpoint for a deployed Aspose.Words for C++ MCP server.
- Network access to the endpoint and any credentials required by its deployment.

To compile or run generated C++ examples, separately install a compatible C++ toolchain and the Aspose.Words for C++ SDK. Follow Aspose.Words licensing requirements for your usage. Neither is needed just to connect the client to MCP.

## Connect the server

Open `cpp-client-copilot-agent.code-workspace` in VS Code. The server is named `words-cpp`; the custom agent's tool configuration refers to that name, so keep it consistent.

Replace the URL in `.vscode/mcp.json` with the full public MCP endpoint supplied by the server operator. For example:

```json
{
  "servers": {
    "words-cpp": {
      "type": "http",
      "url": "https://YOUR_MCP_HOST/YOUR_MCP_ENDPOINT"
    }
  }
}
```

The example URL is a placeholder, not a working endpoint. A repository URL or server homepage is not an MCP endpoint. Start the connection through **MCP: List Servers**. Review VS Code's trust and tool-access prompts, then open a new chat with **Aspose Words C++ MCP** selected.

## Authentication

Follow the [server deployment instructions](https://github.com/aspose-words-mcp/cpp-server) and any authentication instructions supplied by the endpoint operator. Use VS Code's supported authentication mechanism for the server, or the server's documented credential mechanism. Keep credentials out of committed files and logs.

The workspace configuration uses VS Code's `servers` format. For configuration and authentication options, see [VS Code MCP server configuration](https://code.visualstudio.com/docs/agent-customization/mcp-servers).

## Verify the connection

Ask “How do I convert DOCX to PDF using Aspose.Words for C++?” Inspect the chat's tool activity for `words-cpp` requests and documentation citations. Confirm responses are scoped to `aspose.words` and `cpp`. A connected MCP server and a discovered custom agent are separate checks.

## Agent missing from the picker

1. Open the repository root or the supplied workspace file in the same VS Code window as the chat.
2. Confirm `.github/agents/aspose-words-cpp-mcp.agent.md` exists and has `user-invocable: true`.
3. Open **Configure Custom Agent…** and check the workspace agent list.
4. Run **Developer: Reload Window** and start a new chat.
5. If the agent is still missing, inspect **Developer: Open Agent Debug Panel** for discovery diagnostics.

## Server or tool errors

Check the full endpoint URL, authentication, network access, and server logs. Keep the `words-cpp` server identifier consistent with the agent. Empty retrieval results can indicate missing ingestion or an overly specific query; a failed lookup or unavailable tool does not by itself prove a feature is unsupported. If local tools are missing, check VS Code permissions and tool availability.

## Large responses

Inspect saved MCP responses in small chunks using available local tools. Normal VS Code permissions apply. If file access is unavailable or declined, request narrower evidence and explain any unresolved gap.

## References

- [VS Code MCP server configuration](https://code.visualstudio.com/docs/agent-customization/mcp-servers)
- [VS Code custom agents](https://code.visualstudio.com/docs/agent-customization/custom-agents)

## C++ compilation checks

For the included Windows x64 C++17 build project, install Visual Studio C++ Build Tools, the v142 toolset, the Windows 10 SDK, and NuGet CLI, then restore the Aspose.Words.Cpp and CodePorting framework packages. See [C++ build verification](../examples/README.md) for the pinned package version and commands.

Compilation and linking do not execute the program or verify its output. The showcase runner does not execute generated programs; runtime testing requires an explicit, reviewed run and output inspection. If compilation fails, provide the SDK version and compiler diagnostics and verify headers and signatures against that SDK.
