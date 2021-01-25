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
"""Test-Environment for oneliner."""

from pathlib import Path

import pytest

from ai2business.kpi_collector import finance_collector as fnc
from ai2business.macros import oneliner


def test_four_step_trendsearch() -> None:

    result = oneliner.Search.four_step_trendsearch(keyword_list=["2019", "2020"])
    assert list(result.keys()) == [
        "get_interest_over_time",
        "get_interest_by_region",
        "get_related_topics",
        "get_related_queries",
    ]


def test_plotdata() -> None:

    ticker = fnc.FinanceCollector()
    builder = fnc.DesignerFinanceCollector(["GOOG"])
    ticker.builder = builder
    ticker.find_chart_histogram()
    folder = f"{test_plotdata.__name__}"
    oneliner.Plot.plotdata(
        builder.stock.return_product["get_chart_history"]["GOOG"],
        plot_type="lineplot",
        folder=folder,
    )
    assert len(list(Path(f"{folder}").glob("*.png"))) == 1


def test_plotdata_failed() -> None:

    ticker = fnc.FinanceCollector()
    builder = fnc.DesignerFinanceCollector(["GOOG"])
    ticker.builder = builder
    ticker.find_chart_histogram()
    folder = f"{test_plotdata_failed.__name__}"
    oneliner.Plot.plotdata(
        builder.stock.return_product["get_chart_history"]["GOOG"],
        plot_type="don_exist_plot",
        folder=folder,
    )
    assert len(list(Path(f"{folder}").glob("*.png"))) == 0

@pytest.mark.mpl_image_compare
def test_plotdata_show() -> None:

    ticker = fnc.FinanceCollector()
    builder = fnc.DesignerFinanceCollector(["GOOG"])
    ticker.builder = builder
    ticker.find_chart_histogram()
    folder = f"{test_plotdata_show.__name__}"
    oneliner.Plot.plotdata(
        builder.stock.return_product["get_chart_history"]["GOOG"],
        plot_type="lineplot",
        folder=folder,
        show_fig=True,
        save_fig=False,
    )
    assert len(list(Path(f"{folder}").glob("*.png"))) == 0
