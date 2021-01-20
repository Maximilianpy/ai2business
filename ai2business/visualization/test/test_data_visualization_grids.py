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


from pathlib import Path

import seaborn as sns

from ai2business.visualization import data_visualization as dav

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
        iris_dataframe,
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
