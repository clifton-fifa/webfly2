import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle

# โหลดข้อมูล
df = pd.read_excel(r"D:\project5000\project\dataset\New_Trained group_22-9-64.xlsx")
df = df.drop(columns=['ID'])

# กำหนดคอลัมน์ที่เลือก
selected_columns = ['a(1-2)', 'b(2-3)', 'c(3-4)', 'd(4-5)', 'e(6-7)', 'f(7-10)', 'g(9-10)', 'h(9-15)', 'i(15-16)',
                    'j(14-15)', 'k(13-14)', 'l(13-17)', 'm(17-18)', 'n(1-18)', 'o(2-13)', 'p(3-12)', 'q(12-13)',
                    'r(5-12)', 's(11-14)', 't(8-11)', 'u(7-8)', 'v(8-9)', 'w(11-12)']

# แยก features และ target สำหรับ Family
X_family = df[selected_columns]
y_family = df['Family']

# แบ่งข้อมูลสำหรับการทำนาย Family
X_train_family, X_test_family, y_train_family, y_test_family = train_test_split(X_family, y_family, test_size=0.2, random_state=42)
model_family = DecisionTreeClassifier()
model_family.fit(X_train_family, y_train_family)
y_pred_family = model_family.predict(X_test_family)
accuracy_family = accuracy_score(y_test_family, y_pred_family)
report_family = classification_report(y_test_family, y_pred_family)

print(f"Family Model Accuracy: {accuracy_family}")
print(f"Family Classification Report:\n{report_family}")

# บันทึกโมเดล family
with open('predictor/weight/family_predictor.pkl', 'wb') as file:
    pickle.dump(model_family, file)

# แยก features และ target สำหรับ Species
X_species = df[selected_columns]
y_species = df['Species']

# แบ่งข้อมูลสำหรับการทำนาย Species
X_train_species, X_test_species, y_train_species, y_test_species = train_test_split(X_species, y_species, test_size=0.2, random_state=42)
model_species = DecisionTreeClassifier()
model_species.fit(X_train_species, y_train_species)
y_pred_species = model_species.predict(X_test_species)
accuracy_species = accuracy_score(y_test_species, y_pred_species)
report_species = classification_report(y_test_species, y_pred_species)

print(f"Species Model Accuracy: {accuracy_species}")
print(f"Species Classification Report:\n{report_species}")

# บันทึกโมเดล species
with open('predictor/weight/species_predictor.pkl', 'wb') as file:
    pickle.dump(model_species, file)
