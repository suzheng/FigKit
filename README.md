# Generating Figures with Centralized Styling and PDF Combining

This repository provides a framework to generate consistent, publication-quality figures using centralized configurations for constants, figure styles, and an efficient method to combine individual figure PDFs into composite figures. It is designed to streamline the figure creation process for researchers and data scientists preparing figures for academic publications.

## Table of Contents

- [Idea](#idea)
- [Features](#features)
- [File Structure](#file-structure)
- [Configuration](#configuration)
- [Usage](#usage)
  - [1. Centralized Figure Styling](#1-centralized-figure-styling)
  - [2. Centralized Constants with JSON](#2-centralized-constants-with-json)
  - [3. Combining PDFs into Composite Figures](#3-combining-pdfs-into-composite-figures)
- [Example Notebooks](#example-notebooks)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## Idea

The primary idea of this repository is to:

- **Centralize Constants**: Use a JSON configuration file (`config.json`) to define constants such as sample names, group names, colors, and figure dimensions. This ensures consistency across all figures and simplifies updates.
- **Centralize Figure Styles**: Implement a `FigureStyle` class to apply consistent styling to all figures, adhering to publication standards.
- **Efficiently Combine Figures**: Provide a `combine_pdf_figures` function to merge individual figure PDFs into composite figures, managing layouts and labels automatically.

## Features

- **Consistency**: Centralized styles and constants ensure that all figures have a uniform appearance.
- **Ease of Use**: Simple functions and classes abstract away complex styling and combining operations.
- **Flexibility**: Easily customize colors, fonts, figure sizes, and more through the configuration file.
- **Reproducibility**: Scripts and notebooks are organized for clarity and ease of reproduction.

## File Structure

```
project/
├── data/
│   └── config.json               # Centralized configuration file
├── figures/                      # Output directory for generated figures
│   ├── bar_plot1.pdf
│   ├── bar_plot2.pdf
│   ├── bar_plot3.pdf
│   ├── box_plot1.pdf
│   ├── box_plot2.pdf
│   ├── combined_figure1.pdf
│   ├── combined_figure2.pdf
│   ├── combined_figure3.pdf
│   ├── heatmap1.pdf
│   ├── heatmap2.pdf
│   ├── line_plot1.pdf
│   ├── line_plot2.pdf
│   ├── roc_curve1.pdf
│   ├── roc_curve2.pdf
│   ├── scatter_plot1.pdf
│   └── scatter_plot2.pdf
├── notebooks/
│   ├── plot_bar.ipynb            # Notebook for bar plot examples
│   ├── plot_box.ipynb            # Notebook for box plot examples
│   ├── plot_heatmap.ipynb        # Notebook for heatmap examples
│   ├── plot_line.ipynb           # Notebook for line plot examples
│   ├── plot_roc.ipynb            # Notebook for ROC curve examples
│   ├── plot_scatter.ipynb        # Notebook for scatter plot examples
│   └── combine_pdfs.ipynb        # Example notebook to combine figure PDF
├── src/
│   └── utils/
│       ├── __init__.py
│       ├── combine_pdfs.py       # Function to combine PDFs
│       ├── figure_style.py       # FigureStyle class for styling
│       └── json_data_reader.py   # JSONDataReader class to read config
├── requirements.txt              # List of required Python packages
└── README.md                     # This README file
```

## Configuration

### `config.json`

This example JSON file centralizes constants and configurations:

```json
{
    "sample_names": ["Sample A", "Sample B", "Sample C"],
    "group_names": ["Control", "Treatment"],
    "sample_colors": {
        "Sample A": "#1f77b4",
        "Sample B": "#ff7f0e",
        "Sample C": "#2ca02c"
    },
    "group_colors": {
        "Control": "#1f77b4",
        "Treatment": "#ff7f0e"
    },
    "figure_dimensions": {
        "one_third_fig_width": 2.3,
        "half_fig_width": 3.5,
        "full_fig_width": 7.0,
        "fig_height_a0": 2.2,
        "fig_height_a": 2.8,
        "fig_height_b": 3.3
    }
}
```

- **Sample names in sample_names and sample_colors have to match**
- **Group names in group_names and group_colors have to match**

## Usage

### 1. Centralized Figure Styling

Use the `FigureStyle` class from `src/utils/figure_style.py` to apply consistent styling to your figures.

**Note**
- After updating the `src/utils/figure_style.py`, you need to restart your jupyter notebook (by clicking the `Restart` button) to re-import the `FigureStyle` class to take effect.

**Example:**

```python
from utils.figure_style import FigureStyle

# Create an instance of FigureStyle
style_config = FigureStyle()

# Apply the style settings
style_config.apply()

# Generate your plot (e.g., using matplotlib or seaborn)
import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots()
sns.barplot(x='Sample', y='Value', data=your_data, ax=ax)

# Customize titles and labels
style_config.set_titles(ax, 'Your Plot Title')
style_config.set_labels(ax, 'X-axis Label', 'Y-axis Label')

# Save the figure
style_config.save_figure('figures/your_figure.pdf')
```

### 2. Centralized Constants with JSON

Use the `JSONDataReader` class from `src/utils/json_data_reader.py` to read constants from `config.json`.

**Example:**

```python
from utils.json_data_reader import JSONDataReader

# Read the configuration
json_reader = JSONDataReader('data/config.json')

# Access constants
sample_names = json_reader.get('sample_names')
sample_colors = json_reader.get('sample_colors')
figure_dimensions = json_reader.get('figure_dimensions')

# Use constants in your code
print(f"Samples: {sample_names}")
print(f"Sample Colors: {sample_colors}")
```

### 3. Combining PDFs into Composite Figures

Use the `combine_pdf_figures` function from `src/utils/combine_pdfs.py` to merge individual figure PDFs.

**Example:**

```python
from utils.combine_pdfs import combine_pdf_figures

# List of PDF files to combine
pdf_files = [
    'figures/bar_plot1.pdf',
    'figures/bar_plot2.pdf',
    'figures/bar_plot3.pdf'
]

# Labels for each subfigure
labels = ['a', 'b', 'c']

# Define the number of columns per row
cols_per_row = [2, 1]  # First row has 2 columns, second row has 1 column

# Combine the PDFs
combine_pdf_figures(pdf_files, 'figures/combined_figure.pdf', labels, cols_per_row)
```

- **`pdf_files`**: List of paths to individual figure PDFs.
- **`labels`**: List of labels (e.g., ['a', 'b', 'c']) to annotate subfigures.
- **`cols_per_row`**: List specifying the number of columns in each row.
  - Example: `[2]` means one row with two columns.
  - Example: `[2, 1]` means first row with two columns, second row with one column.

## Example Notebooks

The `notebooks/` directory contains Jupyter notebooks for generating various types of plots:

- `plot_bar.ipynb`: Generates bar plots using sample data.
- `plot_box.ipynb`: Creates box plots.
- `plot_line.ipynb`: Produces line plots for time series data.
- `plot_scatter.ipynb`: Generates scatter plots with group coloring.
- `plot_heatmap.ipynb`: Creates heatmaps from correlation matrices.
- `plot_roc.ipynb`: Plots ROC curves for binary classification.
- `combine_pdfs.ipynb`: Demonstrates how to combine individual PDFs into composite figures.


## Requirements

- Python 3.6 or higher
- Required Python packages (listed in `requirements.txt`):
  - matplotlib
  - seaborn
  - numpy
  - pandas
  - scikit-learn
  - PyMuPDF

**Install Packages:**

```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

---

Enjoy creating consistent and publication-ready figures!