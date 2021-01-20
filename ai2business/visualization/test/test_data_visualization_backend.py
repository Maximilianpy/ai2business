# Copyright 2020 AI2Business. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Test-Environment for data_visualization."""

import time
from pathlib import Path

import numpy as np
import pandas as pd
import seaborn as sns

from ai2business.macros import oneliner as one
from ai2business.visualization import data_visualization as dav

df_nan = pd.DataFrame(
    np.random.randn(5, 3),
    index=["a", "c", "e", "f", "h"],
    columns=["one", "two", "three"],
)
df_nan["four"] = "bar"
df_nan["five"] = df_nan["one"] > 0
df_nan = df_nan.reindex(["a", "b", "c", "d", "e", "f", "g", "h"])

time.sleep(180)
df_dict_years = one.TrendSearch.four_step_search(
    keyword_list=[
        "2018",
        "2019",
        "2020",
        "2021",
    ]
)


def test_visual_missing_data():
    data = dav.DataVisualization()
    builder = dav.DesignerDataVisualization(df_nan)
    data.builder = builder
    data.visual_missing_data()
    result = builder.data_figure.return_product
    for i, key in enumerate(result.keys()):
        result[key].savefig(Path(f"./test_visual_missing_data_{key}.png"))

    assert len(list(Path(".").glob("test_visual_missing_data_*.png"))) == i + 1


def test_list_product_parts():
    # Test return of products
    data = dav.DataVisualization()
    builder = dav.DesignerDataVisualization(df_nan)
    data.builder = builder
    data.visual_missing_data()
    result = builder.data_figure.list_product_parts

    assert (
        result
        == "Product parts: get_nullity_matrix, get_nullity_bar, get_nullity_heatmap, get_nullity_dendrogram"
    )


def test_save_all_figures():
    data = dav.DataVisualization()
    builder = dav.DesignerDataVisualization(df_nan)
    data.builder = builder
    data.visual_missing_data()
    builder.data_figure.save_all_figures(folder="tmp")
    assert len(list(Path("tmp").glob("*.png"))) == 4


iris_dataframe = sns.load_dataset("iris")


def test_lineplot_white():
    data = dav.DataVisualization()
    builder = dav.DesignerDataVisualization(iris_dataframe)
    data.builder = builder
    data.lineplot()
    folder = "tmp_white"
    builder.data_figure.save_all_figures(folder=folder)
    assert len(list(Path(f"{folder}").glob("*.png"))) == 1


def test_lineplot_dark():
    data = dav.DataVisualization()
    builder = dav.DesignerDataVisualization(
        df_dict_years["get_interest_over_time"],
        dark_mode=True,
    )
    data.builder = builder
    data.lineplot()
    folder = "tmp_dark"
    builder.data_figure.save_all_figures(folder=folder)
    assert len(list(Path(f"{folder}").glob("*.png"))) == 1


def test_lineplot_whitegrid():
    data = dav.DataVisualization()
    builder = dav.DesignerDataVisualization(iris_dataframe, grid=True)
    data.builder = builder
    data.lineplot()
    folder = "tmp_whitegrid"
    builder.data_figure.save_all_figures(folder=folder)
    assert len(list(Path(f"{folder}").glob("*.png"))) == 1


def test_lineplot_darkgrid():
    data = dav.DataVisualization()
    builder = dav.DesignerDataVisualization(iris_dataframe, dark_mode=True, grid=True)
    data.builder = builder
    data.lineplot()
    folder = "tmp_darkgrid"
    builder.data_figure.save_all_figures(folder=folder)
    assert len(list(Path(f"{folder}").glob("*.png"))) == 1
