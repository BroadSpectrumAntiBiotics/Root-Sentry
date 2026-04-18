# Root Sentry

**A text-based strategy game where you're fighting to finish a system update from the inside of a computer.**

You're deep in your own machine, trying to push through a critical update while viruses and glitches try to tear everything apart. Manage your **system integrity (HP)**, **budget**, and **scripts** wisely. Every "continue" brings you closer to finishing... but also closer to total system failure.

It's a mix of resource management, strategic decisions, and a bit of luck — all wrapped in a retro terminal aesthetic.

### How to Play

1. Clone the repo:
```
git clone https://github.com/BroadSpectrumAntiBiotics/root-sentry.git
cd root-sentry
```
2. Run the game:
```
python game.py
```
-----------------------------------------------------------------------------------------
Commands (type these in the main loop):

continue — Progress the update (risky but necessary)

shop — Spend your budget on useful scripts and upgrades

info — Get help and game information

exit — Quit the game


Your goal is to reach 100% update without your system integrity dropping to zero.

**Features**

Simple but addictive resource management (HP, Budget, Scripts)

In-game shop system

Procedural virus encounters (work in progress)

Multiple stages and an ending

Clean, modular Python code — easy to read and expand

Pure terminal experience (no external dependencies)

**Current State**
This is an early but fully playable personal project. I'm actively adding more depth to the virus system, risk/reward mechanics, and polish.

**Why I Built It**

Started as a way to prove to myself that I can finish what I start. Turning a vague idea into a working game has been a fun (and sometimes stressful) learning experience.

**Future Plans**

More varied viruses with different behaviors

Upgradable scripts with special abilities

Better risk/reward events during "continue"

Multiple endings based on your final stats

Improved UI and flavor text

----------------------------------------------------------------------------------------
Made with ❤️ by a 16-year-old who just wants to ship things.

Feedback, ideas, or bug reports are very welcome — just open an issue or pull request!
