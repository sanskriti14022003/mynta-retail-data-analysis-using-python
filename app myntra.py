import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Page config
st.set_page_config(page_title="Myntra Fashion Data Analysis", layout="wide")

# Load data
@st.cache_data
def load_data():
    file_name = "Myntra Fasion Clothing.csv"  # corrected spelling!
    if not os.path.exists(file_name):
        st.error(f"❌ File '{file_name}' not found.")
        return None
    df = pd.read_csv(file_name)
    return df

df = load_data()

if df is not None:
    st.title("🛍️ Myntra Fashion Clothing Data Explorer")



    # Dataset Preview
    st.subheader("🔍 Dataset Preview")
    st.dataframe(df.head(10))

    # Summary statistics
    st.subheader("📊 Summary Statistics")
    st.write(df.describe())

    # Data types
    st.subheader("📌 Data Types")
    st.write(df.dtypes)

    # Missing values
    st.subheader("🚨 Missing Values")
    st.write(df.isnull().sum())

    # Fill missing values
    df_filled = df.fillna(0)
    st.write("✅ Missing values filled with 0 (Preview):")
    st.dataframe(df_filled.head())

    # Fill a specific column with mean
    if 'Product_id' in df.columns:
        try:
            df['Product_id'] = pd.to_numeric(df['Product_id'], errors='coerce')
            df['Product_id_fillNA'] = df['Product_id'].fillna(df['Product_id'].mean())
            st.write("📥 'Product_id' column filled with mean where missing.")
            st.dataframe(df[['Product_id', 'Product_id_fillNA']].head())
        except Exception as e:
            st.warning(f"⚠️ Couldn't convert Product_id to numeric: {e}")

    # Rename column
    if 'URL' in df.columns:
        df.rename(columns={'URL': 'LINK'}, inplace=True)
        st.write("📝 Column 'URL' renamed to 'LINK'")

    # New Discount column
    if 'DiscountOffer' in df.columns:
        try:
            df['DiscountOffer'] = pd.to_numeric(df['DiscountOffer'], errors='coerce')
            df['New DiscountOffer'] = df['DiscountOffer'].apply(lambda x: x * 2)
            st.write("💸 Created 'New DiscountOffer' column (2x 'DiscountOffer'):")
            st.dataframe(df[['DiscountOffer', 'New DiscountOffer']].head())
        except Exception as e:
            st.warning(f"⚠️ Error calculating new discount: {e}")

    # Aggregation & grouping
    st.subheader("📈 Grouped Statistics")

    if 'DiscountPrice (in Rs)' in df.columns and 'Ratings' in df.columns:
        try:
            df['Ratings'] = pd.to_numeric(df['Ratings'], errors='coerce')
            df['DiscountPrice (in Rs)'] = pd.to_numeric(df['DiscountPrice (in Rs)'], errors='coerce')
            grouped_mean = df.groupby('DiscountPrice (in Rs)')['Ratings'].mean()
            st.write("**Mean Ratings by Discount Price:**")
            st.dataframe(grouped_mean.reset_index())
        except Exception as e:
            st.warning(f"⚠️ Grouped mean error: {e}")

    if {'OriginalPrice (in Rs)', 'Ratings', 'DiscountPrice (in Rs)'}.issubset(df.columns):
        try:
            df['OriginalPrice (in Rs)'] = pd.to_numeric(df['OriginalPrice (in Rs)'], errors='coerce')
            grouped_sum = df.groupby(['OriginalPrice (in Rs)', 'Ratings'])['DiscountPrice (in Rs)'].sum()
            st.write("**Sum of Discount Prices by Original Price and Ratings:**")
            st.dataframe(grouped_sum.reset_index())

            grouped_agg = df.groupby('OriginalPrice (in Rs)')['DiscountPrice (in Rs)'].agg(['mean', 'sum', 'count'])
            st.write("**Aggregate stats of Discount Prices by Original Price:**")
            st.dataframe(grouped_agg)
        except Exception as e:
            st.warning(f"⚠️ Grouped aggregation error: {e}")

    # Data Merging
    st.subheader("🔗 Data Merging Example")

    df1 = pd.DataFrame({'Key': ['A', 'B', 'C'], 'Value1': [1, 2, 3]})
    df2 = pd.DataFrame({'Key': ['A', 'B', 'F'], 'Value2': [4, 5, 6]})

    st.write("**df1:**")
    st.dataframe(df1)

    st.write("**df2:**")
    st.dataframe(df2)

    st.write("**Outer Merge:**")
    st.dataframe(pd.merge(df1, df2, on="Key", how="outer"))

    st.write("**Inner Merge:**")
    st.dataframe(pd.merge(df1, df2, on="Key", how="inner"))

    st.write("**Left Merge:**")
    st.dataframe(pd.merge(df1, df2, on="Key", how="left"))

    st.write("**Right Merge:**")
    st.dataframe(pd.merge(df1, df2, on="Key", how="right"))

    # Basic Line Plot
    st.subheader("📉 Basic Line Plot (Ratings vs Reviews)")
    if 'Ratings' in df.columns and 'Reviews' in df.columns:
        try:
            df['Ratings'] = pd.to_numeric(df['Ratings'], errors='coerce')
            df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')
            df_plot = df.dropna(subset=['Ratings', 'Reviews'])
            fig, ax = plt.subplots()
            ax.plot(df_plot['Ratings'], df_plot['Reviews'])
            ax.set_xlabel('Ratings')
            ax.set_ylabel('Reviews')
            ax.set_title('Basic Line Plot: Ratings vs Reviews')
            st.pyplot(fig)
        except Exception as e:
            st.warning(f"⚠️ Plotting error: {e}")
    else:
        st.warning("Missing 'Ratings' or 'Reviews' column for line plot.")
