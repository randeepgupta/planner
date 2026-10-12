# A planner built around priorities, not a packed schedule

A hyperlinked, handwritten planner designed for my Supernote A5 X. Includes ready-to-use PDFs for **2026–2030** and the Python script that generates them.

## Why I built this

I wanted a planner that helps me decide what matters, gives me room to think, and makes it easy to find my notes later. An hourly schedule was not the most useful way for me to organize the day. I preferred a priority matrix, a generous notes area, and quick navigation between dates.

The design evolved through sketches and revisions:

- Replace hourly scheduling with four task-priority quadrants.
- Give important, non-urgent work more space than tasks to eliminate.
- Reserve roughly the lower half of daily pages for handwritten notes.
- Make the weekly priority matrix the main planning area, with separate Monday–Sunday rows for tasks tied to specific dates.
- Keep weekly quadrant labels small and on the borders so they do not consume writing space.
- Link dates, weeks, months, quarters, and extra notes pages.
- Make week links obvious on the yearly calendar and shade U.S. federal holidays throughout the calendar views.

**The intended outcome:** spend less effort organizing a planner, protect time for important work before it becomes urgent, and keep decisions and follow-ups easy to retrieve. This is a blank planning tool, not an automatic task manager or a guarantee of productivity.

## Download and start

| Year | PDF | Pages |
| --- | --- | ---: |
| 2026 | [2026 planner](planners/2026_Supernote_Planner.pdf) | 865 |
| 2027 | [2027 planner](planners/2027_Supernote_Planner.pdf) | 865 |
| 2028 | [2028 planner](planners/2028_Supernote_Planner.pdf) | 867 |
| 2029 | [2029 planner](planners/2029_Supernote_Planner.pdf) | 865 |
| 2030 | [2030 planner](planners/2030_Supernote_Planner.pdf) | 865 |

On GitHub, download the actual PDF with the file's download button, then transfer it to your Supernote using your preferred supported transfer method. Open the PDF and use its internal links to navigate. Use the pen for handwriting and the device's PDF link interaction for navigation. Exact gestures depend on device settings and firmware.

Keep your annotated working copy separate from these blank templates. Regenerating or replacing a PDF does not merge or preserve handwriting stored on your device. Back up your working planner before replacing files.

### Why one file per year?

Each year is self-contained, easier to archive, and can be regenerated independently. A combined 2026–2030 planner would contain 4,327 pages. Separate files avoid adding another layer of year navigation. The trade-off is that you switch files at the year boundary; links do not cross between PDFs.

## How to use the planner successfully

Use the planner to make choices. You do not need to fill every line or copy every task into every view.

### 1. Set direction each quarter

Use quarterly notes to write two or three outcomes you want to achieve. Describe what “done” means, rather than listing vague intentions. For example, “complete a working prototype and get feedback from three people” is easier to act on than “work on my project.”

Use the monthly calendar for deadlines and commitments. Use monthly notes for milestones, constraints, and decisions that need more space.

### 2. Plan the week in about 10 minutes

Choose up to three meaningful outcomes for the week. Then sort the next actions into the weekly matrix:

| Quadrant | Use it for | What to do |
| --- | --- | --- |
| Do first | Important work with a real deadline or consequence soon | Choose the next action and its deadline. Avoid treating every incoming request as urgent. |
| Schedule | Important work that is not yet urgent | Protect time for it. This is the largest quadrant intentionally. |
| Delegate | Urgent work someone else can appropriately handle | Note the owner and when to follow up. If you cannot delegate it, decide how to handle it deliberately. |
| Eliminate | Work with little value or no longer worth doing | Drop, decline, or defer consciously. This is a decision area, not another backlog to complete. |

Add tasks to the **Monday–Sunday rows only when the day matters**: a submission deadline, a meeting preparation task, or a follow-up you have promised. For a task already in the matrix, a short reference such as “proposal — submit” is enough.

The PDF has no reminders or timed calendar integration. Put appointments and time blocks that require alerts into your regular calendar.

### 3. Start each day in about 3 minutes

Open the day's page from the weekly row or a calendar date. Choose one main outcome and a small number of supporting actions. The daily quadrants are deliberately compact: Do first has 3 lines, Schedule 4, Delegate 2, and Eliminate 1.

Pick at least one action from Schedule when possible, so important work does not wait until it becomes a crisis. Use the lower notes section for meeting notes, decisions, ideas, or context. Use **Extra notes** when you need more room.

A task such as “website” is hard to finish. “Draft the homepage introduction” gives you a clear next step.

### 4. Close the day in about 2 minutes

Mark what is done. For unfinished work, make an explicit choice: carry forward, schedule, delegate, or drop. A simple handwritten convention is enough:

- Checkmark: completed.
- Arrow: moved to another date; write that date alongside it.
- Cross-out: intentionally dropped.

Tasks do not carry forward automatically. Avoid copying everything by default: reconsider whether it still matters. Use the date strip to jump directly to any date within seven days before or after the current page.

### 5. Review the week in about 10 minutes

Use the linked weekly extra notes page to answer:

1. What outcome did I actually move forward?
2. What important work kept getting postponed?
3. What created avoidable urgency?
4. What should I stop doing, delegate, or change next week?

Review delegated items and future commitments. Carry forward only the tasks that still deserve attention. At month-end, compare progress with your quarterly outcomes and adjust the next month's focus.

### How to tell whether it is helping

Look for fewer repeatedly copied tasks, more progress on important non-urgent work, clearer follow-ups, and less time spent finding notes. If maintaining the planner takes more effort than it saves, simplify your routine. The goal is better decisions and follow-through, not perfectly filled pages.

## Navigation and layout

| Control or page | What it does |
| --- | --- |
| YEAR | Returns to the yearly overview. |
| Q1–Q4 side tabs | Opens the selected quarter's notes page. These tabs mean calendar quarters, not task quadrants. |
| JAN–DEC side tabs | Opens a monthly calendar. |
| Month name in a small calendar | Opens that month's calendar. |
| W01, W02, etc. on the yearly calendar | Opens the weekly planner for that calendar row. |
| Week number in monthly or quarterly calendars | Opens the corresponding weekly planner. |
| Date in a calendar or weekly day row | Opens that day's planner. |
| Daily date strip | Offers the previous 7 days, current day, and next 7 days; out-of-year dates are inactive. |
| Week button on a daily page | Opens that day's weekly planner. |
| Extra notes / Daily plan / Weekly plan | Moves between a plan and its paired notes page. |
| Month notes / Calendar | Moves between a monthly calendar and its notes page. |

Dates in an extra daily notes page's strip lead to other extra daily notes pages. Use **Daily plan** to return to the selected date's task page.

The page uses vector text and lines, a monochrome palette, and a 600 × 800-point portrait canvas. It contains no embedded photographs, JavaScript, remote services, or form fields. Checkboxes are handwriting targets, not interactive form controls.

### Holidays

Light-gray shading marks nationwide U.S. federal holidays and their observed dates. It appears in yearly and quarterly mini-calendars, monthly date boxes, weekly day labels, daily date strips, and holiday daily-page headings. A selected date in the daily strip stays dark for navigation clarity.

Saturday holidays include the preceding Friday; Sunday holidays include the following Monday. The actual holiday remains shaded too. The generator also handles an observed date that falls in the previous year, such as December 31, 2027 for New Year's Day 2028.

Reference: [U.S. Office of Personnel Management federal holiday schedules](https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays/), checked October 12, 2026.

State, local, employer-specific, and Washington-area-only Inauguration Day observances are not included. The script uses recurring holiday rules; it does not fetch updates or predict future one-off closures. Holiday shading does not display a popup name in the PDF; dates retain their planner navigation links.

## Generate the PDFs

Requires **Python 3.10+**. ReportLab is the only third-party dependency. No API keys, paid services, or network access are needed after dependency installation.

From the repository directory:

```bash
python -m venv .venv
```

Activate the environment:

```bash
# macOS / Linux
source .venv/bin/activate
```

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install dependencies and generate the default 2026–2030 set:

```bash
python -m pip install -r requirements.txt
python generate_planner.py
```

Generate selected years or choose a different output directory:

```bash
python generate_planner.py 2028
python generate_planner.py 2027 2029 --output-dir my-planners
python generate_planner.py 2031 --author "Your Name"
```

**Existing files with the same output names are overwritten.** Generate into a new directory when you want to compare layouts or keep previous blank versions.

The script supports years 2026–9998 and computes day counts, leap days, and Monday-start weeks dynamically. The included 2026–2030 PDFs are the reviewed examples; inspect newly generated years or layout changes before using them on a device.

### What's inside each year?

- 1 yearly calendar.
- 4 quarterly notes pages.
- 12 monthly calendars and 12 monthly notes pages.
- A weekly planner and extra notes page for every Monday–Sunday week overlapping the year.
- A daily planner and extra notes page for every date in the year.

The included years each overlap 53 Monday-start weeks. Week labels follow ISO week numbers, so an early-January row can belong to week 52 or 53 of the previous ISO year, and late December can belong to week 1 of the next ISO year. Their displayed date ranges identify the actual week.

## Customize the design

The generator is a portable refactoring of the script used to create the PDFs in this repository.

Inside `generate_planner.py`:

- `federal_dates()` calculates holiday shading dates.
- `base()` draws headers, side tabs, and footers.
- `mini()` draws linked year/quarter mini-calendars.
- The monthly, weekly, and daily loops draw their respective layouts.
- Weekly quadrant tuples define position, size, writing-line count, and label.
- Daily quadrant tuples define the compact daily priorities.
- `ruled()` controls the writing-line spacing for notes.

Drawing helpers take coordinates measured from the top-left of the page and translate them to PDF coordinates. After changing dimensions, inspect the result for overlaps and make sure writing lines remain inside their boxes.

## Validation and practical limits

Generation checks the expected page count and verifies that every generated link target exists. The distributed PDFs were also rendered for visual review and their internal links were checked after opening the finished files. A normal year contains roughly 29,000 internal links.

The reusable script was checked by regenerating 2026 and leap-year 2028 and comparing page text, link counts, and representative rendered pages against the distributed versions. PDF metadata can differ between runs, so binary checksums need not match.

Device-specific performance and gestures should be checked on your own firmware. Handwriting is managed by your PDF reader or Supernote, not by this script. There is no automatic task sync, recurring-task engine, reminder system, or annotation migration.

## Repository contents

```text
generate_planner.py   Portable generator with year and output-folder options
requirements.txt      Pinned ReportLab dependency
README.md             Purpose, planning routine, navigation, and generation guide
planners/             Ready-to-use PDFs for 2026–2030
```

Upload these extracted files and the `planners` folder to your repository. The generator does not depend on the original design-reference images or on ChatGPT.
