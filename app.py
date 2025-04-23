import streamlit as st
import psycopg2

st.title("Users from PostgreSQL")

try:
    conn = psycopg2.connect(
        host="db",
        database="mydb",
        user="myuser",
        password="mypassword"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    rows = cur.fetchall()

    st.write("### Users:")
    for row in rows:
        st.write(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

    cur.close()
    conn.close()
except Exception as e:
    st.error(f"Error: {e}")
