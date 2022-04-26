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
    calculate_e_value(sensitivity = 0.76,
                  specificity = 0.69, 
                  PNS = 0.25, 
                  Harvest_value = 1000, 
                  Wait_Harvest_NS = 1500, 
                  Wait_Harvest_S = 500)