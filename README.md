```markdown
# AoT Air Quality Data Annotation

This repository supports the paper **“LLM-based Air Quality Data Annotation using AoT Sensors”**, providing datasets, utilities, and example workflows.

---

## Repository Structure

```

data/         → Datasets

raw/          → Sample raw traces (30s intervals)

metadata/     → Sensor/node metadata (nodes.csv, sensors.csv, provenance.csv)

aggregated/   → Aggregated datasets (10min, 30min, 1hr) + pseudo-labels

docs/         → Research paper (PDF)

figures/      → Final plots used in the paper

notebooks/    → Step-by-step Jupyter notebooks (01–06)

scripts/      → Utilities for aggregation, querying, and plotting

````

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
````

---

## Usage

Run any notebook in `notebooks/` step by step:

```bash
jupyter notebook notebooks/01_data_description.ipynb
```

Raw traces can also be re-downloaded from Waggle, and custom aggregation/plotting utilities are provided in the `scripts/` folder.

---

## Citation

If you use this dataset or code, please cite:

```
Ragini Gupta*, Abbas Ali Mirza*, Claudiu Danilov+, Josh Eckhardt+, Keyshla Bernard+, Klara Nahrstedt*  
*University of Illinois Urbana-Champaign, IL, USA, +Boeing Research and Technology, USA  
{ragingi2, abbasam2, klara}@illinois.edu, {cdanilov, josh.d.eckhardt, keyshla.j.bernard}@boeing.com
```
