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
"""Here all `oneliner` functions listed.

!!! note "What is an `oneliner`?"
        `oneliner` is a function that can be executed in one line and contains all essential
        parameters. No further introductions are needed.
.
"""
from abc import ABC, abstractmethod
from typing import Union

import matplotlib.pyplot as plt
import pandas as pd
from toml import load

from ai2business.kpi_collector import trends_collector
from ai2business.visualization import data_visualization


class OnlinerSearch(ABC):
    """OnlinerSearch contains the abstract methods of the class `Search`.

    Args:
        ABC (class): Helper class that provides a standard way to create an ABC using inheritance.
    """

    @abstractmethod
    def four_step_trendsearch() -> None:
        """Abstract method of four_step_trendsearch."""


class Search(OnlinerSearch):
    """Collection of `oneliner` for searching."""

    def four_step_trendsearch(
        keyword_list: list,
        timeframe: str = "today 5-y",
        language: str = "en-US",
        category: int = 0,
        timezone: int = 360,
        country: str = "",
        property_filter="",
        resolution: str = "COUNTRY",
        **kwargs,
    ) -> dict:
        """four step search

        A four step search includes:

        1. Overtime
        2. By regions
        3. By related topics
        4. By related queries

        Args:
            keyword_list (list): Keyword-list with the items to search for.
            timeframe (str, optional): Time frame, respectively, period to search for.
            Defaults to "today 5-y".
            language (str, optional): Search language. Defaults to "en-US".
            category (int, optional): Define a specific [search category](https://github.com/pat310/google-trends-api/wiki/Google-Trends-Categories). Defaults to 0.
            timezone (int, optional): [Search timezone](https://developers.google.com/maps/documentation/timezone/overview). Defaults to 360.
            country (str, optional): The country, where to search for. Defaults to "".
            property_filter (str, optional): Property filer of the search; only in news, images, YouTube, shopping. Defaults to "".
            resolution (str, optional): The resolution / zoom-factor, where to search for. Defaults to "COUNTRY".

        Returns:
            dict: Dictionary with the keys: 'interest_over_time', 'interest_by_region', 'related_topics', 'related_queries' and its dataframes.
        """
        trends = trends_collector.TrendsCollector()
        builder = trends_collector.DesignerTrendsCollector(
            keyword_list=keyword_list,
            timeframe=timeframe,
            language=language,
            category=category,
            timezone=timezone,
            country=country,
            property_filter=property_filter,
            **kwargs,
        )
        trends.builder = builder
        trends.find_interest_over_time()
        trends.find_interest_by_region(resolution=resolution)
        trends.find_related_topics()
        trends.find_related_queries()
        return builder.trends.return_product


class OnlinerPlot(ABC):
    """OnlinerPlot contains the abstract methods of the class `Plot`.

    Args:
        ABC (class): Helper class that provides a standard way to create an ABC using inheritance.
    """

    @abstractmethod
    def plotdata() -> None:
        """Abstract method of plotdata."""


class Plot(OnlinerPlot):
    """Collection of `oneliner` for plotting."""

    def plotdata(
        df: pd.DataFrame,
        plot_type: str = "lineplot",
        dark_mode: bool = False,
        grid: bool = False,
        figsize: tuple = (12, 8),
        dpi: int = 300,
        save_fig: bool = True,
        show_fig: bool = False,
        x_label: str = None,
        y_label: str = None,
        hue: str = None,
        palette: Union[str, list, dict] = None,
        folder: str = None,
        **kwargs,
    ) -> None:
        """Plotting all pandas dataframes as `oneliner`.

        !!! warning
            All defined functions of`ai2business.visualization.data_visualization` will be
            called via `getattr`, so be sure that the `class DataVisualization` function
            is typed correctly.

        Args:
            df (pd.DataFrame): [description]
            plot_type (str, optional): [description]. Defaults to "lineplot".
            dark_mode (bool, optional): [description]. Defaults to False.
            grid (bool, optional): [description]. Defaults to False.
            figsize (tuple, optional): [description]. Defaults to (12, 8).
            dpi (int, optional): [description]. Defaults to 300.
            save_fig (bool, optional): [description]. Defaults to True.
            show_fig (bool, optional): [description]. Defaults to False.
            x_label (str, optional): [description]. Defaults to None.
            y_label (str, optional): [description]. Defaults to None.
            hue (str, optional): [description]. Defaults to None.
            palette (Union[str, list, dict], optional): [description]. Defaults to None.
            folder (str, optional): [description]. Defaults to None.
        """
        data = data_visualization.DataVisualization()
        builder = data_visualization.DesignerDataVisualization(
            df,
            dark_mode=dark_mode,
            grid=grid,
            figsize=figsize,
            dpi=dpi,
            x_label=x_label,
            y_label=y_label,
            hue=hue,
            palette=palette,
        )
        data.builder = builder
        try:
            getattr(data, plot_type.lower())(**kwargs)
        except AttributeError as exc:
            print(f"ERROR: {exc}")
        if save_fig:
            builder.data_figure.save_all_figures(folder=folder)
        if show_fig:
            plt.show()
