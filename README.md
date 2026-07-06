# Python Classroom Environment

This repo gives you a ready-to-code Python environment in your browser — no installs needed.

## Students: getting started

1. Click the green **Code** button on this repo, then the **Codespaces** tab.
2. Click **Create codespace on main**.
3. Wait 30–60 seconds while your environment builds. You'll land in a full VS Code window running in the cloud.
4. Open `hello.py` in the file explorer on the left, then run it from the terminal at the bottom:
   ```
   python hello.py
   ```
5. When you're done for the day, you can just close the tab — your codespace pauses automatically. Come back anytime via the same **Codespaces** tab; you'll find it listed there.

You'll need a free GitHub account to do this (github.com/join) if you don't already have one.

## Instructor: setting this up for your class

- **To hand this to students each term:** click **Use this template** (top of the repo page) to spin up a fresh copy per class/quarter, or just keep this one repo going and have students fork it.
- **Adding lab files:** drop new `.py` files (or folders per assignment) into the repo; they'll show up for anyone who creates a new codespace. Students who already have a codespace running will need to pull the latest changes (`git pull` in the terminal, or the Source Control panel).
- **Changing installed packages:** edit `requirements.txt` — anything listed there installs automatically the next time a codespace is built.
- **Compute/storage limits:** each student's codespace usage counts against *their own* free GitHub quota (roughly 60 hours/month on a 2-core machine, 15 GB storage), not yours. Idle codespaces auto-stop after 30 minutes.
- **No autograding here** — this is a bare coding environment. For grading, either have students submit via a shared repo/PR, or paste output into your LMS for now.
