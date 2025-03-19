import streamlit as st

st.title("Unit Converter App")
st.markdown("Converts length, weight, and time instantly")
st.write("Welcome! Select a category, enter a value, and get the converted result in real-time.")

category = st.selectbox("Choose a category", ["length", "weight", "time"])

def converter_units(category, value, unit):
    if category == "length": 
        if unit == "kilometer to miles":
            return value * 0.621371
        elif unit == "miles to kilometer":
            return value / 0.621371

    elif category == "weight":
        if unit == "kilogram to pounds":
            return value * 2.20462
        elif unit == "pounds to kilogram":
            return value / 2.20462

    elif category == "time":
        if unit == "seconds to minutes":
            return value / 60
        elif unit == "minutes to seconds":
            return value * 60
        elif unit == "minutes to hours":
            return value / 60
        elif unit == "hours to minutes":
            return value * 60
        elif unit == "hours to days":
            return value / 24
        elif unit == "days to hours":
            return value * 24

    return "Invalid Conversion"

# Select conversion units
if category == "length":
    units = st.selectbox("Select conversion", ["kilometer to miles", "miles to kilometer"])
elif category == "weight":
    units = st.selectbox("Select conversion", ["kilogram to pounds", "pounds to kilogram"])
elif category == "time":
    units = st.selectbox("Select conversion", ["seconds to minutes", "minutes to seconds", 
                                               "minutes to hours", "hours to minutes", 
                                               "hours to days", "days to hours"])

# Input value
value = st.number_input("Enter the value to convert", min_value=0.0)

# Convert button
if st.button("Convert"):
    result = converter_units(category, value, units)
    if isinstance(result, str):
        st.error(result)
    else:
        st.success(f"The result is {result:.2f}")
