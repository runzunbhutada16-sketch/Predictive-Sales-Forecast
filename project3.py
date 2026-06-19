sales_forecast.py
This part includes:
OOP structure
CSV loading
Data cleaning & preprocessing
Exploratory Data Analysis (EDA)
Sales KPIs,Product & Region analysis
Professional console output
Exception handling.

# sales_forecast.py

"""
Predictive Sales Forecast and Business Intelligence System
import pandas as pd
import numpy as np
import os
from tabulate import tabulate
import warnings

warnings.filterwarnings("ignore")


class SalesForecast:

    def __init__(self, file_path="sales_data.csv"):
        """
        Initialize class.
        """

        self.file_path = file_path
        self.df = None

        self.load_data()
        self.clean_data()

        self.reports_dir = "reports"

        os.makedirs(self.reports_dir, exist_ok=True)

    # ---------------------------------------------------
    # LOAD DATA
    # ---------------------------------------------------

    def load_data(self):

        try:

            self.df = pd.read_csv(self.file_path)

            print(f"\n Loaded {len(self.df)} records.")

        except FileNotFoundError:

            print("\n sales_data.csv not found.")

            raise

        except Exception as e:

            print(e)

            raise

    # ---------------------------------------------------
    # CLEAN DATA
    # ---------------------------------------------------

    def clean_data(self):

        print("\n Cleaning Dataset...")

        initial_rows = len(self.df)

        # Remove missing values

        self.df.dropna(
            subset=[
                "Date",
                "Product",
                "Region",
                "Sales",
                "Profit"
            ],

            inplace=True
        )

        print(
            f" Removed {initial_rows-len(self.df)} rows with missing values."
        )

        # Remove duplicates

        duplicates = self.df.duplicated().sum()

        self.df.drop_duplicates(inplace=True)

        print(f" Removed {duplicates} duplicate rows.")

        # Convert date

        self.df["Date"] = pd.to_datetime(
            self.df["Date"],
            errors="coerce"
        )

        invalid_dates = self.df["Date"].isna().sum()

        self.df.dropna(subset=["Date"], inplace=True)

        print(f" Removed {invalid_dates} invalid dates.")

        # Remove outliers

        q1 = self.df["Sales"].quantile(0.25)

        q3 = self.df["Sales"].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - 1.5 * iqr

        upper = q3 + 1.5 * iqr

        self.df = self.df[
            (self.df["Sales"] >= lower)
            &
            (self.df["Sales"] <= upper)
        ]

        print(" Outliers removed.")

        # Standardize names

        self.df["Product"] = (
            self.df["Product"]
            .str.strip()
            .str.title()
        )

        self.df["Region"] = (
            self.df["Region"]
            .str.strip()
            .str.title()
        )

        # Create extra columns

        self.df["Year"] = self.df["Date"].dt.year

        self.df["Month"] = self.df["Date"].dt.month

        self.df["Quarter"] = self.df["Date"].dt.quarter

        print(
            f" Dataset cleaned successfully."
        )

        print(
            f" Final records: {len(self.df)}"
        )

    # ---------------------------------------------------
    # DATASET SUMMARY
    # ---------------------------------------------------

    def dataset_summary(self):

        summary = {

            "Total Records":
                len(self.df),

            "Date Range":

                f"{self.df['Date'].min().date()}"

                +

                " to "

                +

                f"{self.df['Date'].max().date()}",

            "Total Sales":

                round(
                    self.df["Sales"].sum(),
                    2
                ),

            "Total Profit":

                round(
                    self.df["Profit"].sum(),
                    2
                ),

            "Average Revenue":

                round(
                    self.df["Sales"].mean(),
                    2
                ),

            "Unique Products":

                self.df["Product"].nunique(),

            "Unique Regions":

                self.df["Region"].nunique()

        }

        print("\n DATASET SUMMARY\n")

        print(

            tabulate(

                summary.items(),

                headers=["Metric", "Value"],

                tablefmt="pretty"

            )

        )

    # ---------------------------------------------------
    # TOTAL SALES
    # ---------------------------------------------------

    def total_sales(self):

        total = self.df["Sales"].sum()

        print("\n Total Sales")

        print(f"${total:,.2f}")

    # ---------------------------------------------------
    # MONTHLY SALES
    # ---------------------------------------------------

    def monthly_sales(self):

        monthly = (

            self.df

            .groupby("Month")["Sales"]

            .sum()

            .reset_index()

        )

        print("\n Monthly Sales")

        print(

            tabulate(

                monthly,

                headers="keys",

                tablefmt="pretty",

                showindex=False

            )

        )

        return monthly

    # ---------------------------------------------------
    # QUARTERLY SALES
    # ---------------------------------------------------

    def quarterly_sales(self):

        quarterly = (

            self.df

            .groupby("Quarter")["Sales"]

            .sum()

            .reset_index()

        )

        print("\n Quarterly Sales")

        print(

            tabulate(

                quarterly,

                headers="keys",

                tablefmt="pretty",

                showindex=False

            )

        )

        return quarterly

    # ---------------------------------------------------
    # YEARLY SALES
    # ---------------------------------------------------

    def yearly_sales(self):

        yearly = (

            self.df

            .groupby("Year")["Sales"]

            .sum()

            .reset_index()

        )

        print("\n Yearly Sales")

        print(

            tabulate(

                yearly,

                headers="keys",

                tablefmt="pretty",

                showindex=False

            )

        )

        return yearly

    # ---------------------------------------------------
    # GROWTH RATE
    # ---------------------------------------------------

    def growth_rate(self):

        yearly = self.yearly_sales()

        yearly["Growth %"] = (

            yearly["Sales"]

            .pct_change()

            * 100

        )

        print("\n Sales Growth Rate")

        print(

            tabulate(

                yearly,

                headers="keys",

                tablefmt="pretty",

                showindex=False

            )

        )

    # ---------------------------------------------------
    # BEST SELLING PRODUCTS
    # ---------------------------------------------------

    def best_selling_products(self):

        top_products = (

            self.df

            .groupby("Product")["Sales"]

            .sum()

            .sort_values(

                ascending=False

            )

            .head(10)

            .reset_index()

        )

        print("\n TOP SELLING PRODUCTS")

        print(

            tabulate(

                top_products,

                headers="keys",

                tablefmt="pretty",

                showindex=False

            )

        )

        return top_products

    # ---------------------------------------------------
    # TOP REGIONS
    # ---------------------------------------------------

    def top_regions(self):

        regions = (

            self.df

            .groupby("Region")["Sales"]

            .sum()

            .sort_values(

                ascending=False

            )

            .reset_index()

        )

        print("\n TOP REGIONS")

        print(

            tabulate(

                regions,

                headers="keys",

                tablefmt="pretty",

                showindex=False

            )

        )

        return regions


# ---------------------------------------------------
# MAIN FUNCTION
# ---------------------------------------------------

def main():

    print(

        "\n"

        + "="*55

    )

    print(

        " PREDICTIVE SALES FORECAST SYSTEM "

    )

    print(

        "="*55

    )

    try:

        analyzer = SalesForecast()

        analyzer.dataset_summary()

        analyzer.total_sales()

        analyzer.monthly_sales()

        analyzer.quarterly_sales()

        analyzer.yearly_sales()

        analyzer.growth_rate()

        analyzer.best_selling_products()

        analyzer.top_regions()

    except Exception as e:

        print(

            f"\n Error: {e}"

        )


if __name__ == "__main__":

    main()

    
