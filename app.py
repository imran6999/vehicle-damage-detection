import streamlit as st
from model_helper import predict

st.set_page_config(page_title="Vehicle Damage Detection", layout="centered")
st.title("🚗 Vehicle Damage Detection")

uploaded_file = st.file_uploader("📷 Upload an image of your vehicle", type=['jpg', 'png'])

if uploaded_file:
    image_path = "temp_file.jpg"
    with open(image_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())

    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    damage, confidence = predict(image_path)

    st.info(f"🔍 **Damage:** {damage}  \n✅ **Confidence:** {confidence * 100:.2f}%")

    # Real-world recommendation
    recommendations = {
        'Front Breakage': (
            "🔧 **Recommendation:** Front breakage detected — inspect the bumper, grille, or headlights for cracks or loose parts. "
            "It’s advisable to visit a certified body shop to prevent further deterioration."
        ),
        'Front Crushed': (
            "🚨 **Recommendation:** Major front-end crush detected — possible structural damage to hood, fenders, or radiator. "
            "Avoid driving long distances and contact your insurance company for an immediate claim and towing assistance."
        ),
        'Front Normal': (
            "✅ **Recommendation:** No visible front damage detected. Regularly inspect your car and maintain safe driving habits."
        ),
        'Rear Breakage': (
            "🔧 **Recommendation:** Rear breakage found — check tail lights, trunk lid, and bumper for cracks or misalignment. "
            "Schedule a repair to maintain safety and avoid legal issues due to broken lights."
        ),
        'Rear Crushed': (
            "🚨 **Recommendation:** Significant rear-end damage — possible impact on the trunk frame or rear sensors. "
            "It’s recommended to visit a professional repair shop and inform your insurer for a damage claim."
        ),
        'Rear Normal': (
            "✅ **Recommendation:** No visible rear damage detected. Ensure your rear lights and sensors remain clean and functional."
        )
    }

    st.success(recommendations.get(damage, "ℹ️ No recommendation available."))
