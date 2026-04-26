# CLI Fitness Tracker

A simple Python command-line fitness tracker that lets users log workouts, view previous workouts, and generate training summarie

## Features

- Add new workouts
- Save workouts to a local text file
- View previous workouts
- View overall workout summary
- Track:
  - Sessions logged
  - Days trained
  - Total volume
  - Volume per lift
  - Max lifts
- Reset workout data
- Basic input validation

## Tech Used

- Python
- File handling
- CSV-style text storage
- Command-line interface

## How to Run

Make sure Python is installed.

Run:

```bash
python3 fitness_tracker.py
```

## Workout Format

Each workout records:

* Date
* Lift
* Weight
* Reps
* Sets

Supported lifts:

* Bench Press
* Squat
* Deadlift

## Example Summary

<pre class="overflow-visible! px-0!" data-start="845" data-end="1077"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>Sessions logged: 5</span><br/><span>Days trained: 4</span><br/><span>Total volume: 10485kg</span><br/><br/><span>Volume per lift:</span><br/><span>    - Bench Press: 3360kg</span><br/><span>    - Squat: 4875kg</span><br/><span>    - Deadlift: 2250kg</span><br/><br/><span>Max lifts:</span><br/><span>    - Bench Press: 85kg</span><br/><span>    - Squat: 125kg</span><br/><span>    - Deadlift: 150kg</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

## Future Improvements

* Add weekly progress summaries
* Add PR detection
* Add SQLite database storage
* Add charts and analytics
* Build a React frontend
* Turn into a full fitness dashboard
