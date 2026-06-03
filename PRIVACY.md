# Privacy and Credentials

This repository must not contain API keys, `.env` files, personal access tokens, session cookies, or private ChatGPT/OpenAI account details.

The `.gitignore` file excludes common local-secret files and build artifacts. If optional AI integrations are added later, keep credentials in local environment variables or GitHub Actions secrets, never in source control.

Before publishing a release or pushing changes, run a local secret scan or inspect changes manually.
