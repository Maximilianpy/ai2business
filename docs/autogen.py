import os
from pathlib import Path

import keras_autodoc
import tutobooks

PAGES = {
    "AutoML_for_NeuralNetworks.md": [
        "ai2business.ai_engines.automl_neural_network.AutoMLModels",
    ],
    "Key_Performance_Collection.md": [
        "ai2business.kpi_collector.trends_collector.TrendsCollector",
        "ai2business.kpi_collector.finance_collector.FinanceCollector",
    ],
    "Data_Visualization.md": [
        "ai2business.visualization.data_visualization.DataVisualization",
        "ai2business.visualization.data_visualization.DataVisualization.visual_missing_data",
        "ai2business.visualization.data_visualization.DataVisualization.lineplot",
        "ai2business.visualization.data_visualization.DataVisualization.pointplot",
        "ai2business.visualization.data_visualization.DataVisualization.scatterplot",
        "ai2business.visualization.data_visualization.DataVisualization.swarmplot",
        "ai2business.visualization.data_visualization.DataVisualization.distributionplot",
        "ai2business.visualization.data_visualization.DataVisualization.relationalplot",
        "ai2business.visualization.data_visualization.DataVisualization.categoryplot",
        "ai2business.visualization.data_visualization.DataVisualization.boxplot",
        "ai2business.visualization.data_visualization.DataVisualization.stripplot",
        "ai2business.visualization.data_visualization.DataVisualization.hexagonplot",
        "ai2business.visualization.data_visualization.DataVisualization.histogramplot",
        "ai2business.visualization.data_visualization.DataVisualization.violinplot",
        "ai2business.visualization.data_visualization.DataVisualization.residualplot",
        "ai2business.visualization.data_visualization.DataVisualization.regressionplot",
        "ai2business.visualization.data_visualization.DataVisualization.densitymap",
        "ai2business.visualization.data_visualization.DataVisualization.clustermap",
        "ai2business.visualization.data_visualization.DataVisualization.heatmap",
        "ai2business.visualization.data_visualization.DataVisualization.correlationmap",
        "ai2business.visualization.data_visualization.DataVisualization.pairmap",
        "ai2business.visualization.data_visualization.DataVisualization.swarmplot",
    ],
    "Sample_Generators.md": [
        "ai2business.datasets.sample_generator.SampleGenerators",
    ],
    "Oneliner.md": [
        "ai2business.macros.oneliner.Search",
        "ai2business.macros.oneliner.Search.four_step_trendsearch",
        "ai2business.macros.oneliner.Plot",
        "ai2business.macros.oneliner.Plot.plotdata",
    ],
}


aliases_needed = [
    "tensorflow.keras.callbacks.Callback",
    "tensorflow.keras.losses.Loss",
    "tensorflow.keras.metrics.Metric",
    "tensorflow.data.Dataset",
]


ROOT = "https://ai2business.github.io/ai2business/"

ai2business_dir = Path(__file__).resolve().parents[1]


def py_to_nb_md(dest_dir, dir_path="tutorials"):
    for file_path in os.listdir(f"{dir_path}/"):

        file_name = file_path
        py_path = os.path.join(dir_path, file_path)
        file_name_no_ext = os.path.splitext(file_name)[0]
        ext = os.path.splitext(file_name)[1]

        if ext != ".py":
            continue

        nb_path = os.path.join("ipynb", file_name_no_ext + ".ipynb")
        md_path = os.path.join(dest_dir, "tutorials", file_name_no_ext + ".md")

        Path(nb_path).parent.mkdir(exist_ok=True)
        Path(md_path).parent.mkdir(exist_ok=True)

        tutobooks.py_to_nb(py_path, nb_path, fill_outputs=True)
        tutobooks.py_to_md(py_path, nb_path, md_path, "templates/img")
        github_repo_dir = "ai2business/ai2business/blob/main/docs/"
        with open(md_path, "r") as md_file:
            button_lines = [
                ":material-link: "
                "[**View in Colab**](https://colab.research.google.com/github/"
                + github_repo_dir
                + "ipynb/"
                + file_name_no_ext
                + ".ipynb"
                + ")   &nbsp; &nbsp;"
                + '<span class="k-dot">•</span>'
                + ":material-github: "
                "[**GitHub source**](https://github.com/"
                + github_repo_dir
                + "tutorials/"
                + file_name_no_ext
                + ".py)",
                "\n",
            ]
            md_content = "".join(button_lines) + "\n" + md_file.read()

        with open(md_path, "w+") as md_file:
            md_file.write(md_content)


def generate(dest_dir):
    api_dir = ai2business_dir / "docs" / "api"
    template_dir = ai2business_dir / "docs" / "templates"
    doc_generator = keras_autodoc.DocumentationGenerator(
        PAGES,
        "https://github.com/ai2business/ai2business/blob/main",
        api_dir,
        template_dir,
        # ai2business_dir / 'examples',
        extra_aliases=aliases_needed,
    )
    doc_generator.generate(dest_dir)
    readme = (ai2business_dir / "README.md").read_text()
    index = (template_dir / "index.md").read_text()
    index = index.replace("{{autogenerated}}", readme[readme.find("##") :])
    (dest_dir / "index.md").write_text(index, encoding="utf-8")
    py_to_nb_md(dest_dir)


if __name__ == "__main__":
    generate(ai2business_dir / "docs" / "src")
