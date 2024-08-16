import streamlit as st
import pandas as pd
import os

from utils.format import format_number

    
# LOAD
base_path = os.path.dirname(os.path.abspath(__file__))
historic_file_path = os.path.join(base_path, 'export', 'historic.parquet')
general_financials_file_path = os.path.join(base_path, 'export', 'general_financials.parquet')
real_time_file_path = os.path.join(base_path, 'export', 'real_time.parquet')

df_historic = pd.read_parquet(historic_file_path)
df_general_financials = pd.read_parquet(general_financials_file_path)
df_real_time = pd.read_parquet(real_time_file_path)


# TRANSFORMATION
for col in ['open', 'high', 'low', 'close', 'volume']:
    if col in df_historic.columns:
        df_historic[col] = pd.to_numeric(df_historic[col], errors='coerce')

df_historic['date_information'] = pd.to_datetime(df_historic['date_information'], errors='coerce')
df_historic['date_information'] = df_historic['date_information'].dt.tz_localize(None)


# DASHBOARD
st.set_page_config(page_title="Análise de Dados Financeiros", layout="wide")

col1, col2 = st.columns([1, 3])

with col1:
    company_code = st.selectbox('Selecione a empresa', df_historic['company_code'].unique())
    

    general_financials_filtred = df_general_financials[df_general_financials['company_code'] == company_code]
    general_financials_filtred = general_financials_filtred.reset_index()
    
    sector = general_financials_filtred.loc[0, 'sector']
    sector_html = f'<a>Setor: {sector}</a>'
    
    net_sales = general_financials_filtred.loc[0, 'net_sales']
    net_sales = format_number(int(net_sales))
    net_sales_html = f'<a>Receita Líquida: {net_sales}</a>'
    
    net_income = general_financials_filtred.loc[0,'net_income']
    net_income = format_number(int(net_income))
    net_income_html = f'<a>Lucro Líquido (LL): {net_income}</a>'

    net_margin  = general_financials_filtred.loc[0,'net_margin']
    net_margin_html = f'<a>Margem líquida: {net_margin}%</a>'

    ebitda = general_financials_filtred.loc[0, 'ebitda']
    ebitda = format_number(int(ebitda))
    ebitda_html = f'<a>EBITDA: {ebitda}</a>'

    ebitda_margin = general_financials_filtred.loc[0, 'ebitda_margin']
    ebitda_margin_html = f'<a>Margem EBITDA: {ebitda_margin}%</a>'

    total_assets = general_financials_filtred.loc[0, 'total_assets']
    total_assets = format_number(int(total_assets))
    total_assets_html = f'<a>Ativos Totais: {total_assets}</a>'

    gross_debt = general_financials_filtred.loc[0, 'gross_debt']
    gross_debt = format_number(int(gross_debt))
    gross_debt_html = f'<a>Dívida Bruta: {gross_debt}</a>'

    equity = general_financials_filtred.loc[0, 'equity']
    equity = format_number(int(equity))
    equity_html = f'<a>Patrimônio Líquido: {equity}</a>'

    pe_ratio = general_financials_filtred.loc[0, 'pe_ratio']
    pe_ratio_html = f'<a>Relação P/L: {pe_ratio}</a>'

    st.html(sector_html)
    st.html(net_sales_html)
    st.html(net_income_html)
    st.html(net_margin_html)
    st.html(ebitda_html)
    st.html(ebitda_margin_html)
    st.html(total_assets_html)
    st.html(gross_debt_html)
    st.html(equity_html)
    st.html(pe_ratio_html)


df_historic_filtered = df_historic[df_historic['company_code'] == company_code].copy()
df_historic_filtered.set_index('date_information', inplace=True)
df_historic_filtered = df_historic_filtered.sort_index()

start_date = df_historic_filtered.index.min()
end_date = df_historic_filtered.index.max()

with col2:
    selected_dates = st.slider(
        'Selecione o intervalo de datas',
        min_value=start_date.date(),
        max_value=end_date.date(),
        value=(start_date.date(), end_date.date()),
        format='DD/MM/YYYY'
    )

    start_date_selected = pd.Timestamp(selected_dates[0])
    end_date_selected = pd.Timestamp(selected_dates[1] )

    if start_date_selected < start_date:
        start_date_selected = start_date
    if end_date_selected > end_date:
        end_date_selected = end_date
    
    try:
        df_filtered_for_slider = df_historic_filtered.loc[start_date_selected:end_date_selected]
        st.subheader('Gráfico de Preços Históricos')
        st.area_chart(df_filtered_for_slider[['open']])
    except KeyError as e:
        st.error(f"Erro ao filtrar dados: {e}")


