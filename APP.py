import streamlit as st
import numpy as np
import pickle

st.set_page_config(page_title="Prédiction champignons", page_icon="🍄", layout="centered")

model = pickle.load(open(r"C:\Users\ACH\OneDrive - OFPPT\Documents\AI\Machine_Learning\Projet_Mushrooms\random_forest_model.pkl", "rb"))

st.title("🍄 Prédiction de champignons")
st.header("Veuillez entrer les informations sur le champignon :")

# Division en deux colonnes
with st.form("input_form"):
    col1, col2 = st.columns(2)
    
    with col1:

        cap_shape_val = st.selectbox('🔹 Forme du chapeau :', ('Conical', 'Convex', 'Bell', 'Flat', 'Knobbed', 'Sunken'))
        if cap_shape_val == 'Conical':
            cap_shape = 1
        elif cap_shape_val == 'Convex':
            cap_shape = 2
        elif cap_shape_val == 'Bell':
            cap_shape = 0
        elif cap_shape_val == 'Flat':
            cap_shape = 3
        elif cap_shape_val == 'Knobbed':
            cap_shape = 4
        else:
            cap_shape = 5
        
        # Surface du chapeau
        cap_surface_val = st.selectbox('🔹 Surface du chapeau :', ('Fibrous', 'Grooves', 'Scaly', 'Smooth'))
        if cap_surface_val == 'Fibrous':
            cap_surface = 0
        elif cap_surface_val == 'Grooves':
            cap_surface = 1
        elif cap_surface_val == 'Scaly':
            cap_surface = 2
        else:
            cap_surface = 3

        # Couleur du chapeau
        cap_color_val = st.selectbox('🔹 Couleur du chapeau :', ('Brown', 'Buff', 'Cinnamon', 'Gray', 'Green', 'Pink', 'Purple', 'Red', 'White', 'Yellow'))
        if cap_color_val == 'Brown':
            cap_color = 0
        elif cap_color_val == 'Buff':
            cap_color = 1
        elif cap_color_val == 'Cinnamon':
            cap_color = 2
        elif cap_color_val == 'Gray':
            cap_color = 3
        elif cap_color_val == 'Green':
            cap_color = 4
        elif cap_color_val == 'Pink':
            cap_color = 5
        elif cap_color_val == 'Purple':
            cap_color = 6
        elif cap_color_val == 'Red':
            cap_color = 7
        elif cap_color_val == 'White':
            cap_color = 8
        else:
            cap_color = 9

        # Meurtrissures
        bruises_val = st.selectbox('🔹 Présence de meurtrissures :', ('Yes', 'No'))
        bruises = 0 if bruises_val == 'Yes' else 1

        # Odeur
        Odur_val = st.selectbox('🔹 Odeur :', ('Almond', 'Anise', 'Creosote', 'Fishy', 'Foul', 'Musty', 'Pungent', 'Spicy', 'Other'))
        if Odur_val == 'Almond':
            Odur = 0
        elif Odur_val == 'Anise':
            Odur = 1
        elif Odur_val == 'Creosote':
            Odur = 2
        elif Odur_val == 'Fishy':
            Odur = 3
        elif Odur_val == 'Foul':
            Odur = 4
        elif Odur_val == 'Musty':
            Odur = 5
        elif Odur_val == 'Pungent':
            Odur = 6
        elif Odur_val == 'Spicy':
            Odur = 7
        else:
            Odur = 8

        # Attachement des lamelles
        gill_attachment_val = st.selectbox('🔹 Attachement des lamelles :', ('Attached', 'Free'))
        gill_attachment = 0 if gill_attachment_val == 'Attached' else 1

        # Espacement des lamelles
        gill_spacing_val = st.selectbox('🔹 Espacement des lamelles :', ('Close', 'Crowded'))
        gill_spacing = 0 if gill_spacing_val == 'Close' else 1

        # Taille des lamelles
        gill_size_val = st.selectbox('🔹 Taille des lamelles :', ('Broad', 'Narrow'))
        gill_size = 0 if gill_size_val == 'Broad' else 1

        # Couleur des lamelles
        gill_color_val = st.selectbox('🔹 Couleur des lamelles :', ('Black', 'Brown', 'Buff', 'Chocolate', 'Gray', 'Green', 'Orange', 'Pink', 'Purple', 'Red', 'White', 'Yellow'))
        if gill_color_val == 'Black':
            gill_color = 0
        elif gill_color_val == 'Brown':
            gill_color = 1
        elif gill_color_val == 'Buff':
            gill_color = 2
        elif gill_color_val == 'Chocolate':
            gill_color = 3
        elif gill_color_val == 'Gray':
            gill_color = 4
        elif gill_color_val == 'Green':
            gill_color = 5
        elif gill_color_val == 'Orange':
            gill_color = 6
        elif gill_color_val == 'Pink':
            gill_color = 7
        elif gill_color_val == 'Purple':
            gill_color = 8
        elif gill_color_val == 'Red':
            gill_color = 9
        elif gill_color_val == 'White':
            gill_color = 10
        else:
            gill_color = 11

        # Forme du pied
        stalk_shape_val = st.selectbox('🔹 Forme du pied :', ('Enlarging', 'Tapering'))
        stalk_shape = 0 if stalk_shape_val == 'Enlarging' else 1

        # Base du pied
        stalk_root_val = st.selectbox('🔹 Base du pied :', ('Bulbous', 'Club', 'Cup', 'Equal', 'Rhizomorphs', 'Rooted', 'Other'))
        if stalk_root_val == 'Bulbous':
            stalk_root = 0
        elif stalk_root_val == 'Club':
            stalk_root = 1
        elif stalk_root_val == 'Cup':
            stalk_root = 2
        elif stalk_root_val == 'Equal':
            stalk_root = 3
        elif stalk_root_val == 'Rhizomorphs':
            stalk_root = 4
        elif stalk_root_val == 'Rooted':
            stalk_root = 5
        else:
            stalk_root = 6

    with col2:

        # Surface du pied au-dessus de l’anneau
        stalk_surface_above_ring_val = st.selectbox("🔸 Surface du pied au-dessus de l'anneau :", ('Fibrous', 'Scaly', 'Silky', 'Smooth'))
        if stalk_surface_above_ring_val == 'Fibrous':
            stalk_surface_above_ring = 0
        elif stalk_surface_above_ring_val == 'Scaly':
            stalk_surface_above_ring = 1
        elif stalk_surface_above_ring_val == 'Silky':
            stalk_surface_above_ring = 2
        else:
            stalk_surface_above_ring = 3

        # Surface du pied sous l’anneau
        stalk_surface_below_ring_val = st.selectbox("🔸 Surface du pied sous l'anneau :", ('Fibrous', 'Scaly', 'Silky', 'Smooth'))
        if stalk_surface_below_ring_val == 'Fibrous':
            stalk_surface_below_ring = 0
        elif stalk_surface_below_ring_val == 'Scaly':
            stalk_surface_below_ring = 1
        elif stalk_surface_below_ring_val == 'Silky':
            stalk_surface_below_ring = 2
        else:
            stalk_surface_below_ring = 3

        # Couleur du pied au-dessus de l’anneau
        stalk_color_above_ring_val = st.selectbox("🔸 Couleur du pied au-dessus de l'anneau :", ('Brown', 'Buff', 'Cinnamon', 'Gray', 'Orange', 'Pink', 'Red', 'White', 'Yellow'))
        stalk_color_above_ring = ['Brown', 'Buff', 'Cinnamon', 'Gray', 'Orange', 'Pink', 'Red', 'White', 'Yellow'].index(stalk_color_above_ring_val)

        # Couleur du pied sous l’anneau
        stalk_color_below_ring_val = st.selectbox("🔸 Couleur du pied sous l'anneau :", ('Brown', 'Buff', 'Cinnamon', 'Gray', 'Orange', 'Pink', 'Red', 'White', 'Yellow'))
        stalk_color_below_ring = ['Brown', 'Buff', 'Cinnamon', 'Gray', 'Orange', 'Pink', 'Red', 'White', 'Yellow'].index(stalk_color_below_ring_val)

        # Couleur du voile
        veil_color_val = st.selectbox("🔸 Couleur du voile :", ('Brown', 'Orange', 'White', 'Yellow'))
        veil_color = ['Brown', 'Orange', 'White', 'Yellow'].index(veil_color_val)

        # Nombre d’anneaux
        ring_number_val = st.selectbox("🔸 Nombre d'anneaux :", ('One', 'Two', 'Other'))
        if ring_number_val == 'Other':
            ring_number = 0
        elif ring_number_val == 'One':
            ring_number = 1
        else:
            ring_number = 2

        # Type d’anneau
        ring_type_val = st.selectbox("🔸 Type d'anneau :", ('Cobwebby', 'Evanescent', 'Flaring', 'Large', 'Pendant', 'Other'))
        if ring_type_val == 'Cobwebby':
            ring_type = 0
        elif ring_type_val == 'Evanescent':
            ring_type = 1
        elif ring_type_val == 'Flaring':
            ring_type = 2
        elif ring_type_val == 'Large':
            ring_type = 3
        elif ring_type_val == 'Pendant':
            ring_type = 4
        else:
            ring_type = 5

        # Couleur de l'empreinte de spores
        spore_print_color_val = st.selectbox("🔸 Couleur de l'empreinte de spores :", ('Black', 'Brown', 'Buff', 'Chocolate', 'Green', 'Orange', 'Purple', 'White', 'Yellow'))
        spore_print_color = ['Black', 'Brown', 'Buff', 'Chocolate', 'Green', 'Orange', 'Purple', 'White', 'Yellow'].index(spore_print_color_val)

        # Population
        population_val = st.selectbox("🔸 Taille de la population :", ('Abundant', 'Clustered', 'Numerous', 'Scattered', 'Several', 'Solitary'))
        population = ['Abundant', 'Clustered', 'Numerous', 'Scattered', 'Several', 'Solitary'].index(population_val)

        # Habitat
        habitat_val = st.selectbox("🔸 Habitat :", ('Grasses', 'Leaves', 'Meadows', 'Paths', 'Waste', 'Woods'))
        habitat = ['Grasses', 'Leaves', 'Meadows', 'Paths', 'Waste', 'Woods'].index(habitat_val)

        # Valeur fixe
        veil_type = 0

    submit = st.form_submit_button("Prédire")

# Bouton de prédiction
if submit:
    # Vérification
    inputs = [habitat, population, spore_print_color, stalk_root, stalk_shape, ring_number,
            ring_type, veil_color, stalk_color_below_ring, stalk_color_above_ring, veil_type,
            stalk_surface_below_ring, stalk_surface_above_ring, gill_color, gill_size,
            gill_spacing, gill_attachment, cap_color, bruises, Odur, cap_surface, cap_shape]
    
    if all(x == 0.0 for x in inputs):
        st.warning("Veuillez saisir des valeurs valides pour lancer une prédiction.")
    else:
        features = np.array([inputs])
        prediction = model.predict(features)

        st.markdown("---")
        st.subheader("🧠 Résultat de la Prédiction")
        st.success(f"✅ Classe prédite : **{int(prediction[0])}**")

        df_feat = [[habitat_val, population_val, spore_print_color_val, stalk_root_val, stalk_shape_val, ring_number_val,
            ring_type_val, veil_color_val, stalk_color_below_ring_val, stalk_color_above_ring_val,
            stalk_surface_below_ring_val, stalk_surface_above_ring_val, gill_color_val, gill_size_val,
            gill_spacing_val, gill_attachment_val, cap_color_val, bruises_val, Odur_val, cap_surface_val, cap_shape_val]]
        
    with st.expander("📝 Données saisies"):
            st.dataframe(df_feat)
    
# Arriere
st.markdown(
    """
    <style>
    .stApp {
        background-image:linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url("https://plus.unsplash.com/premium_photo-1704737966313-746586e51913?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8bXVzaHJvb218ZW58MHx8MHx8fDA%3D");
        background-size: cover;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)
    
st.markdown("---")  # Ligne de séparation
    
st.markdown("""
### ℹ️ À propos de cette application
Cette application utilise un modèle de machine learning pour prédire si un champignon est comestible ou toxique, en fonction de ses caractéristiques visuelles et biologiques.

**Projet développé par :** Mohamed Yassine Chalbat  
**Technologies utilisées :** Streamlit, Random Forest, Sklearn, Python  
**Source des données :** [Kaggle - Mushroom Dataset](https://www.kaggle.com/uciml/mushroom-classification)
""")