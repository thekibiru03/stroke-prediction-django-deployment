from django.shortcuts import render

# our home page view
def home(request):    
    return render(request, 'index.html')


# custom method for generating predictions
def getPredictions(gender, age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status):
    import pickle
    model = pickle.load(open("stroke_pred/stroke_pred.pkl", "rb"))
    sc = pickle.load(open("stroke_pred/scaler.pkl", "rb"))
    prediction = model.predict(sc.transform([[gender, age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status]]))

    if prediction == 0:
        return "prediction: no stroke"
    elif prediction == 1:
        return "prediction: stroke"
    else:
        return "error"
        

# our result page view
def result(request):
    gender = int(request.GET['gender'])
    age = int(request.GET['age'])
    hypertension = int(request.GET['hypertension'])
    heart_disease = int(request.GET['heart_disease'])
    ever_married = int(request.GET['ever_married'])
    work_type = int(request.GET['work_type'])
    Residence_type = int(request.GET['Residence_type'])
    avg_glucose_level = int(request.GET['avg_glucose_level'])
    bmi = int(request.GET['bmi'])
    smoking_status = int(request.GET['smoking_status'])

    result = getPredictions(gender, age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status)

    return render(request, 'result.html', {'result':result})