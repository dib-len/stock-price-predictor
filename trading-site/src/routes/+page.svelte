<script>
    let predictedPrice = $state("");
    let ticker = $state("");

    async function fetchPredictedPrice() {
        const response = await fetch(`http://localhost:8000/predict/${ticker}`);
        const data = await response.json();
        predictedPrice = data.predicted_price;
    }
    
</script>

<h1>Hello! {predictedPrice}</h1>
<input type="text" bind:value={ticker} placeholder="Enter"/>
<button onclick={fetchPredictedPrice}>
    Predict
</button>
