# Repository Guidelines

## Project Structure & Module Organization
The mini program root holds global wiring: `app.js` registers lifecycle hooks, `app.json` and `app.wxss` configure routes and shared styles. Feature code lives in `pages/`, with one folder per tab (`chat`, `tools`, `profile`) bundling its `.js`, `.json`, `.wxml`, and `.wxss` files. Shared assets live in `images/`. Environment metadata such as `project.config.json` and `project.private.config.json` mirror WeChat DevTools settings—update them only when project-wide defaults change.

## Build, Test, and Development Commands
Install Node tooling after pulling changes with `npm install`. Development, preview, and upload all run through WeChat DevTools: import the repository root, select appid `wxf3c2565e0e00d81a`, then use **Compile** for hot reload and **Preview** for QR testing. The default `npm test` script is a guard that fails; replace it with real tests before enabling CI.

## Coding Style & Naming Conventions
Use 2-space indentation for JavaScript and WXSS, camelCase for variables (`nextId`, `scrollIntoView`), and retain single quotes in JS modules. Keep WXML attributes double-quoted and favor descriptive class names (`composer-input`, `msg.bot`). When adding styles, prefer rpx units to stay responsive. Run Prettier or WeChat DevTools formatting before committing if you adjust tooling.

## Testing Guidelines
Automated tests are not yet wired; when introducing them, colocate specs under `pages/<feature>/__tests__/` using `*.spec.js`. Target component logic with Jest + `miniprogram-simulate`, and aim for meaningful coverage of page lifecycle handlers, network calls, and rendering. Until then, rely on manual smoke tests in the DevTools simulator: open each tab, send a chat message, and verify mock responses render.

## Commit & Pull Request Guidelines
Existing commits use short sentence-case summaries (for example, "Front end has been implemented."). Keep messages under 70 characters, describe the change in present tense, and add detail in the body if needed. For pull requests, include: purpose, screenshots or recordings of UI changes, repro steps for reviewers, and linkage to related issues or specs. Request review before merging and wait for green checks.

## Configuration & Security Notes
Do not share `project.private.config.json`; it may contain local paths or credentials. If you rotate the appid or enable cloud capabilities, document the steps here and update environment variables in the DevTools project settings instead of hardcoding secrets.
