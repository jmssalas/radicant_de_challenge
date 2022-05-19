from django.db import models

# Etf model were created by the following command:
#   $ python manage.py inspectdb
# After the ETFs.csv file was imported to db.sqlite3

class Etf(models.Model):
    fund_symbol = models.TextField(blank=True, null=True)
    quote_type = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    fund_short_name = models.TextField(blank=True, null=True)
    fund_long_name = models.TextField(blank=True, null=True)
    currency = models.TextField(blank=True, null=True)
    fund_category = models.TextField(blank=True, null=True)
    fund_family = models.TextField(blank=True, null=True)
    exchange_code = models.TextField(blank=True, null=True)
    exchange_name = models.TextField(blank=True, null=True)
    exchange_timezone = models.TextField(blank=True, null=True)
    avg_vol_3month = models.TextField(blank=True, null=True)
    avg_vol_10day = models.TextField(blank=True, null=True)
    total_net_assets = models.TextField(blank=True, null=True)
    day50_moving_average = models.TextField(blank=True, null=True)
    day200_moving_average = models.TextField(blank=True, null=True)
    week52_high_low_change = models.TextField(blank=True, null=True)
    week52_high_low_change_perc = models.TextField(blank=True, null=True)
    week52_high = models.TextField(blank=True, null=True)
    week52_high_change = models.TextField(blank=True, null=True)
    week52_high_change_perc = models.TextField(blank=True, null=True)
    week52_low = models.TextField(blank=True, null=True)
    week52_low_change = models.TextField(blank=True, null=True)
    week52_low_change_perc = models.TextField(blank=True, null=True)
    investment_strategy = models.TextField(blank=True, null=True)
    fund_yield = models.TextField(blank=True, null=True)
    inception_date = models.TextField(blank=True, null=True)
    annual_holdings_turnover = models.TextField(blank=True, null=True)
    investment_type = models.TextField(blank=True, null=True)
    size_type = models.TextField(blank=True, null=True)
    fund_annual_report_net_expense_ratio = models.TextField(blank=True, null=True)
    category_annual_report_net_expense_ratio = models.TextField(blank=True, null=True)
    asset_stocks = models.TextField(blank=True, null=True)
    asset_bonds = models.TextField(blank=True, null=True)
    fund_sector_basic_materials = models.TextField(blank=True, null=True)
    fund_sector_communication_services = models.TextField(blank=True, null=True)
    fund_sector_consumer_cyclical = models.TextField(blank=True, null=True)
    fund_sector_consumer_defensive = models.TextField(blank=True, null=True)
    fund_sector_energy = models.TextField(blank=True, null=True)
    fund_sector_financial_services = models.TextField(blank=True, null=True)
    fund_sector_healthcare = models.TextField(blank=True, null=True)
    fund_sector_industrials = models.TextField(blank=True, null=True)
    fund_sector_real_estate = models.TextField(blank=True, null=True)
    fund_sector_technology = models.TextField(blank=True, null=True)
    fund_sector_utilities = models.TextField(blank=True, null=True)
    fund_price_book_ratio = models.TextField(blank=True, null=True)
    fund_price_cashflow_ratio = models.TextField(blank=True, null=True)
    fund_price_earning_ratio = models.TextField(blank=True, null=True)
    fund_price_sales_ratio = models.TextField(blank=True, null=True)
    fund_bond_maturity = models.TextField(blank=True, null=True)
    fund_bond_duration = models.TextField(blank=True, null=True)
    fund_bonds_us_government = models.TextField(blank=True, null=True)
    fund_bonds_aaa = models.TextField(blank=True, null=True)
    fund_bonds_aa = models.TextField(blank=True, null=True)
    fund_bonds_a = models.TextField(blank=True, null=True)
    fund_bonds_bbb = models.TextField(blank=True, null=True)
    fund_bonds_bb = models.TextField(blank=True, null=True)
    fund_bonds_b = models.TextField(blank=True, null=True)
    fund_bonds_below_b = models.TextField(blank=True, null=True)
    fund_bonds_others = models.TextField(blank=True, null=True)
    top10_holdings = models.TextField(blank=True, null=True)
    top10_holdings_total_assets = models.TextField(blank=True, null=True)
    returns_as_of_date = models.TextField(blank=True, null=True)
    fund_return_ytd = models.TextField(blank=True, null=True)
    category_return_ytd = models.TextField(blank=True, null=True)
    fund_return_1month = models.TextField(blank=True, null=True)
    category_return_1month = models.TextField(blank=True, null=True)
    fund_return_3months = models.TextField(blank=True, null=True)
    category_return_3months = models.TextField(blank=True, null=True)
    fund_return_1year = models.TextField(blank=True, null=True)
    category_return_1year = models.TextField(blank=True, null=True)
    fund_return_3years = models.TextField(blank=True, null=True)
    category_return_3years = models.TextField(blank=True, null=True)
    fund_return_5years = models.TextField(blank=True, null=True)
    category_return_5years = models.TextField(blank=True, null=True)
    fund_return_10years = models.TextField(blank=True, null=True)
    category_return_10years = models.TextField(blank=True, null=True)
    years_up = models.TextField(blank=True, null=True)
    years_down = models.TextField(blank=True, null=True)
    fund_return_2020 = models.TextField(blank=True, null=True)
    category_return_2020 = models.TextField(blank=True, null=True)
    fund_return_2019 = models.TextField(blank=True, null=True)
    category_return_2019 = models.TextField(blank=True, null=True)
    fund_return_2018 = models.TextField(blank=True, null=True)
    category_return_2018 = models.TextField(blank=True, null=True)
    fund_return_2017 = models.TextField(blank=True, null=True)
    category_return_2017 = models.TextField(blank=True, null=True)
    fund_return_2016 = models.TextField(blank=True, null=True)
    category_return_2016 = models.TextField(blank=True, null=True)
    fund_return_2015 = models.TextField(blank=True, null=True)
    category_return_2015 = models.TextField(blank=True, null=True)
    fund_return_2014 = models.TextField(blank=True, null=True)
    category_return_2014 = models.TextField(blank=True, null=True)
    fund_return_2013 = models.TextField(blank=True, null=True)
    category_return_2013 = models.TextField(blank=True, null=True)
    fund_return_2012 = models.TextField(blank=True, null=True)
    category_return_2012 = models.TextField(blank=True, null=True)
    fund_return_2011 = models.TextField(blank=True, null=True)
    category_return_2011 = models.TextField(blank=True, null=True)
    fund_return_2010 = models.TextField(blank=True, null=True)
    category_return_2010 = models.TextField(blank=True, null=True)
    fund_return_2009 = models.TextField(blank=True, null=True)
    category_return_2009 = models.TextField(blank=True, null=True)
    fund_return_2008 = models.TextField(blank=True, null=True)
    category_return_2008 = models.TextField(blank=True, null=True)
    fund_return_2007 = models.TextField(blank=True, null=True)
    category_return_2007 = models.TextField(blank=True, null=True)
    fund_return_2006 = models.TextField(blank=True, null=True)
    category_return_2006 = models.TextField(blank=True, null=True)
    fund_return_2005 = models.TextField(blank=True, null=True)
    category_return_2005 = models.TextField(blank=True, null=True)
    fund_return_2004 = models.TextField(blank=True, null=True)
    category_return_2004 = models.TextField(blank=True, null=True)
    fund_return_2003 = models.TextField(blank=True, null=True)
    category_return_2003 = models.TextField(blank=True, null=True)
    fund_return_2002 = models.TextField(blank=True, null=True)
    category_return_2002 = models.TextField(blank=True, null=True)
    fund_return_2001 = models.TextField(blank=True, null=True)
    category_return_2001 = models.TextField(blank=True, null=True)
    fund_return_2000 = models.TextField(blank=True, null=True)
    category_return_2000 = models.TextField(blank=True, null=True)
    fund_alpha_3years = models.TextField(blank=True, null=True)
    fund_beta_3years = models.TextField(blank=True, null=True)
    fund_mean_annual_return_3years = models.TextField(blank=True, null=True)
    fund_r_squared_3years = models.TextField(blank=True, null=True)
    fund_stdev_3years = models.TextField(blank=True, null=True)
    fund_sharpe_ratio_3years = models.TextField(blank=True, null=True)
    fund_treynor_ratio_3years = models.TextField(blank=True, null=True)
    fund_alpha_5years = models.TextField(blank=True, null=True)
    fund_beta_5years = models.TextField(blank=True, null=True)
    fund_mean_annual_return_5years = models.TextField(blank=True, null=True)
    fund_r_squared_5years = models.TextField(blank=True, null=True)
    fund_stdev_5years = models.TextField(blank=True, null=True)
    fund_sharpe_ratio_5years = models.TextField(blank=True, null=True)
    fund_treynor_ratio_5years = models.TextField(blank=True, null=True)
    fund_alpha_10years = models.TextField(blank=True, null=True)
    fund_beta_10years = models.TextField(blank=True, null=True)
    fund_mean_annual_return_10years = models.TextField(blank=True, null=True)
    fund_r_squared_10years = models.TextField(blank=True, null=True)
    fund_stdev_10years = models.TextField(blank=True, null=True)
    fund_sharpe_ratio_10years = models.TextField(blank=True, null=True)
    fund_treynor_ratio_10years = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'etf'