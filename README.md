````markdown


---

## Data

- **Raw traces**

  - `sample_raw_trace.csv`, `query_output.csv` → demo outputs from Waggle queries  
  - Full 30s raw traces are too large; re-download from the [Waggle repository](https://github.com/waggle-sensor/waggle/blob/master/data/README.md)  

- **Metadata**

  - `nodes.csv` → node IDs, locations  
  - `sensors.csv` → sensor types and parameters  
  - `provenance.csv` → provenance records  

- **Aggregated data**

  - `aot_aggregated_10min.csv`  
  - `aot_aggregated_1hour.csv`  
  - `sample_aggregated_[10min|30min|1hour].csv`  
  - `pseudo_labels_dbscan_kmeans_1hour.csv`  

The complete AoT dataset can also be accessed here: [Array of Things](https://arrayofthings.github.io/index.html).

---

## Notebooks

1. **01_data_description.ipynb** → overview of nodes, sensors, metadata  
2. **02_query_waggle.ipynb** → querying raw traces from Waggle  
3. **03_aggregation.ipynb** → aggregation at 10min / 30min / 1hr  
4. **04_visualizations.ipynb** → visualizations (with final paper plots imported)  
5. **05_clustering_labeling.ipynb** → clustering sensor nodes & pseudo-label generation  
6. **06_modeling_evaluation.ipynb** → example ML evaluation with annotated data  

---

## Installation

Clone the repo and install requirements:

```bash
git clone <your-repo-link>
cd <your-repo>
pip install -r requirements.txt
# Aggregation Scripts

This folder contains scripts for aggregating Array of Things (AoT) sensor data into different temporal resolutions.  
These scripts were used to generate the 10-minute, 30-minute, and 1-hour datasets provided in [`/data/aggregated`](../../data/aggregated).

---

## Contents

- **time_slicer.py**  
  Custom script for slicing raw Waggle traces into 10-minute, 30-minute, or 1-hour intervals.  
  - Input: raw AoT CSV file  
  - Output: aggregated CSV (saved in `/data/aggregated/`)  

- **dataReduction.py**  
  AoT utility script for reducing large datasets by filtering or compressing records.  

- **split-into-dates.py**  
  AoT utility script to split large raw files into smaller per-day CSVs.  

- **slice-date-range.py**  
  AoT utility script for extracting a subset of data between specific start and end dates.  

---

## Usage

Aggregate raw traces into hourly intervals using `time_slicer.py`:

```bash
python time_slicer.py --input ../data/raw/sample_raw_trace.csv --interval 1h --output ../data/aggregated/aot_aggregated_1hour.csv
````

Aggregate into 10-minute intervals:

```bash
python time_slicer.py --input ../data/raw/sample_raw_trace.csv --interval 10min --output ../data/aggregated/aot_aggregated_10min.csv
```

Split a large raw file into daily subsets:

```bash
python split-into-dates.py --input raw_traces.csv --output-dir ./daily/
```

Reduce a dataset to specific fields:

```bash
python dataReduction.py --input raw.csv --fields timestamp,node_id,sensor,value --output reduced.csv
```

Extract a specific date range:

```bash
python slice-date-range.py --input raw.csv --start 2020-01-01 --end 2020-01-07 --output week1.csv
```

---

## Notes

* The aggregated CSVs in `/data/aggregated/` were generated using these scripts.
* Users are encouraged to re-run the scripts with raw Waggle traces to reproduce results or generate additional aggregates.
* These utilities (except `time_slicer.py`) are official AoT/Waggle scripts and are included here for convenience.
* For complete raw data access, please refer to Waggle’s data portal and the query scripts provided in this repository.

---

## References

Parts of this folder include **official Array of Things (AoT) / Waggle utility scripts**.
To preserve their context, the original documentation from AoT is included below.

---

### Official AoT README (for reference)

# Data Aggregation and Reduction Scripts

This set of scripts is provided by the Array of Things (AoT) / Waggle project for working with raw sensor data.
They allow users to reduce, slice, and split large datasets into smaller, more manageable pieces.

## Scripts

* **dataReduction.py**
  Reduces large datasets by filtering records or removing unused fields.

* **split-into-dates.py**
  Splits a large CSV file into multiple daily CSV files based on timestamp.

* **slice-date-range.py**
  Extracts a subset of data between a specified start and end date.

## Usage Examples

Reduce a dataset to include only certain fields:

```bash
python dataReduction.py --input raw.csv --fields timestamp,node_id,sensor,value --output reduced.csv
```

Split a dataset into daily files:

```bash
python split-into-dates.py --input raw.csv --output-dir ./daily/
```

Extract data from a specific date range:

```bash
python slice-date-range.py --input raw.csv --start 2020-01-01 --end 2020-01-07 --output week1.csv
```

## Notes

* These scripts are designed for flexibility in working with raw AoT data.
* For aggregation into specific intervals (10min, 30min, 1hr), use the custom `time_slicer.py` script provided in this repo.

```
```
