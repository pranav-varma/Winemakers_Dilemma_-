import streamlit as st

def calculate_e_value(sensitivity, specificity, PNS, Harvest_value=1000, Wait_Harvest_NS=1500, Wait_Harvest_S=500):
    # Probability of detected No Storm
    PDNS = specificity*PNS + (1-sensitivity)*(1-PNS)
    print("PDNS =",PDNS)
    st.write("PDNS =",PDNS)
    
    # Probability of No Storm given Detected No Storm
    P_DNS_NS = specificity*PNS / PDNS
    print("P_DNS_NS =",P_DNS_NS)
    st.write("P_DNS_NS =",P_DNS_NS)
    
    # Probability of Detected Storm
    PDS = 1 - PDNS
    
    eValue = PDNS * ( (Wait_Harvest_NS * P_DNS_NS) + (Wait_Harvest_S * (1 - P_DNS_NS)) ) + \
             PDS  * (Harvest_value)
    print("E Value =",eValue)
    st.write("E Value =",eValue)
    
    if(eValue < Harvest_value):
        print("Recommended Action : Harvest Now")
        st.write("Recommended Action : Harvest Now")
    
    P_S = 1- PNS
    P_DS_S = sensitivity*P_S / PDS
    print("P_DS_S =",P_DS_S)
    st.write("P_DS_S =",P_DS_S)

if __name__ == "__main__":
    sensitivity_ip = st.number_input("Sensitivity")
    specificity_ip = st.number_input("Specificity")
    probability_of_no_storm = st.number_input("Probability of No Storm")
    calculate_e_value(sensitivity = sensitivity_ip/100, 
                  specificity = specificity_ip/100, 
                  PNS = probability_of_no_storm/100, 
                  Harvest_value = 1000, 
                  Wait_Harvest_NS = 1500, 
                  Wait_Harvest_S = 500)