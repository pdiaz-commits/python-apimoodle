import streamlit as st
import pandas as pd
import requests

# Configuración de la API de Moodle
BASE_URL = "http://localhost:8200"
TOKEN = "aec0ed40e3e47d385208c7a0c4c7dd36"
ENDPOINT = f"{BASE_URL}/webservice/rest/server.php"

# Función auxiliar para llamadas a la API de Moodle
def make_request(function_name, params=None):
    if params is None:
        params = {}
    params.update({
        'wstoken': TOKEN,
        'wsfunction': function_name,
        'moodlewsrestformat': 'json'
    })
    try:
        response = requests.get(ENDPOINT, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Función para obtener información del sitio
def test_site_info():
    """Obtiene información básica del sitio Moodle."""
    result = make_request('core_webservice_get_site_info')
    return result

# Función para obtener usuarios
def get_users():
    """Obtiene una lista de usuarios desde Moodle."""
    params = {
        'criteria[0][key]': 'email',
        'criteria[0][value]': '%',  # Busca todos los usuarios
    }
    return make_request('core_user_get_users', params)

# Función para obtener cursos
def get_courses():
    """Obtiene una lista de cursos desde Moodle."""
    return make_request('core_course_get_courses')

# Interfaz mejorada
def main():
    st.title("Python Streamlit integration Moodle API")
    st.subheader("Extiende Moodle con una interfaz interactiva y mejorada.")
    st.subheader("Integra AI de manera personaliza .")

    # Sección: Información del sitio
    with st.expander("Información del Sitio"):
        if st.button("Cargar información del sitio", key="site_info"):
            result = test_site_info()
            if "error" in result:
                st.error(f"Error: {result['error']}")
            else:
                st.success("Información del sitio obtenida")
                # Presenta la información del sitio de forma atractiva
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.image(result.get("userpictureurl", ""), width=100, caption=result.get("fullname", "Usuario"))
                with col2:
                    st.markdown(f"**Nombre del Sitio:** {result.get('sitename', 'Desconocido')}")
                    st.markdown(f"**Administrador:** {result.get('firstname', 'N/A')} {result.get('lastname', 'N/A')} ({result.get('username', 'N/A')})")
                    st.markdown(f"**Idioma:** {result.get('lang', 'N/A')}")
                    st.markdown(f"**URL del Sitio:** [Visitar Sitio]({result.get('siteurl', '#')})")

                # Funciones disponibles
                st.subheader("Funciones Disponibles")
                functions = result.get("functions", [])
                if functions:
                    functions_df = pd.DataFrame(functions)
                    st.dataframe(functions_df)
                else:
                    st.warning("No se encontraron funciones disponibles.")

                # Características avanzadas
                st.subheader("Características Avanzadas")
                advanced_features = result.get("advancedfeatures", [])
                if advanced_features:
                    features_df = pd.DataFrame(advanced_features)
                    features_df["Estado"] = features_df["value"].apply(lambda x: "Habilitado" if x else "Deshabilitado")
                    st.dataframe(features_df[["name", "Estado"]])
                else:
                    st.warning("No se encontraron características avanzadas.")

    # Sección: Usuarios
    with st.expander("Usuarios"):
        if st.button("Cargar usuarios", key="users"):
            result = get_users()
            if "error" in result:
                st.error(f"Error: {result['error']}")
            else:
                if "users" in result:
                    users = pd.DataFrame(result["users"])
                    st.dataframe(users[["id", "firstname", "lastname", "email"]])
                else:
                    st.warning("No se encontraron usuarios.")

    # Sección: Cursos
    with st.expander("Cursos"):
        if st.button("Cargar cursos", key="courses"):
            result = get_courses()
            if "error" in result:
                st.error(f"Error: {result['error']}")
            else:
                if isinstance(result, list):
                    st.success("Cursos obtenidos exitosamente")
                    courses = pd.DataFrame(result)
                    st.dataframe(courses[["id", "fullname", "shortname"]])
                    st.bar_chart(courses.set_index("fullname")["id"])
                else:
                    st.warning("No se encontraron cursos.")


     
    # Sección: Monitorización
    with st.expander("Monitorización del sistema"):
        if st.button("Monitorizar actividad del sistema", key="monitor_activity"):
            result = monitor_system_activity()
            st.json(result)

        if st.button("Consultar estado del Cron", key="cron_status"):
            result = check_cron_status()
            st.json(result)

        if st.button("Consultar logs del sistema", key="system_logs"):
            result = view_logs()
            st.json(result)

            


if __name__ == "__main__":
    main()
