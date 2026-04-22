---
layout: default
title: Long-term scheduler
permalink: /examples/tutorials/notebooks/tutorials_spocklt
---

# Long-term Scheduling

This section presents the **long-term scheduling module** of **SPOCK**.

The long-term scheduler is designed to **optimize the planning of targets**
on the SPECULOOS telescopes (SSO, SNO, Saint-Ex, TS, TN), while following the
observing strategy defined by the consortium.

> **Note:** Before inserting new observations and uploading them, please make sure that the **SPECULOOS consortium has been informed**.

---

## Making schedules

To create **night blocks** for a given date range, the following information
is required:

- **Observatory name**, for example:
  `obs_name = "SSO"`
- **Telescope name**, for example:
  `telescope = "Io"`
- **Date range**, provided as a list:
  `date_range = ["2021-08-01 15:00:00", "2021-08-02 15:00:00"]`

## Example

```python 
import SPOCK.long_term_scheduler as SPOCKLT
from astropy.time import Time

schedule = SPOCKLT.Schedules()
schedule.observatory_name = "SSO"
schedule.telescope = "Io"
schedule.load_parameters(
    date_range=["2021-08-01 15:00:00", "2021-08-02 15:00:00"]
    )

schedule.make_schedule(
    Altitude_constraint=28,
    Moon_constraint=30
    )
```

To inspect the night blocks for a given day:


`display(schedule.night_block_by_day[0])`

---

## Saving schedules

To save the schedules that have just been created, use the
`save_schedule` function. You must specify the telescope name and
the date range to be saved.


```python 
SPOCKLT.save_schedule(
    save=True,
    over_write=True,
    date_range=schedule.date_range,
    telescope=schedule.telescope
    )
```

---

## Making plans

ACP and Astra plans can be generated directly from the saved night blocks:

```python
SPOCKLT.make_plans(
    day=schedule.date_range[0],
    nb_days=schedule.date_range_in_days,
    telescope=schedule.telescope
    )
```

---

## Uploading plans

Once the plans are generated, they can be uploaded to both the
telescope control computer and the Cambridge archive:

```python 
SPOCKLT.upload_plans(
    day=schedule.date_range[0],
    nb_days=schedule.date_range_in_days,
    telescope=schedule.telescope
    )
````

This completes the long-term scheduling workflow.