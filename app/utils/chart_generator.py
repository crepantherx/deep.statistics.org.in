import matplotlib.pyplot as plt
import io
import base64
from typing import List, Dict


import matplotlib.pyplot as plt
import io
import base64
from typing import List, Dict

import matplotlib.pyplot as plt
import io
import base64
from typing import List, Dict

def generate_charts(data, headers, container_width=1200):

    charts = {
        "numerical_columns": [],
        "categorical_columns": [],
        "any_columns": []
    }

    # Calculate chart dimensions
    chart_width_pixels = int(container_width * 0.33)
    dpi = 96
    chart_width_inches = chart_width_pixels / dpi
    chart_height_inches = chart_width_inches * 0.75

    # Detect numerical and categorical columns
    numerical_cols = []
    categorical_cols = []

    for col_idx, header in enumerate(headers):
        try:
            _ = [float(row[col_idx]) for row in data]
            numerical_cols.append((col_idx, header))
        except ValueError:
            categorical_cols.append((col_idx, header))

    all_cols = [(i, h) for i, h in enumerate(headers)]

    # Helper function to convert Matplotlib figure to base64 HTML img tag
    def fig_to_html(fig):
        buf = io.BytesIO()
        fig.savefig(buf, format='png', bbox_inches='tight', dpi=dpi, transparent=True)
        buf.seek(0)
        img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
        buf.close()
        plt.close(fig)
        return f'<img src="data:image/png;base64,{img_base64}" />'

    # Set global text color to white
    plt.rcParams['text.color'] = 'white'
    plt.rcParams['axes.labelcolor'] = 'white'
    plt.rcParams['xtick.color'] = 'white'
    plt.rcParams['ytick.color'] = 'white'
    plt.rcParams['legend.facecolor'] = 'none'  # Transparent legend background
    plt.rcParams['legend.edgecolor'] = 'white'
    plt.rcParams['legend.labelcolor'] = 'white'  # Legend text color

    # Generate charts for numerical columns
    for col_idx, col_name in numerical_cols:
        if len(data) > 1:
            values = [float(row[col_idx]) for row in data if row[col_idx] != ""]
            fig, ax = plt.subplots(figsize=(chart_width_inches, chart_height_inches), facecolor='none')
            box = ax.boxplot(values, vert=True, patch_artist=True, labels=[col_name])
            ax.set_ylabel(col_name)
            legend = ax.legend([col_name], loc='best')
            # Ensure legend text is white
            for text in legend.get_texts():
                text.set_color('white')
            ax.set_facecolor('none')
            charts["numerical_columns"].append(fig_to_html(fig))

    # Generate charts for categorical columns
    for col_idx, col_name in categorical_cols:
        unique_values = set(row[col_idx] for row in data if row[col_idx])
        if len(unique_values) > 1:
            value_counts = {val: sum(1 for row in data if row[col_idx] == val) for val in unique_values}
            fig, ax = plt.subplots(figsize=(chart_width_inches, chart_height_inches), facecolor='none')
            ax.bar(value_counts.keys(), value_counts.values(), label=f'Bar - {col_name}')
            ax.set_xlabel(col_name)
            ax.set_ylabel('Count')
            legend = ax.legend()
            # Ensure legend text is white
            for text in legend.get_texts():
                text.set_color('white')
            plt.xticks(rotation=45, ha='right')
            ax.set_facecolor('none')
            charts["categorical_columns"].append(fig_to_html(fig))

    # Generate scatter plots for all columns
    for col_idx, col_name in all_cols:
        if len(data) > 1:
            values = [row[col_idx] for row in data if row[col_idx] != ""]
            try:
                values = [float(v) for v in values]
                fig, ax = plt.subplots(figsize=(chart_width_inches, chart_height_inches), facecolor='none')
                ax.scatter(range(len(values)), values, label=f'Scatter - {col_name}')
                ax.set_ylabel(col_name)
                legend = ax.legend()
                # Ensure legend text is white
                for text in legend.get_texts():
                    text.set_color('white')
                ax.set_facecolor('none')
                charts["any_columns"].append(fig_to_html(fig))
            except ValueError:
                continue

    return charts