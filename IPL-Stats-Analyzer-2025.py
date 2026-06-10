import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="IPL 2025 Dashboard",page_icon="🏏", layout="wide")
st.markdown("<h1 style='text-align:center; color: #FF4B4B; font-family: sans-serif;'>🏏 IPL 2025 Analytics Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload IPL Batting Dataset",type=["csv"])

if uploaded_file:
    df=pd.read_csv(uploaded_file)

    orange_cap_row = df.sort_values(by="Runs", ascending=False).iloc[0]
    oc_player = orange_cap_row["Player Name"]
    oc_runs = orange_cap_row["Runs"]
    oc_team = orange_cap_row["Team"]

    sr_row = df[df['BF'] > 100].sort_values(by="SR", ascending=False).iloc[0]
    sr_player = sr_row["Player Name"]
    sr_val = sr_row["SR"]

    df['HS'] = pd.to_numeric(df['HS'], errors='coerce')
    hs_row = df.sort_values(by="HS", ascending=False).iloc[0]
    hs_player = hs_row["Player Name"]
    hs_val = hs_row["HS"]

    m_col1, m_col2, m_col3 = st.columns(3)
    m_col1.metric("👑 Orange Cap Leader", f"{oc_player} ({oc_team})", f"{oc_runs} Runs")
    m_col2.metric("⚡ Highest Strike Rate", sr_player, f"{sr_val} SR")
    m_col3.metric("🔥 Highest Individual Score", hs_player, f"{int(hs_val)} Runs")
    st.markdown("---")

    team_list=["All Team"] + list(df["Team"].unique())
    selected_team = st.sidebar.selectbox("Select Team Filter",team_list)

    if selected_team == "All Team":
        filtered_df = df
    else:
        filtered_df = df[df["Team"] == selected_team]

    tab1, tab2, tab3 = st.tabs(["🏏 Batting Leaderboards", "📊 Team Performance", "🔍 Player Search Profile"])
    
    with tab1:
    # top 10 batters:-
        top10 = filtered_df.sort_values(by="Runs", ascending=False).head(10)
        st.subheader("Top 10 Batters in IPL(2025):")
        st.dataframe(top10[["Player Name","Runs","Team","Matches"]], use_container_width=True, hide_index=True)

        fig, ax = plt.subplots(figsize=(10,6))
        sns.barplot(x=top10["Runs"],y=top10["Player Name"],palette="flare",ax=ax)
        plt.title("Top Run Scorers in Ipl 2025")
        plt.xlabel("Runs")
        plt.ylabel("Players")
        plt.tight_layout()
        st.pyplot(fig)
        st.divider()

        #top consistent batters:-
        filtered_df['AVG'] = pd.to_numeric(df['AVG'],errors='coerce')
        avg5 = filtered_df.sort_values(by="AVG",ascending=False).head(5).reset_index(drop=True)
        st.subheader("Top 5 Batters With Highest Average in IPL(2025):")
        st.dataframe(avg5[["Player Name","AVG"]], use_container_width=True, hide_index=True)

        fig_avg, ax_avg = plt.subplots(figsize=(10,5))
        sns.barplot(x=avg5["Player Name"],y=avg5["AVG"],palette="magma",ax=ax_avg)
        plt.title("Top Consistent Batters in Ipl 2025")
        plt.ylabel("Average")
        plt.xlabel("Players")
        plt.tight_layout()
        st.pyplot(fig_avg)
        st.divider()

        #top aggressive players:-
        eligible_players = filtered_df[filtered_df['BF'] > 100]
        sr5 = eligible_players.sort_values(by="SR",ascending=False).head(5).reset_index(drop=True)
        st.subheader("Top 5 Batters With Highest SR in IPL(2025):")
        st.dataframe(sr5[["Player Name","SR"]], use_container_width=True, hide_index=True)

        fig_sr, ax_sr = plt.subplots(figsize=(10,5))
        sns.barplot(x=sr5["SR"],y=sr5["Player Name"],palette="crest",ax=ax_sr)
        plt.title("Top SR Batters in Ipl 2025")
        plt.xlabel("Strike-Rate")
        plt.ylabel("Players")
        plt.tight_layout()
        st.pyplot(fig_sr)
        st.divider()

        #highest individual:-
        filtered_df['HS']=pd.to_numeric(df['HS'],errors='coerce')
        hs3 = filtered_df.sort_values(by="HS",ascending=False).head(3).reset_index(drop=True)
        st.subheader("Top 3 Batters With Highest Individual in IPL(2025):")
        st.dataframe(hs3[["Player Name","HS"]], use_container_width=True, hide_index=True)

        fig_hs, ax_hs = plt.subplots(figsize=(10,5))
        sns.barplot(x=hs3["Player Name"],y=hs3["HS"],palette="Blues_r",ax=ax_hs)
        plt.title("Highest Score Batters in Ipl 2025")
        plt.ylabel("Highest Score")
        plt.xlabel("Players")
        plt.tight_layout()
        st.pyplot(fig_hs)
        st.divider()

        #most 4's and 6's 
        col_four,col_six = st.columns(2)

        with col_four:
            f4 = filtered_df.sort_values(by="4s",ascending=False).head(3)
            st.subheader("Top 3 Batters With Highest Fours in IPL(2025):")
            st.dataframe(f4[["Player Name","4s"]], use_container_width=True, hide_index=True)

            fig_4s, ax_4s = plt.subplots(figsize=(6,4))
            sns.barplot(x=f4["Player Name"],y=f4["4s"],palette="GnBu_r",ax=ax_4s)
            plt.title("Highest Fours Hitter Batters in Ipl 2025")
            plt.xlabel("Players")
            plt.ylabel("Fours")
            plt.tight_layout()
            st.pyplot(fig_4s)
            st.divider()

        with col_six:
            s6 = filtered_df.sort_values(by="6s",ascending=False).head(3).reset_index(drop=True)
            st.subheader("Top 3 Batters With Highest sixes in IPL(2025):")
            st.dataframe(s6[["Player Name","6s"]], use_container_width=True, hide_index=True)

            fig_6s, ax_6s = plt.subplots(figsize=(6,4))
            sns.barplot(x=s6["Player Name"],y=s6["6s"],palette="OrRd_r",ax=ax_6s)
            plt.title("Highest six Hitter Batters in Ipl 2025")
            plt.xlabel("Players")
            plt.ylabel("Sixes")
            plt.tight_layout()
            st.pyplot(fig_6s)
            st.divider()

        #most 100's and 50's 
        col_cen,col_half_cen = st.columns(2)

        with col_cen:
            c = filtered_df.sort_values(by="100s",ascending=False).head(3).reset_index(drop=True)
            st.subheader("Top 3 Batters With Highest Centuries in IPL(2025):")
            st.dataframe(c[["Player Name","100s"]], use_container_width=True, hide_index=True)

            fig_100s, ax_100s = plt.subplots(figsize=(6,4))
            sns.barplot(x=c["Player Name"],y=c["100s"],palette="YlOrBr_r",ax=ax_100s)
            plt.title("Highest Century Hitter Batters in Ipl 2025")
            plt.xlabel("Players")
            plt.ylabel("Century")
            plt.tight_layout()
            st.pyplot(fig_100s)
            st.divider()

        with col_half_cen:
            hc = filtered_df.sort_values(by="50s",ascending=False).head(3).reset_index(drop=True)
            st.subheader("Top 3 Batters With Highest Half Centuries in IPL(2025):")
            st.dataframe(hc[["Player Name","50s"]], use_container_width=True, hide_index=True)

            fig_50s, ax_50s = plt.subplots(figsize=(6,4))
            sns.barplot(x=hc["Player Name"],y=hc["50s"],palette="Purples_r",ax=ax_50s)
            plt.title("Highest Half Century Hitter Batters in Ipl 2025")
            plt.xlabel("Players")
            plt.ylabel("Half Century")
            plt.tight_layout()
            st.pyplot(fig_50s)
            st.divider()
    with tab2:
        #team performance
        st.header("Team Performance Matrix")
        col_team_runs,col_team_top_scorer = st.columns(2)

        with col_team_runs:
            team_runs=df.groupby('Team')['Runs'].sum().sort_values(ascending=False).reset_index()
            st.subheader("Team-Wise Total Runs Share in IPL(2025):")
            st.dataframe(team_runs[["Team","Runs"]], use_container_width=True, hide_index=True)

            fig_team_runs, ax_team_runs = plt.subplots(figsize=(6,5))
            colors_list = sns.color_palette("muted")
            plt.pie(team_runs["Runs"], labels=team_runs["Team"], colors=colors_list, autopct='%1.1f%%', startangle=90,radius=0.90)
            plt.title("Highest Runs by a Team in Ipl 2025")
            plt.tight_layout()
            st.pyplot(fig_team_runs)
            st.divider()

        with col_team_top_scorer:
            team_Top_Scorer=df.loc[df.groupby('Team')['Runs'].idxmax(),['Team','Player Name','Runs']].reset_index(drop=True)
            st.subheader("Team-Wise Top Runs Scorer in IPL(2025):")
            st.dataframe(team_Top_Scorer, use_container_width=True, hide_index=True)

            fig_top, ax_top = plt.subplots(figsize=(6,6.25))
            team_Top_Scorer["Label"] = (team_Top_Scorer["Team"] +"\n(" +team_Top_Scorer["Player Name"] + ")")
            sns.barplot(data=team_Top_Scorer,x="Runs",y="Label",palette="rocket",ax=ax_top)
            plt.xlabel("Runs")
            plt.ylabel("Team/Player")
            plt.tight_layout()
            st.pyplot(fig_top)
            st.divider()


        col_team_as,col_team_bound = st.columns(2)

        with col_team_as:
            team_AvgSR=df.groupby('Team')['SR'].mean().sort_values(ascending=False).reset_index()
            st.subheader("Team-Wise Average Strike-Rate in IPL(2025):")
            st.dataframe(team_AvgSR[["Team","SR"]], use_container_width=True, hide_index=True)

            fig_team_as, ax_team_as = plt.subplots(figsize=(6,6))
            sns.barplot(x=team_AvgSR["Team"],y=team_AvgSR["SR"],palette="mako",ax=ax_team_as)
            plt.title("Team Wise Avg. SR in Ipl 2025")
            plt.xlabel("Team")
            plt.ylabel("Avg. SR")
            plt.tight_layout()
            st.pyplot(fig_team_as)
            st.divider()

        with col_team_bound:
            df['boundaries']=df['4s']+df['6s']
            team_total_boundaries=df.groupby('Team')['boundaries'].sum().sort_values(ascending=False).reset_index()
            st.subheader("Team-Wise Total Boundaries in IPL(2025):")
            st.dataframe(team_total_boundaries[["Team","boundaries"]], use_container_width=True, hide_index=True)

            fig_team_bound, ax_team_bound = plt.subplots(figsize=(6,6))
            sns.barplot(x=team_total_boundaries["Team"],y=team_total_boundaries["boundaries"],palette="viridis",ax=ax_team_bound)
            plt.title("Team Wise Total Boundaries in Ipl 2025")
            plt.xlabel("Team")
            plt.ylabel("Boundaries")
            plt.tight_layout()
            st.pyplot(fig_team_bound)

    with tab3:
        player_list = ["Search Player..."] + sorted(list(filtered_df["Player Name"].unique()))
        selected_player = st.sidebar.selectbox("🔍 Find Player Stats", player_list)

        if selected_player != "Search Player...":
         single_player_df = filtered_df[filtered_df["Player Name"] == selected_player]
        
         st.success(f"📊 Single Player Profile: **{selected_player}**")
         st.dataframe(single_player_df, use_container_width=True, hide_index=True)
         st.info(f"💡 Tip: You can clear the player search from the sidebar to check other profiles.")
        else:
            st.info("🔍 Please use the dropdown in the sidebar to search for a specific player's profile.")
        st.markdown("---")
        
