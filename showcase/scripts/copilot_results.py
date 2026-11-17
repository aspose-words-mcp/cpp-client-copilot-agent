"""Normalize Copilot CLI event logs and render per-run Q&A reports."""
import json
from pathlib import Path


def extract(path):
    events = []
    warnings = []
    for index, line in enumerate(path.read_text(encoding='utf-8', errors='replace').splitlines(), 1):
        if not line.strip():
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            warnings.append(f'Non-JSON output at line {index}; inspect events.jsonl.')
    messages = []
    models = set()
    calls = {}
    agent_names = []
    for event in events:
        kind, data = event.get('type'), event.get('data', {})
        if kind == 'session.custom_agents_updated':
            agent_names = [a.get('id') for a in data.get('agents', [])]
        if kind == 'session.auto_mode_resolved' and data.get('chosenModel'):
            models.add(data['chosenModel'])
        if kind == 'assistant.message':
            if data.get('model'):
                models.add(data['model'])
            if data.get('content') and not data.get('toolRequests'):
                messages.append(data['content'])
        if kind == 'tool.execution_start':
            # A new tool call makes previous prose intermediate, not the final answer.
            messages = []
            calls[data['toolCallId']] = {'name': data.get('toolName'),
                                         'server': data.get('mcpServerName'), 'completed': False}
        if kind == 'tool.execution_complete':
            call = calls.setdefault(data['toolCallId'], {'name': None, 'server': None})
            exit_code = data.get('shellExecution', {}).get('exitCode')
            call.update(completed=True, success=data.get('success'), exit_code=exit_code,
                        failed=data.get('success') is False or exit_code not in (None, 0))
            if 'Saved to:' in json.dumps(data.get('result', {})):
                warnings.append('Tool evidence includes a temporary-file reference; the trace may not contain full documentation.')
        if kind == 'session.error':
            warnings.append('CLI session reported an error; inspect the event log.')
    answer = '\n\n'.join(messages)
    if not answer:
        warnings.append('No final assistant answer found.')
    if not any(c.get('server') == 'words-cpp' for c in calls.values()):
        warnings.append('No words-cpp call recorded.')
    if any(c.get('failed') for c in calls.values()):
        warnings.append('One or more tool executions failed; review the trace.')
    return {'recorded_answer_markdown': answer, 'resolved_models': sorted(models),
            'discovered_agent_ids': agent_names, 'tools': list(calls.values()),
            'warnings': list(dict.fromkeys(warnings))}

