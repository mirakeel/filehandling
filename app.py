import streamlit as st
from pathlib import Path

st.set_page_config(page_title="File Manager", layout="centered")
st.title("📁 File Manager")

operation = st.sidebar.radio(
    "Choose an operation",
    ["Create", "Read", "Update", "Delete"]
)

# ---------------- CREATE ----------------
if operation == "Create":
    st.subheader("Create a new file")
    name = st.text_input("File name")
    data = st.text_area("Content to write")

    if st.button("Create File"):
        if not name:
            st.warning("Enter a file name.")
        else:
            file_path = Path(name)
            try:
                if not file_path.exists():
                    file_path.write_text(data)
                    st.success("File created successfully.")
                else:
                    st.error("File name already exists.")
            except Exception as err:
                st.error(f"An error occurred: {err}")

# ---------------- READ ----------------
elif operation == "Read":
    st.subheader("Read a file")
    name = st.text_input("File name")

    if st.button("Read File"):
        file_path = Path(name)
        try:
            if file_path.exists():
                content = file_path.read_text()
                st.text_area("File content", content, height=250)
            else:
                st.error("No file found.")
        except Exception as err:
            st.error(f"An error occurred: {err}")

# ---------------- UPDATE ----------------
elif operation == "Update":
    st.subheader("Update a file")
    name = st.text_input("File name")
    file_path = Path(name) if name else None

    action = st.radio("Choose action", ["Rename", "Append", "Overwrite"])

    if action == "Rename":
        new_name = st.text_input("New file name")
        if st.button("Rename"):
            try:
                if file_path and file_path.exists():
                    new_path = Path(new_name)
                    if not new_path.exists():
                        file_path.rename(new_path)
                        st.success("Renamed successfully.")
                    else:
                        st.error("A file with that name already exists.")
                else:
                    st.error("No such file found.")
            except Exception as err:
                st.error(f"An error occurred: {err}")

    elif action == "Append":
        data = st.text_area("Text to append")
        if st.button("Append"):
            try:
                if file_path and file_path.exists():
                    with open(file_path, "a") as fs:
                        fs.write("\n" + data)
                    st.success("Appended successfully.")
                else:
                    st.error("No such file found.")
            except Exception as err:
                st.error(f"An error occurred: {err}")

    elif action == "Overwrite":
        data = st.text_area("New content")
        if st.button("Overwrite"):
            try:
                if file_path and file_path.exists():
                    file_path.write_text(data)
                    st.success("Overwritten successfully.")
                else:
                    st.error("No such file found.")
            except Exception as err:
                st.error(f"An error occurred: {err}")

# ---------------- DELETE ----------------
elif operation == "Delete":
    st.subheader("Delete a file")
    name = st.text_input("File name")

    if st.button("Delete File", type="primary"):
        file_path = Path(name)
        try:
            if file_path.exists():
                file_path.unlink()
                st.success("File deleted successfully.")
            else:
                st.error("No such file found.")
        except Exception as err:
            st.error(f"An error occurred: {err}")