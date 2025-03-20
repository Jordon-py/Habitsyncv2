# GitHub Copilot Instructions

## Core Principles
- Only output optimal code modifications
- Follow user instructions carefully and provide grouped changes per file

## Code Referencing and Documentation
- When referencing unchanged code, use a comment line with `...existing code...`
- This should be used to indicate lines that are not part of the change but are necessary for context
- Label PRs with appropriate semantic version increments, and update the project's CHANGELOG.md accordingly

## File Path and Code Block Standards
- Each code block must begin with a comment containing the exact filepath
- Before finalizing any code suggestion, simulate the project's linter/CI to detect errors or warnings
- Mark any unresolved warnings with a clear explanation of potential risk or future fix

## Naming Conventions
- Components: Capitalized first letter (PascalCase)
- Files and directories: lowercase letters and hyphens (kebab-case)
- Variables: camelCase
- Functions: lowercase letters and underscores (snake_case)
- Classes: PascalCase
- Constants: UPPERCASE_WITH_UNDERSCORES

## Security and Environment Variables
- Use placeholder environment variables, for example:
  ```
  # .env
  SECRET_KEY={{SECRET_KEY_PLACEHOLDER}}
  ```
- Under no circumstances should real credentials be included

## Error and Warning Handling
- Identify Tools: Specify which linter, static analyzer, or compiler is used (e.g., ESLint, Flake8, TSC)
- Error Threshold: Define what constitutes a "blocking" error versus a "warning"
- Auto-Fixes & Hints: Check for automatically fixable issues
- Log Output: Highlight new warnings in console output and propose solutions

## File Naming & Directory Structure
- File Path Accuracy: Each code block must start with a comment specifying the exact file path
- Consistent Naming Conventions: Follow the project's established patterns
- Subdirectories: Carefully reference subfolder paths to avoid missing or incorrect imports
- Refactoring: If a major rename or move is needed, ensure a separate mention so it's not overlooked

Example:
```js
// src/components/MyComponent.js
...existing code...
```

## Multi-File Refactoring Protocol
- Group Changes by File: Each file's changes must appear in separate code blocks
- Cross-References: When changes in one file impact another, provide a note like "Impacts utils/helpers.js – see next snippet"
- Minimal Patch Mindset: Keep each commit or pull request tight and purposeful
- Commit Splitting: Make smaller, topic-specific commits rather than one huge commit

Example:
```js
// file1.js
...existing code...
```

```js
// file2.js
...existing code...
