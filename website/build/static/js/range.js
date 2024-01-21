// Get the range input and the span element
var rangeInput = document.getElementById('severity');
var stressInput = document.getElementById('stress');
var rangeValueSpan = document.getElementById('rangeValue');
var stressValueSpan = document.getElementById('stressValue');
// Add an event listener to the range input
rangeInput.addEventListener('input', function () {
    // Update the span element with the current value of the range input
    rangeValueSpan.textContent = rangeInput.value;
});
stressInput.addEventListener('input', function () {
    // Update the span element with the current value of the range input
    stressValueSpan.textContent = stressInput.value;
});