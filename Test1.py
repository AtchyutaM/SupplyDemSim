# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 11:18:53 2021

@author: atchyuta
"""
## Bring in data

import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt

def selected(url):
     st.markdown(f'<p style="color:#33ff33;font-size:12px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)

def selected2(url):
     st.markdown(f'<p style="color:#33ff33;font-size:14px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)

# Streamlit
st.title('A Simple Supply Chain Dynamics Simulator')
st.write('Version 1.1')

#Sidebar Selections:
Select_FillPolicy = st.sidebar.selectbox(
  'Select Fill Policy',
    ('Proprtional Allocation', 'Customer 1 Bias')
)

Select_StartStrategy = st.sidebar.selectbox(
  'Select Start Strategy',
    ( 'Fixed Starts','CONWIP')
)

# if Select_StartStrategy == "CONWIP":
#     Select_SubStartStrategy = st.sidebar.selectbox(
#       'Select Sub level Start Strategy',
#         ( 'Releases equal to Demand','Set Manual start levels')
#     )

Select_DemandStrategy = st.sidebar.selectbox(
  'Select Demand',
    ( 'Fixed Demand','Normal Distibution')
)

# Granular Mode
# st.header('Select Mode:')
# left_column, right_column = st.columns(2)
# # You can use a column just like st.sidebar:
# with left_column:
#     Mode = st.radio(
#         'Choose which mode you want to run in',
#         ("Simplified", "Granular"))
#     st.write(f"You choose {Mode} Mode")
# st.write('Note: Granular mode offers greater control of releases, demand and Inventories across all time periods')

#Select Parameters
st.header('Select Parameters:') 

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
with left_column:
    chosenprods = st.radio(
        'Choose Number of Products',
        ("1", "2"))
    selected(f"You choose {chosenprods} products")

with right_column:
    chosencusts = st.radio(
        'Choose Number of Customers',
        ("1", "2"))
    selected(f"You choose {chosencusts} customers")


left_column2, right_column2 = st.columns(2)
with left_column2:
    chosentime =  st.slider(
    'Choose Number of Time Periods',
    0, 100)
    selected(f"You choose {chosentime} Time Periods")

with right_column2:
    chosenprodstages = st.radio(
        'Choose Number of Production Stages',
        ("1", "2", "3"))
    selected(f"You choose {chosenprodstages} Production Stages")

## The actual program:
chosencusts = int(chosencusts)  
chosenprods = int(chosenprods)  
st.header('Parameters for Selected Policies:')    

st.subheader('Start Strategy:')
selected2(f"Choosen Start Strategy: {Select_StartStrategy}")

if Select_StartStrategy == "Fixed Starts":
    left_column3, right_column3 = st.columns(2)
    # You can use a column just like st.sidebar:
    with left_column3:
        ChosenStartsP1 =  st.slider(
        'Select Number of Starts in each period for Product 1',
        0, 100)
        ChosenStartsP2 = 0
        #st.write(f"You choose {chosenStarts} Fixed Starts for each product")
    if chosenprods> 1:
        with right_column3:
            ChosenStartsP2 = st.slider(
            'Select Number of Starts in each period for Product 2',
            0, 100)

#Select_StartStrategy = "CONWIP"

if Select_StartStrategy == "CONWIP":
    left_column4, right_column4 = st.columns(2)
    # You can use a column just like st.sidebar:
    with left_column4:
        CONWIPTotal =  st.slider(
        'Select CONWIP level:',
        0, 100)
        #st.write(f"You choose {chosenStarts} Fixed Starts for each product")
        chosenStarts = 0


st.subheader('Initial Inventory:')
left_column5, right_column5 = st.columns(2)
with left_column5:
    IntialInv1 =  st.slider(
    'Choose Intial Inv for Product 1',
    0, 10)
    st.write(f"You choose {IntialInv1} units as Inv of product 1")
    IntialInv2 = 0
if chosenprods>1:
    with right_column5:
        IntialInv2 =  st.slider(
        'Choose Intial Inv for product 2',
        0, 10)
        st.write(f"You choose {IntialInv2} units as Inv for product 2")

st.subheader('Fill policy:')
st.write('Choosen Fill policy', Select_FillPolicy)

st.subheader('Demand Generation policy:')
selected2(f"Choosen Demand generation process is: {Select_DemandStrategy}")

if Select_DemandStrategy == "Fixed Demand":
    left_column6, right_column6 = st.columns(2)
    with left_column6:
        ChosenDemandP1 =  st.slider(
        'Select Demand for Product 1',
        0, 100)
        ChosenDemandP2 = 0
        ChosenDemandStDevP1 = 0
        ChosenDemandStDevP2 = 0
        ChosenDemandStDevP1 = 0
        ChosenDemandStDevP2 = 0
        ChosenDemandCVP1 = 0
        ChosenDemandCVP2 = 0
        #st.write(f"You choose {chosenDemand} Fixed Demand for each customer and each product")
        if chosencusts> 1:
            with right_column6:
                ChosenDemandP2 = st.slider(
                'Select Demand for Product 2',
                0, 100)
                
if Select_DemandStrategy == 'Normal Distibution':
    left_column6, right_column6 = st.columns(2)
    with left_column6:
        ChosenDemandP1 =  st.slider(
        'Select Demand for Product 1',
        0, 100)
        ChosenDemandP2 = 0
        ChosenDemandStDevP1 = 0
        ChosenDemandStDevP2 = 0
        ChosenDemandCVP1 = 0
        ChosenDemandCVP2 = 0
        #st.write(f"You choose {chosenDemand} Fixed Demand for each customer and each product")
        if chosencusts> 1:
            with right_column6:
                ChosenDemandP2 = st.slider(
                'Select Demand for Product 2',
                0, 100)
    left_column7, right_column7 = st.columns(2)
    with left_column7:
        ChosenDemandCVP1 =  st.slider(
        'Select Coefficent of Variation (CV) for Demand of Product 1',
        0, 2)
        ChosenDemandStDevP1 = ChosenDemandCVP1 * ChosenDemandP1
        st.write(f"St Dev of Demand for Product 1: {ChosenDemandStDevP1}")
        ChosenDemandCVP2  = 0
        #st.write(f"You choose {chosenDemand} Fixed Demand for each customer and each product")
        if chosencusts> 1:
            with right_column7:
                ChosenDemandCVP2 = st.slider(
                'Select Coefficent of Variation (CV) for Demand of Product 2',
                0, 2)
                ChosenDemandStDevP2 = ChosenDemandCVP2 * ChosenDemandP2
                st.write(f"St Dev of Demand for Product 2: {ChosenDemandStDevP2}")
        
#For debug
# chosenprodstages = 1
# chosentime = 20
# ChosenStartsP1 = 10
# ChosenStartsP2 = 10
# ChosenDemandP1 = 10
# ChosenDemandP2 = 0
# ChosenDemandStDevP2 = 0
# ChosenDemandStDevP1 = 0
# chosenprods = 1
# chosencusts = 1
# IntialInv1 = 0
# IntialInv2 = 0

ChosenDemandStDevP1 = ChosenDemandCVP1 * ChosenDemandP1
ChosenDemandStDevP2 = ChosenDemandCVP2 * ChosenDemandP2
# create supply datafrme

WIP_names=["Stage 1","Stage 2","Stage 3","Stage 4"]
chosenprodstages = int(chosenprodstages)
WIP_names = WIP_names[0:chosenprodstages]
column_names = WIP_names.copy()
column_names.insert(0,"Releases")
column_names.extend(["Inv"])
no_of_stages = chosenprodstages
#row_names = ["Period 0","Period 1", "Period 2", "Period 3", "Period 4","Period 5", "Period 6",
# "Period 7", "Period 8", "Period 9", "Period 10"]
row_names = ['Period ' + str(x) for x in range(1,100)]
row_names = row_names[0:chosentime+1]

Products = ["Prod 1","Prod 2"]    
zero_data = np.zeros(shape=(len(row_names),len(column_names)))
Prod1_Supply = pd.DataFrame(zero_data,row_names, column_names)
#print(Prod1_Supply)

Prod2_Supply= pd.DataFrame(zero_data,row_names, column_names)
#print(Prod2_Supply)

WIP = np.zeros(shape=(len(row_names),1), dtype=int)

# Release and Inv for period 1
IntialRel = [10,10]
IntialInv = [IntialInv1,IntialInv2]
IntialInv_Stage_Prod1 = [0,0,0]
IntialInv_Stage2_prod2 = [0,0,0]  

# create demand data frames 
Demand_stages = ["Period-1","Period-2","Period-3"]
Demand_stages = Demand_stages[0:chosenprodstages]
column_names_dem = Demand_stages
column_names_dem.insert(0,"New Order")
column_names_dem.extend(["Current Period"])

zero_data_dem = np.zeros(shape=(len(row_names),len(column_names_dem)))


dem_cust1_prod1 = pd.DataFrame(zero_data_dem,row_names, column_names_dem)
dem_cust1_prod2 = dem_cust1_prod1.copy()
#print(dem_cust1_prod2)

if chosencusts > 1:
    dem_cust2_prod1 = dem_cust1_prod1.copy()
    dem_cust2_prod2 = dem_cust1_prod1.copy()


# Create Fill Strategy dataframe
Cust_names = ["Cust1","Cust2"]
zero_data_fill = np.zeros(shape=(len(row_names),len(Cust_names)))
Fill_prod1 = pd.DataFrame(zero_data_fill,row_names, Cust_names)
Fill_prod2 = pd.DataFrame(zero_data_fill,row_names, Cust_names)


# # supply Logic
# periods = 4
# steps = 3

# probs_supply
p_sit = 0
p_move = 1
p_scarp = 0

# Demand_prob
p_sit_dem = 0
p_move_dem = 1
p_scarp_dem = 0

# New reeleases generation
NewReleases_Prod1 = np.zeros(shape=(len(row_names),1), dtype=int) + ChosenStartsP1 
NewReleases_Prod2 = np.zeros(shape=(len(row_names),1), dtype=int) + ChosenStartsP2

# New order generation
# New orders coming in for each period

np.random.seed(30)
NewOrders_Prod1_cust1 =  (np.random.normal(size=(len(row_names),1)) * ChosenDemandStDevP1) + ChosenDemandP1
NewOrders_Prod1_cust1 = np.maximum(NewOrders_Prod1_cust1,np.zeros(shape=NewOrders_Prod1_cust1.shape, dtype = NewOrders_Prod1_cust1.dtype)) 
NewOrders_Prod2_cust1 =  (np.random.normal(size=(len(row_names),1)) * ChosenDemandStDevP2) + ChosenDemandP2
NewOrders_Prod2_cust1 = np.maximum(NewOrders_Prod2_cust1,np.zeros(shape=NewOrders_Prod2_cust1.shape, dtype = NewOrders_Prod2_cust1.dtype)) 

if chosencusts > 1:
    NewOrders_Prod1_cust2 =  (np.random.normal(size=(len(row_names),1)) * ChosenDemandStDevP1) + ChosenDemandP1 
    NewOrders_Prod1_cust2 = np.maximum(NewOrders_Prod1_cust2,np.zeros(shape=NewOrders_Prod1_cust2.shape, dtype = NewOrders_Prod1_cust2.dtype)) 
    NewOrders_Prod2_cust2 =  (np.random.normal(size=(len(row_names),1)) * ChosenDemandStDevP2)  + ChosenDemandP2
    NewOrders_Prod2_cust2 = np.maximum(NewOrders_Prod2_cust2,np.zeros(shape=NewOrders_Prod2_cust2.shape, dtype = NewOrders_Prod2_cust2.dtype)) 


column_names_inv = ["Inv","Demand_c1", "Fullfilled_c1", "Backorders_c1","FGI"]
if chosencusts > 1:
    column_names_inv = ["Inv","Demand_c1", "Fullfilled_c1", "Backorders_c1", "Demand_c2", "Fullfilled_c2", "Backorders_c2","FGI"]
zero_data_inv = np.zeros(shape=(len(row_names),len(column_names_inv)))
Inv_Prod1 = pd.DataFrame(zero_data_inv,row_names, column_names_inv)
#print(Inv_Prod1)

Inv_Prod2 = pd.DataFrame(zero_data_inv,row_names, column_names_inv)
#print(Inv_Prod2)

FGI = np.zeros(shape=(len(row_names),1), dtype=int)

# Start stategy
column_names_StartStrat = ["Start Prod1","Start Prod2"]
zero_data_StartStrat = np.zeros(shape=(len(row_names),len(column_names_StartStrat)))
df_StartStrat = pd.DataFrame(zero_data_StartStrat,row_names, column_names_StartStrat)
#print(df_StartStrat)


# Fill stategy
column_names_FillStrat = ["Fill Cust1"]
if chosencusts > 1:
    column_names_FillStrat = ["Fill Cust1","Fill Cust2"]
zero_data_FillStrat = np.zeros(shape=(len(row_names),len(column_names_FillStrat)))

FillStrat_prod1 = pd.DataFrame(zero_data_FillStrat,row_names, column_names_FillStrat)

FillStrat_prod2 = pd.DataFrame(zero_data_FillStrat,row_names, column_names_FillStrat)



#The actual calculation
# Python index starts from 0
for i in range(len(row_names)):
    j=len(column_names)
    if i == 0: # Releases
        # Step 1: run the factory backwards
        Prod1_Supply["Inv"][i] = IntialInv[0] # Allocate initial final inv
        Prod2_Supply["Inv"][i] = IntialInv[1]
        for j in range(no_of_stages):
            k = no_of_stages - (j)
            Prod1_Supply.iloc[i,k] = IntialInv_Stage_Prod1[k-1]
            Prod2_Supply.iloc[i,k] = IntialInv_Stage_Prod1[k-1]
        WIP =  Prod1_Supply[WIP_names].sum(axis=1) + Prod2_Supply[WIP_names].sum(axis=1)
        # Step 2: update the warehouse with the factory output
        Inv_Prod1["Inv"][i] =  Prod1_Supply["Inv"][i]
        Inv_Prod2["Inv"][i] =  Prod2_Supply["Inv"][i]
        # Step 3: Run the demand backwards
            # Do nothing about demand in period 0
        # Step 4: Update Inv DF with Supply and Demand results
        Inv_Prod1["Inv"][i] =  Prod1_Supply["Inv"][i]
        Inv_Prod2["Inv"][i] =  Prod2_Supply["Inv"][i]
        Inv_Prod1['FGI'][i] =  Inv_Prod1["Inv"][i]
        Inv_Prod2['FGI'][i] =  Inv_Prod2["Inv"][i]
        # Step 5: Run the start policy
        #Prod1_Supply.iloc[i,0] = IntialRel[0]
        #Prod2_Supply.iloc[i,0] = IntialRel[1]
        Prod1_Supply.iloc[i,0] = 0
        Prod2_Supply.iloc[i,0] = 0
      
    else:
        # Step 1: run the factory backwards
        #move from last step to inv
        Prod1_Supply["Inv"][i] = Prod1_Supply.iloc[i-1,chosenprodstages]*p_move + Inv_Prod1['FGI'][i-1]
        Prod2_Supply["Inv"][i] = Prod2_Supply.iloc[i-1,chosenprodstages]*p_move + Inv_Prod2['FGI'][i-1]
        for j in range(no_of_stages):
            k = no_of_stages - (j)
            # What ever sits from last period moves to next period 
            Prod1_Supply.iloc[i,k] = Prod1_Supply.iloc[i-1,k] * p_sit + Prod1_Supply.iloc[i-1][k-1]*p_move
            Prod2_Supply.iloc[i,k] = Prod2_Supply.iloc[i-1,k] * p_sit + Prod2_Supply.iloc[i-1][k-1]*p_move
        #calculate releases:
        if Select_StartStrategy == "CONWIP":  
            TotalWIP = Prod1_Supply[WIP_names].sum(axis=1)
            if chosencusts > 1:
                TotalWIP = Prod1_Supply[WIP_names].sum(axis=1) + Prod2_Supply[WIP_names].sum(axis=1)
            AvailforRelease = CONWIPTotal - TotalWIP[i]
            if AvailforRelease >= ChosenDemandP1 + ChosenDemandP2:
                NewReleases_Prod1[i] = ChosenDemandP1
                if chosencusts > 1:
                    NewReleases_Prod2[i] = ChosenDemandP2
            else:
                NewReleases_Prod1[i] = AvailforRelease/chosencusts
                if chosencusts > 1:
                    NewReleases_Prod2[i] = AvailforRelease/chosencusts
        Prod1_Supply.iloc[i,0] = NewReleases_Prod1[i]
        if chosencusts > 1:
            Prod2_Supply.iloc[i,0] = NewReleases_Prod2[i]
        WIP =  Prod1_Supply[WIP_names].sum(axis=1) + Prod2_Supply[WIP_names].sum(axis=1)

        # Step 2: update the warehouse with the factory output
        Inv_Prod1["Inv"][i] =  Prod1_Supply["Inv"][i]
        Inv_Prod2["Inv"][i] =  Prod2_Supply["Inv"][i]
        
        # Step 3: Run the demand backwards
        dem_cust1_prod1['Current Period'] [i] = dem_cust1_prod1.iloc[i-1,chosenprodstages]*p_move + Inv_Prod1['Backorders_c1'][i-1]
        dem_cust1_prod2['Current Period'] [i] = dem_cust1_prod2.iloc[i-1,chosenprodstages]*p_move + Inv_Prod2['Backorders_c1'][i-1]
        if chosencusts > 1:
            dem_cust2_prod1['Current Period'] [i] = dem_cust2_prod1.iloc[i-1,chosenprodstages]*p_move + Inv_Prod1['Backorders_c2'][i-1]
            dem_cust2_prod2['Current Period'] [i] = dem_cust2_prod2.iloc[i-1,chosenprodstages]*p_move + Inv_Prod2['Backorders_c2'][i-1]  
        for j in range(no_of_stages):
            k = no_of_stages - (j)
            dem_cust1_prod1.iloc[i,k] = dem_cust1_prod1.iloc[i-1,k] * p_sit_dem + dem_cust1_prod1.iloc[i-1][k-1]*p_move_dem
            dem_cust1_prod2.iloc[i,k] = dem_cust1_prod2.iloc[i-1,k] * p_sit_dem + dem_cust1_prod2.iloc[i-1][k-1]*p_move_dem
            if chosencusts > 1:
                dem_cust2_prod1.iloc[i,k] = dem_cust2_prod1.iloc[i-1,k] * p_sit_dem + dem_cust2_prod1.iloc[i-1][k-1]*p_move_dem
                dem_cust2_prod2.iloc[i,k] = dem_cust2_prod2.iloc[i-1,k] * p_sit_dem + dem_cust2_prod2.iloc[i-1][k-1]*p_move_dem
        dem_cust1_prod1['New Order'] [i] = NewOrders_Prod1_cust1[i]
        dem_cust1_prod2['New Order'] [i] = NewOrders_Prod2_cust1[i]
        if chosencusts >1:
            dem_cust2_prod1['New Order'] [i] = NewOrders_Prod1_cust2[i]
            dem_cust2_prod2['New Order'] [i] = NewOrders_Prod2_cust2[i]
            print("I am inside even through it should be",i)
        print("This is outside")  

        
        # Step 4: Run the Fill policy
        if (dem_cust1_prod1['Current Period'] [i]) != 0 :
            FillStrat_prod1['Fill Cust1'] [i] =  dem_cust1_prod1['Current Period'] [i]/ (dem_cust1_prod1['Current Period'] [i])
            if chosencusts > 1:
                FillStrat_prod1['Fill Cust1'] [i] =  dem_cust1_prod1['Current Period'] [i]/ (dem_cust1_prod1['Current Period'] [i] + dem_cust2_prod1['Current Period'] [i])
                FillStrat_prod1['Fill Cust2'] [i] =  dem_cust2_prod1['Current Period'] [i]/ (dem_cust1_prod1['Current Period'] [i] + dem_cust2_prod1['Current Period'] [i])
            FillStrat_prod2['Fill Cust1'] [i] =  dem_cust1_prod2['Current Period'] [i]/ (dem_cust1_prod2['Current Period'] [i])
            if chosencusts > 1:
                FillStrat_prod2['Fill Cust1'] [i] =  dem_cust1_prod2['Current Period'] [i]/ (dem_cust1_prod2['Current Period'] [i] + dem_cust2_prod2['Current Period'] [i])
                FillStrat_prod2['Fill Cust2'] [i] =  dem_cust2_prod2['Current Period'] [i]/ (dem_cust1_prod2['Current Period'] [i] + dem_cust2_prod2['Current Period'] [i])
            
        # Step 5: Update Inv DF with Supply and Demand results
        Inv_Prod1['Demand_c1'] [i] = dem_cust1_prod1['Current Period'] [i]
        if chosencusts > 1:
            Inv_Prod1['Demand_c2'] [i] = dem_cust2_prod1['Current Period'] [i]
        Inv_Prod2['Demand_c1'] [i] = dem_cust1_prod2['Current Period'] [i]
        if chosencusts > 1:
            Inv_Prod2['Demand_c2'] [i] = dem_cust2_prod2['Current Period'] [i]
        
        Inv_Prod1['Fullfilled_c1'] [i] = min((Inv_Prod1["Inv"][i]* FillStrat_prod1['Fill Cust1'] [i]),Inv_Prod1['Demand_c1'] [i])
        if chosencusts > 1:
            Inv_Prod1['Fullfilled_c2'] [i] = min((Inv_Prod1["Inv"][i]* FillStrat_prod1['Fill Cust2'] [i]),Inv_Prod1['Demand_c2'] [i])
        Inv_Prod2['Fullfilled_c1'] [i] = min((Inv_Prod2["Inv"][i]* FillStrat_prod2['Fill Cust1'] [i]),Inv_Prod2['Demand_c1'] [i])
        if chosencusts > 1:
            Inv_Prod2['Fullfilled_c2'] [i] = min((Inv_Prod2["Inv"][i]* FillStrat_prod2['Fill Cust2'] [i]),Inv_Prod2['Demand_c2'] [i])
         
        Inv_Prod1['Backorders_c1'] [i] = max(Inv_Prod1['Demand_c1'] [i] - Inv_Prod1['Fullfilled_c1'] [i], 0)
        if chosencusts > 1:
            Inv_Prod1['Backorders_c2'] [i] = max(Inv_Prod1['Demand_c2'] [i] - Inv_Prod1['Fullfilled_c2'] [i], 0)
        Inv_Prod2['Backorders_c1'] [i] = max(Inv_Prod2['Demand_c1'] [i] - Inv_Prod2['Fullfilled_c1'] [i], 0)
        if chosencusts > 1:
            Inv_Prod2['Backorders_c2'] [i] = max(Inv_Prod2['Demand_c2'] [i] - Inv_Prod2['Fullfilled_c2'] [i], 0)
        
        Inv_Prod1['FGI'][i] =  Inv_Prod1["Inv"][i] -  Inv_Prod1['Fullfilled_c1'] [i]
        Inv_Prod2['FGI'][i] =  Inv_Prod2["Inv"][i] -  Inv_Prod2['Fullfilled_c1'] [i]
        if chosencusts > 1:
            Inv_Prod1['FGI'][i] =  Inv_Prod1["Inv"][i] -  Inv_Prod1['Fullfilled_c1'] [i] - Inv_Prod1['Fullfilled_c2'] [i]
            Inv_Prod2['FGI'][i] =  Inv_Prod2["Inv"][i] -  Inv_Prod2['Fullfilled_c1'] [i] - Inv_Prod2['Fullfilled_c2'] [i]




print(Inv_Prod1)
print(Inv_Prod2)
print(FillStrat_prod1)
print(FillStrat_prod2)

print(Prod1_Supply)
print(Prod2_Supply) 
print('demand data')   
print(dem_cust1_prod1)
print(dem_cust1_prod2)
print(Inv_Prod1)
print(Inv_Prod2)
print(FillStrat_prod1)
print(FillStrat_prod2)

# display output:

st.header("Supply Data")
st.write('Product 1')
st.table(Prod1_Supply.style.format("{:.2f}"))

if chosenprods >1:
    st.write('Product 2')
    st.table(Prod2_Supply.style.format("{:.2f}"))


st.header("Demand Data")
st.write('Customer 1 Demand product 1')
st.table(dem_cust1_prod1.style.format("{:.2f}"))
if chosenprods > 1:
    st.write('Customer 1 Demand product 2')
    st.table(dem_cust2_prod2.style.format("{:.2f}"))
if chosencusts >1:
    st.write('Customer 2 Demand product 1')
    st.table(dem_cust2_prod1.style.format("{:.2f}"))
if chosenprods > 1 and chosencusts > 1:
    st.write('Customer 2 Demand product 2')
    st.table(dem_cust2_prod2.style.format("{:.2f}"))

st.header("Inv Data")
#st.write('Prod 1 Inv Data')
#st.table(Inv_Prod1)
#st.line_chart(Inv_Prod1[['Inv','Demand_c1','Backorders_c1']])
#if chosenprods > 1:
    #st.write('Prod 2 Inv Data')
    #st.line_chart(Inv_Prod2[['Inv','Demand_c2','Backorders_c2']])
    #st.table(Inv_Prod2)
    
#st.bar_chart(Inv_Prod1[['Inv','Demand_c1','Backorders_c1']])

Inv_Prod1['Periods'] = Inv_Prod1.index.copy()
c = alt.Chart(Inv_Prod1).mark_bar().encode(
    alt.X('Periods',sort=None),
    alt.Y('Inv'),
    column='Periods')


#st.altair_chart(c, use_container_width=True)
#st.plt.bar(x-0.2, y1, width)
#st.plt.bar(x+0.2, y2, width)
Inv_Prodplot = Inv_Prod1
if chosenprods >1:
    # Inv_Prod1.rename(columns = {'Inv':'InvProd1'}, inplace = True)
    # Inv_Prod2.rename(columns = {'Inv':'InvProd2'}, inplace = True)
    #frames = [Inv_Prod1,Inv_Prod2]
    Inv_Prod1.columns = [str(col)+'_P1' for col in Inv_Prod1.columns]
    Inv_Prod2.columns = [str(col)+'_P2' for col in Inv_Prod2.columns]
    Inv_Prodplot = Inv_Prod1.join(Inv_Prod2)
#st.write('This is it')
print(Inv_Prodplot)
if chosencusts == 1 and chosenprods ==1:
    Inv_Prodplot = Inv_Prodplot[['Inv','Demand_c1','Fullfilled_c1','Backorders_c1']]
    Inv_Prodplot['Periods'] = Inv_Prod1.index.copy()
    #fig=plt.figure()
    f = Inv_Prodplot.plot(x='Periods', kind ='bar',stacked=False,width =1.5).figure
    st.pyplot(f,use_container_width=True)
if chosencusts >1 and chosenprods ==1:
    Inv_Prodplot = Inv_Prodplot[['Inv_P1','Demand_c1_p1','Demand_c1_P1', 'Fullfilled_c1_P1', 'Backorders_c1_P1',
       'Demand_c2_P1', 'Fullfilled_c2_P1', 'Backorders_c2_P1']]
    Inv_Prodplot['Periods'] = Inv_Prod1.index.copy()
    #fig=plt.figure()
    f = Inv_Prodplot.plot(x='Periods', kind ='bar',stacked=False,width =1.5).figure
    st.pyplot(f,use_container_width=True)
if chosencusts >1 and chosenprods >1:
    Inv_Prodplot = Inv_Prodplot[['Inv_P1', 'Demand_c1_P1', 'Fullfilled_c1_P1', 'Backorders_c1_P1',
       'Demand_c2_P1', 'Fullfilled_c2_P1', 'Backorders_c2_P1', 'FGI_P1',
       'Periods_P1', 'Inv_P2', 'Demand_c1_P2', 'Fullfilled_c1_P2',
       'Backorders_c1_P2', 'Demand_c2_P2', 'Fullfilled_c2_P2',
       'Backorders_c2_P2', 'FGI_P2']]
    st.write('intelligent Plots')
    if max(Inv_Prodplot[['Inv_P1','Inv_P2']].sum(axis=1)) > 5*(ChosenDemandP1+ChosenDemandP2):
        index_min = np.argmax((Inv_Prodplot[['Inv_P1','Inv_P2']].sum(axis=1)) > 5*(ChosenDemandP1+ChosenDemandP2))
        st.write(f"Too much Inv strating in period {index_min}: Reduce starts")
        Plot_int1 = Inv_Prodplot[['Inv_P1', 'Demand_c1_P1', 'Fullfilled_c1_P1', 'Backorders_c1_P1',
           'Demand_c2_P1', 'Fullfilled_c2_P1', 'Backorders_c2_P1',
           'Periods_P1', 'Inv_P2', 'Demand_c1_P2', 'Fullfilled_c1_P2', 'Demand_c2_P2', 'Fullfilled_c2_P2']]
        Plot_int1['Periods'] = Inv_Prod1.index.copy()
        #fig=plt.figure()
        f = Plot_int1.plot(x='Periods', kind ='bar',stacked=False,width =1.5).figure
        st.pyplot(f,use_container_width=True)
    elif max(Inv_Prodplot[['Backorders_c1_P1','Backorders_c1_P2','Backorders_c2_P2','Backorders_c2_P2']].sum(axis=1)) > 3*(ChosenStartsP1+ChosenStartsP2):
        index_min = np.argmax((Inv_Prodplot[['Backorders_c1_P1','Backorders_c1_P2','Backorders_c2_P2','Backorders_c2_P2']].sum(axis=1)) > 3*(ChosenStartsP1+ChosenStartsP2))
        st.write(f"Too many Backorders strating in period {index_min}: Increase supply")
        Plot_int1 = Inv_Prodplot[['Inv_P1', 'Demand_c1_P1', 'Fullfilled_c1_P1', 'Backorders_c1_P1',
           'Demand_c2_P1', 'Fullfilled_c2_P1', 'Backorders_c2_P1',
           'Periods_P1', 'Inv_P2', 'Demand_c1_P2', 'Fullfilled_c1_P2', 'Demand_c2_P2', 'Fullfilled_c2_P2']]
        Plot_int1['Periods'] = Inv_Prod1.index.copy()
        #fig=plt.figure()
        f = Plot_int1.plot(x='Periods', kind ='bar',stacked=False,width =1.5).figure
        st.pyplot(f,use_container_width=True)
    else:
        Plot_int1 = Inv_Prodplot[['Inv_P1', 'Demand_c1_P1', 'Fullfilled_c1_P1', 'Backorders_c1_P1',
           'Demand_c2_P1', 'Fullfilled_c2_P1',
           'Periods_P1', 'Inv_P2', 'Demand_c1_P2', 'Fullfilled_c1_P2', 'Demand_c2_P2', 'Fullfilled_c2_P2']]
        Plot_int1['Periods'] = Inv_Prod1.index.copy()
        #fig=plt.figure()
        f = Plot_int1.plot(x='Periods', kind ='bar',stacked=False,width =1.5).figure
        st.pyplot(f,use_container_width=True)   

#st.write("Demand Data")
#st.table('Customer 1 Demand product 1',dem_cust1_prod1)
#st.table('Customer 1 Demand product 2',dem_cust1_prod2)
#st.table('Customer 2 Demand product 2',dem_cust2_prod2)

#x = st.slider('Select Number of Products')  # 👈 this is a widget
#st.write('Number of Products Selected', 'is', x)

#Y = st.slider('Select Number of Customers')  # 👈 this is a widget
#st.write('Number of Customers Selected', 'is', Y)

