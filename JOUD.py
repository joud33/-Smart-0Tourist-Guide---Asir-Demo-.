import streamlit as st
from dataclasses import dataclass
from typing import List, Dict

# إعداد الصفحة
st.set_page_config(page_title="الدليل السياحي الذكي - عسير", page_icon="🏞️", layout="wide")

# =========================
# 🎨 CSS + هوية عسير
# =========================
ASIR_CSS = """
<style>
:root{
  --asir-green:#0f6b4f;
  --asir-dark:#0b2e24;
  --asir-sand:#efe7d6;
  --asir-fog:#f6f7f7;
}

html, body, [class*="css"]  { direction: rtl; font-family: "Tahoma", sans-serif; }
.stApp { background: linear-gradient(180deg, var(--asir-fog) 0%, #ffffff 60%, var(--asir-sand) 120%); }

.hero{
  background: linear-gradient(135deg, var(--asir-green), var(--asir-dark));
  border-radius: 18px;
  padding: 22px;
  color: white;
  margin-bottom:20px;
}

.card{
  background: white;
  border-radius: 16px;
  padding: 14px;
  border: 1px solid rgba(15,107,79,0.15);
  box-shadow: 0 6px 16px rgba(0,0,0,0.06);
  margin-bottom:15px;
}

.card-img{
  width:100%;
  height:170px;
  object-fit:cover;
  border-radius:12px;
  margin-bottom:10px;
}

.tag{
  display:inline-block;
  padding:4px 10px;
  border-radius:999px;
  font-size:12px;
  margin-top:8px;
}

/* ألوان التكلفة */
.cost-low { background:#e7f6ee; color:#0f6b4f; }
.cost-medium { background:#fff3e6; color:#b06000; }
.cost-high { background:#fde8e8; color:#b00020; }

.small { color:gray; font-size:13px; }

</style>
"""
st.markdown(ASIR_CSS, unsafe_allow_html=True)

# =========================
# 📍 تعريف الأماكن
# =========================
@dataclass
class Place:
    name: str
    city: str
    category: str
    cost_level: str
    best_time: str
    description: str
    maps_url: str
    image_url: str

PLACES: List[Place] = [

    Place(
        "الجبل الأخضر",
        "أبها",
        "طبيعة",
        "متوسط",
        "مساء",
        "إطلالة جميلة وتجربة ممتعة.",
        "https://www.google.com/maps/search/?api=1&query=الجبل+الأخضر+أبها",
        "https://images.unsplash.com/photo-1469474968028-56623f02e42e"
    ),

    Place(
        "ممشى الضباب",
        "أبها",
        "طبيعة",
        "منخفض",
        "مساء",
        "ممشى رائع بجو منعش خصوصًا في المساء.",
        "https://www.google.com/maps/search/?api=1&query=ممشى+الضباب+أبها",
        "https://images.unsplash.com/photo-1501785888041-af3ef285b470"
    ),

    Place(
        "قرية رجال ألمع",
        "رجال ألمع",
        "ثقافة/تراث",
        "متوسط",
        "صباح",
        "موقع تراثي مميز بعمارة عسيرية رائعة.",
        "https://www.google.com/maps/search/?api=1&query=رجال+ألمع",
        "https://images.unsplash.com/photo-1528127269322-539801943592"
    ),

    Place(
        "قرية المفتاحة",
        "أبها",
        "ثقافة/تراث",
        "منخفض",
        "مساء",
        "ساحة ثقافية وفنية جميلة للتصوير.",
        "https://www.google.com/maps/search/?api=1&query=قرية+المفتاحة+أبها",
        "https://images.unsplash.com/photo-1523413651479-597eb2da0ad6"
    ),
]

# =========================
# 🎨 دالة لون التكلفة
# =========================
def cost_class(level):
    if level == "منخفض":
        return "cost-low"
    if level == "متوسط":
        return "cost-medium"
    return "cost-high"

# =========================
# 🖼 عرض البطاقة
# =========================
def place_card(p: Place):
    st.markdown(
        f"""
        <div class="card">
            <img class="card-img" src="{p.image_url}">
            <h4>{p.name}</h4>
            <div class="small">{p.city} • أفضل وقت: {p.best_time}</div>
            <div class="tag {cost_class(p.cost_level)}">{p.cost_level}</div>
            <p class="small">{p.description}</p>
            <a href="{p.maps_url}" target="_blank">📍 فتح في الخرائط</a>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================
# 🏞 الواجهة
# =========================
st.markdown("""
<div class="hero">
<h2>🏞 الدليل السياحي الذكي - عسير</h2>
نسخة تجريبية تقترح خطة زيارة حسب اهتماماتك.
</div>
""", unsafe_allow_html=True)

days = st.slider("عدد الأيام", 1, 3, 2)
interest = st.selectbox("اختر اهتمامك", ["طبيعة", "ثقافة/تراث"])

st.subheader("الاقتراحات:")

filtered = [p for p in PLACES if p.category == interest]

for p in filtered[:days+1]:
    place_card(p)

st.caption("نسخة تجريبية قابلة للتطوير.")
