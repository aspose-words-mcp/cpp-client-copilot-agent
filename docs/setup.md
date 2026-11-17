# Client setup

## Prerequisites

- VS Code with GitHub Copilot Chat access.
- A deployed Aspose.Words C++ MCP server and network access to its endpoint.
- Any credentials required by that deployment.

A C++ compiler and Aspose.Words SDK are needed only for compiling/executing examples, not for connecting to MCP.

## Connect the server

Open `cpp-client-copilot-agent.code-workspace`. Keep the `words-cpp` server identifier: the existing agent selects `words-cpp/*` tools.

Replace the placeholder in `.vscode/mcp.json` with the full deployed endpoint. For example, if your server runs locally on port 8080:

```json
{
  "servers": {
    "words-cpp": {
      "type": "http",
      "url": "http://127.0.0.1:8080/words/cpp/mcp/v1/streamable-http"
    }
  }
}
```

Use your actual port; 8080 is only an example. Start the connection with **MCP: List Servers**, review trust prompts, and open a fresh chat with **Aspose Words C++ MCP** selected. A connected MCP server and a discovered custom agent are separate checks.

### SSH tunnel option

If your server listens only on a VM's loopback address, a tunnel can expose it locally. Replace the user and host in this example, and adjust the remote port to the actual service:

```powershell
ssh -o ExitOnForwardFailure=yes -o ServerAliveInterval=30 -N -L 8084:127.0.0.1:8083 USER@VM_HOST
```

Keep the tunnel running and use `http://127.0.0.1:8084/words/cpp/mcp/v1/streamable-http` in the client. Localhost refers to the machine running the client; it is not automatically the VM.

## Authentication

Follow the [server deployment instructions](https://github.com/aspose-words-mcp/cpp-server). Use your client's supported authentication mechanism for that server. Keep credentials out of committed configuration and logs. No authentication header or token is bundled here.

## Verify the connection

Ask “How do I convert DOCX to PDF using Aspose.Words for C++?” Inspect tool activity for `words-cpp` requests and source citations. Confirm responses are scoped to `aspose.words` and `cpp`. Empty retrieval results can indicate missing ingestion or an overly specific query; they do not by themselves prove an API is unsupported.

## Troubleshooting

- Missing agent: open the repository root or workspace, confirm the agent file exists, reload the window, and inspect available agent diagnostics.
- Missing MCP tools: check endpoint, port, authentication, network/tunnel and server output. Keep the server ID consistent with the agent.
- Missing local tools: check client permissions and available tools; instructions alone cannot grant access.
- Large response: inspect saved response files in bounded chunks, or request narrower evidence if file access is unavailable.
- Incorrect C++: provide the installed SDK version and full compiler diagnostics; validate headers and signatures against that SDK.

## Validation limits

Static JSON and file-link checks do not establish live Copilot behavior. Test the connection and agent in VS Code. Compilation, execution and output inspection require your build project; see [C++ validation](../examples/README.md).
