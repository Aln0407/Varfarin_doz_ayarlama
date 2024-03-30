import streamlit as st

st.set_page_config(page_title='Hasta Kontrol Platformu',layout='wide')

st.title('Hasta Kontrol Platformuna Hosgeldiniz!!!')

st.header('Lutfen bilgilerinizi giriniz!')

st.subheader('Gunluk Tablet Kullanim Sayisi(1 tablet 5 mg)')

st.write('Pazartesi gunu ilac kullanim adeti:')

patient_value1 = st.number_input(label='Pazartesi degeri',step=0.25,format="%.2f")

st.write('Sali gunu ilac kullanim adeti:')

patient_value2 = st.number_input(label='Sali degeri',step=0.25,format="%.2f")

st.write('Carsamba gunu ilac kullanim adeti:')

patient_value3 = st.number_input(label='Carsamba degeri',step=0.25,format="%.2f")

st.write('Persembe gunu ilac kullanim adeti:')

patient_value4 = st.number_input(label='Persembe degeri',step=0.25,format="%.2f")

st.write('Cuma gunu ilac kullanim adeti:')

patient_value5 = st.number_input(label='Cuma degeri',step=0.25,format="%.2f")

st.write('Cumartesi gunu ilac kullanim adeti:')

patient_value6 = st.number_input(label='Cumartesi degeri',step=0.25,format="%.2f")

st.write('Pazar gunu ilac kullanim adeti:')

patient_value7 = st.number_input(label='Pazar degeri',step=0.25,format="%.2f")

st.subheader('Toplam Bilgisi')

patient_value_sum = patient_value1 + patient_value2 + patient_value3 + patient_value4 + patient_value5 + patient_value6 + patient_value7

patient_value_sum_mg = patient_value_sum*5

st.write(f'Haftalik toplam aldiginiz ilac miktari (mg): {patient_value_sum_mg}')

st.subheader('INR Bilgisi')

st.write('INR degeriniz (1den buyuk olmak zorundadir):')

patient_inr = st.number_input(label='INR degeri',step=0.01,format="%.2f", value=2.5)

target_inr = st.number_input(label='Hedef INR degeri (Deger girilmezse hedef 2.5 alinacaktir)',step=0.01,format="%.2f", value=2.5)

st.subheader('Sonuc:')

need_mg = ((target_inr-1)/(patient_inr-1))*patient_value_sum_mg

st.write(f'Haftalik almaniz gereken mg: {need_mg}')

st.write(f'Dagitilacak tablet sayisi: {round(need_mg/5)}')

total_tablet_sum = round(need_mg/5)

current_sum = 0

day_names = ['Pazartesi', 'Sali', 'Carsamba', 'Persembe', 'Cuma', 'Cumartesi', 'Pazar']

days_tablet_values = [0]*7

finish_condition = False

i = 0

if total_tablet_sum < 3.5:
    tablet_increment = 0.25
else: 
    tablet_increment = 0.5

while 1 and total_tablet_sum>0 and patient_value_sum_mg>0:
    days_tablet_values[i%7] += tablet_increment
    current_sum += tablet_increment
    if current_sum == total_tablet_sum:
        finish_condition = True
        break
    if finish_condition:
        break
    i += 2

i += 2

value_to_counts = dict()
for j in range(7):
    if days_tablet_values[j] not in value_to_counts:
        value_to_counts[days_tablet_values[j]] = 1
    else:
        value_to_counts[days_tablet_values[j]] += 1

if len(value_to_counts.keys())==2 and 2 in value_to_counts.values():
    temp_value = days_tablet_values[i%7]
    days_tablet_values[i%7] = days_tablet_values[(i-1)%7]
    days_tablet_values[(i-1)%7] = temp_value

st.subheader('Gunluk dagiliminiz:')
for i in range(7):
    st.write(f'{day_names[i]}: {days_tablet_values[i]} tablet')
