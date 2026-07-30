// ===============================
// Backend API URL
// Replace this after deployment
// ===============================
const API_URL = "YOUR_RENDER_BACKEND_URL/predict";

// Elements
const predictBtn = document.getElementById("predictBtn");
const result = document.getElementById("result");
const loading = document.getElementById("loading");

predictBtn.addEventListener("click", async () => {

    const year = document.getElementById("Year").value.trim();
    const mileage = document.getElementById("Mileage").value.trim();

    result.style.display = "none";
    result.className = "result";

    if (year === "" || mileage === "") {
        result.style.display = "block";
        result.classList.add("error");
        result.innerHTML = "Please fill all the fields.";
        return;
    }

    loading.innerHTML = "Predicting...";

    predictBtn.disabled = true;

    try {

        const response = await fetch(API_URL, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                Year: Number(year),
                Mileage: Number(mileage)
            })

        });

        const data = await response.json();

        loading.innerHTML = "";
        predictBtn.disabled = false;

        if (data.predicted_price !== undefined) {

            result.style.display = "block";

            result.innerHTML =
                `Estimated Car Price<br><br><strong>₹ ${data.predicted_price.toLocaleString()}</strong>`;

        } else {

            result.style.display = "block";
            result.classList.add("error");
            result.innerHTML = data.error || "Prediction failed.";

        }

    }

    catch (error) {

        loading.innerHTML = "";
        predictBtn.disabled = false;

        result.style.display = "block";
        result.classList.add("error");

        result.innerHTML =
            "Unable to connect to the server. Please try again later.";

        console.error(error);

    }

});