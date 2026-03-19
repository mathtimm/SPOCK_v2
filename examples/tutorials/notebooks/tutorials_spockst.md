---
layout: default
title: Short-term scheduler
permalink: /examples/tutorials/notebooks/tutorials_spockstbundle install
---

# Short-term scheduling

Here we present the short-term scheduling module. The short-term scheduling module of spock has been concived to modify existing plan in order to add special or follow up observations, like transits or monitoring for instance.

> **Note:** Before you insert new observations and upload them please make sure you have informed the SPECULOOS consortium

## 1- Special target

> **WARNING:** First of all, users must ensure that they have entered requiered information of the target they wish to schedule in the **WG6 spread sheet**. Either under the tab `Annex_Targets_V2-STARS` for a external program observation without specific ephemeris or the tab `Annex_Targets_V1-PLANETS` if ephemeris (mostly transits) are required. 

### 1.1 For a special observation with given start/end time

Here is the existing `**night_blocks**` for a given `date` and a given `telescope`:

```python
import SPOCK.stats as SPOCKstats

SPOCKstats.read_night_plans_server(telescope='Io',date='2021-08-01')
```

First you want to create the **night_blocks**. The only essential information are:

the name of the site, ex: obs_name = 'SSO'

the name of the telescope (because there can be several telescope per site), ex: telescope ='Europa'

the date the night starts, ex: `day_of_night ='2020-12-12 15:00:00'`

and the name of your target, input_name = `'Trappist-1'`

start and end time in a list, ex: `start_end_range = ['2020-12-12 23:00:00','2020-12-13 01:00:00']``

> **Nota Bene:** you must first have filled info on the target on the WG6 spreadsheet beforehand

This is the block you wish to insert:

```python
import SPOCK.short_term_scheduler as SPOCKST
from astropy.time import Time

schedule = SPOCKST.Schedules()
schedule.load_parameters()
schedule.day_of_night = Time('2021-08-01 15:00:00')
schedule.observatory_name = 'SSO'
schedule.telescope = 'Io'
schedule.start_end_range = Time(['2021-08-02 04:00:00','2021-08-02 08:00:00'])
schedule.special_target_with_start_end(input_name="Nemesis-5")
```

Now you modify existing plan to insert your observation block:

```python
schedule.make_scheduled_table()
schedule.planification()
schedule.make_night_block()
```

Here is how the modified night_blocks looks like:

```python
display(schedule.scheduled_table_sorted)
```

### 1.2 For a special target that you wish to observe as much as possible

Here is the existing night_blocks for a given date and a given telescope:

```python
import SPOCK.stats as SPOCKstats

SPOCKstats.read_night_plans_server(telescope='Artemis',date='2020-12-10')
```

First you want to create the **night_blocks**. The only essential information needed are:

the name of the site, ex: `obs_name = 'SSO'`

the name of the telescope (because there can be several telescope per site), ex: `telescope = 'Europa'`

the date the night starts, ex: day_of_night = `'2020-12-12 15:00:00'`

and the name of your target, input_name = `'Trappist-1'`

> **Nota Bene:** you must first have filled info on the target in target_list_special.txt beforehand


```python
import SPOCK.short_term_scheduler as SPOCKST
from astropy.time import Time

schedule = SPOCKST.Schedules()
schedule.load_parameters()
schedule.day_of_night = Time('2020-12-10 15:00:00')
schedule.observatory_name = 'SNO'
schedule.telescope = 'Artemis'
schedule.special_target(input_name="WASP-85Ab")
schedule.make_scheduled_table()
schedule.planification()
schedule.make_night_block()
display(schedule.scheduled_table_sorted)
```


## 2- Follow up

Here is the existing night_blocks for a given date and a given telescope:

```python
import SPOCK.stats as SPOCKstats

SPOCKstats.read_night_plans_server(telescope='Artemis',date='2020-09-15')
```

here is an example of how to add a transit of TRAPPIST-1 b:

```python
import SPOCK.short_term_scheduler as SPOCKST
from astropy.time import Time

schedule = SPOCKST.Schedules()
schedule.load_parameters()
schedule.day_of_night = Time('2020-09-15 15:00:00')
schedule.observatory_name = 'SNO'
schedule.telescope = 'Artemis'
schedule.transit_follow_up(input_name="Trappist-1b")
schedule.make_scheduled_table()
schedule.planification()
schedule.make_night_block()
display(schedule.scheduled_table_sorted)
```

## 3- Save your plans and night blocks


If you are satisfied with this modified night_blocks you can save it. Executing this cell will update your local spock database. The night_blocks will be saved in `your_spock_path + "/DATABASE/telescope/Archive_night_blocks/"`


```python
schedule = SPOCKST.Schedules()
schedule.day_of_night = Time('2021-08-01 15:00:00')
schedule.telescope = 'Io'
SPOCKST.save_schedule(save=True,over_write=True,day=schedule.day_of_night,telescope=schedule.telescope)
```


Now that you have saved the night block it's time to create the ACP plans to send to the control PC of the corresponding telescope. To do so you just have to execute the cell below with the following information:

- `day`, start date you wish to make ACP plans for

- `nb_days`, number of days you wish to make plan for (starting at the date defined in `day`)

- `telescope`, name of the telescope at stake

ACP plans will be saved in `your_spock_path + "/DATABASE/telescope/Plans_by_date/"`


## 4- Make ACP and Astra format plans

```python 
SPOCKST.make_plans(day = schedule.day_of_night, nb_days=1, telescope = schedule.telescope)
```

Now you can upload these ACP plans and night_blocks to the [Cambridge Archive](https://www.mrao.cam.ac.uk/SPECULOOS/) as well as the plans sent to the control PCs. You will just need to provide:

- `day`, start date for which you wish to upload plans and night_blocks

- `nb_days`, number of days you wish to upload (starting at the date defined in `day`)

- `telescope`, name of the telescope at stake

## 5- Upload your plans and night_blocks on the control computers and archive

```python
SPOCKST.upload_plans(day=schedule.day_of_night, nb_days=1, telescope = schedule.telescope)
```

