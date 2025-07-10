# 🚗🔍 Vehicle Damage Detection AI

Welcome to **Vehicle Damage Detection AI** — an intelligent tool that analyzes images of a vehicle and automatically detects visible front or rear damage conditions.
It helps car owners, garages, and insurance companies quickly assess damage and get practical recommendations for what to do next.

![app](app_screenshot.jpg.png)

## 📌 **Key Features**

✅ **Upload an image** — Just drop a photo of your car’s front or rear.  
✅ **Get instant detection** — The model analyzes the image and predicts the damage type.  
✅ **See the confidence** — Know how confident the AI is about its prediction.  
✅ **Receive clear recommendations** — Get actionable advice for repairs or next steps.  
✅ **Simple and intuitive** — Runs in your browser with an elegant Streamlit UI.

---

## 🚙 **How It Works**

Under the hood, this app uses a **ResNet50 deep learning model** fine-tuned to classify six conditions:

- **Front Breakage**
- **Front Crushed**
- **Front Normal**
- **Rear Breakage**
- **Rear Crushed**
- **Rear Normal**

It processes the uploaded image, makes a prediction, shows the model’s confidence, and provides a **practical, real-world repair recommendation**.

---

## 🛠️ **Tech Stack**

- **Python**
- **PyTorch** — for the deep learning model.
- **Torchvision** — for ResNet50 and transforms.
- **Streamlit** — to create a friendly web app.
- **PIL** — for image processing.

---

## 🚀 **Quick Start**

1️⃣ **Clone the repo**
```bash
git clone https://github.com/yourusername/vehicle-damage-detection.git
cd vehicle-damage-detection
````

2️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

3️⃣ **Add your trained model**

Place your trained model checkpoint here:

```
/model/saved_model.pth
```

4️⃣ **Run the app**

```bash
streamlit run app.py
```

5️⃣ **Open your browser**

Upload your car image and see the results instantly!

---

## 📂 **Project Structure**

```
├── app.py                 # Streamlit app
├── model_helper.py          # Model and prediction logic
├── model/
│   └── saved_model.pth    # Trained model weights
├── requirements.txt       # Python dependencies
├── README.md              # This file
```

---

## 💡 **Example**

Here’s what you’ll see:

> **Damage:** Front Breakage
> **Confidence:** 97.5%
> **Recommendation:** Front breakage detected — inspect the bumper, grille, or headlights for cracks or loose parts. Visit a certified body shop to prevent further deterioration.

---

## ✅ **Why Use This?**

* **Fast & convenient:** Get an instant check without visiting a garage first.
* **Save time & money:** Helps you decide if you need minor repairs or insurance claims.
* **Transparency:** Shows confidence so you understand the AI’s certainty.
* **Practical:** Actionable tips make it more than just a detection tool — it’s like a first step towards solving the problem.

---

## 📜 **License**

This project is open-source for learning and personal use. For commercial use or integration, please contact the author.

---

## ✨ **Future Improvements**

✅ Multi-angle image support
✅ Estimate repair cost
✅ Integration with insurance claim systems
✅ Before-and-after damage comparison

---

## 👨‍💻 **Author**

Built with ❤️ by \[Imran Chowdhury].
Feel free to fork, use, and improve — contributions welcome!

---

## ⭐️ **Show your support**

If you like this project:

* 🌟 Star this repo
* 📣 Share it
* 🛠️ Use it in your portfolio!

---

**Drive safe — and fix your car smartly! 🚗🔧**
