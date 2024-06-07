document.getElementById('predictionForm').addEventListener('submit', async function (event) {
    event.preventDefault();
    let formData = new FormData(this);
    let data = {};
    formData.forEach((value, key) => data[key] = value);

    let bloodPressure = data["bloodPressure"].split("/");
    data["Systolic Pressure"] = parseInt(bloodPressure[0]);
    data["Diastolic Pressure"] = parseInt(bloodPressure[1]);
    delete data["bloodPressure"];

    // Prever usando KNN
    let responseKNN = await fetch('http://127.0.0.1:5000/predict_knn', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    });

    let resultKNN = await responseKNN.json();
    alert('Previsão KNN: ' + resultKNN.prediction);
