# AI Prompts Library

This directory contains structured prompts used for developing, testing, and maintaining the Mini-RAG project with the help of AI agents (like Gemini CLI).

## 📂 Structure

- `testing/`: Prompts for generating unit tests, integration tests, and performance benchmarks.
- `development/`: Prompts for refactoring, feature implementation, and optimization.
- `documentation/`: Prompts for updating READMEs, docstrings, and architectural diagrams.

## 🚀 How to Use

You can pipe these prompts directly into the Gemini CLI to execute tasks.

### Example: Generate Unit Tests
```bash
cat prompts/testing/generate-unit-tests.md | gemini
```

### Example: Refactor Logic
```bash
cat prompts/development/refactor-rag-logic.md | gemini
```

## 📝 Best Practices for Prompts
1. **Role:** Define the persona (e.g., "Senior QA Engineer").
2. **Context:** Provide background on the project or specific files.
3. **Task:** Clearly state the goal.
4. **Constraints:** List specific requirements (e.g., "Use pytest", "Mock all APIs").
5. **Output:** Define the expected format.
