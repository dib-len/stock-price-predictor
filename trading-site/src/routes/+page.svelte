<script>
    let predictedPrice = $state(0);
    let ticker = $state("");
    let errorMessage = $state("");

    async function fetchPredictedPrice() {
        errorMessage = "";
        if (ticker === "") {
            errorMessage = "Please input a stock symbol";
            return;
        }

        try {
            const response = await fetch(`http://localhost:8000/predict/${ticker}`);
            const data = await response.json();
            predictedPrice = data.predicted_price;
        } catch (error) {
            errorMessage = "Error! Please try again";
        }
    }
</script>

<div class="flex flex-col items-center space-y-4">
    <h1 class="text-3xl font-bold"> 
        Welcome!
    </h1>

    <input class="px-3 py-1 border border-gray-300 rounded-lg focus:ring-1" 
            type="text" bind:value={ticker}
            placeholder="Input stock symbol here"/>
    <button onclick={fetchPredictedPrice}>
        Predict!
    </button>

    <h1 class="text-3xl font-bold text-red-500">
        {errorMessage}
    </h1>

    <h1 class="text-3xl font-bold">
        Predicted price:
        £{predictedPrice.toFixed(2)}
    </h1>
</div>