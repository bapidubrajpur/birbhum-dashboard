import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Set page config
st.set_page_config(
    page_title="VB-G RAM G Birbhum Dashboard",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for custom styling (orange-cream corporate color scheme)
st.markdown("""
<style>
    /* Main layout style */
    .reportview-container {
        background-color: #FAFAFA;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #FFF8E1;
        border-right: 2px solid #FFE082;
    }
    
    section[data-testid="stSidebar"] .sidebar-content {
        padding-top: 20px;
    }
    
    /* Headers custom color */
    h1, h2, h3 {
        color: #5D4037;
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }
    
    /* Metrics panel card style */
    div[data-testid="metric-container"] {
        background-color: #FFFFFF;
        border: 1px solid #FFE082;
        border-radius: 8px;
        padding: 12px 18px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        border-left: 5px solid #FF8F00;
    }
    
    /* Tab custom styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #FFF3E0;
        border-radius: 5px 5px 0px 0px;
        padding: 8px 16px;
        color: #E65100;
        font-weight: bold;
        border: 1px solid #FFE082;
        border-bottom: none;
    }
    .stTabs [aria-selected="true"] {
        background-color: #FFB300 !important;
        color: #3E2723 !important;
        border-color: #FF8F00 !important;
    }
</style>
""", unsafe_allow_html=True)

# ----------------- DATA LOADING & REFRESH LOGIC -----------------
DATA_DIR = "data"

@st.cache_data
def load_table_data(filename):
    filepath = os.path.join(DATA_DIR, filename)
    if os.path.exists(filepath):
        return pd.read_csv(filepath)
    else:
        st.error(f"Data file {filename} not found in the scratch directory!")
        return None

# Load all 6 tables
df_ongoing = load_table_data("ongoing_scheme_status.csv")
df_ekyc = load_table_data("ekyc_status.csv")
df_live = load_table_data("live_nmms_status.csv")
df_fto = load_table_data("material_fto_status.csv")
df_category = load_table_data("work_category_status.csv")
df_dsc = load_table_data("dsc_status.csv")

# ----------------- PERSISTENCE UPDATE FUNCTIONS -----------------
def save_table_data(df, filename):
    filepath = os.path.join(DATA_DIR, filename)
    df.to_csv(filepath, index=False)
    st.cache_data.clear() # Clear streamlit cache to reload new data

# ----------------- HEADER RENDERING (MATCHING POSTER) -----------------
st.markdown("""
<div style="background: linear-gradient(135deg, #FFFDF9, #FFF8E7); border: 3px solid #E67E22; border-radius: 15px; padding: 25px; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.08); margin-bottom: 25px; border-left: 10px solid #E67E22;">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 5px;">
        <span style="font-size: 24px;">🏛️</span> 
        <span style="font-size: 14px; font-weight: bold; color: #D35400; font-family: sans-serif; border: 2px solid #D35400; padding: 4px 10px; border-radius: 6px; background-color: #FFF3E0;">Viksit Bharat - 2047</span>
    </div>
    <h1 style="color: #2E1A11; font-family: 'Times New Roman', Times, serif; font-size: 44px; margin: 0; font-weight: 900; letter-spacing: 2px; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">
        VB-<span style="color: #27AE60;">G</span> RAM <span style="color: #27AE60; position: relative;">G <span style="color: #27AE60; font-size: 24px; vertical-align: super;">🍃</span></span>
    </h1>
    <h2 style="color: #C0392B; font-family: 'Impact', 'Arial Black', sans-serif; font-size: 40px; margin: 3px 0 10px 0; letter-spacing: 4px; text-transform: uppercase;">
        BIRBHUM
    </h2>
    <div style="font-size: 12px; font-weight: 800; color: #5D4037; letter-spacing: 4px; border-top: 2px solid #E67E22; border-bottom: 2px solid #E67E22; padding: 7px 0; margin: 12px auto; max-width: 700px; text-transform: uppercase;">
        TRANSPARENCY &nbsp;|&nbsp; ACCOUNTABILITY &nbsp;|&nbsp; PARTICIPATION &nbsp;|&nbsp; PROGRESS
    </div>
    <div style="background: linear-gradient(90deg, #E67E22, #C0392B); color: white; padding: 10px 30px; font-size: 22px; font-weight: bold; border-radius: 8px; display: inline-block; margin-top: 10px; box-shadow: 0 4px 8px rgba(192, 57, 43, 0.25); letter-spacing: 1px;">
        125 DAYS WORK
    </div>
    <div style="color: #C0392B; font-style: italic; font-size: 15px; font-weight: bold; margin-top: 7px; letter-spacing: 1px;">
        — Towards Sustainable Rural Transformation —
    </div>
    <div style="font-size: 13px; color: #3E2723; font-weight: 800; margin-top: 12px; font-family: sans-serif; text-transform: uppercase; letter-spacing: 0.5px;">
        A Report on RURAL DEVELOPMENT & GOOD GOVERNANCE
    </div>
</div>
""", unsafe_allow_html=True)

# Five Pillars section (styled beautiful cards)
st.markdown("""
<div style="display: flex; justify-content: space-between; gap: 12px; margin-bottom: 30px; flex-wrap: wrap;">
    <div style="flex: 1; min-width: 160px; background-color: #FFF3E0; border-top: 4px solid #E65100; padding: 12px; border-radius: 6px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.04); transition: transform 0.2s;">
        <div style="font-size: 22px; margin-bottom: 4px;">👥</div>
        <div style="font-weight: 800; font-size: 12px; color: #E65100; text-transform: uppercase; margin-bottom: 2px;">Empowering People</div>
        <div style="font-size: 10px; color: #5D4037; font-weight: 500;">Strengthening Rural Livelihoods</div>
    </div>
    <div style="flex: 1; min-width: 160px; background-color: #FFF3E0; border-top: 4px solid #E65100; padding: 12px; border-radius: 6px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.04);">
        <div style="font-size: 22px; margin-bottom: 4px;">📋</div>
        <div style="font-weight: 800; font-size: 12px; color: #E65100; text-transform: uppercase; margin-bottom: 2px;">Timely Works</div>
        <div style="font-size: 10px; color: #5D4037; font-weight: 500;">Quality Execution On Ground</div>
    </div>
    <div style="flex: 1; min-width: 160px; background-color: #FFF3E0; border-top: 4px solid #E65100; padding: 12px; border-radius: 6px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.04);">
        <div style="font-size: 22px; margin-bottom: 4px;">🌱</div>
        <div style="font-weight: 800; font-size: 12px; color: #E65100; text-transform: uppercase; margin-bottom: 2px;">Sustainable Dev</div>
        <div style="font-size: 10px; color: #5D4037; font-weight: 500;">Building Resilient Communities</div>
    </div>
    <div style="flex: 1; min-width: 160px; background-color: #FFF3E0; border-top: 4px solid #E65100; padding: 12px; border-radius: 6px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.04);">
        <div style="font-size: 22px; margin-bottom: 4px;">📈</div>
        <div style="font-weight: 800; font-size: 12px; color: #E65100; text-transform: uppercase; margin-bottom: 2px;">Data Governance</div>
        <div style="font-size: 10px; color: #5D4037; font-weight: 500;">Real Time Monitoring & Impact</div>
    </div>
    <div style="flex: 1; min-width: 160px; background-color: #FFF3E0; border-top: 4px solid #E65100; padding: 12px; border-radius: 6px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.04);">
        <div style="font-size: 22px; margin-bottom: 4px;">🤝</div>
        <div style="font-weight: 800; font-size: 12px; color: #E65100; text-transform: uppercase; margin-bottom: 2px;">Jan Bhagidari</div>
        <div style="font-size: 10px; color: #5D4037; font-weight: 500;">People's Participation & Progress</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ----------------- SIDEBAR ROLE NAVIGATION -----------------
st.sidebar.image("https://img.icons8.com/color/96/dashboard.png", width=70)
st.sidebar.title("Navigation & Roles")
role = st.sidebar.radio("Select Role:", ["👥 Viewer (Reports Only)", "🔒 Admin (Upload & Edit)"])

# Quick Overview card in sidebar
st.sidebar.markdown("---")
st.sidebar.subheader("District Overview")
st.sidebar.info("""
**District:** Birbhum, West Bengal  
**Total GPs:** 167  
**Report Date:** 22 August 2026  
**Scheme:** VB-GRAM G (125 Days Work)
""")

# ----------------- MAIN VIEW FLOWS -----------------
if role == "👥 Viewer (Reports Only)":
    
    st.subheader("📊 Viewer Dashboard - Live Reports")
    
    # 5 tabs for Viewer reports
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📱 Live Work Status (NMMS)",
        "🏗️ Scheme & Ongoing Status",
        "🔒 e-KYC Verification Status",
        "💳 Material FTO Checking",
        "🛠️ Work Category wise Breakdown"
    ])
    
    with tab1:
        st.markdown("### 📱 Live work status through NMMS App (Daily Attendance)")
        st.caption("Reporting Date: 22-08-2026 09:59 AM")
        
        # Summary Metrics
        if df_live is not None:
            m1, m2, m3, m4 = st.columns(4)
            m1.metric("Total Approved Works", f"{df_live['No of VB-G RAM G Works AS Approved'].sum():,}")
            m2.metric("Total Works Ongoing Today", f"{df_live['Total Works Ongoing'].sum():,}")
            m3.metric("Persondays Generated Today", f"{df_live['Persondays Generated in Field Todays'].sum():,}")
            m4.metric("GPs Not Running Today", f"{df_live['GPs Not Running Today'].sum()} / 167")
            
            # Interactive Plotly Chart
            st.markdown("#### Blockwise Works: Approved vs. Ongoing Today")
            fig = px.bar(
                df_live, 
                x="Block Name", 
                y=["No of VB-G RAM G Works AS Approved", "Total Works Ongoing"],
                barmode="group",
                color_discrete_sequence=["#FF9800", "#C0392B"],
                labels={"value": "Count of Works", "variable": "Work Type"}
            )
            fig.update_layout(xaxis_tickangle=-45, legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
            st.plotly_chart(fig, use_container_width=True)
            
            # Plotly Line Chart for Persondays
            st.markdown("#### Persondays Generated Today by Block")
            fig2 = px.line(
                df_live,
                x="Block Name",
                y="Persondays Generated in Field Todays",
                markers=True,
                line_shape="spline",
                color_discrete_sequence=["#27AE60"]
            )
            fig2.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig2, use_container_width=True)
            
            # Interactive Data Table
            st.markdown("#### Live Status Detailed Table")
            search_query = st.text_input("🔍 Search block in NMMS table:", "")
            filtered_df = df_live[df_live['Block Name'].str.contains(search_query, case=False)] if search_query else df_live
            st.dataframe(filtered_df, use_container_width=True)
            
            # Download button
            csv = filtered_df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download filtered NMMS report as CSV", csv, "live_nmms_report.csv", "text/csv")
            
    with tab2:
        st.markdown("### 🏗️ Blockwise Villages and Ongoing Scheme Status (DP Report)")
        st.caption("Active Village scheme ratios and approvals as on 22.08.2026")
        
        if df_ongoing is not None:
            o1, o2, o3 = st.columns(3)
            o1.metric("Total Villages Covered", f"{df_ongoing['No. of Villages'].sum():,}")
            o2.metric("Total Approved Works", f"{df_ongoing['No. of Approved Works'].sum():,}")
            o3.metric("Average Approved %", f"{df_ongoing['% of Approved Works against Villages'].mean():.2f}%")
            
            # Plotly scatter plot: Approved vs. Ongoing Works
            st.markdown("#### Approved vs. Ongoing Works Comparison")
            fig_scatter = px.scatter(
                df_ongoing,
                x="No. of Approved Works",
                y="No. of Ongoing Works",
                size="No. of Villages",
                color="Block Name",
                hover_name="Block Name",
                text="Block Name",
                size_max=35,
                title="Approved vs Ongoing Schemes (Bubble size represents No. of Villages)"
            )
            fig_scatter.update_traces(textposition='top center')
            st.plotly_chart(fig_scatter, use_container_width=True)
            
            # Data table
            st.markdown("#### Scheme Status Detailed Table")
            search_query2 = st.text_input("🔍 Search block in Scheme table:", "")
            filtered_df2 = df_ongoing[df_ongoing['Block Name'].str.contains(search_query2, case=False)] if search_query2 else df_ongoing
            st.dataframe(filtered_df2, use_container_width=True)
            
            # Download button
            csv2 = filtered_df2.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download Scheme report as CSV", csv2, "ongoing_scheme_report.csv", "text/csv")

    with tab3:
        st.markdown("### 🔒 e-KYC Verification Status of Workers")
        st.caption("Target: 100% e-KYC of active rural workforce (District Average: 86.33%)")
        
        if df_ekyc is not None:
            k1, k2, k3 = st.columns(3)
            k1.metric("Total Workforce", f"{df_ekyc['Total Workers'].sum():,}")
            k2.metric("Total e-KYC Done Today", f"{df_ekyc['e-KYC Today'].sum():,}")
            avg_ekyc = (df_ekyc['e-KYC Today'].sum() / df_ekyc['Total Workers'].sum()) * 100
            k3.metric("Birbhum District Average %", f"{avg_ekyc:.2f}%")
            
            # e-KYC completion bar chart (color-coded by Above vs Below state/district average)
            st.markdown("#### e-KYC Completion Percentage by Block")
            df_ekyc_sorted = df_ekyc.sort_values(by="% e-KYC", ascending=False)
            df_ekyc_sorted['Status'] = df_ekyc_sorted['Remarks']
            
            fig_ekyc = px.bar(
                df_ekyc_sorted,
                x="Block Name",
                y="% e-KYC",
                color="Status",
                color_discrete_map={"Above Dist. %": "#27AE60", "Below Dist. %": "#C0392B"},
                labels={"% e-KYC": "e-KYC Completion %"},
                text_auto='.1f'
            )
            fig_ekyc.add_hline(y=86.33, line_dash="dash", line_color="black", annotation_text="Birbhum Average: 86.33%")
            st.plotly_chart(fig_ekyc, use_container_width=True)
            
            # Data table
            st.markdown("#### e-KYC Verification Detailed Table")
            search_query3 = st.text_input("🔍 Search block in e-KYC table:", "")
            filtered_df3 = df_ekyc[df_ekyc['Block Name'].str.contains(search_query3, case=False)] if search_query3 else df_ekyc
            st.dataframe(filtered_df3, use_container_width=True)
            
            # Download button
            csv3 = filtered_df3.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download e-KYC report as CSV", csv3, "ekyc_report.csv", "text/csv")

    with tab4:
        st.markdown("### 💳 Checking of Material Funds / Financial FTO Status")
        st.caption("Verification and checks status of pending financial FTO transactions")
        
        if df_fto is not None:
            f1, f2, f3 = st.columns(3)
            f1.metric("Total FTO Pending Count", f"{df_fto['Pending FTOs'].sum():,}")
            f2.metric("Total Pending Funds (Rs.)", f"₹ {df_fto['Pending Amount (Rs.)'].sum():,}")
            total_verified = df_fto['Verified Amount (Rs.)'].sum()
            f3.metric("Verified/Approved Funds (Rs.)", f"₹ {total_verified:,}")
            
            # Visualizing Pending Amount
            st.markdown("#### Remaining Pending Funds (in Rs.) by Block")
            fig_fto = px.bar(
                df_fto,
                x="Block Name",
                y="Pending Amount (Rs.) Remaining",
                color="% Pending",
                color_continuous_scale=px.colors.sequential.Oranges,
                labels={"Pending Amount (Rs.) Remaining": "Remaining Pending (₹)"}
            )
            fig_fto.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig_fto, use_container_width=True)
            
            # Data table
            st.markdown("#### Material FTO Status Detailed Table")
            search_query4 = st.text_input("🔍 Search block in FTO table:", "")
            filtered_df4 = df_fto[df_fto['Block Name'].str.contains(search_query4, case=False)] if search_query4 else df_fto
            st.dataframe(filtered_df4, use_container_width=True)
            
            # Download button
            csv4 = filtered_df4.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download FTO report as CSV", csv4, "fto_report.csv", "text/csv")

    with tab5:
        st.markdown("### 🛠️ Blockwise & Work Category-wise Scheme Breakdown")
        st.caption("Active distribution across categories of public rural infrastructure works")
        
        if df_category is not None:
            # Multi-select for category filters
            cols = [c for c in df_category.columns if c not in ["Block Name", "Grand Total"]]
            selected_categories = st.multiselect("Select Categories to Chart:", cols, default=cols[:4])
            
            # Stacked bar chart
            st.markdown("#### Work Category Distribution by Block")
            fig_cat = px.bar(
                df_category,
                x="Block Name",
                y=selected_categories,
                barmode="stack",
                title="Scheme Distribution by Rural Asset Category"
            )
            fig_cat.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig_cat, use_container_width=True)
            
            # Category Totals Pie Chart
            st.markdown("#### Overall Category Proportion in Birbhum")
            category_totals = df_category[cols].sum().reset_index()
            category_totals.columns = ["Category", "Total Schemes"]
            fig_pie = px.pie(
                category_totals,
                values="Total Schemes",
                names="Category",
                color_discrete_sequence=px.colors.qualitative.Pastel
            )
            st.plotly_chart(fig_pie, use_container_width=True)
            
            # Data table
            st.markdown("#### Detailed Category Table")
            search_query5 = st.text_input("🔍 Search block in Categories table:", "")
            filtered_df5 = df_category[df_category['Block Name'].str.contains(search_query5, case=False)] if search_query5 else df_category
            st.dataframe(filtered_df5, use_container_width=True)
            
            # Download button
            csv5 = filtered_df5.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download Category report as CSV", csv5, "category_report.csv", "text/csv")


elif role == "🔒 Admin (Upload & Edit)":
    st.subheader("🔒 Administrator Management Panel")
    st.markdown("---")
    
    # Simple password protection
    passwd = st.text_input("Enter Administrator Access Password:", type="password")
    
    if passwd == "admin123":
        st.success("Access Granted! You can now update report data dynamically.")
        
        admin_tab1, admin_tab2 = st.tabs([
            "📤 Dynamic Data Editor (Manual Updates)",
            "📁 Bulk Report File Uploader (.CSV)"
        ])
        
        with admin_tab1:
            st.markdown("### Live Table Editor")
            st.info("Directly modify any row or value below. Remember to click **'Save All Changes'** to update the database.")
            
            table_to_edit = st.selectbox("Select Report Table to Modify:", [
                "📱 Live NMMS Status", 
                "🏗️ Scheme & Ongoing Status", 
                "🔒 e-KYC Verification Status", 
                "💳 Material FTO Checking",
                "🛠️ Work Category Status",
                "🔑 DSC Enrolment Status"
            ])
            
            if table_to_edit == "📱 Live NMMS Status" and df_live is not None:
                edited_df = st.data_editor(df_live, num_rows="dynamic", use_container_width=True)
                if st.button("💾 Save Changes to NMMS Status"):
                    save_table_data(edited_df, "live_nmms_status.csv")
                    st.success("NMMS Live Report database successfully updated and saved!")
                    st.balloons()
                    
            elif table_to_edit == "🏗️ Scheme & Ongoing Status" and df_ongoing is not None:
                edited_df = st.data_editor(df_ongoing, num_rows="dynamic", use_container_width=True)
                if st.button("💾 Save Changes to Scheme Status"):
                    save_table_data(edited_df, "ongoing_scheme_status.csv")
                    st.success("Scheme & Ongoing status database successfully updated!")
                    st.balloons()
                    
            elif table_to_edit == "🔒 e-KYC Verification Status" and df_ekyc is not None:
                edited_df = st.data_editor(df_ekyc, num_rows="dynamic", use_container_width=True)
                if st.button("💾 Save Changes to e-KYC Status"):
                    save_table_data(edited_df, "ekyc_status.csv")
                    st.success("e-KYC verification database successfully updated!")
                    st.balloons()
                    
            elif table_to_edit == "💳 Material FTO Checking" and df_fto is not None:
                edited_df = st.data_editor(df_fto, num_rows="dynamic", use_container_width=True)
                if st.button("💾 Save Changes to FTO Status"):
                    save_table_data(edited_df, "material_fto_status.csv")
                    st.success("Material FTO database successfully updated!")
                    st.balloons()
                    
            elif table_to_edit == "🛠️ Work Category Status" and df_category is not None:
                edited_df = st.data_editor(df_category, num_rows="dynamic", use_container_width=True)
                if st.button("💾 Save Changes to Categories"):
                    save_table_data(edited_df, "work_category_status.csv")
                    st.success("Category status database successfully updated!")
                    st.balloons()
                    
            elif table_to_edit == "🔑 DSC Enrolment Status" and df_dsc is not None:
                edited_df = st.data_editor(df_dsc, num_rows="dynamic", use_container_width=True)
                if st.button("💾 Save Changes to DSC Enrolment"):
                    save_table_data(edited_df, "dsc_status.csv")
                    st.success("DSC Enrolment database successfully updated!")
                    st.balloons()
                    
        with admin_tab2:
            st.markdown("### Bulk Data Upload")
            st.warning("Uploading a CSV file will completely replace the current version of the selected table. Make sure the headers match perfectly.")
            
            table_to_replace = st.selectbox("Select Report Table to Overwrite via File:", [
                "📱 Live NMMS Status", 
                "🏗️ Scheme & Ongoing Status", 
                "🔒 e-KYC Verification Status", 
                "💳 Material FTO Checking",
                "🛠️ Work Category Status",
                "🔑 DSC Enrolment Status"
            ], key="replace_selectbox")
            
            uploaded_file = st.file_uploader("Upload CSV File:", type=["csv"])
            
            if uploaded_file is not None:
                try:
                    uploaded_df = pd.read_csv(uploaded_file)
                    st.write("Preview of Uploaded Data:")
                    st.dataframe(uploaded_df.head(5), use_container_width=True)
                    
                    filename_map = {
                        "📱 Live NMMS Status": "live_nmms_status.csv",
                        "🏗️ Scheme & Ongoing Status": "ongoing_scheme_status.csv",
                        "🔒 e-KYC Verification Status": "ekyc_status.csv",
                        "💳 Material FTO Checking": "material_fto_status.csv",
                        "🛠️ Work Category Status": "work_category_status.csv",
                        "🔑 DSC Enrolment Status": "dsc_status.csv"
                    }
                    
                    if st.button("🔥 Overwrite Database Table with File"):
                        target_filename = filename_map[table_to_replace]
                        save_table_data(uploaded_df, target_filename)
                        st.success(f"Successfully overwrote table with uploaded {uploaded_file.name}!")
                        st.balloons()
                except Exception as e:
                    st.error(f"Error parsing uploaded file: {e}")
                    
    elif passwd != "":
        st.error("Incorrect administrator access password. Please try again.")
