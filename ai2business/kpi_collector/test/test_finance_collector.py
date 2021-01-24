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
"""Test-Environment for finance_collector."""
import pandas as pd

from ai2business.kpi_collector import finance_collector as fnc

ticker = fnc.FinanceCollector()
builder = fnc.DesignerFinanceCollector(["SPY", "AAPL", "MSFT"])
ticker.builder = builder


def test_find_chart_history():
    ticker.find_chart_histogram()
    assert type(builder.stock.return_product["get_chart_history"]) == type(dict())


def test_find_isin_code():
    ticker.find_isin_code()
    assert type(builder.stock.return_product["get_isin_code"]) == type(dict())


def test_find_major_holders_dict():
    ticker.find_major_holders()
    assert type(builder.stock.return_product["get_major_holders"]) == type(dict())


def test_find_institutional_holders():
    ticker.find_institutional_holders()
    assert type(builder.stock.return_product["get_institutional_holders"]) == type(
        dict()
    )


def test_find_mutualfund_holders():
    ticker.find_mutualfund_holders()
    assert type(builder.stock.return_product["get_mutualfund_holders"]) == type(dict())


def test_find_dividends():
    ticker.find_dividends()
    assert type(builder.stock.return_product["get_dividends"]) == type(dict())


def test_find_splits():
    ticker.find_splits()
    assert type(builder.stock.return_product["get_splits"]) == type(dict())


def test_find_actions():
    ticker.find_actions()
    assert type(builder.stock.return_product["get_actions"]) == type(dict())


def test_find_info():
    ticker.find_info()
    assert type(builder.stock.return_product["get_info"]) == type(dict())


def test_find_calendar():
    ticker.find_calendar()
    assert type(builder.stock.return_product["get_calendar"]) == type(dict())


def test_find_recommendation():
    ticker.find_recommendations()
    assert type(builder.stock.return_product["get_recommendations"]) == type(dict())


def test_find_earnings():
    ticker.find_earnings()
    assert type(builder.stock.return_product["get_earnings"]) == type(dict())


def test_find_quarterly_earnings():
    ticker.find_quarterly_earnings()
    assert type(builder.stock.return_product["get_quarterly_earnings"]) == type(dict())


def test_find_financials():
    ticker.find_financials()
    assert type(builder.stock.return_product["get_financials"]) == type(dict())


def test_find_quarterly_financials():
    ticker.find_quarterly_financials()
    assert type(builder.stock.return_product["get_quarterly_financials"]) == type(
        dict()
    )


def test_find_balancesheet():
    ticker.find_balancesheet()
    assert type(builder.stock.return_product["get_balancesheet"]) == type(dict())


def test_find_quarterly_balancesheet():
    ticker.find_quarterly_balancesheet()
    assert type(builder.stock.return_product["get_quarterly_balancesheet"]) == type(
        dict()
    )


def test_find_cashflow():
    ticker.find_cashflow()
    assert type(builder.stock.return_product["get_cashflow"]) == type(dict())


def test_find_quarterly_cashflow():
    ticker.find_quarterly_cashflow()
    assert type(builder.stock.return_product["get_quarterly_cashflow"]) == type(dict())


def test_find_sustainability():
    ticker.find_sustainability()
    assert type(builder.stock.return_product["get_sustainability"]) == type(dict())


def test_find_options():
    ticker.find_options()
    assert type(builder.stock.return_product["get_options"]) == type(dict())


def test_special_char():
    ticker = fnc.FinanceCollector()
    builder = fnc.DesignerFinanceCollector(
        [
            "CLT=F",
            "^GSPC",
        ]
    )
    ticker.builder = builder
    ticker.find_chart_histogram()
    assert type(builder.stock.return_product["get_chart_history"]) == type(dict())
