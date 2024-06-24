document.getElementById("height").addEventListener("input", calculateBMI);
document.getElementById("weight").addEventListener("input", calculateBMI);

function calculateBMI() {
    const height = parseFloat(document.getElementById("height").value);
    const weight = parseFloat(document.getElementById("weight").value);
    if (height && weight) {
        const bmi = (weight / (height * height)).toFixed(1);
        document.getElementById("bmi").value = bmi;
    }
}

document.getElementById("testar").addEventListener("click", function () {
    const exampleData = {
        age: 60,
        sex: "Male",
        cholesterol: 250,
        heartRate: 80,
        diabetes: 1,
        familyHistory: 1,
        smoking: 0,
        alcoholConsumption: 0,
        exerciseHoursPerWeek: 3,
        diet: "Healthy",
        stressLevel: 5,
        bloodPressure: "130/85",
        height: 1.75,
        weight: 75,
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
    document.getElementById("alcoholConsumption").value = exampleData.alcoholConsumption;
    document.getElementById("exerciseHoursPerWeek").value = exampleData.exerciseHoursPerWeek;
    document.getElementById("diet").value = exampleData.diet;
    document.getElementById("stressLevel").value = exampleData.stressLevel;
    document.getElementById("bloodPressure").value = exampleData.bloodPressure;
    document.getElementById("height").value = exampleData.height;
    document.getElementById("weight").value = exampleData.weight;
    document.getElementById("bmi").value = exampleData.bmi;
    document.getElementById("triglycerides").value = exampleData.triglycerides;
    document.getElementById("physicalActivityDaysPerWeek").value = exampleData.physicalActivityDaysPerWeek;
    document.getElementById("sleepHoursPerDay").value = exampleData.sleepHoursPerDay;
    document.getElementById("medicationUse").value = exampleData.medicationUse;
    document.getElementById("previousHeartProblems").value = exampleData.previousHeartProblems;
    document.getElementById("sedentaryHoursPerDay").value = exampleData.sedentaryHoursPerDay;

    calculateBMI(); // Calcular IMC
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
    const alcoholConsumption = document.getElementById("alcoholConsumption").value;
    const diet = document.getElementById("diet").value;
    const stressLevel = document.getElementById("stressLevel").value;
    const bloodPressure = document.getElementById("bloodPressure").value.split("/");
    const height = parseFloat(document.getElementById("height").value);
    const weight = parseFloat(document.getElementById("weight").value);
    const bmi = document.getElementById("bmi").value;
    const triglycerides = document.getElementById("triglycerides").value;
    const physicalActivityDaysPerWeek = document.getElementById("physicalActivityDaysPerWeek").value;
    const sleepHoursPerDay = document.getElementById("sleepHoursPerDay").value;
    const medicationUse = document.getElementById("medicationUse").value;
    const previousHeartProblems = document.getElementById("previousHeartProblems").value;
    const sedentaryHoursPerDay = document.getElementById("sedentaryHoursPerDay").value
    
    // Calcular obesidade com base no IMC
    const obesity = bmi >= 30 ? 1 : 0;

    const data = {
        Age: parseInt(age),
        Sex: sex,
        Cholesterol: parseInt(cholesterol),
        "Heart Rate": parseInt(heartRate),
        Diabetes: parseInt(diabetes),
        "Family History": parseInt(familyHistory),
        Smoking: parseInt(smoking),
        Obesity: obesity,
        "Alcohol Consumption": parseInt(alcoholConsumption),
        Diet: diet,
        "Stress Level": parseInt(stressLevel),
        "Systolic Blood Pressure": parseInt(bloodPressure[0]),
        "Diastolic Blood Pressure": parseInt(bloodPressure[1]),
        Height: height,
        Weight: weight,
        BMI: parseFloat(bmi),
        Triglycerides: parseInt(triglycerides),
        "Physical Activity Days Per Week": parseInt(physicalActivityDaysPerWeek),
        "Sleep Hours Per Day": parseInt(sleepHoursPerDay),
        "Medication Use": parseInt(medicationUse),
        "Previous Heart Problems": parseInt(previousHeartProblems),
        "Sedentary Hours Per Day": parseInt(sedentaryHoursPerDay)
    };


    fetch('http://localhost:5000/predict', {
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
            let count = risk_knn + risk_svm;
            let resulfin;
            
            if (count === 0 ){
                resulfin = "Não foi detectado risco de ataque cardíaco.";
            }
            else if (count === 1){
                resulfin = "Foi detectado risco moderado de ataque cardíaco.";
            }
            else if (count === 2) { 
                resulfin = "Foi detectado risco alto de ataque cardíaco."}
            else {
                resulfin= "Resultado inconclusivo"};


            message = "Risco de ataque cardíaco (KNN): " + (risk_knn === 1 ? "Sim" : "Não") + "\n" + 
                        "Risco de ataque cardíaco (SVM): " + (risk_svm === 1 ? "Sim" : "Não") + "\n" + "\n" +
                        "Conclusão Final: " + resulfin + "\n"+ "\n" +
                        "Os resultados aqui arepsentados não são conclusivos, consulte um médico para uma avaliação mais precisa.";

        // Exibir o prompt com a mensagem
        alert(message);
    })
    .catch(error => {
        console.error('Erro:', error);
        alert("Ocorreu um erro ao tentar prever o risco.");
    });
});

