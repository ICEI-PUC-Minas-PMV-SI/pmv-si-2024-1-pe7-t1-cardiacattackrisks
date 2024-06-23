document.getElementById("testar").addEventListener("click", function () {
    const exampleData = {
        age: 60,
        sex: "Male",
        cholesterol: 250,
        heartRate: 80,
        diabetes: 1,
        familyHistory: 1,
        smoking: 0,
        obesity: 1,
        alcoholConsumption: 0,
        exerciseHoursPerWeek: 3,
        diet: "Healthy",
        stressLevel: 5,
        bloodPressure: "130/85",
        income: 60000,
        bmi: 27.5,
        triglycerides: 190,
        physicalActivityDaysPerWeek: 3,
        sleepHoursPerDay: 7,
        medicationUse: 1,
        previousHeartProblems: 1,
        sedentaryHoursPerDay: 6
    };

    document.getElementById("age").value = exampleData.age;
    document.getElementById("sex").value = exampleData.sex;
    document.getElementById("cholesterol").value = exampleData.cholesterol;
    document.getElementById("heartRate").value = exampleData.heartRate;
    document.getElementById("diabetes").value = exampleData.diabetes;
    document.getElementById("familyHistory").value = exampleData.familyHistory;
    document.getElementById("smoking").value = exampleData.smoking;
    document.getElementById("obesity").value = exampleData.obesity;
    document.getElementById("alcoholConsumption").value = exampleData.alcoholConsumption;
    document.getElementById("exerciseHoursPerWeek").value = exampleData.exerciseHoursPerWeek;
    document.getElementById("diet").value = exampleData.diet;
    document.getElementById("stressLevel").value = exampleData.stressLevel;
    document.getElementById("bloodPressure").value = exampleData.bloodPressure;
    document.getElementById("income").value = exampleData.income;
    document.getElementById("bmi").value = exampleData.bmi;
    document.getElementById("triglycerides").value = exampleData.triglycerides;
    document.getElementById("physicalActivityDaysPerWeek").value = exampleData.physicalActivityDaysPerWeek;
    document.getElementById("sleepHoursPerDay").value = exampleData.sleepHoursPerDay;
    document.getElementById("medicationUse").value = exampleData.medicationUse;
    document.getElementById("previousHeartProblems").value = exampleData.previousHeartProblems;
    document.getElementById("sedentaryHoursPerDay").value = exampleData.sedentaryHoursPerDay;
});

document.getElementById("predictionForm").addEventListener("submit", function (event) {
    event.preventDefault();

    const age = document.getElementById("age").value;
    const sex = document.getElementById("sex").value;
    const cholesterol = document.getElementById("cholesterol").value;
    const heartRate = document.getElementById("heartRate").value;
    const diabetes = document.getElementById("diabetes").value;
    const familyHistory = document.getElementById("familyHistory").value;
    const smoking = document.getElementById("smoking").value;
    const obesity = document.getElementById("obesity").value;
    const alcoholConsumption = document.getElementById("alcoholConsumption").value;
    const diet = document.getElementById("diet").value;
    const stressLevel = document.getElementById("stressLevel").value;
    const bloodPressure = document.getElementById("bloodPressure").value.split("/");
    const income = document.getElementById("income").value;
    const bmi = document.getElementById("bmi").value;
    const triglycerides = document.getElementById("triglycerides").value;
    const physicalActivityDaysPerWeek = document.getElementById("physicalActivityDaysPerWeek").value;
    const sleepHoursPerDay = document.getElementById("sleepHoursPerDay").value;
    const medicationUse = document.getElementById("medicationUse").value;
    const previousHeartProblems = document.getElementById("previousHeartProblems").value;
    const sedentaryHoursPerDay = document.getElementById("sedentaryHoursPerDay").value;

    const data = {
        Age: parseInt(age),
        Sex: sex,
        Cholesterol: parseInt(cholesterol),
        "Heart Rate": parseInt(heartRate),
        Diabetes: parseInt(diabetes),
        "Family History": parseInt(familyHistory),
        Smoking: parseInt(smoking),
        Obesity: parseInt(obesity),
        "Alcohol Consumption": parseInt(alcoholConsumption),
        Diet: diet,
        "Stress Level": parseInt(stressLevel),
        "Systolic Blood Pressure": parseInt(bloodPressure[0]),
        "Diastolic Blood Pressure": parseInt(bloodPressure[1]),
        Income: parseInt(income),
        BMI: parseFloat(bmi),
        Triglycerides: parseInt(triglycerides),
        "Physical Activity Days Per Week": parseInt(physicalActivityDaysPerWeek),
        "Sleep Hours Per Day": parseInt(sleepHoursPerDay),
        "Medication Use": parseInt(medicationUse),
        "Previous Heart Problems": parseInt(previousHeartProblems),
        "Sedentary Hours Per Day": parseInt(sedentaryHoursPerDay)
    };

    fetch('https://heartattackriskprediction.azurewebsites.net/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(result => {
            const risk_knn = result['Heart Attack Risk (KNN)'];
            const risk_svm = result['Heart Attack Risk (SVM)'];
            let message;

            // if (risk_knn === 1 && risk_svm === 1) {
            //     message = "Risco alto de ataque cardíaco! Consulte seu médico.";
            // } else {
            //     message = "Risco baixo de ataque cardíaco. Continue se cuidando!";
            // }

            message = "Risco de ataque cardíaco (KNN): " + risk_knn === 1 ? "Sim" : "Não" + "\\n" + "Risco de ataque cardíaco (SVM): " + risk_svm === 1 ? "Sim" : "Não";

        // Exibir o prompt com a mensagem
        alert(message);
    })
    .catch(error => {
        console.error('Erro:', error);
        alert("Ocorreu um erro ao tentar prever o risco.");
    });
});
