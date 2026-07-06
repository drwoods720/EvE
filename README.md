# EvE
EvE - (EvE)aluates Various modEls

EvE is a cell segmentation model evaluation tool. The aim for EvE was to create 
a quantitative method to evaluate the results of a cell segmentation model without
requiring a manually generated segmentation mask to compare to.

## Inputs

EvE takes a path to a single **input directory**. That directory must contain two types of files:

### 1. Labeled mask files (`.tif`)

Segmentation masks to evaluate, provided as **labeled masks:** each cell's pixels are assigned
a unique integer ID, distinguishing it from every other cell in the image. Background pixels have the value `0`.

#### File naming pattern

Mask filenames must follow this naming pattern:

`{image_name}.ome.tif - Image{n}_{model_name}_label.tif`

Example:

`CellDIVE_SLIDE-123_A-1.ome.tif - Image0_cellpose_label.tif`

| Field | Description |
|-------|-------------|
| {image_name} | Name of the original image (matches the corresponding `.ome.tif` file) |
| {n} | Image index number (optional, may be omitted) |
| {model_name} | Name of the model or method used to generate the mask |



### 2. GeoJSON annotation files (`.geojson`)

Annotation data exported from QuPath, corresponding to each sample.

#### File naming pattern

GeoJSON files must follow this naming pattern:

`{image_name}.ome.tif - Image{n}.geojson`

Example:

`CellDIVE_SLIDE-123_A-1.ome.tif - Image1.geojson`

| Field | Description |
|-------|-------------|
| {image_name} | Name of the original image. This must exactly match the `{image_name}` in the corresponding mask filename |
| {n} | Image index number (optional, may be omitted) |

#### Each file must contain at least the following annotation types
| Annotation Type | Geometry Type | Description |
|-----------------|---------------|-------------|
| Sample area | Polygon | Defines the region of the mask to include in evaluation. Exactly one per file. This annotation must be named "cell_segmentation_sample_area" |
| Point annotations | MultiPoint | Individual annotated points marking the center of each cell. |

## Outputs
Outputs are written to a specified output directory.
If no output directory is specified outputs will be written to a directory alongside
the input directory.


# Installing

## Option 1: Run using the Apptainer container (recommended)

### Prerequisites
- Apptainer 1.5+
  
### Getting the container

#### Download pre-built container from Github
Download the .sif file from the [releases](https://github.com/drwoods720/EvE/releases) section.

#### Or build locally
Clone the repository
```bash
git clone https://github.com/drwoods720/EvE.git
```

Navigate to the apptainer directory
```bash
cd EvE/apptainer
```

Build the container
```bash
apptainer build eve.sif eve.def
```

### Run
```bash
apptainer run eve.sif --help
```

## Option 2: Run locally

### Prerequisites
- Python 3.14+
- pip

### Clone the repository
```bash
git clone https://github.com/drwoods720/EvE.git
cd EvE
```
### Create a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```
### Install dependencies
```bash
pip install -r requirements.txt
```
### Run
```bash
python eve.py --help
```

# Usage

Running EvE can be done directly with python or using the Apptainer container.

## Apptainer container

Basic usage:
``` bash
apptainer run eve.sif -i [/path/to/input] -o [/path/to/output]
```

## Options
| Option | Description |
|----------|-------------|
| `-h` or `--help` | Show the help message and exit. |
| `-i` or `--input` | **(Required)** Specify the input directory. |
| `-o` or `--output` | Specify the output directory. |
| `-w` or `--workers` | Specify the maximum number of parallel processors. |

Future of this document:
1. How to install (done)
2. How to run
3. What inputs it takes
4. What outputs it gives
5. What processing it does
