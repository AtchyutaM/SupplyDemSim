# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 11:18:53 2021

@author: atchyuta
"""

import pandas as pd
import numpy as np
import streamlit as st
# Step 1 - no randomness - 1 product

# Streamlit
st.title('A Simple Supply Chain Dynamics Simulator')
st.write('Version 1.0')

#Add a selectbox to the sidebar:
Select_FillPolicy = st.sidebar.selectbox(
  'Select Fill Policy',
    ('Proprtional Allocation', 'Customer 1 Bias')
)

Select_StartStrategy = st.sidebar.selectbox(
  'Select Start Strategy',
    ( 'Fixed Starts','Releases equal to demand')
)


Select_DemandStrategy = st.sidebar.selectbox(
  'Select Demand',
    ( 'Fixed Demand','Normal Distibution')
)


#st.text('Please choose ')
st.header('Select Paramters:') 

left_column, right_column = st.beta_columns(2)
# You can use a column just like st.sidebar:
with left_column:
    chosenprods = st.radio(
        'Choose Number of Products',
        ("1", "2"))
    st.write(f"You choose {chosenprods} products")

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosencusts = st.radio(
        'Choose Number of Customers',
        ("1", "2"))
    st.write(f"You choose {chosencusts} customers")


left_column2, right_column2 = st.beta_columns(2)
# You can use a column just like st.sidebar:
with left_column2:
    chosentime =  st.slider(
    'Choose Number of Time Periods',
    0, 10)
    st.write(f"You choose {chosentime} Time Periods")

# Or even better, call Streamlit functions inside a "with" block:
with right_column2:
    chosenprodstages = st.radio(
        'Choose Number of Production Stages',
        ("1", "2", "3"))
    st.write(f"You choose {chosenprodstages} Production Stages")

##
    
st.header('Parameters for Selected Policies:')    

st.subheader('Start Strategy:')
st.write('Choosen Start Strategy', 'is', Select_StartStrategy)
left_column3, right_column3 = st.beta_columns(2)
# You can use a column just like st.sidebar:
with left_column3:
    chosenStarts =  st.slider(
    'Select Number of Fixed Starts',
    0, 20)
    #st.write(f"You choose {chosenStarts} Fixed Starts for each product")

st.subheader('Fill policy:')
st.write('Choosen Fill policy', 'is:', Select_FillPolicy)

st.subheader('Demand Generation policy:')
st.write('Choosen Demand generation process', 'is:', Select_DemandStrategy)

left_column4, right_column4 = st.beta_columns(2)
# You can use a column just like st.sidebar:
with left_column4:
    chosenDemand =  st.slider(
    'Choose Number of Fixed Demands',
    0, 20)
    #st.write(f"You choose {chosenDemand} Fixed Demand for each customer and each product")

#chosenprodstages = 3
#chosentime = 6


# with st.form("my_form"):
#     st.write("Inside the form")
#     slider_val = st.slider("Form slider")
#     checkbox_val = st.checkbox("Form checkbox")

#     # Every form must have a submit button.
#     submitted = st.form_submit_button("Submit")
#     if submitted:
#         st.write("slider", slider_val, "checkbox", checkbox_val)

# st.write("Outside the form")


# create supply datafrme

WIP_names=["Stage 1","Stage 2","Stage 3","Stage 4"]
chosenprodstages = int(chosenprodstages)
WIP_names = WIP_names[0:chosenprodstages]
column_names = WIP_names.copy()
column_names.insert(0,"Releases")
column_names.extend(["Inv"])
no_of_stages = chosenprodstages
row_names = ["Period 0","Period 1", "Period 2", "Period 3", "Period 4","Period 5", "Period 6",
             "Period 7", "Period 8", "Period 9", "Period 10"]
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
IntialInv = [10,10]
IntialInv_Stage_Prod1 = [0,0,0]
IntialInv_Stage2_prod2 = [0,0,0]  

# create demand data frame 
Demand_stages = ["Period-1","Period-2","Period-3"]
Demand_stages = Demand_stages[0:chosenprodstages]
column_names_dem = Demand_stages
column_names_dem.insert(0,"New Order")
column_names_dem.extend(["Current Period"])
#column_names_dem = ["New Orders","Period-3","Next Period 2","Next Period 3","Period Now"]
row_names_dem = ["Period 0","Period 1", "Period 2", "Period 3", "Period 4","Period 5", "Period 6",
             "Period 7", "Period 8", "Period 9", "Period 10"]
row_names_dem = row_names[0:chosentime+1]
zero_data_dem = np.zeros(shape=(len(row_names_dem),len(column_names_dem)))
dem_cust1_prod1 = pd.DataFrame(zero_data_dem,row_names_dem, column_names_dem)
#print(dem_cust1_prod1)

dem_cust1_prod2 = pd.DataFrame(zero_data_dem,row_names_dem, column_names_dem)
#print(dem_cust1_prod2)

if chosencusts > 1:
    dem_cust2_prod1 = pd.DataFrame(zero_data_dem,row_names_dem, column_names_dem)
    #print(dem_cust2_prod1)
    
    dem_cust2_prod2 = pd.DataFrame(zero_data_dem,row_names_dem, column_names_dem)
    #print(dem_cust2_prod2)


# Create Fill Strategy dataframe
Cust_names = ["Cust1","Cust2"]
zero_data_fill = np.zeros(shape=(len(row_names_dem),len(Cust_names)))
Fill_prod1 = pd.DataFrame(zero_data_fill,row_names_dem, Cust_names)
Fill_prod2 = pd.DataFrame(zero_data_fill,row_names_dem, Cust_names)


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

#for now fixed

#How many periods I want to run?
# A Simple check

#Start os Prod A
# Starts of Prod B

#output - Period by Period report of inv, backroders 

# I always tell people, 
# The useful support tool allows 

# porfolo of fab release policies, 4 ways I can do Demand policies, which policy do I want to test out.



# # create supply datafrme
# column_names = ["Releases","Stage 1","Stage 2","Stage 3","Inv"]
# WIP_names=["Stage 1","Stage 2","Stage 3"]
# no_of_stages = 3
# row_names = ["Period 0","Period 1", "Period 2", "Period 3", "Period 4","Period 5", "Period 6",
#              "Period 7", "Period 8", "Period 9", "Period 10"]
# Products = ["Prod 1","Prod 2"]    
# zero_data = np.zeros(shape=(len(row_names),len(column_names)))
# Prod1_Supply = pd.DataFrame(zero_data,row_names, column_names)
# print(Prod1_Supply)

# Prod2_Supply= pd.DataFrame(zero_data,row_names, column_names)
# print(Prod2_Supply)

# WIP = np.zeros(shape=(len(row_names),1), dtype=int)

# # Release and Inv for period 1
IntialRel = [10,10]
IntialInv = [10,10]
IntialInv_Stage_Prod1 = [0,0,0]
IntialInv_Stage2_prod2 = [0,0,0]  

# New reeleases generation
NewReleases_Prod1 = np.zeros(shape=(len(row_names),1), dtype=int) + chosenStarts 
NewReleases_Prod2 = np.zeros(shape=(len(row_names),1), dtype=int) + chosenStarts

# New order generation
# New orders coming in for each period
NewOrders_Prod1_cust1 =  np.zeros(shape=(len(row_names),1), dtype=int) + chosenDemand 
NewOrders_Prod2_cust1 =  np.zeros(shape=(len(row_names),1), dtype=int) + chosenDemand

if chosencusts > 1:
    NewOrders_Prod1_cust2 =  np.zeros(shape=(len(row_names),1), dtype=int) + chosenDemand 
    NewOrders_Prod2_cust2 =  np.zeros(shape=(len(row_names),1), dtype=int) + chosenDemand



# # create demand data frame 
# column_names_dem = ["New Orders","Period-3","Next Period 2","Next Period 3","Period Now"]
# row_names_dem = ["Period 0","Period 1", "Period 2", "Period 3", "Period 4","Period 5", "Period 6",
#              "Period 7", "Period 8", "Period 9", "Period 10"]
# zero_data_dem = np.zeros(shape=(len(row_names_dem),len(column_names_dem)))
# dem_cust1_prod1 = pd.DataFrame(zero_data_dem,row_names_dem, column_names_dem)
# print(dem_cust1_prod1)

# dem_cust1_prod2 = pd.DataFrame(zero_data_dem,row_names_dem, column_names_dem)
# print(dem_cust1_prod2)

# dem_cust2_prod1 = pd.DataFrame(zero_data_dem,row_names_dem, column_names_dem)
# print(dem_cust2_prod1)

# dem_cust2_prod2 = pd.DataFrame(zero_data_dem,row_names_dem, column_names_dem)
# print(dem_cust2_prod2)

# create Inv data frame 
#INV DF is tracking the inventory for a product
#INV_prod1 = np.zeros(shape=(len(row_names),1), dtype=int)
#INV_Prod2 = np.zeros(shape=(len(row_names),1), dtype=int)

#FGI_prod1 = np.zeros(shape=(len(row_names),1), dtype=int)
#FGI_Prod2 = np.zeros(shape=(len(row_names),1), dtype=int)

column_names_inv = ["Inv","Demand_c1", "Fullfilled_c1", "Backorders_c1", "Demand_c2", "Fullfilled_c2", "Backorders_c2","FGI"]

row_names_inv = ["Period 0","Period 1", "Period 2", "Period 3", "Period 4","Period 5", "Period 6",
             "Period 7", "Period 8", "Period 9", "Period 10"]
zero_data_inv = np.zeros(shape=(len(row_names_inv),len(column_names_inv)))
Inv_Prod1 = pd.DataFrame(zero_data_inv,row_names_inv, column_names_inv)
#print(Inv_Prod1)

Inv_Prod2 = pd.DataFrame(zero_data_inv,row_names_inv, column_names_inv)
#print(Inv_Prod2)

FGI = np.zeros(shape=(len(row_names),1), dtype=int)

# Start stategy
column_names_StartStrat = ["Start Prod1","Start Prod2"]
row_names_StartStrat = ["Period 0","Period 1", "Period 2", "Period 3", "Period 4","Period 5", "Period 6",
             "Period 7", "Period 8", "Period 9", "Period 10"]
zero_data_StartStrat = np.zeros(shape=(len(row_names_StartStrat),len(column_names_StartStrat)))
df_StartStrat = pd.DataFrame(zero_data_StartStrat,row_names_StartStrat, column_names_StartStrat)
#print(df_StartStrat)


# Fill stategy
column_names_FillStrat = ["Fill Cust1","Fill Cust2"]
row_names_FillStrat = ["Period 0","Period 1", "Period 2", "Period 3", "Period 4","Period 5", "Period 6",
             "Period 7", "Period 8", "Period 9", "Period 10"]
zero_data_FillStrat = np.zeros(shape=(len(row_names_FillStrat),len(column_names_FillStrat)))
FillStrat_prod1 = pd.DataFrame(zero_data_FillStrat,row_names_FillStrat, column_names_FillStrat)
#print(FillStrat_prod1)

FillStrat_prod2 = pd.DataFrame(zero_data_FillStrat,row_names_FillStrat, column_names_FillStrat)
#print(FillStrat_prod2)


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
          #dem_cust1_prod1['Current Period'] = 
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
          Prod1_Supply.iloc[i,0] = NewReleases_Prod1[i]
          Prod2_Supply.iloc[i,0] = NewReleases_Prod2[i]
          WIP =  Prod1_Supply[WIP_names].sum(axis=1) + Prod2_Supply[WIP_names].sum(axis=1)
          print("I am in:",i)
          print(Prod1_Supply)
          print(Prod2_Supply)
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
          # Step 4: Run the Fill policy
          if (dem_cust1_prod1['Current Period'] [i] + dem_cust2_prod1['Current Period'] [i]) != 0 :
              FillStrat_prod1['Fill Cust1'] [i] =  dem_cust1_prod1['Current Period'] [i]/ (dem_cust1_prod1['Current Period'] [i] + dem_cust2_prod1['Current Period'] [i])
              if chosencusts > 1:
                  FillStrat_prod1['Fill Cust2'] [i] =  dem_cust2_prod1['Current Period'] [i]/ (dem_cust1_prod1['Current Period'] [i] + dem_cust2_prod1['Current Period'] [i])
              FillStrat_prod2['Fill Cust1'] [i] =  dem_cust1_prod2['Current Period'] [i]/ (dem_cust1_prod2['Current Period'] [i] + dem_cust2_prod2['Current Period'] [i])
              if chosencusts > 1:
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
          
          Inv_Prod1['FGI'][i] =  Inv_Prod1["Inv"][i] -  Inv_Prod1['Fullfilled_c1'] [i] - Inv_Prod1['Fullfilled_c2'] [i]
          Inv_Prod2['FGI'][i] =  Inv_Prod2["Inv"][i] -  Inv_Prod2['Fullfilled_c1'] [i] - Inv_Prod2['Fullfilled_c2'] [i]
          
print(Prod1_Supply)
print(Prod2_Supply)     
print(dem_cust1_prod1)
print(dem_cust2_prod1)
print(dem_cust1_prod2)
print(dem_cust2_prod2)
print(Inv_Prod1)
print(Inv_Prod2)
print(FillStrat_prod1)
print(FillStrat_prod2)


          
        
              
              
              
                            
              
              
          
        
        
                
            
            
#             df.iloc[i,0] = 10
            
    


# # Python index starts from 0
# for i in range(len(row_names)):
#     for j in range(len(column_names)):
#         #df[j][i]
#         if j == 0: # Releases
#             df.iloc[i,j] = 10
#         elif j == 4: # Inv
#              if i ==0 :
#                  df.iloc[i,j] =0;
#              else:
#                  df.iloc[i,j] = df.iloc[i-1][j]+ df.iloc[i][j-1]*p_move
#         elif j == 1: # stage 1
#             if i ==0: # if period 1clc
#                  df.iloc[i,j] = df.iloc[i,j-1]
#             else: # not period 1
#                 # at stage 1 and period 1 in a period, releases in this period + what ever was left behind from previous period
#                 df.iloc[i,j] = df.iloc[i,j-1] + df.iloc[i-1,j]*p_sit
#         else: # any other stage
#             if i == 0: # in period 1
#                 df.iloc[i,j] = 0
#             else: # in any otehr period
#             # whatever has stayed from previous period same stage+ whatever has moved from pervious period previous stage
#                 df.iloc[i,j] = df.iloc[i-1,j]* p_sit + df.iloc[i-1,j-1]* p_move
# print(df)

#improvement options - use iterrows and itter tuples doe speed if needed 

# demand logic

# #probs_demand
# p_sit_dem = 0.2
# p_move_dem = 0.7
# p_scarp_dem = 0.1


# # create demand data frame 
# # separte for now - but we can integrate into the for loop
# column_names_dem = ["Period Now","Next Period 1","Next Period 2","Next Period 3"]
# row_names_dem = ["Demand"]
# zero_data_dem = np.zeros(shape=(len(row_names_dem),len(column_names_dem)))
# df_dem = pd.DataFrame(zero_data_dem,row_names_dem, column_names_dem)
# print(df_dem)

# for i in range(len(row_names_dem)):
#     for j in range(len(column_names_dem)):
#     # first step is to compute and move demands
#         if j == 0:
#             Real_demand = df.iloc[i,j] # these will all be integarted into one for loop
#             df_dem.iloc[i,j]= df_dem.iloc[i,j]*p_sit_dem + df_dem.iloc[i,j+1]*p_move_dem # generate the next periods real demand
#         elif j<len(column_names_dem)-2:
#             df_dem.iloc[i,j]= df_dem.iloc[i,j]*p_sit_dem + df_dem.iloc[i,j+1]*p_move_dem
#         else:
#             df_dem.iloc[i,j]= df_dem.iloc[i,j]*p_sit_dem + 10 # for now lets generate 10 units of demand determinitsically

# print(df_dem)

            
st.header("Supply Data")
st.write('Product 1')
st.table(Prod1_Supply)
st.write('Product 2')
st.table(Prod2_Supply)


st.header("Demand Data")
st.write('Customer 1 Demand product 1')
st.table(dem_cust1_prod1)
st.write('Customer 1 Demand product 2')
st.table(dem_cust1_prod2)
st.write('Customer 2 Demand product 1')
st.table(dem_cust2_prod1)
st.write('Customer 2 Demand product 2')
st.table(dem_cust2_prod2)

st.header("Inv Data")
st.write('Prod 1 Inv Data')
st.table(Inv_Prod1)
st.write('Prod 2 Inv Data')
st.table(Inv_Prod2)

#st.write("Demand Data")
#st.table('Customer 1 Demand product 1',dem_cust1_prod1)
#st.table('Customer 1 Demand product 2',dem_cust1_prod2)
#st.table('Customer 2 Demand product 2',dem_cust2_prod2)

#x = st.slider('Select Number of Products')  # 👈 this is a widget
#st.write('Number of Products Selected', 'is', x)

#Y = st.slider('Select Number of Customers')  # 👈 this is a widget
#st.write('Number of Customers Selected', 'is', Y)



